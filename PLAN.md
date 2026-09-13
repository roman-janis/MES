# Plán práce od začátku podle učitele

Aktualizace: 10. 9. 2026

Plán je sladěn s návrhem cíle a osnovy v `EMAIL_VEDOUCIMU_KOMENTOVANY_UPRAVENY_2.md`. Tento e-mail zatím nebyl odeslán a vedoucí návrh ještě neschválil. Po jeho vyjádření se plán a zadání ve STAGu doladí.

## Výchozí stav

- Teoretický základ práce se vrací na finální seminární verzi podle `seminární práce/MES_Janiš_final.txt`.
- Praktická část (PHP aplikace) se zatím neimplementuje.
- Rozsah praktické části je vymezen návrhem e-mailu vedoucímu: podpůrná AHP aplikace, ověření na modelovém případu, nezávislý kontrolní výpočet, tři změny citlivosti.
- Soubor `hodnoceni_4_nastroju.xlsx` je založený jako pracovní sešit. Vyplňovat se začne až při reálném hodnocení čtyř nástrojů podle K1–K8.
- Zadávací list ve STAGu se doplní až po odsouhlasení cíle a osnovy vedoucím (termín 15. 10. 2026).

## Hlavní princip

**Těžiště práce:** navrhnout a vytvořit jednoduchou webovou aplikaci v PHP pro podporu výběru nástroje pro návrh a vývoj databázových systémů metodou AHP a ověřit její funkčnost.

**Demonstrační obsah:** čtyři nástroje a kritéria K1–K8 ze seminární práce, jeden modelový případ (Cykloservis), tři změny důležitosti kritérií.

**Pořadí práce:**

1. mít jasný účel aplikace, alternativy, kritéria a scénář (hotovo jako pracovní vymezení),
2. připravit datový návrh a ověřený postup AHP výpočtu včetně způsobu nezávislé kontroly,
3. teprve potom implementovat minimální PHP aplikaci,
4. ověřit výpočty a použití na modelovém případu,
5. zhodnotit výsledky, omezení a rozšiřitelnost.

Komparace nástrojů není druhé paralelní téma bakalářské práce. Je připraveným obsahem aplikace a způsobem, jak doložit, že aplikace funguje.

## Návrh z e-mailu vedoucímu (pracovní znění)

Zdroj: `EMAIL_VEDOUCIMU_KOMENTOVANY_UPRAVENY_2.md`. Stav: připraveno k odeslání / odeslání zatím nepotvrzeno.

### Název

- Česky: Komparace nástrojů pro návrh a vývoj databázových systémů pomocí AHP
- Anglicky: Comparison of Tools for Database System Design and Development Using AHP

### Cíl práce

Cílem bakalářské práce je navrhnout a vytvořit jednoduchou webovou aplikaci pro podporu výběru nástrojů určených pro návrh a vývoj databázových systémů s použitím rozhodovací metody AHP a následně ověřit její funkčnost na modelovém případu. Aplikace bude implementována v jazyce PHP a umožní uživateli vybírat z připravených nástrojů a hodnoticích kritérií, doplňovat vlastní položky a zadávat párová porovnání podle svých preferencí. Na základě zadaných porovnání vypočítá výsledné pořadí nástrojů. Ověření bude zahrnovat kontrolu správnosti výpočtů nezávislým kontrolním výpočtem a použití aplikace na modelovém případu Cykloservisu se čtyřmi vybranými nástroji a kritérii K1 až K8, včetně posouzení vlivu tří samostatných změn důležitosti kritérií na výsledek.

### Osnova (zásady pro vypracování)

1. Vymezit problematiku návrhu relačních databází.
2. Popsat metodu AHP a postup výpočtu vah a kontroly konzistence.
3. Vybrat a vymezit porovnávané nástroje a hodnoticí kritéria.
4. Navrhnout a vytvořit jednoduchou webovou aplikaci v PHP pro podporu výběru nástroje pomocí párových porovnání a výpočtů AHP.
5. Ověřit správnost výpočtů a fungování aplikace na modelovém případu a posoudit vliv změn důležitosti kritérií na výsledek.
6. Zhodnotit výsledky, omezení a možnosti dalšího rozšíření.

### Literatura do zadání (5 zdrojů)

1. CARVALHO et al. (2022) – IEEE Access, datové modelovací nástroje.
2. CHLAPEK, KUČERA, PALOVSKÁ (2019) – datové modelování.
3. ISHIZAKA, LABIB (2011) – přehled AHP.
4. POKORNÝ, VALENTA (2020) – databázové systémy.
5. SAATY (1990) – AHP.

