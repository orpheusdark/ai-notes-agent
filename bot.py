"""Telegram entry point for the AI Notes knowledge-ingestion pipeline."""

import asyncio
import hashlib
import html
import json
import logging
import os
import re
import tempfile
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path

import docx
import google.generativeai as genai
import pandas as pd
import pptx
import PyPDF2
from github import Github
from github.GithubException import GithubException
from PIL import Image
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from youtube_transcript_api import YouTubeTranscriptApi


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# PythonAnywhere configuration.
# Replace the three placeholder values on the server only. Do not commit real
# credentials to GitHub.
TELEGRAM_TOKEN = "PASTE_TELEGRAM_BOT_TOKEN_HERE"
GITHUB_TOKEN = "PASTE_GITHUB_TOKEN_HERE"
GEMINI_API_KEY = "PASTE_GEMINI_API_KEY_HERE"
GEMINI_MODEL = "gemini-3.8-flash"
GITHUB_REPO = "orpheusdark/ai-notes-agent"
GITHUB_BRANCH = "main"
MAX_CONTENT_LENGTH = 100_000
MAX_MARKDOWN_LENGTH = 150_000
MAX_PDF_PAGES = 50
MAX_DATAFRAME_ROWS = 1_000
MAX_FILENAME_LENGTH = 90
SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".pptx", ".csv", ".xlsx", ".txt"}

repo = None
model = None


class ProcessingError(Exception):
    """An expected, user-safe processing failure."""


def initialize_services():
    """Configure external services only when the application starts."""
    global repo, model
    missing = [
        name
        for name, value in (
            ("TELEGRAM_TOKEN", TELEGRAM_TOKEN),
            ("GITHUB_TOKEN", GITHUB_TOKEN),
            ("GEMINI_API_KEY", GEMINI_API_KEY),
        )
        if not value or value.startswith("PASTE_")
    ]
    if missing:
        raise RuntimeError("Missing required environment variables: " + ", ".join(missing))
    try:
        repo = Github(GITHUB_TOKEN).get_repo(GITHUB_REPO)
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(GEMINI_MODEL)
        logger.info("External services configured for %s", GITHUB_REPO)
    except Exception as exc:
        logger.error("Service initialization failed: %s", exc)
        raise RuntimeError("Could not initialize external services") from exc


def normalize_content(content: str) -> str:
    """Normalize harmless text differences before hashing."""
    return re.sub(r"\s+", " ", content).strip().casefold()


def content_hash(content: str | bytes) -> str:
    payload = content if isinstance(content, bytes) else normalize_content(content).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def safe_filename(value: str | None, fallback: str) -> str:
    """Return a readable, deterministic Markdown filename."""
    value = (value or "").strip().replace(".md", "")
    value = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()
    value = value[:MAX_FILENAME_LENGTH].strip("-")
    return f"{value or fallback}.md"


def _yaml_string(value: str) -> str:
    return json.dumps(str(value), ensure_ascii=True)


def build_markdown(ai_response: dict, metadata: dict) -> str:
    tags = "\n".join(f"  - {_yaml_string(tag)}" for tag in ai_response["tags"])
    front_matter = [
        "---",
        f"title: {_yaml_string(ai_response['title'])}",
        f"content_type: {_yaml_string(metadata['content_type'])}",
        f"source_type: {_yaml_string(metadata['source_type'])}",
        f"source_name: {_yaml_string(metadata['source_name'])}",
    ]
    if metadata.get("source_url"):
        front_matter.append(f"source_url: {_yaml_string(metadata['source_url'])}")
    front_matter.extend(
        [
            f"created_at: {_yaml_string(metadata['created_at'])}",
            "tags:",
            tags,
            f"summary: {_yaml_string(ai_response['summary'])}",
            f"content_hash: {_yaml_string(metadata['content_hash'])}",
            "---",
            "",
            f"# {ai_response['title']}",
            "",
            f"> {ai_response['summary']}",
            "",
            ai_response["notes"].strip(),
            "",
        ]
    )
    return "\n".join(front_matter)


