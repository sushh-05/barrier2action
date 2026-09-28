# Barrier2Action - See the Barrier, Start the Change

🏆 **1st Place — Campulsy Hack Days × MLH × Gemini**

## Live Demo

[https://barrier2action.vercel.app/](https://barrier2action.vercel.app/)

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
- Vercel full-stack deployment with FastAPI serverless functions

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

## Deploy on Vercel

Import this repository into Vercel with the repository root as the project root.
The committed `vercel.json` builds the Vue frontend and routes `/api/*` to the
FastAPI serverless function.

Set these environment variables:

```text
GEMINI_API_KEY=your_actual_key
GEMINI_MODEL=gemini-2.5-flash-lite
FRONTEND_ORIGIN=https://barrier2action.vercel.app
MAX_IMAGE_MB=8
```

The live deployment is:

```text
https://barrier2action.vercel.app/
```

## Important limitation

Barrier2Action is a visual screening assistant, not professional accessibility certification or legal compliance advice. Exact dimensions, gradients, unseen routes, and legal compliance require on-site verification.
