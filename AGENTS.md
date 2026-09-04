# Repository Guidelines

## Start Here: Load the Current Context

Before substantive work, read `PŘEHLED.md`, `PLAN.md`, `POZADAVKY_UCITELE.md`, and `ZDROJE.md`. Then load `AHP_NAVOD_SAATY.md` for calculations, `CYKLOSERVIS_ZADANI.md` and `docker/README.md` for tool tests, or the relevant `BP <number>.md` chapter for writing. `.agents/AGENTS.md` describes an older seminar-paper layout; do not treat it as current.

Discover project Markdown (excluding bundled third-party documentation) with `rg --files -g "*.md" -g "!nastroje/**"`. Read a file exactly in PowerShell with `Get-Content -Raw -LiteralPath '.\PLAN.md' -Encoding UTF8`. Re-check dated status instead of assuming it is still current.

## Project Structure & Module Organization

This is a Czech bachelor-thesis workspace, not an application. Edit numbered chapter sources `BP 0.md` through `BP 15.md`; `BP.md` is generated. Files 0–3 contain front matter, introduction, objectives, and methodology; 4–8 contain theory, tools, and criteria; 9–13 contain the practical study and conclusion; 14–15 contain references and appendices. Treat `seminární práce/` as read-only. Assignment PDFs are in `zadani/`, research in `literatura/`, installers in `nastroje/`, and databases in `docker/`.

## Build, Test, and Development Commands

- `.\spoj.ps1` rebuilds `BP.md` from chapters 0–15 and warns about remaining work markers.
- `.\spoj.ps1 2 3 8 -Out vyber.md` creates a selected-chapter draft without replacing `BP.md`.
- `.\extrahuj.ps1` generates citation-free `BP 4x.md` through `BP 7x.md` review copies.
- `docker compose --env-file docker/.env -f docker/docker-compose.yml config` validates the Compose configuration.
- `cd docker; docker compose up -d; docker compose ps` starts and checks MySQL, PostgreSQL, and Oracle.

Run scripts from PowerShell at the repository root.

## Writing Style & Naming Conventions

Write in formal Czech and save Markdown as UTF-8. Preserve the `BP <number>.md` naming pattern and heading hierarchy. Use author-year citations compliant with ISO 690:2022. Cite only checked sources and synchronize bibliography details with `ZDROJE.md`. The review prompts in `.claude/commands/` apply only to documents that actually contain their legacy `***` block structure.

Search `rg -n -g "BP *.md" "BP-(ZMĚNA|DOPLNIT|OVĚŘIT)" .` before handoff. `BP-ZMĚNA` identifies rewritten passages; `BP-DOPLNIT` and `BP-OVĚŘIT` must be resolved before submission. Never invent test values, AHP matrices, rankings, or conclusions.

## Verification Guidelines

There is no automated test suite. After chapter changes, rebuild `BP.md` and inspect headings, order, Czech characters, citations, and the final newline. Validate Docker edits with Compose configuration and health checks. Because Google Drive can corrupt newly written binaries asynchronously, verify generated DOCX, XLSX, or PDF files twice, several seconds apart.

For the final BP document use `oliva/sablony/šablona( nová (1).docx`, not the seminar-paper template. Use Cambria or Times New Roman 12 pt, line spacing 1.5, a 3.5 cm left margin and 2 cm on the other sides. Page numbering begins with the introduction on page 1. Keep one alphabetic bibliography without grouping by source type. Describe any use of AI tools in the methodology, including the tool, version, purpose, method, and scope. When producing a binary document in this Google Drive workspace, retain a known-good copy outside the synchronized destination and re-check the destination more than once before handoff.

## Commit & Pull Request Guidelines

History uses milestone-style subjects such as `30`, `30-1`, and `31-1`. Keep commits focused with a concise document or milestone subject. Pull requests should summarize affected chapters, justify structural or citation changes, list verification, and include screenshots only for layout changes. Never commit `docker/.env`, credentials, installers, or large local research files.
