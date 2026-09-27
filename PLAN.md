# Detailní prováděcí plán BP (krok za krokem)

Aktualizace: 27. 9. 2026
Jediné platné zadání: podklad VŠKP v IS/STAG, export `oliva/temata_vskp_-_podklady_pro_zadani_vskp.pdf` (janisro1, 23. 9. 2026 20:40). Přepis je v `CIL_BP.md`. Stejný text je v posledním e-mailu vedoucího (`EMAIL_KONVERZACE.md`, 15. 9. 2026). Starší návrhy neplatí.

**Jak s tímto souborem pracovat**

1. Jdi **shora dolů**. Další krok začni, až má předchozí zaškrtnutý výstup.
2. U každého kroku je: *co udělat*, *kde*, *výstup*, *hotovo když*.
3. Stav: `[ ]` nehotovo · `[~]` rozpracováno · `[x]` hotovo.
4. Čísla, matice, pořadí, CR, ceny a verze nástrojů **nevymýšlej** — jen z testu / výpočtu.
5. Kapitoly BP nepřepisuj dřív, než říká příslušná fáze (kromě drobných oprav chyb).

---

## Stav teď (výchozí bod)

| ID | Položka | Stav |
|---|---|---|
| S0 | E-mail vedoucímu odeslán a schválen | `[ ]` ne |
| S1 | STAG zadávací list vyplněn | `[ ]` ne |
| S2 | Rozsah uzamčen (účel, 4 nástroje, K1–K8, 1 scénář, 3 citlivosti) | `[x]` ano — Fáze A |
| S3 | AHP specifikace + Excel kontrolní příklad | `[ ]` ne |
| S4 | XLSX hodnocení / párová porovnání vyplněná z testů | `[ ]` ne (soubor existuje prázdný/pracovní) |
| S5 | PHP aplikace naprogramovaná | `[ ]` ne |
| S6 | Aplikace nasazená a ověřená kontrolním výpočtem | `[ ]` ne |
| S7 | Cykloservis otestován ve 4 nástrojích | `[ ]` ne |
| S8 | Základní AHP běh + 3 citlivosti spočítané v app | `[ ]` ne |
| S9 | Text BP podle nového cíle a osnovy 1–6 | `[ ]` ne (stále seminární rámování) |
| S10 | Finální DOCX odevzdán | `[ ]` ne |

**Poslední splněný celek:** Fáze A (jen rozhodnutí o rozsahu).
**Právě plnit:** Fáze 0 (e-mail/STAG), pak okamžitě Fáze B (AHP + Excel).

---

# FÁZE 0 — E-mail vedoucímu a STAG

## Krok 0.1 — Opravit a odeslat e-mail

**Kde:** `EMAIL.md` (dopis) + `CIL_BP.md` (cíl/osnova/literatura)

1. Otevři soubor.
2. ~~V odstavci **Cíl práce** najdi `přípdně` a oprav na `případně`.~~ **Hotovo 13. 9. 2026** — v `EMAIL.md / CIL_BP.md` je `případně`.
3. Zkontroluj, že v mailu je odděleně: (a) název CZ+EN, (b) **cíl** (jen odstavec cíle — bez literatury), (c) osnova 1–6, (d) **literatura do zadání** jako samostatný blok 5 zdrojů, (e) otázka k formě kontrolního výpočtu. Literatura **nepatří do textu cíle**.
4. Zkopíruj text do školního mailu vedoucímu (Ing. et Ing. Martin Lněnička, Ph.D.).
5. Odešli.
6. Do `EMAIL_KONVERZACE.md` doplň datum odeslání (stručně: „odeslán návrh cíle a osnovy“ + datum).

**Výstup:** odeslaný e-mail.
**Hotovo když:** máš odeslanou položku v odeslané poště.

## Krok 0.2 — Po schválení vyplnit STAG

**Kdy:** až vedoucí napíše, že je to v pořádku (nebo pošle úpravy — nejdřív uprav e-mail/tento plán, pak STAG).

1. Přihlas se do IS/STAG → podklad VŠKP / zadávací list.
2. Vyplň **název CZ:** Komparace nástrojů pro návrh a vývoj databázových systémů pomocí AHP.
3. Vyplň **název EN:** Comparison of Tools for Database System Design and Development Using AHP.
4. Vlož **cíl** — **pouze** znění cíle z e-mailu (s `případně`). Do cíle **nevkládej** seznam literatury, názvy článků ani „podle Saaty/Ishizaka“.
5. Vlož **zásady pro vypracování** = osnova 1–6 z e-mailu (to taky není literatura).
6. Vlož **literaturu** do **samostatného pole** zadávacího listu (ne do cíle): 4–5 zdrojů ISO 690. Vedoucí to chtěl už dřív u doplnění STAGu (18. 8. / 11. 5.), **ne** jako téma posledního mailu o volbě cesty 1/2. Pracovní doporučení které PDF brát = sekce L1 níže (interní, pro tebe).
7. Odešli ke schválení tlačítkem ve STAGu.
8. Termín listu: **15. 10. 2026**.

**Výstup:** STAG ve stavu čeká na / schváleno vedoucím.
**Hotovo když:** vidíš odeslání / schválení v IS.

---

# FÁZE A — Uzamčený rozsah (už hotovo — jen dodržovat)

Toto **nedělej znovu**. Při každém dalším kroku kontroluj, že se neodchyluješ.

| Pravidlo | Hodnota |
|---|---|
| Účel app | výběr nástroje pro **návrh a vývoj** DB systémů metodou AHP |
| Mimo hodnocení | správa serverů, zálohování, výkon DBMS |
| Alternativy | 1) Oracle SQL Developer Data Modeler 2) DBeaver Community Edition 3) MySQL Workbench Community Edition 4) pgModeler |
| Kritéria | K1–K8 (viz Fáze B/E a `BP 8.md`) |
| Scénář | 1× Cykloservis (`CYKLOSERVIS_ZADANI.md`) |
| Citlivost | 3 oddělené změny: vyšší K8, vyšší K1, vyšší K3; matice alternativ stejné |
| Hodnotitel | autor (v textu uvést jako omezení) |
| App baseline | připravené položky + vlastní, popisy/odkazy, páry, výpočet, pořadí; bez login/admin/REST |

**Hotovo:** `[x]` jako rozhodnutí.

---

# FÁZE B — Specifikace výpočtu, kritérií a Excelu (dělej teď po 0.1)

Cíl fáze: než napíšeš jediný řádek PHP a než vyplníš reálné páry nástrojů, musíš mít **jeden** závazný výpočetní postup a **ověřený** malý Excel.

## Krok B1 — Založit pracovní složky a soubory

