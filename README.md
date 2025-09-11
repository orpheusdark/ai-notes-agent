# 🤖 AI Notes Agent for Telegram

Welcome to **AI Notes Agent** — your personal AI-powered content processor for Telegram!
This bot receives content like **text, images, documents**, and even **YouTube links**, and automatically creates clean, concise, and structured **Markdown notes**.
All notes are stored right here in this GitHub repository — creating your own **searchable knowledge base**, effortlessly. 🧠📚

## @MyContentProcessorBot

---

## 🎯 Project Goal

Build a **zero-cost, fully automated** content pipeline — where any interesting idea, resource, or piece of knowledge can be captured, processed by AI, and stored — all by sending a message to a Telegram bot.
No manual effort. No financial cost. Just seamless **AI-driven note creation**. 💡🚀

---

## ✨ Features

This bot is a Swiss Army knife of content processing! Here's what it can do:

### 📦 Multi-Content Processing
- 📝 **Plain Text** — Just send a message.
- 🖼️ **Images** — Get detailed visual descriptions.
- 📄 **Documents** — Supports `.pdf`, `.docx`, `.pptx`, `.csv`, `.xlsx`, and `.txt` files.
- 🔗 **YouTube Links** — Summarizes English transcripts.

### 🧠 AI-Powered Summarization
Uses **Google's Gemini AI** to generate rich, structured notes with:
- A **main title** and **executive summary**
- Headings, subheadings, and bullet points
- *Bold* and _italic_ emphasis
- 🎨 Emojis for visual clarity

### 📁 Smart File Naming
- Filenames like `Introduction-to-Data-Structures.md` are AI-generated, descriptive, and URL-safe. ✍️

### 🗣️ Custom Prompts
- Add custom instructions via captions
  _Example: "Create a 5-question quiz from this document."_

### 💬 Telegram Bot Commands
- `/start` — Friendly welcome message
- `/help` — List of all features & how-tos
- `/list` — Shows 5 latest saved notes with links

---

## 🛠️ How It Works (Tech Stack)

This project brings together several free-tier tools:

| Layer        | Tech Used                        |
|--------------|----------------------------------|
| Interface    | [Telegram Bot](https://core.telegram.org/bots/api) 📱  |
| Logic        | Python script 🐍                 |
| Hosting      | [PythonAnywhere](https://www.pythonanywhere.com/) ☁️ |
| Intelligence | [Gemini 1.5 Flash](https://ai.google.dev/) 🤖 |
| Storage      | GitHub Repository 🗃️              |

---

## 🚀 Current Status: **Fully Functional**

✅ Bot is live on PythonAnywhere
✅ Gemini AI is processing all inputs
✅ Markdown notes are saved directly to this repo
✅ Telegram interface is stable and user-friendly

---

## 🚧 Challenges Faced

Here’s the dirt from the trenches:

### 🏠 Finding a Free Host
- Most “free” platforms like Render and Fly.io had hidden limits or required cards.
- **PythonAnywhere** (with an open console) met the truly free, 24/7 requirement.

### 🔐 GitHub Auth Woes
- Faced `401: Bad credentials` errors.
- Fixed by generating a **GitHub Personal Access Token** with `repo` scope and properly configuring it in the script.

### 📉 API Model Deprecation
- Initially used `gemini-pro`, which led to `404` errors.
- Switched to `gemini-1.5-flash`, which is faster and more reliable.

### 🧩 Library Versioning
- Upgraded to the latest `python-telegram-bot` library.
- Refactored code using `Application.builder()` and `async` methods.

---

## 🤝 Contributing

Pull requests are welcome!
Feel free to fork the repo, suggest features, or help squash bugs. 🐛

---

## 📜 License

MIT License © 2025 — Made with ❤️ for the open-source community.

---

> _"Turn your Telegram into a knowledge vault. Let AI do the heavy lifting."_ ⚡
> — **AI Notes Agent**
