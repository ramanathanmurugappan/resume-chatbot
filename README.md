# Resume Chatbot

An interactive resume chatbot built with Flask that lets you chat with Ramanathan Murugappan's resume — styled as a WhatsApp conversation with a live AI assistant.

Live demo: https://resume-chatbot-9860.onrender.com

## Features

- **WhatsApp-style chat UI** — message bubbles, timestamps, typing indicator, and a doodle background
- **AI-powered Q&A** — ask anything about skills, projects, or experience; answered in first person as Ramanathan
- **LLM fallback chain** — Groq (Llama 3.3 70B → Llama 3.1 70B → Llama 3.1 8B → Llama 3 8B) → Gemini 2.0 Flash as last resort, via LiteLLM
- **Streaming responses** — answers stream token-by-token in real time
- **Download PDF** — one-click resume PDF export via html2pdf.js
- **Prompt injection guard** — regex-based filter blocks adversarial inputs before they reach the LLM
- **Text-to-chat** — select any text in the resume panel to instantly ask about it in the chat
- **macOS Sonoma wallpaper** — layered CSS radial gradients as the page background with canvas doodles
- **Dockerized** — ready to deploy on Render.com or any container platform

## Tech Stack

| Layer | Tech |
|---|---|
| Backend | Python, Flask |
| LLM routing | LiteLLM |
| LLM providers | Groq (Llama 3.x), Google Gemini |
| Frontend | Vanilla JS, HTML/CSS |
| PDF export | html2pdf.js |
| Containerization | Docker |
| Hosting | Render.com |

## Setup

### 1. Clone

```bash
git clone https://github.com/ramanathanmurugappan/resume-chatbot.git
cd resume-chatbot
```

### 2. Environment variables

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
GEMINI_API_KEY=your_gemini_api_key
```

### 3. Run locally

```bash
pip install -r requirements.txt
python app.py
```

App runs at `http://localhost:5001`.

### 4. Run with Docker

```bash
docker build -t resume-chatbot .
docker run -d -p 5001:5001 --env-file .env resume-chatbot
```

### 5. Deploy to Render.com

- Connect your GitHub repo on Render.com
- Add `GROQ_API_KEY` and `GEMINI_API_KEY` as environment variables
- Use the existing `render.yaml` for configuration

## Project Structure

```
resume-chatbot/
├── app.py               # Flask app, LiteLLM routing, streaming, injection guard
├── Dockerfile
├── requirements.txt
├── render.yaml
└── templates/
    └── index.htm        # Single-page UI (resume panel + WhatsApp chat)
```
