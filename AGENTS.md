# Repository Guidelines

Czech bachelor-thesis workspace for Roman Janiš (FIM UHK). Topic: *Komparace nástrojů pro návrh a vývoj databázových systémů pomocí AHP*. Supervisor: Ing. et Ing. Martin Lněnička, Ph.D. This is not an application repository yet; the PHP app is planned, not started.

On Windows this file is the same as `Agents.md`. `.agents/AGENTS.md` describes an older seminar-paper layout; do not treat it as current.

## Start Here

Before substantive work, re-read dated status in `PLAN.md`, then `EMAIL_KONVERZACE.md` and `ZDROJE.md`. Load extra files only as needed:

- Goal / STAG proposal: source of truth for title, goal, outline, assignment literature is `CIL_BP.md`; outgoing letter is `EMAIL.md` (not yet sent).
- Detailed step-by-step execution plan (phases 0, A–H with concrete file/Excel/app/chapter steps): `PLAN.md`.
- AHP calculations: `AHP_NAVOD_SAATY.md` (recompute the worked example before treating it as a specification).
- Tool tests: `CYKLOSERVIS_ZADANI.md`, `docker/README.md`.
- Writing: the relevant `BP <n>.md` chapter.
- Outline mapping (older 7-point draft; for STAG and PLAN the **6-point outline in the email** wins): `VYSVETLENI_OSNOVY_A_NAVAZNOST_NA_SEMINARKU.md`.

Discover project Markdown with `rg --files -g "*.md" -g "!nastroje/**"`. Read files in PowerShell with `Get-Content -Raw -LiteralPath '.\PLAN.md' -Encoding UTF8` so Czech path characters stay intact.

## Current Status (13 September 2026)

`EMAIL.md` + `CIL_BP.md` is the current proposal of title, goal, 6-point outline, and five assignment sources. It is prepared to send; the supervisor has not approved it. Do not treat it as an approved STAG assignment.

`PLAN.md` is the full roadmap to submission (phases 0, A–H), aligned to that email. Phase A locks **scope only** (app purpose, four alternatives, K1–K8, one Cykloservis case, three sensitivity changes) — that is not a finished thesis. Next real work is phase B (data design, one AHP procedure, small control example), then C–D (minimal PHP app + verify), E–F (tool tests → pairwise matrices → run + sensitivity), G–H (write BP text, formal DOCX, submit).

**Do not rewrite BP chapters yet** to match the new goal. `BP 0.md`–`BP 3.md` and `BP 9.md` still use seminar framing. After supervisor approval and practical results, reframe them in phase G.

Immediate work: send `EMAIL.md` + `CIL_BP.md`; after the reply, edit STAG (phase 0). In parallel start phase B (AHP spec + control example) and tool install notes for phase E. Do not start full PHP coding before phase B.

STAG assignment-sheet deadline: 15 October 2026. The thesis needs at least 30 used sources, of which at least 20 are books or journal articles. `ZDROJE.md` already tracks 27 seminar items plus 3 approved extras; bibliography edits belong in `BP 10.md` and must stay in sync with `ZDROJE.md`.

## Locked Decisions

Keep these unless the supervisor changes them. They match `EMAIL.md` + `CIL_BP.md` plus working detail in `PLAN.md`:

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

Soubory `BP 0.md` až `BP 10.md` obsahují text ze schválené verze seminární práce `seminární práce/MES_Janiš_final.txt` s minimem změn:

| Files | Kapitola v seminárce (`MES_Janiš_final.txt`) | Role v BP |
|---|---|---|
| `BP 0.md` | Titulní strana, anotace, obsah, seznam tabulek | Úvodní náležitosti (přizpůsobí se pro BP po schválení cíle). |
| `BP 1.md` | 1 Úvod | Úvod (přerámuje se na BP v souladu s novým cílem). |
| `BP 2.md` | 2 Cíl práce a výzkumné otázky | Cíl a VO (převezme cíl z `CIL_BP.md` / `EMAIL.md`). |
| `BP 3.md` | 3 Metodika práce | Metodika (rozšíří se o popis vývoje app, testů a AI). |
| `BP 4.md` | 4 Databázové systémy (4.1–4.4) | Teorie DB (hotovo ze seminárky, minimální změny). |
| `BP 5.md` | 5 Datové modely (5.1–5.4) | Teorie datových modelů (hotovo ze seminárky, minimální změny). |
| `BP 6.md` | 6 Vícekriteriální rozhodování (vč. 6.3 AHP) | Teorie MCDM a AHP (hotovo ze seminárky, sladí se s `AHP_SPECIFIKACE.md`). |
| `BP 7.md` | 7 Nástroje pro návrh a vývoj databází (7.1–7.4) | Přehled 4 nástrojů (doplní se přesné testované verze). |
| `BP 8.md` | 8 Návrh hodnoticích kritérií | Kritéria K1–K8 (pod `---` je připraven návrh operacionalizace). |
| `BP 9.md` | 9 Shrnutí, diskuse výsledků a doporučení | Závěr seminárky (nenahrazuje závěr BP; bude nahrazen novým zhodnocením). |
| `BP 10.md` | Seznam zdrojů (26 položek) | Bibliografie (rozšiřuje se na 30 položek dle `ZDROJE.md`). |
| `BP 11.md`–`BP 13.md` | Budoucí praktické kapitoly BP dle osnovy | 11: Návrh a app PHP, 12: Ověření + Cykloservis + citlivost, 13: Zhodnocení. |

