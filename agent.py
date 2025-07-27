import os
import google.generativeai as genai
import fitz  # PyMuPDF
from youtube_transcript_api import YouTubeTranscriptApi
import requests
import argparse

# --- Configuration ---
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

# --- Helper Functions ---
def get_text_from_youtube(url):
    """Fetches the transcript from a YouTube URL."""
    try:
        video_id = url.split("v=")[1].split("&")[0]
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([d['text'] for d in transcript_list])
    except Exception as e:
        print(f"Error getting YouTube transcript: {e}")
        return None

def get_text_from_pdf(file_path):
    """Extracts text from a local PDF file."""
    try:
        with fitz.open(file_path) as doc:
            return "".join(page.get_text() for page in doc)
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def generate_notes(content, file_name):
    """Generates markdown notes using the Gemini AI."""
    prompt = f"""
    Based on the following content, create detailed, well-structured notes in Markdown format.
    The notes should have a clear title, headings, bullet points, and bold key terms.
    The final output should ONLY be the markdown content, with no extra explanations.

    Content:
    {content[:15000]}
    """ # Slicing content to respect token limits if necessary
    
    try:
        response = model.generate_content(prompt)
        # Save the markdown notes to a file
        with open(file_name, "w") as f:
            f.write(response.text)
        print(f"Notes successfully generated and saved to {file_name}")
        return response.text
    except Exception as e:
        print(f"Error generating notes: {e}")
        return None

def send_notification(file_name):
    """Sends a notification to a webhook."""
    webhook_url = os.environ.get("WEBHOOK_URL")
    if not webhook_url:
        return # Silently fail if no webhook is configured

    data = {
        "content": f"✅ New AI notes have been generated and uploaded: `{file_name}`"
    }
    requests.post(webhook_url, json=data)


# --- Main Execution Logic ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Note-Taking Agent")
    parser.add_argument("--youtube-url", help="URL of the YouTube video")
    parser.add_argument("--pdf-file", help="Path to the PDF file")
    parser.add_argument("--text-content", help="Raw text content")
    parser.add_argument("--output-name", help="Name of the output markdown file (e.g., 'My-Awesome-Notes')", required=True)
    
    args = parser.parse_args()

    content = ""
    source_type = ""

    if args.youtube_url:
        print(f"Processing YouTube URL: {args.youtube_url}")
        content = get_text_from_youtube(args.youtube_url)
        source_type = "YouTube"
    elif args.pdf_file:
        print(f"Processing PDF file: {args.pdf_file}")
        content = get_text_from_pdf(args.pdf_file)
        source_type = "PDF"
    elif args.text_content:
        print("Processing raw text...")
        content = args.text_content
        source_type = "Text"

    if content:
        output_filename = f"{args.output_name.replace(' ', '-')}.md"
        notes = generate_notes(content, output_filename)
        if notes:
            send_notification(output_filename)
    else:
        print("No content could be extracted. Exiting.")