Úplné citace jsou v e-mailovém návrhu a musí zůstat sladěné s `ZDROJE.md` / `BP 10.md`. Pro celou BP platí požadavek nejméně 30 použitých zdrojů, z toho alespoň 20 knih nebo odborných článků.

## Pořadí kroků

### 1. Vymezit přesný účel aplikace

**Stav: hotovo (pracovní vymezení podle návrhu e-mailu).**

Účelem aplikace je podpořit výběr nástroje pro **návrh a vývoj** databázových systémů podle preferencí uživatele pomocí metody AHP. Nehodnotí se provozní správa serverů, zálohování ani výkon DBMS.

Aplikace:

- nabídne připravené nástroje a hodnoticí kritéria s popisy a odkazy,
- umožní doplnit vlastní položky,
- umožní zadat párová porovnání,
- vypočítá váhy, konzistenci a výsledné pořadí,
- zobrazí výsledek odpovídající zadaným preferencím (ne univerzálně nejlepší nástroj).

Vstupy:

- výběr připravených alternativ a kritérií,
- případné vlastní alternativy a kritéria,
- párová porovnání důležitosti kritérií,
- párová porovnání alternativ podle jednotlivých kritérií.

Výstupy:

- váhy kritérií a lokální váhy alternativ,
- kontrola konzistence a upozornění na problematické vstupy,
- celkové priority a výsledné pořadí.

Základní verze neobsahuje účty, role, rozsáhlou administraci, REST API ani automatický sběr produktových dat. Rozšíření na jinou rozhodovací doménu stačí popsat, pokud na implementaci nezbude prostor.

### 2. Uzamknout seznam alternativ

**Stav: hotovo.**

Konečný seznam alternativ (ze seminární práce; připravený obsah aplikace a ověřovací případ):

- Oracle SQL Developer Data Modeler,
- DBeaver Community Edition,
- MySQL Workbench Community Edition,
- pgModeler.

Přesné edice a verze se zaznamenají podle skutečně testovaných instalací. Bezplatnost, open-source a placená distribuce nejsou totéž. Zdůvodnění výběru je v `BP 7.md`.

### 3. Uzamknout seznam kritérií

**Stav: hotovo.**

Konečný seznam K1–K8:

| Kritérium | Název | Stručný význam | Charakter posouzení |
|:--:|:---|:---|:---|
| K1 | Funkcionalita modelování | Podpora modelu, databázových objektů, datových typů, klíčů, vztahů a integritních omezení. | Převážně objektivní. |
| K2 | Použitelnost | Přehlednost, dohledatelnost funkcí, srozumitelnost chyb, počet kroků, čas a nutné obchvaty. | Převážně subjektivní, podložené pozorováním. |
| K3 | Kompatibilita s DBMS | Rozsah skutečné podpory modelování, generování DDL a reverse engineeringu pro různé DBMS. | Převážně objektivní. |
| K4 | Forward engineering | Vytvoření spustitelného DDL nebo databázového schématu z modelu při zachování klíčů a omezení. | Převážně objektivní. |
| K5 | Reverse engineering | Načtení existujícího schématu do modelu nebo diagramu včetně klíčů, vztahů a omezení. | Převážně objektivní. |
| K6 | Dokumentace a komunitní podpora | Dostupnost, aktuálnost a použitelnost dokumentace a relevantní komunitní pomoci. | Kombinované objektivní a kvalitativní posouzení. |
| K7 | Import a export modelu | Dostupnost a použitelnost nativních formátů pro import a export modelu nebo diagramu. | Převážně objektivní. |
| K8 | Náklady a licenční omezení | Cena, typ licence a omezení použité bezplatné nebo komunitní edice. | Převážně objektivní, časově závislé. |

„Převážně objektivní“ označuje charakter podkladů, nikoli automaticky objektivní párový úsudek. K1, K4, K5 a K7 držet odděleně; totéž DDL nehodnotit znovu v K7.

Praktické ověření ve čtyřech nástrojích podle stejného zadání Cykloservisu dodá podklady pro párová porovnání. Pomocné známky 1–5 z checklistu se nepřevádějí automaticky na Saatyho škálu.

### 4. Připravit jeden hlavní scénář

**Stav: hotovo.**