### Přehled klíčových souborů – kde co najít

- **Zadání a cíle:** `CIL_BP.md` (zdroj pro STAG: název, cíl, 6 bodů osnovy, 5 zdrojů), `EMAIL.md` (dopis vedoucímu), `EMAIL_KONVERZACE.md` (historie e-mailů s vedoucím Ing. Lněničkou).
- **Plán postupu:** `PLAN.md` (prováděcí plán krok za krokem, fáze 0, A–H, checklisty).
- **Literatura a citace:** `ZDROJE.md` (audit všech 30 zdrojů, odkazy na PDF v `literatura/`, připravené citace ISO 690 pro `BP 10.md`).
- **AHP matematika:** `AHP_NAVOD_SAATY.md` (postup geometrického průměru, Saatyho matice, konzistence CI/CR, kontrolní 3×3 příklad).
- **Modelový scénář:** `CYKLOSERVIS_ZADANI.md` (10 entit jádra cykloservisu, referenční DDL pro PostgreSQL, MySQL i Oracle, 4 kroky testování).
- **Databázové prostředí:** `docker/` (`docker-compose.yml`, README pro PostgreSQL 16, MySQL 8, Oracle Free 23).
- **Excelové soubory:**
  - `hodnoceni_4_nastroju.xlsx` — hlavní pracovní sešit v rootu (struktura listů pro záznam testů a AHP matic).
  - `z emailu/Projekty_s_AHP/` — vzorové studentské projekty a šablony zaslané vedoucím (`Priklad_Vyber susicky.xlsx`, `cv3_michalkova.xlsx`, `example1_methods.xlsx`, `example2_methods.xlsx`).
- **Formální požadavky a šablony fakulty (`oliva/`):**
  - `oliva/pokyny/Metodické pokyny pro vypracování bakalářských a diplomových prací.pdf` — Výnos děkana FIM č. 6/2023 (závazná pravidla FIM UHK: doporučený rozsah BP 35–45 stran / cca 70 000 znaků, struktura od titulního listu po zadání, pasivum v textu, pravidla pro citace a povinná deklarace využití AI v metodice).
  - `oliva/sablony/šablona( nová (1).docx` — oficiální šablona FIM pro finální bakalářskou práci (přednastavené styly, okraje 3,5 cm u hřbetu / 2 cm ostatní, písmo Cambria 12 pt text / bezpatkové nadpisy, řádkování 1,5, prohlášení včetně AI).
  - `oliva/pokyny/` a `oliva/vzory/` — doplňkové metodické pokyny k psaní odborných prací a vzory prací z kurzu MES.
- **Zdrojová seminární práce (pouze ke čtení):** `seminární práce/MES_Janiš_final.txt` a `seminární práce/MES_Janis_final.docx`.

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
- Source of truth for proposed STAG goal/outline: `EMAIL.md` + `CIL_BP.md`. Keep `PLAN.md` aligned to it. Do not silently expand scope beyond the email.

## Verification

There is no automated test suite. After chapter edits, rebuild only a selected draft if needed, then check headings, order, Czech characters, citations, and a trailing newline. After Docker edits, validate Compose and healthchecks; Oracle can take several minutes on first start.

Final Word document: `oliva/sablony/šablona( nová (1).docx` (not the seminar template). Cambria or Times New Roman 12 pt, line spacing 1.5, left margin 3.5 cm, other margins 2 cm. Page numbering starts at the introduction as page 1.

This workspace lives on Google Drive. Newly written DOCX, XLSX, or PDF files can be corrupted asynchronously. Keep a known-good copy outside the synced destination and re-check the destination more than once, several seconds apart, before handoff.

## Git

Milestone-style subjects: `30`, `30-1`, `31-1`. Keep commits focused. Never commit `docker/.env`, credentials, installers, or large local research files (`literatura/`, `nastroje/`, `oliva/`, `cykloservis/` are gitignored).