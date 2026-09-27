# Barrier2Action

Barrier2Action turns one accessibility photo into a cautious, evidence-based action report. It identifies visible barriers, separates uncertainty from observation, suggests what to photograph next, and helps route a case to a responsible reporting channel.

## What it does

- Uploads JPG, PNG, WebP, or AVIF images
- Uses Gemini multimodal analysis with structured Pydantic output
- Validates contradictory AI findings before displaying them
- Reports visible evidence, affected users, confidence, and practical actions
- Requests closer follow-up evidence when a view is insufficient
- Generates case IDs, local audit history, and downloadable reports
- Includes dark mode and an accessibility toolbar with text scaling, high contrast, reduced motion, OpenDyslexic, Atkinson Hyperlegible, and read-aloud controls

## Stack

- Vue 3 + TypeScript + Vite
- FastAPI + Pydantic
- Google Gemini API via `google-genai`
- Pillow and AVIF support
- Render backend + Vercel frontend deployment

## Run locally

Backend:

```powershell
cd backend
python -m pip install -r requirements.txt
Copy-Item .env.example .env
# Add GEMINI_API_KEY to backend/.env
python -m uvicorn app.main:app --reload --port 8000
```

Frontend, in a second terminal:

```powershell
cd frontend
npm install
Copy-Item .env.example .env
npm run dev
```

Open `http://localhost:5173`.

## Deploy

### Backend on Render

Create a new Render Blueprint from this repository using `render.yaml`. Set:

- `GEMINI_API_KEY`
- `FRONTEND_ORIGIN` to the deployed Vercel URL

### Frontend on Vercel

Import the repository, set the project root to `frontend`, and add:

```text
VITE_API_BASE_URL=https://your-render-service.onrender.com
```

Deploy after setting the environment variable.

## Important limitation

Barrier2Action is a visual screening assistant, not professional accessibility certification or legal compliance advice. Exact dimensions, gradients, unseen routes, and legal compliance require on-site verification.

