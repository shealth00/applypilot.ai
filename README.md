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
```

## Scripts

| Command         | Description          |
| --------------- | -------------------- |
| `npm run dev`   | Development server   |
| `npm run build` | Production build     |
| `npm run start` | Run production server|
| `npm run lint`  | ESLint               |
| `pytest`        | Python domain tests  |

## Deploy / host (web)

The Next.js app supports two build modes (see [`web/next.config.ts`](web/next.config.ts)):

| Mode | When | Output |
|------|------|--------|
| **standalone** (default) | `npm run build` with no extra env | Node server; used by [`web/Dockerfile`](web/Dockerfile), Vercel, etc. |
| **static export** | `NEXT_OUTPUT_MODE=export` | Static files for GitHub Pages |

### Option A: Vercel (simplest for Next.js)

1. Push `main` to GitHub (already the default remote).
2. In [Vercel](https://vercel.com), **Add New Project** → import this repo.
3. Set **Root Directory** to `web`, then deploy. Vercel runs `npm run build` and hosts the app on a `*.vercel.app` URL (add a custom domain under Project Settings → Domains).

### Option B: Docker (Fly.io, Railway, ECS, etc.)

From the repository root:

```bash
docker build -f web/Dockerfile -t applypilot-web web
docker run -p 3000:3000 applypilot-web
```

Open [http://localhost:3000](http://localhost:3000). Push the image to a registry and run it on your platform of choice.

### Option C: GitHub Pages (static)

On pushes to `main`, [`.github/workflows/deploy-github-pages.yml`](.github/workflows/deploy-github-pages.yml) builds with `NEXT_OUTPUT_MODE=export` and deploys the `web/out` folder to GitHub Pages.

- **Live URL (after Pages is enabled):** `https://shealth00.github.io/applypilot.ai/`
- **One-time setup:** **Settings → Pages → Build and deployment** → source **GitHub Actions**.

The workflow sets `NEXT_PUBLIC_BASE_PATH=/applypilot.ai` so assets resolve under the default project Pages path.

### CI

[`.github/workflows/web-ci.yml`](.github/workflows/web-ci.yml) runs lint and production build on pushes and PRs that touch `web/`.

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