1. V rootu vytvoř (pokud nejsou):
   - `app/` — budoucí PHP aplikace
   - `vypocty/` — Excel kontrolní příklad a později exporty z app
   - `protokoly/` — zápisy z testů 4 nástrojů
2. Soubory, které hned založ prázdné s nadpisem:
   - `vypocty/AHP_SPECIFIKACE.md` — závazný postup výpočtu
   - `vypocty/kontrolni_priklad.xlsx` — malý AHP příklad
   - `protokoly/README.md` — seznam protokolů
3. Pracovní hodnocení zůstává: `hodnoceni_4_nastroju.xlsx` (root).

**Výstup:** složky + prázdné soubory existují.
**Hotovo když:** vidíš je ve stromu projektu.

## Krok B2 — Napsat závaznou AHP specifikaci

**Kde:** `vypocty/AHP_SPECIFIKACE.md`
**Podklad:** `AHP_NAVOD_SAATY.md`, `BP 6.md`, Saaty / Ishizaka v `ZDROJE.md`

Do souboru **doslova** zapiš a rozhodni:

### B2.1 Škála a matice

1. Saaty 1–9 a převrácené hodnoty.
2. Diagonála vždy 1.
3. Když uživatel zadá a_ij = x, systém nastaví a_ji = 1/x.
4. Povolení jen kladných hodnot ze škály (1,2,…,9 a převrácené).

### B2.2 Výpočet vah (jeden postup — držet všude)

Pro matici n×n:

1. Pro každý řádek i: GM_i = (a_i1 · a_i2 · … · a_in)^(1/n). V Excelu: GEOMEAN přes buňky řádku.
2. Součet S = GM_1 + … + GM_n.
3. Váha w_i = GM_i / S.
4. Kontrola: součet vah = 1 (tolerance např. 1e-9).

**Toto je jediný povolený postup vah** v Excelu, v PHP i v textu BP.

### B2.3 Konzistence

1. Spočti vektor Aw (matice × váhy).
2. Pro každý i: t_i = (Aw)_i / w_i.
3. λmax = průměr(t_i).
4. CI = (λmax − n)/(n − 1) pro n > 1; pro n=1 konzistenci neřeš.
5. CR = CI / RI(n).
6. Tabulka RI (Saaty) zapiš do specifikace:

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| RI | 0 | 0 | 0,58 | 0,90 | 1,12 | 1,24 | 1,32 | 1,41 | 1,45 | 1,49 |

7. Pravidlo app:
   - CR ≤ 0,10 → OK, výsledek použitelný.
   - CR > 0,10 → spočti stejně, ale **zobraz varování**.
8. Pro n=2: RI=0 — ošetři dělení nulou (zapiš přesné chování do spec).

### B2.4 Hierarchie pro BP případ

1. Cíl: výběr nástroje.
2. Úroveň kritérií: u modelového případu K1–K8 → matice 8×8, RI=1,41.
3. Pro **každé** kritérium matice alternativ 4×4, RI=0,90.
4. Globální priorita alternativy A: P_A = suma_k (w_k · l_A,k).
5. Pořadí = sestupně podle P_A.

### B2.5 Zaokrouhlení

1. Při výpočtu drž alespoň 8 desetinných míst interně.
2. Zobrazení: váhy a priority na **4 desetinná místa**, CR na **4**.
3. Shoda app vs Excel: absolutní rozdíl váhy ≤ **0,001** (akceptace Fáze D).

**Výstup:** `vypocty/AHP_SPECIFIKACE.md` s body B2.1–B2.5.
**Hotovo když:** podle textu umíš spočítat libovolnou matici stejně v Excelu i později v PHP.

## Krok B3 — Spočítat malý kontrolní příklad v Excelu

**Kde:** `vypocty/kontrolni_priklad.xlsx`
**Podklad:** sekce 5 v `AHP_NAVOD_SAATY.md` (3 kritéria × 3 alternativy) — **čísla sám přepočítej**, neber slepě.

### Listy sešitu (vytvoř přesně tyto)

| List | Obsah |
|---|---|
| `0_zadani` | popis příkladu, škála; jde o kontrolu postupu, ne o Cykloservis |
| `1_matice_kriterii` | 3×3 matice kritérií + reciproky vzorcem |
| `2_vahy_kriterii` | GEOMEAN, normalizace, součet=1 |
| `3_konzistence_krit` | Aw, λmax, CI, CR |
| `4_matice_alt_K1` | 3×3 alternativy vzhledem ke kritériu 1 |
| `5_matice_alt_K2` | totéž pro kritérium 2 |
| `6_matice_alt_K3` | totéž pro kritérium 3 |
| `7_lokalni_vahy` | lokální váhy + CR u každé matice alt |
| `8_globalni` | globální priority, pořadí |
| `9_souhrn` | finální váhy, CR, pořadí — etalon pro app |

### Postup vyplnění

1. Na `1_matice_kriterii` zadej **jen horní trojúhelník** ručně; spodní `=1/horní`; diagonála 1.
2. Na `2_vahy_kriterii` spočítej GM a váhy podle B2.
3. Na `3_konzistence_krit` spočítej λmax, CI, CR.
4. Stejně pro tři matice alternativ.
5. Na `8_globalni` spočítej priority a pořadí.
6. Na `9_souhrn` zkopíruj hodnoty **jako hodnoty** (ne jen vzorce) pro archiv.
7. Ulož sešit; po uložení otevři znovu a zkontroluj čísla (Drive může kazit XLSX).

**Výstup:** vyplněný `kontrolni_priklad.xlsx` + v `AHP_SPECIFIKACE.md` odstavec „Etalon: list 9_souhrn“.
**Hotovo když:** list `9_souhrn` má konkrétní čísla z tvého výpočtu.

## Krok B4 — Operacionalizovat kritéria K1–K8 (jak přesně porovnávat)

**Kde:** `protokoly/K_OPERACIONALIZACE.md`
**Podklad:** `BP 8.md`, cíl e-mailu (ne správa/zálohy/výkon)

Pro **každé** Ki napiš tabulku: kód/název; co se hodnotí (2–4 pozorovatelné věci); co se nehodnotí; jak otestuji na Cykloservisu; důkaz do protokolu; podklad pro Saaty.

### Minimální checklist po kritériích

**K1 Funkcionalita modelování**
- Entity, atributy, PK/FK, 1:N, M:N (asociační entita), 1:1, nullable FK?
- Datové typy, unique, check/stav?
- Nehodnotí se tu generování DDL (K4) ani reverse (K5).

**K2 Použitelnost**
- Počet kroků / čas na jádro modelu Cykloservis.
- Přehlednost, chybové hlášky, obchvaty.
- Zapisuj čas a problémy — subjektivní, ale podložené zápisem.

