# Plán další práce

Aktualizace: 6. 7. 2026.

Pracuje se po kapitolách v souborech `Seminární práce 0.md` – `Seminární práce 11.md`. Finální `Seminární práce.md` a `.docx` se z nich jen generují (viz `PŘEHLED.md`).

---

## 1. Seminární práce — co zbývá udělat

### 🔴 Nejbližší úkoly (Finální opravy před odevzdáním)

Tyto úkoly vycházejí z komplexní kontroly po vašich posledních úpravách (commity 19a, 19b) a je nutné je dokončit jako poslední krok před odevzdáním:

1. **Kapitola 0 (abstrakt EN):** Opravit překlep `Methodological` (velké písmeno uprostřed věty) -> **methodological**.
2. **Kapitola 2 (odstavec 2):** Opravit překlep `hodnocená` -> **hodnocení**.
3. **Kapitola 3 (odstavec 2):** Opravit hrubou gramatickou chybu v souřadném spojení: `nejen..., tak i...` -> **nejen..., ale i...** (nebo *nejen..., ale také...*).
4. **Kapitola 3 (odstavec 2):** Opravit překlep `prace Saatyho` -> **práce Saatyho**.
5. **Kapitola 3 (odstavec 3):** Opravit hrubou gramatickou chybu v pádu `Při jejich výběr` -> **Při jejich výběru**.
6. **Kapitola 4 a `4x.md`:** Opravit překlep a syntaktickou chybu `Tento datábázový systém který usnadňuje procesy...` -> **Tento databázový systém usnadňuje procesy...**.
7. **Kapitola 6:** Odstranit stále přetrvávající překlep `jsou jdou` -> **lze**.
8. **Kapitola 6:** Opravit hrubou gramatickou chybu: `bylo zvolenou metodou, metoda AHP a to...` -> **byla zvolena metoda AHP, a to...**.
9. ~~**Kapitola 11 (Seznam zdrojů):** Dočistit soubor `Seminární práce 11.md` — odstranit `[101]`, `[102]` a pomocné cesty.~~ ✅ Hotovo 6. 7. 2026.
10. **Kapitola 4:** Nahradit nespisovné slovo `taky` spisovnou variantou **také** (`...ale také externími nástroji...`).
11. **Kapitola 7:** Nahradit nevhodnou předložku `U navazující praktické části...` přirozenější vazbou **V navazující praktické části...**.
12. **Kapitola 8 (sekce 8.4 pgModeler):** Nahradit neurčitou verzi `bude testována aktuální stabilní verze...` konkrétním číslem (např. **verze 1.1**).

---

### Co je hotovo (Archiv splněných úkolů z revize)

* ✅ Sjednoceno a upraveno záhlaví v `Seminární práce 0.md` na *„Teoretická a metodická východiska“* (bod D10).
* ✅ Vyřešena shoda podmětu a přísudku u slova *patřily* a opraven překlep *sdílení dat* v kapitole 4.
* ✅ Upřesněna a doplněna definice databázového systému (DBS) o uživatele a aplikační software v širším smyslu (bod D1).
* ✅ Vyřešena vazba *u nichž* namísto časového *kdy* u tranzitivních závislostí v kapitole 5.
* ✅ Opravena shoda pádů u výčtu objektů v kapitole 9 (*„podpora objektů, jako jsou tabulky...“*).
* ✅ Odstraněna nadbytečná čárka v souřadném spojení *„jak... tak...“* u VO2 v kapitole 10.
* ✅ Opravena kritická stylistická chyba v Kapitole 1 (vazba *brání intuitivní volbě* a oprava dvojité mezery).
* ✅ Doplněna chybějící definice dominance v Kapitole 6 (ve Vrstvě 1 i Vrstvě 2).
* ✅ Přerozděleny citace po větách ve Vrstvě 2 u kapitol 6 a 7 (29. 6. 2026).
* ✅ Sjednoceny oddělovače vrstev na `****` a opravena kurzíva u termínu *rank reversal*.
* ✅ Z metodiky odstraněna věta o citování (požadavek vedoucího).
* ✅ Doplněny a vyhledány DB zdroje pro kapitoly 4 a 5 (19. 6. 2026).
* ✅ Opraven překlep `nasledující` -> `následující` v kapitole 10.
* ✅ Opraven nesoulad rodu přísudku `bude rozpracován ... aplikace` v kapitole 10.
* ✅ Opraven překlep s mezerou u citace Catak v kapitole 7 (`Catak et al., 2012;`).

---

### Co musí být hotovo PŘED odesláním vedoucímu (Odevzdání)

1. **Přesunout text do oficiální šablony** z předmětu MES (složka `oliva/sablony/`).
2. **Vygenerovat a sestavit finální dokument:**
   ```powershell
   .\extrahuj.ps1                          # z kapitol 4–7 vytvoří 4x–7x (odstraní řádky začínající ">")
   .\spoj.ps1 0 1 2 3 4x 5x 6x 7x 8 9 10 11 -Out "Seminární práce.md"
   pandoc "Seminární práce.md" -o "Seminární práce.docx" --reference-doc="oliva/sablony/sablona_MES.docx"
   ```
3. **Zkontrolovat celkový rozsah:** Teorie (kapitoly 4–7) musí mít ve Wordu min. 10 normostran.
4. **Zkontrolovat shodu citací:** Ověřit, že každý odkaz v textu (zejména nově přidané a upravené) přesně odpovídá seznamu v kapitole 11.
5. **Odeslat vedoucímu k finálnímu schválení.**

---

## 2. Paralelně: STAG zadávací list (do 31. 8. 2026)

Vyplnit ve STAGu:
- Anglický název: *Comparison of Database Design and Development Tools Using AHP*
- 4–5 zdrojů (alespoň 2–3 knihy + článek/web), citace dle ISO 690:2022
- Odeslat ke schválení

---

## 3. Bakalářská práce — následně

Seminárka slouží jako teoretický základ. BP doplní:
1. Instalace a testování nástrojů (MySQL Workbench, Oracle SQL Developer Data Modeler, DBeaver CE, pgModeler).
2. Jednotný testovací scénář (model → SQL → reverzní inženýrství).
3. AHP výpočty: Saatyho matice, váhy, CR < 0,1, analýza citlivosti.
4. Doporučení pro praxi.
5. Rozšíření literatury na min. 30 zdrojů (20 knih/článků).

---

## 4. Milníky

| Termín | Úkol | Stav |
|---|---|---|
| 26. 6. 2026 (pátek) | Poslat vedoucímu průběžnou ukázku pro rychlou kontrolu. | ✅ Splněno |
| 6. 7. 2026 (dnes) | Provést finální gramatické a stylistické opravy a vyřešit zbývající drobné resty. | ⏳ Probíhá |
| 7. 7. 2026 (úterý) | Sestavit finální dokument v šabloně a odeslat vedoucímu k schválení. | ⏳ Plánováno |
| červenec 2026 | Odevzdat v Olivě, splnit zápočtový test. | ⏳ Plánováno |
| do 31. 8. 2026 | Vyplnit a odeslat zadávací list do STAGu. | ⏳ Plánováno |
| podzim 2026 / 2027 | Realizace praktické části bakalářské práce. | ⏳ Plánováno |