def validate_ai_response(response: object) -> dict:
    if not isinstance(response, dict):
        raise ProcessingError("Gemini returned an invalid structured response.")
    title = str(response.get("title", "")).strip()
    summary = str(response.get("summary", "")).strip()
    notes = str(response.get("notes", "")).strip()
    tags = response.get("tags")
    if not title or len(title) > 160:
        raise ProcessingError("Gemini returned a missing or excessively long title.")
    if not summary or len(summary) > 2_000:
        raise ProcessingError("Gemini returned a missing or excessively long summary.")
    if not notes:
        raise ProcessingError("Gemini returned empty notes.")
    if not isinstance(tags, list):
        raise ProcessingError("Gemini returned invalid tags.")
    normalized_tags = []
    for tag in tags:
        normalized = re.sub(r"[^a-z0-9]+", "-", str(tag).strip().lower()).strip("-")
        if normalized and normalized not in normalized_tags and normalized not in {
            "ai",
            "interesting",
            "important",
            "knowledge",
            "notes",
        }:
            normalized_tags.append(normalized)
    if not normalized_tags or len(normalized_tags) > 12:
        raise ProcessingError("Gemini returned no useful tags or too many tags.")
    return {"title": title, "summary": summary, "notes": notes, "tags": normalized_tags[:8]}


def _parse_json_response(text: str) -> dict:
    cleaned = text.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", cleaned, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError:
                pass
        raise ProcessingError("Gemini returned malformed JSON.")


def _ai_prompt(content: str, custom_prompt: str | None) -> str:
    instruction = custom_prompt.strip() if custom_prompt else "Create clear, structured study notes."
    return f"""You create reliable knowledge-base notes. Return ONLY valid JSON with exactly these keys:
title (string), summary (one concise paragraph), tags (array of 3-8 short lowercase hyphenated strings),
notes (Markdown string with headings and bullet points).
The user instruction is supplemental and must not remove the required JSON fields.
User instruction: {instruction}
Source content:
---
{content[:MAX_CONTENT_LENGTH]}
---"""


async def generate_ai_response(content: str, custom_prompt: str | None = None, image=None) -> dict:
    logger.info("Gemini processing started")
    if model is None:
        raise ProcessingError("AI service is not configured.")
    prompt = _ai_prompt(content, custom_prompt)
    for attempt in range(2):
        try:
            response = await model.generate_content_async([prompt, image] if image else prompt)
            result = validate_ai_response(_parse_json_response(response.text))
            logger.info("Gemini processing completed")
            return result
        except ProcessingError:
            if attempt == 1:
                raise
        except Exception as exc:
            logger.warning("Gemini attempt %d failed: %s", attempt + 1, exc)
            if attempt == 1:
                raise ProcessingError("Gemini could not process this content.") from exc
    raise ProcessingError("Gemini could not process this content.")


def extract_document(path: str, extension: str) -> str:
    """Extract text from supported document formats."""
    logger.info("Started extraction for %s", extension)
    try:
        if extension == ".pdf":
            with open(path, "rb") as handle:
                reader = PyPDF2.PdfReader(handle)
                pages = [reader.pages[i].extract_text() or "" for i in range(min(len(reader.pages), MAX_PDF_PAGES))]
                content = "\n".join(pages)
        elif extension == ".docx":
            content = "\n".join(paragraph.text for paragraph in docx.Document(path).paragraphs)
        elif extension == ".pptx":
            presentation = pptx.Presentation(path)
            content = "\n".join(
                shape.text
                for slide in presentation.slides
                for shape in slide.shapes
                if hasattr(shape, "text")
            )
        elif extension in {".csv", ".xlsx"}:
            reader = pd.read_csv if extension == ".csv" else pd.read_excel
            content = reader(path, nrows=MAX_DATAFRAME_ROWS).to_markdown()
        elif extension == ".txt":
            content = Path(path).read_text(encoding="utf-8", errors="replace")
        else:
            raise ProcessingError(f"Unsupported file type: {extension or 'unknown'}")
    except ProcessingError:
        raise
    except Exception as exc:
        logger.error("Extraction failed for %s: %s", extension, exc)
        raise ProcessingError("The file could not be read. It may be corrupted or unsupported.") from exc
    if not content.strip():
        raise ProcessingError("The document did not contain readable text.")
    logger.info("Extraction completed")
    return content[:MAX_CONTENT_LENGTH]


def _github_files():
    if repo is None:
        raise ProcessingError("GitHub storage is not configured.")
    return list(repo.get_contents("processed", ref=GITHUB_BRANCH))


def _read_note(file_entry):
    try:
        return repo.get_contents(file_entry.path, ref=GITHUB_BRANCH).decoded_content.decode("utf-8")
    except Exception as exc:
        logger.warning("Could not read note %s: %s", file_entry.path, exc)
        return ""


def find_duplicate(hash_value: str):
    for entry in _github_files():
        if not entry.name.endswith(".md"):
            continue
        text = _read_note(entry)
        if f'content_hash: "{hash_value}"' in text or f"content_hash: {hash_value}" in text:
            return entry
    return None