Modelový případ: **Cykloservis** – malá firma vybírá nástroj pro návrh relační databáze. Omezený rozpočet, bez specializovaného databázového architekta. Cílový DBMS nemusí být předem pevně dán.

Rozsah: návrh relační databáze a výběr modelovacího nástroje. Mimo rozsah: celý IS cykloservisu; provozní správa serverů, zálohování a výkon.

Hodnotitelem demonstračního případu je autor; toto omezení se v práci výslovně uvede.

### 5. Připravit změny pro citlivost

**Stav: hotovo v rozsahu přípravy. Výpočty a výsledky dosud nejsou provedeny.**

Tři samostatné změny důležitosti kritérií (nekumulují se). Matice alternativ zůstávají stejné.

| Změna | Co se upraví | Co se bude ověřovat |
|---|---|---|
| Přísnější rozpočet | Vyšší důležitost K8 | Vliv ekonomických a licenčních preferencí na pořadí |
| Vyšší důraz na modelování | Vyšší důležitost K1 | Vliv důrazu na funkcionalitu modelování |
| Vyšší důraz na více DBMS | Vyšší důležitost K3 | Vliv důrazu na šíři podpory platforem |

Výstup: tabulka základního výsledku a tří změn + krátká interpretace. Nezměněné pořadí je platný výsledek.

### 6. Připravit datový návrh aplikace

**Stav: otevřené.**

Navrhnout entity a vazby pro:

- připravené alternativy a kritéria (popis, odkazy),
- vlastní položky,
- konkrétní hodnocení / scénář,
- párová porovnání,
- vypočtené váhy, konzistenci a pořadí.

Rozšířitelnost o další sadu kritérií a alternativ popsat ve struktuře dat; implementaci přepínače domén nepožadovat v základní verzi.

### 7. Připravit logiku AHP výpočtu a způsob nezávislé kontroly

**Stav: otevřené. V e-mailu je k vedoucímu otevřená otázka k formě kontroly.**

Ujasnit před programováním:

- postup párového porovnání a reciprocity,
- výpočet vah (zvolit **jeden** postup a držet ho v teorii, aplikaci i kontrole),
- lambda max, CI, CR a práci s RI,
- skládání lokálních vah do celkového pořadí,
- citlivost (tři změny matice kritérií).

**Pracovní doporučení pro nezávislý kontrolní výpočet (lehké, dokud vedoucí nerozhodne jinak):**

- připravit malý pevný kontrolní příklad (např. matice 3×3 nebo 4×4), ne celý Cykloservis ručně;
- spočítat ho mimo aplikaci stejným postupem (ručně nebo v Excelu);
- stejná data zadat do aplikace a porovnat váhy, CR a pořadí v rámci zaokrouhlení;
- cizí AHP web není nutný jako hlavní důkaz (může počítat jiným postupem); případně jen jako doplněk;
- plný Cykloservis slouží k ověření použití aplikace a citlivosti, ne k ručnímu přepočtu všech matic.

Kontrolní příklad v `AHP_NAVOD_SAATY.md` před převzetím nezávisle přepočítat; jeho zaokrouhlená čísla nejsou specifikací.

### 8. Rozhodnout podobu implementace a vytvořit minimální aplikaci

**Stav: otevřené. Nezačínat plnou implementaci dříve, než jsou hotové body 6–7.**

Minimální verze:

- PHP webové rozhraní,
- připravené seznamy s popisy a odkazy,
- vlastní položky,
- zadávání párů s automatickou reciprocalitou,
- kontrola vstupů,
- výpočet vah a konzistence,
- zobrazení pořadí a možnost přepočtu.

Až po ověřené výpočetní specifikaci.

## Pevné požadavky (z e-mailu vedoucího a návrhu odpovědi)

- Aplikace podporuje výběr / porovnání nástrojů pro **návrh a vývoj** databázových systémů metodou AHP.
- Připravená kritéria a alternativy + možnost vlastních položek.
- Popisy a odkazy u připravených položek.
- Párové matice, výpočty AHP, zobrazení výsledku.
- Fungování na **jednom** modelovém případu (Cykloservis) se **čtyřmi** nástroji a **K1–K8** ze seminární práce.
- **Tři** samostatné změny důležitosti kritérií pro citlivost.
- Nezávislý kontrolní výpočet správnosti výpočtů.
- Mimo rozsah hodnocení: správa serverů, zálohování, výkon.
- Hodnotitel demonstračního případu: autor (uvést jako omezení).
- Rozšiřitelnost stačí popsat, pokud základní práce stačí.
- Před vložením do STAGu poslat cíl, osnovu a 4–5 zdrojů; termín zadávacího listu 15. 10. 2026.
- BP: nejméně 30 použitých zdrojů, z toho alespoň 20 knih nebo odborných článků.
- Správnost výpočtů a srozumitelné chování při špatných vstupech jsou důležitější než rozsáhlé vedlejší funkce.

