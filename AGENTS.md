# Repository Guidelines

Czech bachelor-thesis workspace for Roman Janiš (FIM UHK). Topic: *Komparace nástrojů pro návrh a vývoj databázových systémů pomocí AHP*. Supervisor: Ing. et Ing. Martin Lněnička, Ph.D. This is not an application repository yet; the PHP app is planned, not started.

On Windows this file is the same as `Agents.md`. `.agents/AGENTS.md` describes an older seminar-paper layout; do not treat it as current.

## Start Here

Before substantive work, re-read dated status in `PLAN.md`, then `EMAIL_KONVERZACE.md` and `ZDROJE.md`. Load extra files only as needed:

- Goal / STAG proposal (source of truth for title, goal, outline, assignment literature; not yet sent): `EMAIL_VEDOUCIMU_A_CIL_BP.md`.
- Detailed step-by-step execution plan (phases 0, A–H with concrete file/Excel/app/chapter steps): `PLAN.md`.
- AHP calculations: `AHP_NAVOD_SAATY.md` (recompute the worked example before treating it as a specification).
- Tool tests: `CYKLOSERVIS_ZADANI.md`, `docker/README.md`.
- Writing: the relevant `BP <n>.md` chapter.
- Outline mapping (older 7-point draft; for STAG and PLAN the **6-point outline in the email** wins): `VYSVETLENI_OSNOVY_A_NAVAZNOST_NA_SEMINARKU.md`.

Discover project Markdown with `rg --files -g "*.md" -g "!nastroje/**"`. Read files in PowerShell with `Get-Content -Raw -LiteralPath '.\PLAN.md' -Encoding UTF8` so Czech path characters stay intact.

## Current Status (13 September 2026)

`EMAIL_VEDOUCIMU_A_CIL_BP.md` is the current proposal of title, goal, 6-point outline, and five assignment sources. It is prepared to send; the supervisor has not approved it. Do not treat it as an approved STAG assignment.

`PLAN.md` is the full roadmap to submission (phases 0, A–H), aligned to that email. Phase A locks **scope only** (app purpose, four alternatives, K1–K8, one Cykloservis case, three sensitivity changes) — that is not a finished thesis. Next real work is phase B (data design, one AHP procedure, small control example), then C–D (minimal PHP app + verify), E–F (tool tests → pairwise matrices → run + sensitivity), G–H (write BP text, formal DOCX, submit).

**Do not rewrite BP chapters yet** to match the new goal. `BP 0.md`–`BP 3.md` and `BP 9.md` still use seminar framing. After supervisor approval and practical results, reframe them in phase G.

Immediate work: send `EMAIL_VEDOUCIMU_A_CIL_BP.md`; after the reply, edit STAG (phase 0). In parallel start phase B (AHP spec + control example) and tool install notes for phase E. Do not start full PHP coding before phase B.

STAG assignment-sheet deadline: 15 October 2026. The thesis needs at least 30 used sources, of which at least 20 are books or journal articles. `ZDROJE.md` already tracks 27 seminar items plus 3 approved extras; bibliography edits belong in `BP 10.md` and must stay in sync with `ZDROJE.md`.

## Locked Decisions

Keep these unless the supervisor changes them. They match `EMAIL_VEDOUCIMU_A_CIL_BP.md` plus working detail in `PLAN.md`:

- **Contribution / goal:** design, implement, and verify a simple PHP web AHP app for choosing tools for *návrh a vývoj databázových systémů*; verify on one model case. Comparing tools is the demonstration domain, not a second parallel thesis.
- **Terminology:** “návrh a vývoj databázových systémů”. Operating, backup, and DBMS performance are out of scope (email: správa serverů, zálohování, výkon).
- **Alternatives:** four tools from the seminar paper — Oracle SQL Developer Data Modeler; DBeaver Community Edition; MySQL Workbench Community Edition; pgModeler. Record exact editions/versions from the installs actually tested. Free, open-source, and paid distributions are not the same.
- **Criteria K1–K8:** modelling functionality; usability; DBMS compatibility; forward engineering; reverse engineering; documentation and community; model import/export; cost and licence. “Převážně objektivní” describes evidence, not automatic pairwise scores. Keep K1, K4, K5, and K7 distinct; do not score the same DDL twice in K7.
- **App baseline (from email):** prepared lists with descriptions and links; optional custom items; pairwise comparisons; computed ranking. Working detail in PLAN also includes automatic reciprocals, input checks, weights and consistency, recalculation. No accounts, roles, admin, REST API, or product-data scraping in the baseline. Extensibility to another decision domain may be described rather than implemented.
- **Scenario:** one model case (working name Cykloservis). The decision-maker is a developer choosing a modelling tool before a DBMS is fixed. The author is the single evaluator; that limitation must be stated. The sent goal text says only “modelový případ”, not the name Cykloservis.
- **Sensitivity:** three separate changes to criteria importance (working detail: stricter budget / K8, more modelling / K1, broader DBMS support / K3). Alternative matrices stay unchanged. Unchanged ranking is a valid result.
- **Verification:** independent control calculation of AHP results; form still an open question to the supervisor in the email (other tool vs manual/Excel).
- **STAG outline (6 points from email):** (1) relational DB design problem, (2) AHP and consistency, (3) tools and criteria, (4) PHP AHP app, (5) verify calculations and model case + sensitivity, (6) results, limits, further extension.

