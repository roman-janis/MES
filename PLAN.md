# Plán práce od začátku podle učitele

Aktualizace: 7. 9. 2026

## Výchozí stav

- Teoretický základ práce se vrací na finální seminární verzi podle `seminární práce/MES_Janiš_final.txt`.
- Praktická část se zatím neimplementuje.
- Cílem první fáze je ujasnit přesný rozsah budoucí praktické části a až potom řešit aplikaci.
- Soubor `hodnoceni_4_nastroju.xlsx` je založený jako pracovní sešit pro budoucí porovnání nástrojů. Vyplňovat se začne až po uzamčení seznamu alternativ a kritérií.

## Hlavní princip

Nejdřív musí být jasné:

- co přesně bude aplikace dělat,
- jaké budou alternativy,
- jaká budou kritéria,
- jak bude vypadat jeden konkrétní scénář,
- jak budou provedeny AHP výpočty,
- a teprve potom má smysl řešit implementaci v PHP.

## Pořadí kroků

### 1. Vymezit přesný účel aplikace

**Stav: hotovo.**

Účelem aplikace je podpořit výběr nástroje pro návrh a správu databázových systémů podle preferencí uživatele pomocí metody AHP. Uživatel si vybere porovnávané nástroje a hodnoticí kritéria z připravených seznamů, případně doplní vlastní. U alternativ a kritérií bude dostupný popis a odkazy na další informace.

Uživatel párově porovná důležitost kritérií a následně nástroje podle jednotlivých kritérií. Aplikace zkontroluje úplnost a platnost vstupů, vypočítá váhy a konzistenci porovnání a zobrazí výsledné pořadí nástrojů. Při problematických vstupech nebo nedostatečné konzistenci zobrazí srozumitelné upozornění.

Výsledek bude doporučením odpovídajícím zadaným preferencím, nikoli univerzálním určením nejlepšího nástroje. Funkčnost aplikace bude v práci předvedena na jednom konkrétním scénáři a dvou až třech změnách hodnocení pro ověření citlivosti výsledku. Rozsáhlá administrace a rozšíření na jiné oblasti rozhodování nejsou součástí základní verze.

Vstupy aplikace:

- výběr připravených alternativ a kritérií,
- případné vlastní alternativy a kritéria,
- párová porovnání důležitosti kritérií,
- párová porovnání alternativ podle jednotlivých kritérií.

Výstupy aplikace:

- vypočtené váhy kritérií a lokální váhy alternativ,
- hodnoty kontroly konzistence a upozornění na problematické vstupy,
- celkové priority a výsledné pořadí alternativ.

### 2. Uzamknout seznam alternativ

**Stav: hotovo.**

Konečný seznam alternativ:

- Oracle SQL Developer Data Modeler,
- DBeaver Community Edition,
- MySQL Workbench Community Edition,
- pgModeler.

Výběr pokrývá tři nástroje zaměřené především na významné databázové platformy Oracle Database, MySQL a PostgreSQL a jeden univerzálnější nástroj podporující více DBMS. Všechny alternativy jsou dostupné v bezplatné, komunitní nebo open-source podobě a umožňují prakticky ověřovat funkce související s návrhem databáze. Čtyři alternativy zároveň zachovávají zvládnutelný rozsah párového porovnávání metodou AHP. Podrobné zdůvodnění výběru je uvedeno v kapitole `BP 7.md`; přesné verze se v práci zaznamenají podle skutečně testovaných instalací.

### 3. Uzamknout seznam kritérií

Stanovit konečný pracovní seznam hodnoticích kritérií.

Výstup:

- seznam kritérií,
- stručný význam každého kritéria,
- poznámka, zda je kritérium spíše objektivní nebo subjektivní.

### 4. Připravit jeden hlavní scénář

Zvolit jeden konkrétní případ použití, na kterém se ukáže fungování práce.

Výstup:

- popis jednoho scénáře,
- proč je zvolen,
- jaké preference v něm budou důležité.

### 5. Připravit změny pro citlivost

Nevytvářet složitou analýzu předem, ale připravit 2 až 3 změny, které se později vyzkouší.

Výstup:

- seznam 2 až 3 změn vah nebo hodnocení,
- stručný předpoklad, co mohou udělat s výsledkem.

### 6. Připravit datový návrh aplikace

Navrhnout, jaká data bude potřeba ukládat.

Výstup:

- návrh tabulek nebo datových entit,
- vazby mezi alternativami, kritérii, scénářem, hodnocením a výsledkem.

### 7. Připravit logiku AHP výpočtu

Ujasnit výpočetní postup ještě před programováním.

Výstup:

- postup párového porovnání,
- výpočet vah,
- kontrola konzistence,
- výpočet výsledného pořadí,
- stručný popis citlivosti.

### 8. Rozhodnout podobu implementace

Až po předchozích bodech rozhodnout, jak jednoduchá bude aplikace v PHP.

Výstup:

- návrh minimální verze aplikace,
- rozhodnutí, co bude povinné a co už by bylo navíc.

## Pevné požadavky vedoucího

- Aplikace bude zaměřena na porovnání nástrojů pro návrh a správu databázových systémů.
- Nabídne připravená kritéria a alternativy a zároveň umožní přidat vlastní.
- Z těchto vstupů sestaví párové matice, provede AHP výpočty a zobrazí výsledek.
- U kritérií a alternativ uvede popis a odkazy na další informace.
- Fungování bude předvedeno na jednom konkrétním scénáři a na 2 až 3 změnách pro citlivost.
- Správnost výpočtů, kontroly vstupů a srozumitelná upozornění jsou důležitější než rozsáhlé vedlejší funkce.
- Rozšiřitelnost o další sadu kritérií a alternativ stačí popsat, pokud na její implementaci nezbude prostor.
- Před doplněním zadávacího listu do STAGu poslat vedoucímu ke kontrole upravený cíl, osnovu a 4 až 5 zdrojů. Termín podle e-mailu je 15. 10. 2026.
- Bakalářská práce má mít nejméně 30 skutečně použitých zdrojů, z toho alespoň 20 knih nebo odborných článků.

## Co později doplnit do bakalářské práce

- Upravit anotaci, abstract, úvodní údaje a popis struktury podle skutečně dokončené práce.
- V metodice uvést skutečně použité nástroje AI, jejich verzi, účel, způsob a rozsah použití.
- Uvést přesné verze a edice testovaných databázových nástrojů.
- Doplnit operacionalizaci kritérií, pravidla převodu pozorování na Saatyho škálu a aktuální údaje o cenách a licencích.
- Praktické kapitoly naplnit pouze skutečnými testy, AHP maticemi, výsledky a jejich interpretací; nevytvářet odhady ani ilustrativní výsledky.
- Nakonec zkontrolovat použité zdroje a připravit přílohy z reálně vzniklých diagramů, DDL skriptů, protokolů, matic a aplikace.

## Co teď nedělat

- nezačínat hned programovat celou aplikaci,
- nerozšiřovat práci o zbytečně velkou administraci,
- nepřidávat více scénářů, pokud pro to nebude důvod,
- nepřipravovat složité funkce navíc bez vazby na požadavky vedoucího.

## Bezprostřední další krok

Dokončit bod 3: uzamknout seznam kritérií K1 až K8, zpřesnit význam každého kritéria a určit, která kritéria jsou převážně objektivní a která vyžadují subjektivní posouzení uživatele.