**K3 Kompatibilita s DBMS**
- Pro které DBMS umí modelovat / generovat / reverse v otestované edici.
- DBeaver: šíře; ostatní: primární platforma + další.

**K4 Forward engineering**
- Export/spuštění DDL z modelu.
- Zachování PK/FK/omezení po nahrání do docker DB.

**K5 Reverse engineering**
- Načtení schématu z docker DB do diagramu/modelu.
- Co se ztratí?

**K6 Dokumentace a komunita**
- Oficiální docs (URL + datum), nápověda v nástroji.

**K7 Import/export modelu**
- Nativní formáty modelu/diagramu.
- **Nehodnotit znovu** totéž DDL jako v K4.

**K8 Náklady a licence**
- Edice, cena k datu testu, omezení community/free.
- Zdroj URL + datum.

**Výstup:** `protokoly/K_OPERACIONALIZACE.md` komplet K1–K8.
**Hotovo když:** u každého K víš přesně, co v nástroji klikneš a co zapíšeš.

## Krok B5 — Připravit strukturu `hodnoceni_4_nastroju.xlsx`

**Kde:** `hodnoceni_4_nastroju.xlsx`
**Až po B4.** Zatím **nevyplňuj Saaty známky** — jen strukturu a identifikaci.

### Doporučené listy

| List | Účel | Kdy vyplnit |
|---|---|---|
| `A_nastroje` | název, edice, verze, OS, datum instalace, licence URL | po instalaci (E1) |
| `B_checklist_K1` … `B_checklist_K8` | pozorování ano/ne/částečně + poznámka | při testech (E) |
| `C_saaty_kriteria` | matice 8×8 důležitosti kritérií pro Cykloservis | **až po** testech |
| `D_saaty_K1` … `D_saaty_K8` | matice 4×4 nástrojů pro dané Ki | až po testech |
| `E_vypocet` | váhy, CR, priority (app primárně; Excel volitelně) | po C/D maticích |
| `F_citlivost` | 3 varianty + nová pořadí | po základním běhu |
| `G_zdroje_cen` | K8 podklady s datem | při E |

### Pravidla XLSX

1. Checklist listy = **důkazy**, ne Saaty.
2. Saaty listy = jen 1–9 a reciproky; diagonála 1.
3. Žádné automatické převod checklistu 1–5 na Saaty.
4. Po větším uložení ověř, že soubor není poškozený.

**Výstup:** připravená struktura listů.
**Hotovo když:** listy existují a `A_nastroje` má sloupce pro 4 nástroje.

## Krok B6 — Datový návrh aplikace (konkrétní entity)

**Kde:** `app/SPEC.md`

### B6.1 Entity (i když začneš na JSON bez DB)

1. `Criterion` — id, code (K1…), name, description, link, is_builtin
2. `Alternative` — id, name, description, link, is_builtin
3. `Evaluation` — id, created_at, title (např. Cykloservis)
4. `EvaluationCriterion` / `EvaluationAlternative` — výběr do session
5. `PairwiseCriteria` — evaluation_id, i, j, value
6. `PairwiseAlternatives` — evaluation_id, criterion_id, i, j, value
7. `Result` — weights, CR, global_scores, ranking

### B6.2 Připravená data (seed)

Specifikuj pole pro:
- `app/data/seed_criteria.json` — K1–K8
- `app/data/seed_alternatives.json` — 4 nástroje
(soubory vytvoříš ve Fázi C)

### B6.3 Tok obrazovek (povinné pořadí)

1. Úvod
2. Výběr alternativ + vlastní
3. Výběr kritérií + vlastní
4. Popisy a odkazy
5. Páry kritérií (horní trojúhelník)
6. Páry alternativ pro každé kritérium
7. Spočítat
8. Výsledek (váhy, CR, pořadí, varování) + zpět

### B6.4 Mimofunkční

- PHP 8.x; bez zbytečného frameworku — rozhodni a zapiš.
- Session nebo souborové uložení evaluation.
- Cíl nasazení: webhosting s PHP (nebo VPS) — zapiš variantu pro C9.

**Výstup:** `app/SPEC.md`.
**Hotovo když:** podle SPEC umíš kódit bez vymýšlení rozsahu.

---

# FÁZE C — Naprogramovat a nasadit minimální PHP aplikaci

**Vstupní podmínka:** hotové B2 a B3 (spec + Excel etalon). B4–B6 ideálně taky.
**Složka:** `app/`

## Krok C1 — Kostra projektu

1. Vytvoř strukturu:

```text
app/
  public/           # document root
    index.php
    assets/style.css
  src/
    AhpCalculator.php
    PairwiseMatrix.php
    Repository.php
  data/
    seed_criteria.json
    seed_alternatives.json
  templates/
  SPEC.md
  README.md
```

2. Do `README.md`: jak spustit lokálně (`php -S localhost:8080 -t public`), požadavky PHP.
3. Git: commituj `app/`; necommituj hesla.

**Hotovo když:** `php -S` zobrazí úvodní stránku.

## Krok C2 — Seed dat

1. Vyplň `seed_criteria.json` pro K1–K8 (název, description z B4, link).
2. Vyplň `seed_alternatives.json` pro 4 nástroje (oficiální odkazy; verze doplň po E1).
3. Repository umí načíst seed a listovat položky.

## Krok C3 — Výběr položek + vlastní položky

1. Formulář checkboxů z seed.
2. Pole název, popis, odkaz pro vlastní alternativu i kritérium.
3. Validace: min. 2 kritéria a min. 2 alternativy.
4. Ulož výběr do PHP session (nebo `data/evaluations/{id}.json`).

## Krok C4 — Párová porovnání UI

1. Pro kritéria vygeneruj všechny dvojice i < j.
2. Select/input Saaty; automaticky reciprok.
3. Stejně pro alternativy **pod každým kritériem**.
4. Nesmí jít odeslat výpočet s prázdnou buňkou.

## Krok C5 — Implementovat `AhpCalculator` podle B2

1. `weights(matrix): array`
2. `consistency(matrix, weights): lambdaMax, CI, CR`
3. `globalScores(criteriaWeights, localWeightMatrix): array`
4. Smoke test: matice z Excelu B3 → `php app/test_control.php` (nebo ekvivalent).

## Krok C6 — Stránka výsledků

1. Tabulka vah kritérií + CR.
2. Pro každé kritérium: lokální váhy + CR.
3. Celkové priority + pořadí.
4. CR > 0,10 → varování.
5. Zpět na matice; nová evaluace; volitelně export JSON do `vypocty/`.

## Krok C7 — Popisy a odkazy

