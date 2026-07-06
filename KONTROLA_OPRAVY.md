# KONTROLA OPRAVY

Kontrola vychází z aktuálního souboru `seminarka_kontrola.md` a je sloučená s předchozím souborem `KONTROLA_DOPORUCENI.md`. Starší body, které už jsou v aktuální verzi opravené nebo se týkají pouze dílčích pracovních souborů, nejsou vedené jako aktivní chyby.

Cílem tohoto souboru je evidovat jen skutečné chyby: gramatické chyby, překlepy, citační/formální problémy, metodické nejasnosti a rozpory v logice práce. Kostrbaté nebo osobité formulace nejsou zahrnuté, pokud nejsou věcně špatně.

## 1. Aktivní opravy v `seminarka_kontrola.md`

### 1.1 Chybí seznam zdrojů

**Místo:** konec souboru po řádku 396

**Problém:** Soubor aktuálně končí závěrem a zalomením stránky. Chybí část `Seznam zdrojů`, přestože text používá mnoho průběžných citací, například:

- `(Elmasri a Navathe, 2016)`,
- `(Pokorný a Valenta, 2020)`,
- `(Carvalho et al., 2022)`,
- `(Saaty, 1990; Saaty, 2008)`,
- `(Oracle, 2026)`, `(DBeaver, 2026)`, `(MySQL, 2026)`, `(pgModeler, 2026)`.

**Proč opravit:** Pokud text obsahuje citace v těle práce, musí mít odpovídající bibliografický seznam. Bez seznamu zdrojů je práce formálně nedokončená.

**Návrh opravy:** Na konec dokumentu doplnit kapitolu:

```markdown
# Seznam zdrojů
```

a uvést všechny zdroje citované v textu.

### 1.2 Gramatická chyba: `V navazují práci`

**Místo:** řádek 128

**Původní text:**

> V navazují práci budou nástroje hodnoceny podle jednotného postupu.

**Návrh opravy:**

> V navazující práci budou nástroje hodnoceny podle jednotného postupu.

**Lepší sjednocená varianta:**

> V navazující praktické části budou nástroje hodnoceny podle jednotného postupu.

**Proč opravit:** `navazují práci` je gramaticky chybný tvar. Správně má být `navazující práci`, případně `navazující praktické části`.

### 1.3 Sjednocení označení navazující části

**Místo:** řádky 128 a 130

**Původní texty:**

> V navazují práci budou nástroje hodnoceny podle jednotného postupu.

> Samotné porovnání nástrojů proběhne v navazující části pomocí metody AHP.

**Návrh opravy:**

> V navazující praktické části budou nástroje hodnoceny podle jednotného postupu.

> Samotné porovnání nástrojů proběhne v navazující praktické části pomocí metody AHP.

**Proč opravit:** Nejde jen o styl. Text má jasně oddělit, co řeší tato seminární práce a co bude následovat až v praktické části. Použití stejného výrazu sníží riziko nejasnosti.

### 1.4 Nejednotná verze pgModeleru

**Místo:** řádek 344

**Původní text:**

> Pro účely této práce bude testována aktuální stabilní verze ke dni testování.

**Problém:** U Oracle SQL Developer Data Modeler, DBeaveru a MySQL Workbench jsou uvedené konkrétní verze, ale u pgModeleru ne.

**Návrh opravy:** Buď doplnit konkrétní verzi pgModeleru, nebo stejnou obecnou formulaci použít u všech nástrojů.

**Proč opravit:** U porovnávání nástrojů je verze důležitá kvůli opakovatelnosti. Tři konkrétní verze a jedna neurčitá verze působí metodicky nejednotně.

### 1.5 Kritérium K8 není v souladu s typem kritéria

**Místo:** řádek 361 a navazující vysvětlení na řádku 381

**Původní text v tabulce:**

> K8 | Náklady a výhodnost licence | minimalizační | typ licence, omezení bezplatné verze, celková cena