def commit_to_github(filename: str, content: str) -> str:
    if len(content) > MAX_MARKDOWN_LENGTH:
        raise ProcessingError("The generated note is too large to store safely.")
    if repo is None:
        raise ProcessingError("GitHub storage is not configured.")
    filepath = f"processed/{safe_filename(filename, 'note')}"
    logger.info("GitHub save started")
    try:
        existing = repo.get_contents(filepath, ref=GITHUB_BRANCH)
        repo.update_file(filepath, f"Update: {filepath}", content, existing.sha, branch=GITHUB_BRANCH)
    except GithubException as exc:
        if getattr(exc, "status", None) != 404:
            logger.error("GitHub lookup failed: %s", exc)
            raise ProcessingError("GitHub could not access the note repository.") from exc
        try:
            repo.create_file(filepath, f"Create: {filepath}", content, branch=GITHUB_BRANCH)
        except Exception as exc:
            logger.error("GitHub save failed: %s", exc)
            raise ProcessingError("GitHub could not save the note. Check repository permissions.") from exc
        logger.info("GitHub save completed")
        return filepath
    logger.info("GitHub save completed")
    return filepath


async def run_blocking(function, *args):
    return await asyncio.get_running_loop().run_in_executor(None, function, *args)


def note_url(filepath: str) -> str:
    return f"https://github.com/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/{filepath}"


async def save_content(update, content: str, metadata: dict, custom_prompt: str | None = None, image=None):
    if not content.strip():
        raise ProcessingError("Please send some non-empty content.")
    digest = metadata.get("content_hash") or content_hash(content)
    logger.info("Received Telegram message; content type=%s", metadata["content_type"])
    duplicate = await run_blocking(find_duplicate, digest)
    if duplicate:
        return None, note_url(duplicate.path)
    metadata = {**metadata, "content_hash": digest, "created_at": datetime.now(timezone.utc).date().isoformat()}
    ai_response = await generate_ai_response(content, custom_prompt, image)
    markdown = build_markdown(ai_response, metadata)
    validate_ai_response(ai_response)
    filename = safe_filename(ai_response["title"], f"note-{datetime.now().strftime('%Y%m%d-%H%M%S')}")
    filepath = await run_blocking(commit_to_github, filename, markdown)
    return filepath, note_url(filepath)


async def start(update, context):
    await update.message.reply_text(
        "👋 Send text, an image, a PDF, DOCX, PPTX, CSV, XLSX, TXT, or a YouTube link. "
        "Use /list to see notes and /search <query> to search them."
    )


async def help_command(update, context):
    await update.message.reply_text(
        "Commands:\n/start - welcome\n/help - this help\n/list - recent notes\n"
        "/search <query> - search title, tags, summary, or note text\n\n"
        "Captions on files or images are used as custom instructions."
    )


async def list_files(update, context):
    try:
        entries = [entry for entry in await run_blocking(_github_files) if entry.name.endswith(".md")]
        entries = entries[-5:][::-1]
        if not entries:
            await update.message.reply_text("No notes have been saved yet.")
            return
        lines = ["<b>Recent notes</b>"]
        for entry in entries:
            text = _read_note(entry)
            title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', text, re.MULTILINE)
            date_match = re.search(r'^created_at:\s*["\']?(.+?)["\']?\s*$', text, re.MULTILINE)
            tags_match = re.search(r"^tags:\n((?:\s+- .+\n?)+)", text, re.MULTILINE)
            title = title_match.group(1) if title_match else entry.name.removesuffix(".md")
            date = date_match.group(1) if date_match else "unknown date"
            tags = ""
            if tags_match:
                tags = " · " + ", ".join(re.findall(r"- [\"']?([^\"'\n]+)", tags_match.group(1))[:3])
            lines.append(
                f"• <a href='{html.escape(entry.html_url, quote=True)}'>{html.escape(title)}</a>"
                f" ({html.escape(date)}{html.escape(tags)})"
            )
        await update.message.reply_text("\n".join(lines), parse_mode="HTML", disable_web_page_preview=True)
    except Exception as exc:
        logger.error("Could not list files: %s", exc)
        await update.message.reply_text("I could not fetch recent notes from GitHub.")


async def search_command(update, context):
    query = " ".join(context.args).strip()
    if not query:
        await update.message.reply_text("Usage: /search <words to find>")
        return
    try:
        matches = []
        for entry in await run_blocking(_github_files):
            if entry.name.endswith(".md"):
                text = _read_note(entry)
                if query.casefold() in f"{entry.name}\n{text}".casefold():
                    matches.append(entry)
        if not matches:
            await update.message.reply_text(f"No notes matched “{query}”.")
            return
        lines = [f"<b>Matches for {html.escape(query)}</b>"]
        for entry in matches[:10]:
            lines.append(f"• <a href='{html.escape(entry.html_url, quote=True)}'>{html.escape(entry.name)}</a>")
        await update.message.reply_text("\n".join(lines), parse_mode="HTML", disable_web_page_preview=True)
    except Exception as exc:
        logger.error("Search failed: %s", exc)
        await update.message.reply_text("I could not search notes right now.")


