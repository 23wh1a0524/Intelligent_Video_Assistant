# Project Plan

## Product boundary

The application turns long meeting recordings and YouTube videos into reusable knowledge documents. A document contains the source, transcript metadata, main theme, concise summary, key topics, important points, and action items.

## Model responsibilities

`gpt-4o-mini` is used for language understanding and structured report generation after transcription. It should receive transcript chunks or a condensed transcript and return validated structured fields. It is not responsible for downloading video, extracting audio, or replacing the deterministic TextRank step.

## Functional requirements

- Users can create an account and log in.
- A logged-in user can submit a supported video URL or local video input.
- The input is validated before processing.
- The system extracts audio and creates a transcript with Whisper.
- The system identifies important sentences with TextRank.
- The system generates a main theme, summary, topics, important points, and action items with GPT-4o-mini.
- Each result is stored under the authenticated user's session.
- Users can search, open, and download their own generated documents.
- Users cannot access another user's documents.

## Incremental delivery

### Milestone 1: repository contract

Done when the repository has Git hygiene, an agreed stack, a staged plan, and no runtime secrets.

### Milestone 2: authentication and sessions

Deliver a minimal Streamlit login flow backed by SQLite. Store password hashes, not passwords. Add tests for registration, login failure, session restoration, and user isolation.

### Milestone 3: input boundary

Accept and validate a URL first. Add local file input only after URL validation is tested. Store a source record before expensive processing so failures are visible.

### Milestone 4: media and transcription

Add audio extraction and Whisper behind a service boundary. Test with a short fixture and make processing status explicit.

### Milestone 5: analysis

Implement TextRank extraction, then call GPT-4o-mini with a strict JSON schema. Validate model output and persist the main theme alongside the report.

### Milestone 6: document lifecycle

Persist transcript metadata and structured reports in SQLite. Add ownership checks, search, document detail, and download.

### Milestone 7: integration and collaboration

Add end-to-end tests, rate/size limits, error handling, cleanup of temporary media, deployment configuration, and a GitHub pull-request workflow.

## Decisions to revisit

- Whether Whisper runs locally or through a hosted transcription API.
- Which YouTube downloader is approved for the project and its usage constraints.
- Whether Tavily is needed for video research or remains optional.
- Deployment target and SQLite backup strategy.