## Project Structure

Edit numbered chapter sources. `BP.md` is generated.

| Files | Role now |
|---|---|
| `BP 0.md`–`BP 3.md` | Front matter, introduction, objectives, methodology (**still seminar framing**; do not rewrite until goal is approved). |
| `BP 4.md`–`BP 8.md` | Theory, tools, criteria. Keep unless a documented error or required continuity change. |
| `BP 9.md` | Seminar conclusion. Do not present it as the finished BP conclusion. |
| `BP 10.md` | Bibliography. |
| `BP 11.md`–`BP 15.md` | Not present. Older instructions and `spoj.ps1` still assume 0–15. Do not rebuild `BP.md` from an incomplete chapter set. |

Treat `seminární práce/` as read-only. Assignment PDFs are in `zadani/`, research in `literatura/`, Cykloservis artefacts in `cykloservis/`, databases in `docker/`. Installers belong in `nastroje/` (gitignored; currently absent). Working Excel `hodnoceni_4_nastroju.xlsx` stays empty until alternatives and criteria stay locked and real tests exist.

When rewriting an existing chapter later, keep under a horizontal rule a dated block “Pracovní poznámka – původní znění před úpravou, datum, důvod” with the exact original passage. Those blocks are working comparison only and must be excluded from the final assembly. `BP 8.md` already has such a draft section.

## Commands

Run from PowerShell at the repository root.

- `.\spoj.ps1` — joins `BP 0.md`–`BP 15.md` into `BP.md` and warns about leftover work markers. Currently fails or is incomplete because chapters 11–15 do not exist.
- `.\spoj.ps1 2 3 8 -Out vyber.md` — selected-chapter draft; use `-Out` so `BP.md` is not overwritten.
- `.\extrahuj.ps1` — citation-free `BP 4x.md`–`BP 7x.md` review copies (drops `>` blockquote lines).
- `docker compose --env-file docker/.env -f docker/docker-compose.yml config` — validate Compose.
- From `docker/`: `docker compose up -d` then `docker compose ps`. Stack: MySQL 8 (`mes-mysql:3306`), PostgreSQL 16 (`mes-postgres:5432`), Oracle Free 23 (`mes-oracle:1521`).

## Writing and Citations

Write formal Czech, UTF-8 Markdown. Keep `BP <n>.md` names and heading hierarchy. Cite author-year per ISO 690:2022. Cite only checked sources. Sync bibliography details with `ZDROJE.md`. Do not cite files in `literatura/inspirace/`. One alphabetic bibliography; do not group by source type.

Current `BP 0.md`–`BP 10.md` do **not** use the legacy `***` two-layer blocks. The prompts in `.claude/commands/` apply only to documents that still have that structure (mainly `seminární práce/`).

Search `rg -n -g "BP *.md" "BP-(ZMĚNA|DOPLNIT|OVĚŘIT)|⟦"` before handoff. `BP-ZMĚNA` marks rewritten passages. `BP-DOPLNIT`, `BP-OVĚŘIT`, and `⟦...⟧` placeholders must be gone before submission.

## Hard Constraints

- Never invent test values, AHP matrices, rankings, CR figures, tool versions, prices, or conclusions.
- Do not start coding the full PHP app before PLAN phase B (AHP + data spec) is done; implement in phase C.
- Do not rewrite BP chapters solely to match the new email goal until the supervisor responds (plan and goal docs first).
- Do not add extra scenarios, group AHP, questionnaires, extra MCDM methods, or a large admin UI.
- Do not mass-rewrite theory chapters for style.
- Do not treat helper checklist scores 1–5 as Saaty inputs.
- Do not treat the control example in `AHP_NAVOD_SAATY.md` as verified until independently recomputed; rounded figures and λmax claims there are not a spec.
- Describe any AI use in the methodology: tool, version, purpose, method, and scope.
- Source of truth for proposed STAG goal/outline: `EMAIL_VEDOUCIMU_A_CIL_BP.md`. Keep `PLAN.md` aligned to it. Do not silently expand scope beyond the email.

## Verification

There is no automated test suite. After chapter edits, rebuild only a selected draft if needed, then check headings, order, Czech characters, citations, and a trailing newline. After Docker edits, validate Compose and healthchecks; Oracle can take several minutes on first start.

Final Word document: `oliva/sablony/šablona( nová (1).docx` (not the seminar template). Cambria or Times New Roman 12 pt, line spacing 1.5, left margin 3.5 cm, other margins 2 cm. Page numbering starts at the introduction as page 1.

This workspace lives on Google Drive. Newly written DOCX, XLSX, or PDF files can be corrupted asynchronously. Keep a known-good copy outside the synced destination and re-check the destination more than once, several seconds apart, before handoff.

## Git

Milestone-style subjects: `30`, `30-1`, `31-1`. Keep commits focused. Never commit `docker/.env`, credentials, installers, or large local research files (`literatura/`, `nastroje/`, `oliva/`, `cykloservis/` are gitignored).