**Problém:** `Náklady` jsou minimalizační kritérium, protože nižší náklady jsou lepší. `Výhodnost licence` je ale významově spíš maximalizační, protože vyšší výhodnost je lepší.

**Návrh opravy 1:**

> K8 | Náklady a licenční omezení | minimalizační | celková cena, omezení bezplatné verze, náročnost zavedení

**Návrh opravy 2:**

> K8 | Výhodnost nákladů a licence | maximalizační | nižší náklady, výhodnost licenčních podmínek, dostupnost bezplatné verze

**Proč opravit:** V AHP musí být jasné, co znamená lepší hodnota. Současný název kritéria a typ `minimalizační` nejsou úplně v souladu.

### 1.6 Popisek tabulky 1

**Místo:** řádek 328

**Původní text:**

> Tabulka 1 – Základní charakteristiky vybraných nástrojů (zdroje: Oracle, 2026; DBeaver, 2026; MySQL, 2026; pgModeler, 2026)

**Návrh opravy:**

> Tabulka 1 – Základní charakteristiky vybraných nástrojů (vlastní zpracování podle Oracle, 2026; DBeaver, 2026; MySQL, 2026; pgModeler, 2026)

**Proč opravit:** Tabulka není přímo převzatá jako celek. Je autorsky sestavená podle dokumentací, proto je přesnější uvést `vlastní zpracování podle...`.

### 1.7 Dvojitá mezera v závěru

**Místo:** řádek 391

**Původní text:**

> ...bude v následující práci podrobněji  popsán testovací scénář...

**Návrh opravy:**

> ...bude v následující práci podrobněji popsán testovací scénář...

**Proč opravit:** Mezi slovy `podrobněji` a `popsán` jsou dvě mezery. Jde o technický překlep.

## 2. Body převzaté ze staré kontroly, které jsou v aktuálním souboru už opravené

Tyto body byly v `KONTROLA_DOPORUCENI.md`, ale v aktuálním `seminarka_kontrola.md` už nejsou aktivním problémem:

- Anglický abstrakt: `Methodological` s velkým písmenem uprostřed věty už v aktuálním souboru není.
- Kapitola 2: překlep `hodnocená` už v aktuálním souboru není.
- Kapitola 3: spojení `nejen..., tak i...` už je opravené na `nejen..., ale i...`.
- Kapitola 3: `prace Saatyho` už je opravené na `práce Saatyho`.
- Kapitola 3: `Při jejich výběr` už je opravené na `Při jejich výběru`.
- Kapitola 4: chyba `datábázový systém který...` už je opravena.
- Kapitola 6: chyba `jsou jdou použít` už v aktuálním souboru není.
- Kapitola 6: věta `bylo zvolenou metodou, metoda AHP` už v aktuálním souboru není.
- Kapitola 11: pracovní zdroje `[101]` a `[102]` v aktuálním souboru nejsou, protože aktuální soubor nemá seznam zdrojů vůbec. Tento problém se tedy přesouvá pod aktivní bod 1.1 `Chybí seznam zdrojů`.
- Menší stylistické body jako `taky` nebo `U navazující praktické části` nejsou vedené jako aktivní chyby, pokud v aktuálním souboru nejsou nebo nejde o skutečný rozpor.

## 3. Co záměrně neřešit

Neoznačovat jako chyby:

- osobitější nebo jednodušší formulace typu `je potřeba`,
- věty, které jsou trochu těžkopádné, ale významově správné,
- formulace typu `Ze studie vyplývá...`,
- výraz `sdílenost dat`, pokud nevadí stylově,
- opakování slov, pokud nezpůsobuje nejasnost nebo rozpor.

## 4. Priorita oprav

1. Doplnit `Seznam zdrojů`.
2. Opravit řádek 128: `V navazují práci`.
3. Sjednotit označení `navazující praktická část` v řádcích 128 a 130.
4. Vyřešit konkrétní verzi pgModeleru.
5. Upravit kritérium K8 tak, aby seděl název a typ kritéria.
6. Opravit popisek tabulky 1.
7. Opravit dvojitou mezeru v závěru.
