# Repository Guidelines

## Project Structure & Module Organization
This repository is a Lektor-based static site. Key locations:
- `content/`: Site content entries in `contents.lr` (e.g., `content/members/*/contents.lr`).
- `templates/`: Jinja2 templates and macros (`templates/macros/`).
- `assets/static/`: CSS, JS, fonts, and images served as static assets.
- `models/`: Lektor model definitions (`*.ini`).
- `packages/`: Local Lektor plugins (e.g., `packages/lektor-math-markdown/`).
- `www.yoavram.com.lektorproject`: Lektor project config.

## Build, Test, and Development Commands
Install dependencies:
- `python -m venv .venv && source .venv/bin/activate`
- `pip install -r requirements.txt`

Common Lektor tasks:
- `lektor server` (or `lektor serve`): Run a local dev server with live rebuilds.
- `lektor build`: Generate the static site into the build output directory.
- `lektor clean`: Remove the build output (useful before a clean rebuild).

## Coding Style & Naming Conventions
- Indentation: follow existing files; CSS and templates generally use 4 spaces.
- Content entries use lowercase, hyphenated slugs for directories (e.g., `content/members/yoav-ram/`).
- Keep field names in `contents.lr` and `models/*.ini` consistent with existing models.
- Templates are Jinja2; prefer existing macro patterns in `templates/macros/`.

## Testing Guidelines
There are no automated tests in this repo. Validate changes by running `lektor serve` and checking affected pages in the browser. For template or plugin changes, spot-check relevant pages and navigation paths.

## Commit & Pull Request Guidelines
Commit messages in this repo are short, imperative sentences (e.g., “Fix typo in …”, “Update contents.lr”). Keep them concise and specific.

PRs should include:
- A clear description of what changed and why.
- Links to relevant pages or content entries.
- Screenshots for visual/template changes when applicable.

## Deployment
Deployments are handled by Netlify via a GitHub hook. Pushing to GitHub triggers a new Netlify build and deploy automatically for the `www.yoavram.com` site.