1. U built-in položek zobraz description + klikací link.
2. Ověř, že odkazy nejsou 404.

## Krok C8 — Lokální end-to-end = Excel etalon

1. Spusť app.
2. Zadej **stejné** matice jako v `kontrolni_priklad.xlsx`.
3. Porovnej s listem `9_souhrn`.
4. Zapiš `vypocty/APP_VS_EXCEL_kontrolni.md` (Excel | App | rozdíl | OK?).
5. Akceptace: |Δw| ≤ 0,001, stejné pořadí.

## Krok C9 — Nasazení na server

Zvol jednu variantu a zapiš do `app/README.md`.

**Varianta A — PHP webhosting (doporučeno)**
1. Document root = `app/public`.
2. PHP ≥ 8.0, session zapnuté.
3. Zápis na `data/evaluations/` pokud ukládáš soubory.
4. Nahraj FTP/SFTP.
5. Otevři veřejnou URL, zopakuj C8 na serveru.
6. URL zapiš do README a později do BP.

**Varianta B — VPS:** Nginx/Apache → `public` (jen pokud umíš; pro BP netřeba overkill).

**Hotovo když:** z jiného PC/telefonu spočítáš kontrolní příklad.

## Krok C10 — Záloha app

1. Commit/tag: `app-v0.1-control-ok`.
2. ZIP do `vypocty/app_build_YYYYMMDD.zip` (bez tajemství).
3. Ověř ZIP mimo Drive sync.

---

# FÁZE D — Oficiální ověření výpočtů (pro text BP)

## Krok D1 — Protokol kontrolního výpočtu

**Soubor:** `vypocty/PROTOKOL_KONTROLNI_VYPOCET.md`

1. Datum, verze app, URL (local + server).
2. Vstupní matice (z Excelu).
3. Excel výsledky.
4. App výsledky.
5. Tabulka shody.
6. Závěr: app odpovídá nezávislému výpočtu podle AHP_SPECIFIKACE.
7. Cizí AHP web není hlavní důkaz (max doplněk).

## Krok D2 — Test špatných vstupů

1. Prázdné pole → hláška, nespadne.
2. Vysoké CR → varování.
3. Jen 1 alternativa → odmítnout.
4. Zapiš 3–5 bulletů do protokolu.

**Hotovo když:** D1+D2 existují a jsou pravdivé.

---

# FÁZE E — Testy 4 nástrojů na Cykloservisu a vyplnění XLSX

**Vstup:** B4, struktura XLSX z B5.
**Částečně paralelně s C**; Saaty matice až po dokončení testů.

## Krok E1 — Instalace nástrojů a zápis verzí

Pro každý nástroj:
1. Stáhni oficiální instalátor do `nastroje/` (gitignored).
2. Nainstaluj.
3. Do listu `A_nastroje` zapiš: název, verze z Help→About, OS, licence, URL, datum instalace.
4. Stejné stručně do `protokoly/VERZE_NASTROJU.md`.

Nástroje:
1. Oracle SQL Developer **Data Modeler**
2. DBeaver **Community**
3. MySQL Workbench **Community**
4. pgModeler (přesná edice; reverse ověř na tvé sestavení)

## Krok E2 — Spustit databázové servery

**Kde:** `docker/`

1. `.env.example` → `.env` pokud chybí.
2. `cd docker`
3. `docker compose config`
4. `docker compose up -d`
5. `docker compose ps` — Oracle i několik minut do healthy.
6. Ověř připojení dle `docker/README.md` (3306, 5432, 1521).

## Krok E3 — Referenční DDL Cykloservis do DB

**Podklad:** `CYKLOSERVIS_ZADANI.md` (jádro 10 entit)

1. SQL skripty pro MySQL, PostgreSQL, Oracle (`docker/sql` nebo `cykloservis/`).
2. Nahraj stejné jádro do všech tří DB (dialekty různé, obsah stejný).
3. Ověř tabulky a FK.
4. Zápis `protokoly/DDL_NASIENI.md`.

## Krok E4 — Šablona protokolu na 1 nástroj

Vytvoř pro každý nástroj `protokoly/P_<zkratka>.md` (P_MW, P_DBEAVER, P_OSDM, P_PGM) podle šablony:

1. Instalace a spuštění
2. Nový model Cykloservis (K1, K2) — 10 entit, M:N, 1:1, nullable FK
3. Forward (K4) — DDL cesta, DB, chyby
4. Reverse (K5) — zdrojová DB, co chybí
5. Import/export modelu (K7)
6. DBMS pokrytí (K3)
7. Dokumentace (K6) + URL
8. Licence/cena (K8) + URL + datum
9. Čas a použitelnost (K2)
10. Souhrn silných/slabých stránek **bez Saaty čísel**

## Krok E5 — Provést testy nástroj po nástroji

Doporučené pořadí: MySQL Workbench → pgModeler → Oracle DM → DBeaver.

U každého:
1. Vyplň protokol.
2. Ulož artefakty do `cykloservis/<nastroj>/`.
3. Do XLSX `B_checklist_K*` doplň ano/ne/částečně + poznámka.
4. **Neházej Saaty**, dokud nemáš všechny 4 protokoly.

## Krok E6 — Saaty matice kritérií (Cykloservis)

**List:** `C_saaty_kriteria` (8×8)

1. Rozhodovatel: vývojář malé firmy, omezený rozpočet, DBMS ne definitivní.
2. Horní trojúhelník podle preferencí **scénáře**.
3. Spodní = 1/x.
4. CR v Excelu nebo v app; pokud CR > 0,10, uprav páry a zapiš proč.

## Krok E7 — Osm matic alternativ (4×4)

Pro každé Ki list `D_saaty_Ki`:
1. 4 protokoly vedle sebe.
2. Saaty 1–9 **jen podle důkazů k danému Ki**.
3. U silných úsudků (5,7,9) 1 věta poznámky + odkaz na protokol.
4. CR oprav, pokud > 0,10.

**Zákaz:** kopírovat jednu matici do všech Ki; hodnotit K4 a K7 stejným DDL bez rozdílu.

## Krok E8 — Záloha XLSX

1. Ulož `hodnoceni_4_nastroju.xlsx`.
2. Kopie mimo sync: `vypocty/hodnoceni_4_nastroju_YYYYMMDD.xlsx`.
3. Otevři kopii a ověř nepoškozenost.

**Hotovo E:** 4 protokoly + verze + checklisty + matice C a D_saaty_K1…K8 z testů.

---

# FÁZE F — Běh v aplikaci + 3 citlivosti

## Krok F1 — Seed podle reality

1. Do popisu alternativ doplň **přesné verze** z E1.
2. Texty kritérií sjednoť s B4.
3. Znovu nasaď, pokud běží na serveru.

