# Intelligent Video Assistant

A staged implementation of the video-to-knowledge workflow described in `ppt_review1.pdf`:

`video file or YouTube URL -> audio extraction -> Whisper transcript -> TextRank/NLP -> GPT-4o-mini summary and action items -> structured document -> persistent storage -> search/retrieve/download`

## Confirmed technology direction

- Python
- Streamlit
- LangChain
- OpenAI GPT-4o-mini
- Whisper for speech-to-text
- TextRank for extractive importance ranking
- SQLite and JSON for persistence/configuration
- Requests and BeautifulSoup for webpage content
- Tavily API for optional web research
- Git/GitHub and VS Code

## Collaboration rule

This repository is intentionally being built in small milestones. Each milestone should be completed, tested, reviewed, and committed separately. Do not implement the whole pipeline in one change.

Suggested branch names:

- `main`: reviewed milestones only
- `feat/auth`
- `feat/video-input`
- `feat/transcription`
- `feat/analysis`
- `feat/documents`
- `feat/search`

## Milestones

1. Repository contract and environment setup (current)
2. Login and session persistence
3. Video URL/file intake and input validation
4. Audio extraction and Whisper transcription
5. TextRank key-sentence extraction
6. GPT-4o-mini structured summary, topics, and action items
7. SQLite document storage and retrieval
8. Search and download
9. Integration tests, security review, and deployment

## Start the repository

Run these commands from this folder:

```powershell
git init
git add .
git status
git commit -m "chore: establish project contract"
```

The next implementation slice is milestone 2: authentication and session persistence. No API keys belong in Git; use a local `.env` file when that slice begins.
