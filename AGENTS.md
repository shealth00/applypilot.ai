# AGENTS.md

## Cursor Cloud specific instructions

### Project overview

applypilot.ai is a job application tracking tool with two components:

| Component | Location | Tech | Run |
|-----------|----------|------|-----|
| Web frontend | `web/` | Next.js 16, React 19, TypeScript, Tailwind CSS 4 | `cd web && npm run dev` (port 3000) |
| Domain package | `src/applypilot/` | Python 3.12, pytest | `source .venv/bin/activate && pytest` |

### Caveats

- The `main` branch only has a README. All code lives on feature branches (`cursor/project-development-a1b1` for web, `cursor/project-continuation-e0bc` for Python). Both must be merged before working with the full codebase.
- `python3.12-venv` must be installed (`sudo apt-get install -y python3.12-venv`) before creating the Python venv. The update script handles this.
- Next.js 16 has breaking API changes from earlier versions. See `web/AGENTS.md` — always check `node_modules/next/dist/docs/` before writing Next.js code.
- The Python package has no runtime dependencies; `pytest` is the only dev dependency.
- ESLint config uses the flat config format (`eslint.config.mjs`) with `eslint-config-next`.

### Commands reference

See `README.md` for the full scripts table. Key commands:

- **Lint (frontend):** `cd web && npm run lint`
- **Build (frontend):** `cd web && npm run build`
- **Dev server (frontend):** `cd web && npm run dev`
- **Python tests:** `source .venv/bin/activate && pytest`