## Krok F2 — Základní běh Cykloservis

1. App (server URL).
2. Vyber 4 nástroje + K1–K8.
3. Zadej `C_saaty_kriteria` a osm `D_saaty_K*`.
4. Spočítej.
5. Ulož `vypocty/VYSLEDEK_zakladni.md` (+ volitelně JSON): váhy, všechna CR, priority, pořadí, datum, URL app, verze nástrojů.

## Krok F3 — Citlivost K8

1. **Neměň** matice alternativ.
2. Ze **základní** matice kritérií zvyš K8 (zapiš které buňky).
3. Spočítej → `vypocty/VYSLEDEK_citlivost_K8.md`.

## Krok F4 — Citlivost K1

1. Opět ze základní matice (ne z K8).
2. Zvyš K1 → `VYSLEDEK_citlivost_K1.md`.

## Krok F5 — Citlivost K3

1. Ze základní matice zvyš K3 → `VYSLEDEK_citlivost_K3.md`.

## Krok F6 — Srovnávací tabulka

**Soubor:** `vypocty/VYSLEDEK_srovnani.md`

| Varianta | 1. | 2. | 3. | 4. | Poznámka |
|---|---|---|---|---|---|
| Základ | | | | | |
| +K8 | | | | | |
| +K1 | | | | | |
| +K3 | | | | | |

+ 5–10 vět interpretace; nezměněné pořadí je platný výsledek.

**Hotovo F:** 4 výsledkové md + srovnání, čísla z app.

---

# FÁZE G — Napsat a upravit text BP (kapitoly)

**Vstup:** schválený cíl; ideálně D a F hotové (teorii G4–G5 lze částečně dřív).
**Při změně existujícího textu:** pod `---` blok  
`Pracovní poznámka – původní znění před úpravou, RRRR-MM-DD, důvod:` + starý text.

## Mapování osnovy STAG → soubory

| Osnova STAG | Soubory | Akce |
|---|---|---|
| Titul, anotace | `BP 0.md` | přepsat |
| Úvod | `BP 1.md` | přepsat rámování |
| Cíl a VO | `BP 2.md` | **přepsat cíl z e-mailu** |
| Metodika | `BP 3.md` | přepsat podle B–F |
| 1 Problematika relačních DB | `BP 4.md`, `BP 5.md` | doladit, ne hromadný styl |
| 2 Metoda AHP | `BP 6.md` | sladit s AHP_SPECIFIKACE |
| 3 Nástroje a kritéria | `BP 7.md`, `BP 8.md` | verze + operacionalizace |
| 4 Návrh a app v PHP | nové `BP 11.md` | napsat |
| 5 Ověření + modelový případ + citlivost | nové `BP 12.md` | napsat |
| 6 Zhodnocení | nové `BP 13.md` | napsat (**ne** starý BP 9) |
| Literatura | `BP 10.md`, `ZDROJE.md` | sladit |
| Starý závěr seminárky | `BP 9.md` | nepoužít jako závěr BP |

Čísla 11–13 jsou pracovní; drž obsah osnovy 1–6.

## Krok G0 — `BP 0.md`

1. Název CZ/EN = e-mail.
2. Anotace CZ: problém výběru nástroje; řešení PHP+AHP; ověření kontrolním výpočtem + modelový případ (4 nástroje, K1–K8, 3 citlivosti); výstup = app + výsledky.
3. Abstract EN stejně.
4. Klíčová slova aktualizuj.
5. Obsah doladíš na konci G.

**Hotovo když:** anotace už netvrdí, že výstupem je jen teoretický podklad seminárky.

## Krok G1 — `BP 1.md` Úvod

1. Kontext výběru modelovacího nástroje.
2. Proč AHP + vlastní app (připravené položky, popisy, hlášky).
3. Cíl jednou větou → kap. 2.
4. Struktura podle osnovy 1–6.
5. Odstraň jako hlavní cíl „jen příprava východisek“.

## Krok G2 — `BP 2.md` Cíl a VO  ★ klíčové

1. **Hlavní cíl** = odstavec z e-mailu (s `případně`).
2. Dílčí cíle = DC1…DC6 podle osnovy 1–6.
3. VO příklad:
   - VO1: Jak navrhnout a spočítat AHP v webové app pro výběr DB modelovacích nástrojů?
   - VO2: Odpovídají výpočty app nezávislému kontrolnímu výpočtu?
   - VO3: Jaké pořadí u Cykloservisu a jak ho změní tři citlivosti?
4. Staré VO jen o teorii smaž nebo podřaď.

## Krok G3 — `BP 3.md` Metodika

1. Rešerše / seminárka.
2. Finalizace nástrojů a K1–K8.
3. Operacionalizace + testy Cykloservis (odkaz protokoly).
4. AHP postup z AHP_SPECIFIKACE (geometrický průměr…).
5. Implementace PHP + nasazení.
6. Kontrolní příklad Excel vs app.
7. Základní běh + 3 citlivosti.
8. Omezení: 1 hodnotitel.
9. **AI:** nástroj, verze, účel, co nedělala (matice/výsledky).

## Krok G4 — `BP 4.md` + `BP 5.md` (osnova 1)

1. Oprav jen chyby a nutnou návaznost.
2. Ne hromadný stylistický přepis.
3. 1–2 věty na konci: východisko pro kritéria a app.

## Krok G5 — `BP 6.md` (osnova 2)

1. Vzorce = AHP_SPECIFIKACE.
2. RI tabulka, CR ≤ 0,10.
3. Krátce proč vlastní app (jen s přečtenými zdroji).
4. Odkaz na kapitolu implementace.

## Krok G6 — `BP 7.md` + `BP 8.md` (osnova 3)

1. Přesné verze/edice z E1.
2. Operacionalizace K1–K8 (tabulka z B4).
3. Oddělení K1/K4/K5/K7.
4. Páry z testů Cykloservis → přílohy.

## Krok G7 — `BP 11.md` Návrh a implementace app (osnova 4)

1. Požadavky F/NF.
2. Datový návrh (B6).
3. Architektura PHP.
4. Výpočetní jádro.
5. UI kroky + screenshoty v přílohách.
6. Nasazení (URL).
7. Co není (login, admin…).

## Krok G8 — `BP 12.md` Ověření a modelový případ (osnova 5)

1. Kontrolní výpočet (D1).
2. Špatné vstupy (D2).
3. Cykloservis popis.
4. Testy 4 nástrojů stručně + přílohy.
5. Vstupní matice (příloha XLSX).
6. Základní výsledek (F2).
7. Tři citlivosti (F3–F6).
8. Interpretace.

