# applypilot.ai

Web application lives in [`web/`](./web/) (Next.js App Router, TypeScript, Tailwind CSS).

Core domain models for tracking job applications live in [`src/applypilot/`](./src/applypilot/).

## Local development

### Web frontend

```bash
cd web
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

### Python domain package

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
pytest
```

## Scripts

| Command         | Description          |
| --------------- | -------------------- |
| `npm run dev`   | Development server   |
| `npm run build` | Production build     |
| `npm run start` | Run production server|
| `npm run lint`  | ESLint               |
| `pytest`        | Python domain tests  |

## Usage example

```python
from datetime import date
from applypilot import ApplicationStatus, JobApplication

app = JobApplication(
    company="OpenAI",
    role="Software Engineer",
    source="Careers page",
    applied_on=date.today(),
)

app.transition_to(ApplicationStatus.APPLIED)
app.transition_to(ApplicationStatus.INTERVIEW)
app.transition_to(ApplicationStatus.OFFER)
```

## Deployment (web / hosting)

The Next.js app is under **`web/`**. Production hosting is easiest on **[Vercel](https://vercel.com)** (native Next.js support).

### Option A — Vercel + GitHub (recommended)

1. Import this repo in the [Vercel dashboard](https://vercel.com/new).
2. Set **Root Directory** to `web` (required because the app is not at the repo root).
3. Leave **Build Command** as `npm run build` and **Output** as default for Next.js.
4. Deploy. Every push to the connected branch triggers a new deployment.

### Option B — Manual CLI (from your machine)

```bash
cd web
npx vercel login
npx vercel        # preview
npx vercel --prod
```

### Option C — GitHub Actions

A workflow is defined at [`.github/workflows/vercel-deploy.yml`](./.github/workflows/vercel-deploy.yml). It runs only when you trigger it manually (`workflow_dispatch`) and expects `VERCEL_TOKEN`, `VERCEL_ORG_ID`, and `VERCEL_PROJECT_ID` in the repo secrets. Use this if you prefer CI deploys instead of Vercel’s built-in Git integration.
