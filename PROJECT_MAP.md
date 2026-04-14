# Project map — applypilot.ai

This document merges the repository layout into a single map: **what lives where**, **how the pieces connect**, and **what is generated locally** versus **tracked in Git**.

## Architecture (one repo, two runtimes)

| Area | Path | Role |
|------|------|------|
| **Domain (Python)** | `src/applypilot/` | Job-application domain models and status transitions (library; no web dependency). |
| **Web (Next.js)** | `web/` | UI and API surface for the product; Docker/Vercel/GitHub Pages targets. |
| **Tests (Python)** | `tests/` | `pytest` for the domain package. |
| **Automation** | `.github/workflows/` | Web CI, optional GitHub Pages static deploy, optional Vercel CLI deploy. |
| **Root metadata** | `pyproject.toml`, `README.md`, `AGENTS.md` | Package definition, human docs, agent-oriented notes. |

There is **no separate “fork” folder**: prior workstreams are merged into **`main`**; feature branches exist only as Git refs on the remote.

## Directory tree (source tracked in Git)

```
applypilot.ai/
├── AGENTS.md                 # Agent / contributor notes (repo-wide)
├── PROJECT_MAP.md            # This file — layout and navigation
├── README.md                 # Setup: web + Python + deploy
├── pyproject.toml            # Python package: applypilot
├── .gitignore                # Root ignores (Python venv, caches, etc.)
├── src/
│   └── applypilot/
│       ├── __init__.py
│       └── domain.py         # JobApplication, ApplicationStatus, …
├── tests/
│   └── test_domain.py
├── web/                      # Next.js 16 app (App Router)
│   ├── AGENTS.md / CLAUDE.md # Next-specific agent hints
│   ├── Dockerfile            # Standalone Node image for container hosts
│   ├── README.md
│   ├── eslint.config.mjs
│   ├── next.config.ts        # standalone vs static export (Pages)
│   ├── package.json
│   ├── package-lock.json
│   ├── postcss.config.mjs
│   ├── tsconfig.json
│   ├── public/               # Static assets (SVG, etc.)
│   └── src/app/              # Routes, layout, global styles, favicon
└── .github/
    └── workflows/
        ├── web-ci.yml                    # Lint + build on web/ changes
        ├── deploy-github-pages.yml     # Static export → Pages (gated deploy)
        └── vercel-deploy.yml           # Manual optional Vercel CLI deploy
```

## Local-only / generated (not committed)

These appear after install or build; they are normal and reproducible.

| Path | Created by | Purpose |
|------|--------------|---------|
| `web/node_modules/` | `npm ci` or `npm install` in `web/` | JavaScript dependencies. |
| `web/.next/` | `npm run build` or `next dev` | Next.js build cache and output. |
| `web/out/` | `NEXT_OUTPUT_MODE=export` + build | Static export for GitHub Pages. |
| `.venv/` | `python3 -m venv .venv` | Python tooling and editable install. |

## How to restore a full working tree

1. **Clone** the repository (includes `.git` history).
2. **Web:** `cd web && npm ci`
3. **Python:** create `.venv`, then `pip install -e ".[dev]"` from repo root.
4. **Run web:** `cd web && npm run dev`
5. **Run tests:** `pytest` (from venv, repo root).

## Archives (generated locally; ignored by Git)

| File | Contents |
|------|----------|
| **`applypilot.ai-complete.zip`** | Entire project folder on disk: `.git`, `web/node_modules`, `web/.next` if present, etc. Large; use for a full offline mirror. |
| **`applypilot.ai-source.zip`** | `git archive` at current `HEAD` — tracked source only (no `node_modules`, no `.git`). Small; use for sharing or clean backup. |

Regenerate from the repository root:

```bash
npm run zip
```

This runs [`scripts/zip-project.sh`](./scripts/zip-project.sh) (same as the manual `zip` / `git archive` commands documented previously).