## Krok G9 — `BP 13.md` Zhodnocení (osnova 6)

1. Splnění cíle a VO.
2. Přínos app.
3. Omezení.
4. Rozšiřitelnost (stačí popsat).
5. Další vývoj.
6. Nezálohuj sem text ze starého `BP 9.md` seminárky jako finál.

## Krok G10 — `BP 10.md` + `ZDROJE.md`

Řiď se sekcí **LITERATURA A ZDROJE (L0–L6)** níže v tomto plánu.

1. Citace v textu ⊆ seznam.
2. ≥ 30 zdrojů, ≥ 20 knih/článků.
3. 5 STAG zdrojů = sada **L1** (ne nutně stará pětice s Ishizakou).
4. AHP kapitola opřená o **L2** (Saaty 1990 + Soukopová + Tomeš; Ishizaka jen po přečtení).
5. DB kapitola opřená o **L3** (Valenta, Chlapek, Carvalho, docs nástrojů).
6. Abecedně, ISO 690; sladit s `ZDROJE.md`.
7. Bez `literatura/inspirace/`; bez Vaidya 2006 bez lokálního PDF.
8. Elmasri jen z místního výňatku.

## Krok G11 — Kontrola a spojení

1. Hledej `BP-DOPLNIT`, `BP-OVĚŘIT`, `⟦`.
2. Spoj draft:  
   `.\spoj.ps1 0 1 2 3 4 5 6 7 8 11 12 13 10 -Out vyber_bp_draft.md`  
   (uprav čísla podle reality; nepřepisuj slepě `BP.md` dokud něco chybí).
3. Kontrola češtiny, nadpisů, souladu cíl↔obsah↔závěr.

---

# FÁZE H — Přílohy, Word, odevzdání

## Krok H1 — Přílohy

Minimálně:
1. AHP_SPECIFIKACE
2. kontrolni_priklad.xlsx + protokol D1
3. hodnoceni_4_nastroju.xlsx finál
4. 4 protokoly nástrojů
5. Výsledky F (základ + 3 citlivosti)
6. Screenshoty app
7. DDL Cykloservis
8. ZIP app / odkaz na kód

## Krok H2 — Word

1. Šablona: `oliva/sablony/šablona( nová (1).docx` (ne seminární).
2. Cambria nebo Times New Roman 12, řádkování 1,5.
3. Okraje: vlevo 3,5 cm, ostatní 2 cm.
4. Číslování od úvodu = strana 1.
5. Ulož `BP_Janis_odeslani_YYYYMMDD.docx`.
6. Drive: po uložení ověř otevřením 2×; kopie mimo sync.

## Krok H3 — Checklist před odevzdáním

- [ ] Cíl v textu = STAG = e-mail
- [ ] Osnova 1–6 pokrytá
- [ ] App na serveru, kontrolní výpočet sedí
- [ ] 4 nástroje: verze + protokoly
- [ ] Matice/výsledky z testů a app
- [ ] 3 citlivosti
- [ ] Literatura ≥ 30 / ≥ 20
- [ ] AI v metodice
- [ ] Omezení 1 hodnotitele
- [ ] Formát šablony BP
- [ ] Vedoucí viděl předfinál (doporučeno)

## Krok H4 — Odevzdání

1. Termín odevzdání BP z harmonogramu FIM (**není** 15. 10. 2026 — to je zadávací list).
2. Odevzdej dle STAG/pokynů.
3. Archiv ZIP: text + app + vypocty + protokoly.

---

# Pořadí „co teď přesně“ (bez skákání)

| # | Krok | Fáze | Stav teď |
|---:|---|---|---|
| 1 | 0.1 Odeslat e-mail (překlep už opraven) | 0 | **dělej první** |
| 1b | L1 (jen literatura, **ne cíl**): rozhodnout Soukopová vs Tomeš pro pole Literatura ve STAGu / v bloku literatury v mailu | L | volitelně před odesláním mailu; cíl se kvůli tomu nemění |
| 2 | B1 Složky app/, vypocty/, protokoly/ | B | hned / paralelně |
| 3 | B2 AHP_SPECIFIKACE.md | B | |
| 4 | B3 kontrolni_priklad.xlsx | B | |
| 5 | B4 K_OPERACIONALIZACE.md | B | |
| 6 | B5 struktura hodnoceni_4_nastroju.xlsx | B | |
| 7 | B6 app/SPEC.md | B | |
| 8 | 0.2 STAG po schválení | 0 | čeká na učitele |
| 9 | C1–C8 PHP app + shoda s Excelem | C | až po B2–B3 |
| 10 | C9–C10 nasazení na server + záloha | C | |
| 11 | D1–D2 protokol ověření | D | |
| 12 | E1–E5 instalace, docker, testy, protokoly | E | lze souběžně s C |
| 13 | E6–E8 Saaty matice do XLSX | E | až po testech |
| 14 | F1–F6 běh v app + citlivosti | F | |
| 15 | G0–G3 BP 0, 1, 2, 3 | G | po schválení; G2 brzy |
| 16 | G4–G6 BP 4–8 doladění | G | |
| 17 | G7–G9 BP 11–13 praxe + závěr | G | až po D–F |
| 18 | G10–G11 literatura + spojení | G | |
| 19 | H1–H4 přílohy, Word, odevzdání | H | |

---

# Definice hotové práce (vše `[x]`)

- [ ] Fáze 0 STAG
- [ ] Fáze B spec + Excel etalon + operacionalizace + XLSX struktura + app SPEC
- [ ] Fáze C app lokálně i na serveru
- [ ] Fáze D protokol app = Excel
- [ ] Fáze E 4 protokoly + matice z testů
- [ ] Fáze F základní výsledek + 3 citlivosti
- [ ] Fáze G text osnovy 1–6 včetně BP 2 a BP 0
- [ ] Fáze H DOCX + odevzdání

**Celá BP = tento seznam hotový.**

---


---

# LITERATURA A ZDROJE (co mám, co citovat, co do STAGu)

## Důležité oddělení (ať se to neplete s cílem)

| Položka | Co to je | Kam to patří | Na co se vedoucí ptál naposledy (2. 9.) |
|---|---|---|---|
| **Cíl práce** | 1–2 odstavce: app + AHP + ověření | pole Cíl ve STAGu / blok **Cíl práce** v mailu | **Ano** — upřesnit cíl a rozsah praxe |
| **Osnova** | body 1–6 | zásady pro vypracování | **Ano** |
| **Literatura do zadání** | 4–5 bibliografických záznamů | **samostatné** pole Literatura ve STAGu / samostatný blok v mailu | **Ne v mailu 2. 9.** — to je starší požadavek k zadávacímu listu (cca 4–5 zdrojů ze seminárky, ISO 690). Vedoucí se **neptal**, které AHP články máš vyměnit |
| Celá bibliografie BP | ≥ 30 zdrojů | `BP 10.md` na konci práce | až při psaní textu |