## Co později doplnit do bakalářské práce

- Upravit anotaci, abstract, úvod a strukturu podle schválené osnovy a skutečně dokončené práce.
- V metodice uvést AI nástroje (verze, účel, způsob, rozsah).
- Uvést přesné verze a edice testovaných nástrojů.
- Doplnit operacionalizaci kritérií a doložené párové úsudky; žádné smyšlené matice ani výsledky.
- Kapitoly podle osnovy 1–6; současný `BP 9.md` je závěr seminárky, ne závěr BP.
- Bibliografie v `BP 10.md` sladěná s `ZDROJE.md`.
- Přílohy: diagramy, DDL, protokoly, kontrolní výpočet, matice, aplikace.

## Co teď nedělat

- nezačínat programovat celou aplikaci před body 6–7,
- nerozšiřovat o účty, admin, REST, další MCDM metody, skupinové AHP ani dotazníky,
- nepřidávat další scénáře,
- nepovažovat pomocné známky 1–5 za Saatyho vstupy,
- nevymýšlet testovací hodnoty, pořadí, CR ani ceny,
- nehromadně přepisovat teorii v `BP 4.md`–`BP 8.md` jen kvůli stylu,
- neplést „odeslaný e-mail“ se „schváleným zadáním“.

## Bezprostřední další krok

1. **Odeslat** návrh v `EMAIL_VEDOUCIMU_KOMENTOVANY_UPRAVENY_2.md` (nebo jeho čistou odesílací verzi).
2. Po odpovědi vedoucího upravit cíl/osnovu ve STAGu a případně tento plán.
3. Mezitím připravit:
   - volbu jednoho výpočetního postupu AHP,
   - malý kontrolní příklad pro nezávislý přepočet (Excel/ručně),
   - datový návrh aplikace (bod 6),
   - minimální rozsah obrazovek (bod 8, zatím jen návrh).

## Hranice a pracovní upřesnění (platí do změny od vedoucího)

- Terminologie: **návrh a vývoj** databázových systémů; provozní správa, zálohy a výkon mimo hodnocení.
- Čtyři alternativy a K1–K8 ze seminárky zůstávají připraveným obsahem i ověřovacím případem.
- Jeden modelový případ Cykloservis; tři změny citlivosti jen v matici kritérií.
- Autor je jediný hodnotitel demonstračního případu.
- Přínos BP: funkční podpůrná AHP aplikace + doložené ověření; komparace je demonstrační doména, ne samostatná druhá práce.
- Kapitoly `BP 0.md`–`BP 10.md` se po schválení osnovy postupně sladí s body 1–6; `BP 11.md`–`BP 15.md` zatím neexistují — nesestavovat úplný `BP.md` jako finální dokument.

### Návaznost na seminární práci

| Soubor | Role teď |
|---|---|
| `BP 0.md`–`BP 3.md` | Po schválení upravit rámování k aplikaci a ověření |
| `BP 4.md`–`BP 8.md` | Zachovat teorii/nástroje/kritéria; měnit jen chyby a nutnou návaznost |
| `BP 9.md` | Závěr seminárky – ne vydávat za závěr BP |
| `BP 10.md`, `ZDROJE.md` | Bibliografie; sladit s použitými zdroji |
| `seminární práce/` | Read-only podklad |

Při pozdější změně existující kapitoly ponechat pod vodorovnou čarou blok „Pracovní poznámka – původní znění před úpravou, datum, důvod“.

### Další postup po schválení e-mailu

1. Vložit odsouhlasený cíl, osnovu a literaturu do STAGu.
2. Dokončit body 6–7 (data + AHP + kontrolní příklad).
3. Implementovat minimální PHP aplikaci (bod 8).
4. Nezávisle ověřit výpočty; pak spustit Cykloservis v aplikaci včetně tří změn.
5. Doplnit praktické kapitoly, omezení, rozšiřitelnost, AI v metodice, přílohy a finální sestavení.

Kvalitu doložit řetězcem cíl → požadavky → implementace → kontrolní výpočet → demonstrační případ → závěr, nikoli počtem screenshotů.