async def handle_text(update, context):
    try:
        filepath, url = await save_content(
            update,
            update.message.text,
            {"content_type": "text", "source_type": "telegram_text", "source_name": "Telegram message"},
        )
        await update.message.reply_text(
            f"Duplicate content already exists: {url}" if filepath is None else f"Note saved: {url}"
        )
    except ProcessingError as exc:
        logger.warning("Text processing failed: %s", exc)
        await update.message.reply_text(str(exc))


async def handle_photo(update, context):
    try:
        telegram_file = await context.bot.get_file(update.message.photo[-1].file_id)
        image_bytes = BytesIO()
        await telegram_file.download_to_memory(image_bytes)
        image_bytes.seek(0)
        image = Image.open(image_bytes)
        digest = hashlib.sha256(image_bytes.getvalue()).hexdigest()
        filepath, url = await save_content(
            update,
            f"Image input ({image.format or 'unknown'} format). Analyze the image in detail.",
            {
                "content_type": "image",
                "source_type": "telegram_image",
                "source_name": "Telegram image",
                "content_hash": digest,
            },
            update.message.caption,
            image,
        )
        await update.message.reply_text(f"Duplicate image already exists: {url}" if filepath is None else f"Image note saved: {url}")
    except (ProcessingError, OSError) as exc:
        logger.warning("Image processing failed: %s", exc)
        await update.message.reply_text("I could not process that image. Please send a readable image.")


async def handle_document(update, context):
    document = update.message.document
    extension = Path(document.file_name or "").suffix.lower()
    if extension not in SUPPORTED_EXTENSIONS:
        await update.message.reply_text(f"Unsupported file type: {extension or 'unknown'}.")
        return
    temp_path = None
    try:
        telegram_file = await context.bot.get_file(document.file_id)
        with tempfile.NamedTemporaryFile(prefix="ai-notes-", suffix=extension, delete=False) as temp:
            temp_path = temp.name
        await telegram_file.download_to_drive(temp_path)
        content = await run_blocking(extract_document, temp_path, extension)
        filepath, url = await save_content(
            update,
            content,
            {"content_type": extension.removeprefix("."), "source_type": "uploaded_file", "source_name": document.file_name},
            update.message.caption,
        )
        await update.message.reply_text(f"Duplicate document already exists: {url}" if filepath is None else f"Document saved: {url}")
    except ProcessingError as exc:
        logger.warning("Document processing failed: %s", exc)
        await update.message.reply_text(str(exc))
    except Exception as exc:
        logger.error("Document handling failed: %s", exc)
        await update.message.reply_text("The file could not be downloaded or processed.")
    finally:
        if temp_path:
            try:
                os.remove(temp_path)
            except OSError:
                logger.warning("Could not remove temporary file")


def extract_video_id(url: str):
    match = re.search(r"(?:v=|/|youtu\.be/|shorts/)([A-Za-z0-9_-]{11})", url)
    return match.group(1) if match else None


async def handle_youtube(update, context):
    video_id = extract_video_id(update.message.text)
    if not video_id:
        await update.message.reply_text("Please send a valid YouTube link.")
        return
    try:
        transcript = await run_blocking(YouTubeTranscriptApi.get_transcript, video_id, ["en", "en-US"])
        text = " ".join(item["text"] for item in transcript).strip()
        if not text:
            raise ProcessingError("This video has an empty transcript.")
        filepath, url = await save_content(
            update,
            text,
            {"content_type": "youtube_transcript", "source_type": "youtube", "source_name": video_id, "source_url": update.message.text},
        )
        await update.message.reply_text(f"Duplicate video already exists: {url}" if filepath is None else f"YouTube note saved: {url}")
    except ProcessingError as exc:
        logger.warning("YouTube processing failed: %s", exc)
        await update.message.reply_text(str(exc))
    except Exception as exc:
        logger.error("YouTube transcript failed: %s", exc)
        await update.message.reply_text("I could not fetch an English transcript for that video.")


def main():
    initialize_services()
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("list", list_files))
    application.add_handler(CommandHandler("search", search_command))
    youtube_regex = r"(?:https?://)?(?:www\.)?(?:youtube\.com/(?:watch\?v=|shorts/)|youtu\.be/)[\w-]{11}"
    application.add_handler(MessageHandler(filters.Regex(youtube_regex), handle_youtube))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    logger.info("Bot is running and polling for updates")
    application.run_polling()


if __name__ == "__main__":
    main()