**Cíl se nemění kvůli literatuře.** V cíli nebudou autoři, názvy článků ani „použiji Ishizaku/Soukopovou“.  
Sekce L0–L6 je **interní pracovní doporučení pro tebe** (co máš jako PDF, co uneseš číst, co dát do pole Literatura). Není to úkol od vedoucího ve smyslu „rozhodni se mezi Ishizakou a Soukopovou“.

Podklad evidence: `ZDROJE.md` (aktualizace 8. 9. 2026).  
Pravidlo: **cituj jen to, co máš a co reálně použiješ.** Nespoléhej na angličtinu „naslepo“.  
Složka `literatura/inspirace/` = **necitovat v BP** (cizí BP/DP jen jako vzor postupu).

## L0 — Stav na disku (ověřeno)

### AHP — lokální PDF v `literatura/AHP/` (máš)

| Zdroj | Soubor | Jazyk | Priorita pro tebe |
|---|---|---|---|
| Saaty (1990) | `Saaty_1990_How_to_make_a_decision_AHP.pdf` | EN | **Povinný základ metody** (PDF plný text) |
| Saaty (2008) | `Saaty_2008_Decision_making_with_AHP.pdf` | EN | Doplněk k 1990 |
| Ishizaka a Labib (2011) | `Ishizaka_Labib_2011_Review_AHP_Developments.pdf` | EN | PDF máš; do textu jen když ho opravdu pročteš (těžší AJ) |
| Soukopová (2016) | `Soukopova_2016_Vicekriterialni_metody_hodnoceni.pdf` | **CZ** | **Hlavní český výklad MCDM/AHP** |
| Tomeš a Alcnauer (2014) | `Tomes_Alcnauer_2014_AHP_konzistence_matice.pdf` | **CZ** | **Konzistence CI/CR** — ideál k app |
| Vlčková a Friebel (2015) | `Vlckova_Friebel_2015_Kvalita_dat_financniho_ucetnictvi_AHP.pdf` | **CZ** | Český příklad **použití** AHP |
| Velasquez a Hester (2013) | `Velasquez_Hester_2013_…pdf` | EN | PDF máš; volitelně MCDM přehled |
| Mardani et al. (2015) | `Mardani_2015_…pdf` | EN | PDF máš; volitelně |
| Ho (2008), Catak (2012), Ebrahimi (2015), Simanavičienė (2023), Moreno-Jiménez (2018) | v `literatura/AHP/` | EN | PDF máš; cituj jen při reálném použití |
| Bunruamkaew (2012) Excel návod | `Bunruamkaew_2012_How_to_do_AHP_analysis_in_Excel.pdf` | EN | **Pomůcka k Excelu**, do bibliografie BP spíš **ne** |

### DB — lokální PDF v `literatura/DB/` (výběr)

| Zdroj | Soubor | Poznámka |
|---|---|---|
| Pokorný a Valenta (2020) | `Pokorny_Valenta_2020_Databazove_systemy.pdf` | **CZ kniha, plné PDF, koupená — držet** |
| Chlapek, Kučera, Palovská (2019) | `Chlapek_Kucera_Palovska_2019_…pdf` | **CZ kniha, plné PDF — držet** |
| Carvalho et al. (2022) | `Carvalho_2022_…pdf` | EN článek o modelovacích nástrojích — PDF máš |
| Chen (1976), Codd (1970), Watt a Eng (2014), Rosenthal (1994), Feinberg (2017), Laranjeiro (2024) | v `DB/` | PDF máš; cituj jen použité pasáže |
| Elmasri a Navathe (2016) | `Elmasri_Navathe_2016_…pdf` | **jen výňatek kap. 1–3** — cituj jen z výňatku |
| Hronek (2007), Otte (2013) | v `DB/` | PDF na disku, **nejsou** v oficiálních 27 — jen po přečtení |
| Dokumentace nástrojů + DB-Engines | `*.url` v `DB/` | weby — citovat s datem přístupu |

### Online bez lokálního PDF

| Zdroj | Stav | Pravidlo |
|---|---|---|
| Vaidya a Kumar (2006) | v `ZDROJE` jen ResearchGate odkaz | **Necituj**, dokud si nestáhneš a neověříš plný text |

### Necitovat

- cokoliv v `literatura/inspirace/` (Jakubek, Jandová, Vohradský, Müllerová, …)
- prezentace UHK jako „odborný zdroj“ (max studijní pomůcka, ne do BP 10)
- zdroje, které jsi neotevřel / nerozumíš jim natolik, abys obhájil citaci

## L1 — Pět zdrojů do pole **Literatura** (STAG / samostatný blok v mailu) — doporučená sada`n`nToto **není součást cíle**. Vedoucí v posledním mailu neřekl „vyměň Ishizaku“. Jde o praktickou volbu pro tebe: do pole Literatura dej zdroje, které **máš jako PDF** a zvládneš.

**Cíl sady:** 2–3 knihy/články česky nebo dobře zvládnutelné + Saaty jako primární AHP + 1 zdroj k nástrojům. Vše **máš jako PDF**.

| # | Zdroj do STAGu | Proč |
|---|---|---|
| 1 | **CHLAPEK, KUČERA, PALOVSKÁ (2019)** | CZ, modelování, PDF máš |
| 2 | **POKORNÝ, VALENTA (2020)** | CZ, DB systémy, PDF + koupená kniha |
| 3 | **SAATY (1990)** | primární AHP, PDF máš (EN, ale krátký klasický text na vzorce) |
| 4 | **SOUKOPOVÁ (2016)** *nebo* **TOMEŠ a ALCNAUER (2014)** | **česky AHP/MCDM** — viz L1a |
| 5 | **CARVALHO et al. (2022)** | srovnání modelovacích nástrojů, PDF máš |

### L1a — Volba položky 4 (české AHP)

| Varianta | Kdy zvolit |
|---|---|
| **A — Soukopová (2016)** | chceš v zadání spíš **výklad vícekriteriálních metod / AHP česky** |
| **B — Tomeš a Alcnauer (2014)** | chceš v zadání silně **konzistenci matic (CI, CR)** k aplikaci |

**Doporučení default:** varianta **A (Soukopová)** do STAGu; Tomeše i Vlčkovou stejně **zařaď do plné bibliografie BP** (G10).

### L1b — Co ze staré pětice vynechat ve STAGu

| Zdroj | Ve STAGu | V celé BP |
|---|---|---|
| **Ishizaka a Labib (2011)** | **ne jako povinná 5.** (PDF máš, ale těžká AJ review) | volitelně až po reálném přečtení |
| Saaty 1990 | **ano** | ano |
| Valenta, Chlapek, Carvalho | **ano** | ano |

### L1c — Kdy sahat na literaturu v mailu / STAGu (cíl netyká)

1. **Cíl a osnovu** v mailu kvůli literatuře **neměň**.
2. Pokud e-mail **ještě neodešel** a chceš v bloku **Literatura do zadání** (ne v cíli) vyměnit Ishizaku za Soukopovou/Tomeše: ano, jen ten blok; citace z `ZDROJE.md`.
3. Pokud e-mail **už odešel** s Ishizakou v literatuře: nic nedramatizuj — PDF máš. Ve STAGu po schválení můžeš nechat nebo v poli Literatura doladit.
4. Po schválení cíle: do STAGu cíl = e-mailový cíl; literatura = samostatné pole (L1 jako nápověda).

### L1d — Hotové citace pro STAG (ISO 690, pracovní)

Použij přesné znění z e-mailu / `ZDROJE.md`. Pro novou položku 4:

**Soukopová (2016)** — ověř přesný bibliografický zápis podle PDF a IS MUNI; v projektu je učební text ESF MU, rok 2016 dle `ZDROJE.md`.

**Tomeš a Alcnauer (2014)** (z `ZDROJE.md`):  
`TOMEŠ, Rostislav a Július ALCNAUER. Konzistence matice párových porovnání při použití Analytického hierarchického procesu (AHP). Business & IT. 2014, 4(2), 114–124. ISSN 1805-0794.`

**Vlčková a Friebel (2015)** (do plné BP, ne nutně STAG 5):  
`VLČKOVÁ, Miroslava a Ludvík FRIEBEL. Návrh metodiky na hodnocení kvality dat finančního účetnictví metodou AHP. Český finanční a účetní časopis. 2015, 10(2), 58–69. ISSN 1802-2367. DOI: 10.18267/j.cfuc.443.`

## L2 — Minimální sada pro kapitolu AHP v textu BP (co opravdu číst)

Bez těchto tří **nepiš** AHP kapitolu „od oka“:

1. **Saaty (1990)** — škála 1–9, párové matice, princip vah a konzistence (klidně s překladačem po odstavcích; cituj vzorce a definice).  
2. **Soukopová (2016)** — český rámec vícekriteriálního hodnocení / AHP.  
3. **Tomeš a Alcnauer (2014)** — konzistence matice, CI, CR (napojení na app a Excel).

Doplňky podle potřeby:

4. **Vlčková a Friebel (2015)** — jeden český příklad aplikace AHP.  
5. **Saaty (2008)** — pokud něco chybí v 1990.  
6. **Velasquez a Hester (2013)** — proč AHP mezi MCDM (až když článek otevřeš).

**Ishizaka (2011)** — neblokuje práci; zařaď až když zvládneš shrnout review vlastními slovy.

## L3 — Minimální sada pro DB / modelování / nástroje

1. **Pokorný a Valenta (2020)** — pojmy DB, DBMS, návrh.  
2. **Chlapek, Kučera, Palovská (2019)** — datové modelování, relační návrh.  
3. **Carvalho et al. (2022)** — srovnání nástrojů datového modelování (podklad výběru alternativ).  
4. Oficiální dokumentace 4 nástrojů (weby + datum citace) — při charakteristice nástrojů a verzích.  
5. Volitelně: Chen (1976) u ER, Codd (1970) u relačního modelu, Watt a Eng (2014) jako otevřená učebnice — **jen citované stránky z PDF**.

## L4 — Pravidla citování po celou BP

1. Každá citace v textu musí být v `BP 10.md` a v souladu s `ZDROJE.md`.  
2. Celkem **≥ 30 použitých** zdrojů, z toho **≥ 20 knih nebo odborných článků** (požadavek vedoucího).  
3. Web dokumentace nástrojů se počítá, ale **nesmí** nahradit knihy/články u AHP a DB teorie.  
4. U anglických článků cituj jen tvrzení, které v PDF najdeš (číslo stránky / sekce).  
5. U Elmasriho cituj jen z místního výňatku.  
6. Nekopíruj bibliografii „pro dojem“ z inspiračních DP.  
7. Při psaní kapitoly nejdřív otevři PDF → pak piš → pak cituj (ne naopak).

## L5 — Checklist před odevzdáním literatury

- [ ] STAG 5 zdrojů = schválená sada (L1) a všechny mají soubor nebo ověřený web  
- [ ] Saaty 1990 + Soukopová + Tomeš v BP 10 a použité v textu AHP  
- [ ] Valenta + Chlapek použité v DB kapitolách  
- [ ] Carvalho nebo jiný zdroj u výběru nástrojů  
- [ ] 4× dokumentace nástrojů s datem  
- [ ] Žádná citace jen z `inspirace/`  
- [ ] Ishizaka jen pokud je v textu reálně použit  
- [ ] `ZDROJE.md` a `BP 10.md` sladěné  
- [ ] Počet ≥ 30 / ≥ 20 knih+článků

## L6 — Úkoly v pořadí práce (literatura)

| Kdy | Úkol |
|---|---|
| Teď / Fáze 0 | Cíl odeslat jak je (bez literatury v cíli). Volitelně jen blok Literatura v mailu dle L1a. Po schválení: cíl → pole Cíl; 5 zdrojů → pole Literatura |
| Fáze B (AHP spec) | Číst Saaty 1990 (vzorce) + Tomeš (CR) + Soukopová; citace půjdou do spec/metodiky později |
| Fáze G (text) | Stavět AHP kapitolu na L2; DB na L3; průběžně doplňovat BP 10 |
| Fáze G10 | Finální sladění BP 10 ↔ ZDROJE ↔ skutečné citace v textu |
| Fáze H | Checklist L5 |

---

# Zákazy

1. Nevymýšlet matice, pořadí, CR, ceny, verze.
2. Nekódit celou app před B2–B3.
3. Nedělat Saaty před protokoly z testů.
4. Nepřevádět checklist 1–5 automaticky na Saaty.
5. Nepřidávat 2. scénář, group AHP, jinou MCDM, login/admin.
6. Nehodnotit správu serverů, zálohy, výkon.
7. Nepoužít BP 9 seminárky jako závěr BP.
8. Nebrat čísla z AHP_NAVOD_SAATY.md bez vlastního přepočtu.
9. Necitovat zdroje bez ověřeného PDF/webu, inspirace/, ani anglické review (Ishizaka aj.), které jsi reálně nepoužil — viz sekce Literatura L0–L4.
