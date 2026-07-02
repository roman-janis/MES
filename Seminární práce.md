# Univerzita Hradec Králové

## Fakulta informatiky a managementu

### Katedra informatiky a kvantitativních metod

&nbsp;

&nbsp;

&nbsp;

# Komparace nástrojů pro návrh a vývoj databázových systémů pomocí AHP

## Teoretická východiska – práce

&nbsp;

Práce v předmětu KRCR-MES Metodologický seminář

&nbsp;

&nbsp;

| | |
|---|---|
| **Autor:** | Roman Janiš |
| **Osobní číslo:** | I2400792 |
| **Studijní program:** | B0613A140033 Aplikovaná informatika |
| **Specializace:** | Softwarové inženýrství |
| **Vedoucí bakalářské práce:** | Ing. et Ing. Martin Lněnička, Ph.D. |
| **Pracoviště vedoucího:** | Katedra informatiky a kvantitativních metod |

&nbsp;

&nbsp;

Hradec Králové, červen 2026


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Prohlášení

Prohlašuji, že jsem tuto práci vypracoval samostatně a uvedl jsem všechny použité prameny a literaturu.

&nbsp;

&nbsp;

V Hradci Králové dne ………………………… &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ……………………………………

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Roman Janiš


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Poděkování

Tímto bych rád poděkoval vedoucímu bakalářské práce Ing. et Ing. Martinu Lněničkovi, Ph.D., za odborné vedení, věcné připomínky a konzultace, které přispěly ke zpracování této práce.


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Abstrakt

Práce představuje teoretická východiska bakalářské práce zaměřené na komparaci nástrojů pro návrh a vývoj databázových systémů s využitím metody vícekriteriálního rozhodování Analytic Hierarchy Process. V první části jsou vymezeny základní pojmy z oblasti databázových systémů, popsány fáze návrhu databáze a vysvětleny datové modely používané při návrhu, zejména entitně-relační model a model relační. Druhá část je věnována vícekriteriálnímu rozhodování, vymezení pojmů alternativa, kritérium a váha kritéria a podrobnému výkladu metody AHP, včetně párového porovnávání, Saatyho škály a kontroly konzistence. Třetí část představuje nástroje, které budou předmětem navazující praktické komparace v bakalářské práci, navrhuje hodnoticí kritéria a popisuje metodický rámec dalšího postupu. Výstupem práce je teoretický a metodický základ, na který přímo naváže praktická část bakalářské práce.

**Klíčová slova:** databázový systém, návrh databází, datové modelování, vícekriteriální rozhodování, Analytic Hierarchy Process.

&nbsp;

# Abstract

**Title:** Comparison of Database Design and Development Tools Using AHP – Theoretical Background

This paper presents the theoretical background of a bachelor thesis focused on the comparison of tools for the design and development of database systems using the Analytic Hierarchy Process, a multi-criteria decision-making method. The first part defines fundamental terms related to database systems, describes the phases of database design and explains the data models used in design, in particular the entity–relationship model and the relational model. The second part addresses multi-criteria decision making, defines the terms alternative, criterion and criterion weight, and provides a detailed explanation of the AHP method, including pairwise comparison, Saaty's scale and consistency checking. The third part introduces the tools that will be the subject of the follow-up practical comparison in the bachelor thesis, proposes evaluation criteria and describes the methodological framework of further work. The result is a theoretical and methodological foundation on which the practical part of the bachelor thesis will directly build.

**Keywords:** database system, database design, data modelling, multi-criteria decision making, Analytic Hierarchy Process.


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
<w:p><w:pPr><w:pStyle w:val="Nadpisobsahu"/></w:pPr><w:r><w:t>Obsah</w:t></w:r></w:p>
<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/><w:instrText xml:space="preserve"> TOC \o "1-3" \h \z \u </w:instrText><w:fldChar w:fldCharType="separate"/><w:t>Pole obsahu – ve Wordu klikněte do pole pravým tlačítkem a zvolte „Aktualizovat pole", případně stiskněte F9.</w:t><w:fldChar w:fldCharType="end"/></w:r></w:p>
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# 1 Úvod

Návrh databáze předchází samotnou implementaci informačního systému. Kvalita takového datového návrhu značně ovlivňuje spolehlivost, výkon a možnosti dalšího rozšiřování systému. V případě, že při návrhu vzniknou chyby, jejich odstranění je v dalších etapách složité a nákladné. Při návrhu a vývoji databází se proto využívají různé softwarové nástroje, jako například nástroje pro datové modelování, tvorbu ER diagramů, generování SQL skriptů nebo správu databázových schémat. Jednotlivé nástroje se mezi sebou liší rozsahem nabízených funkcí, podporovanými databázemi, možnostmi modelování nebo licenčními podmínkami.

Vybrat vhodný nástroj není v praxi často jednoduché. Obvykle se nedá rozhodovat jen podle jednoho kritéria, například podle ceny nebo rozšířenosti nástroje. Většinou do výběru vstupují další kritéria, která se navzájem dostávají do konfliktu. Proto je vhodné použít postup, který umožní jednotlivá kritéria porovnat a následně podle nich posoudit, který z nástrojů je nejvhodnější. Díky tomu nedojde k výběru podle subjektivního názoru, ale ke skutečně podloženému vyhodnocení. Tato práce se proto zaměřuje na porovnání nástrojů pro návrh a vývoj databází. Pro toto porovnání je využita metoda vícekriteriálního rozhodování Analytic Hierarchy Process (AHP). Na ní je pak celý postup hodnocení založen.

Práce tak tvoří teoretický a metodický podklad pro navazující praktické porovnání těchto nástrojů. Na začátku se text věnuje definicím a termínům spojenými s databázovými systémy, datovým modelováním a návrhem databáze, poté vysvětluje princip vícekriteriálního rozhodování a metodu AHP. Na tento rámec navazuje výběr nástrojů a návrh hodnoticích kritérií. S těmi se bude dále pokračovat v praktické části. Výsledné porovnání pak pomůže lépe rozhodnout, který nástroj je vhodný pro různé typy použití, a zároveň ukázat, jak se výsledek mění podle změn priorit.

# 2 Cíl práce a výzkumné otázky

Cílem práce je připravit teoretická a metodická východiska pro porovnání vybraných nástrojů pro návrh a vývoj databázových systémů. K dosažení hlavního cíle bude potřeba splnit tyto dílčí cíle:

- vymezit základní pojmy z oblasti databázových systémů, datového modelování a návrhu databáze,
- vysvětlit principy vícekriteriálního rozhodování, metodu AHP a její použitelnost pro porovnání softwarových nástrojů,
- vybrat a charakterizovat nástroje, které budou předmětem porovnávání, a navrhnout hodnoticí kritéria.

Výzkumné otázky vycházejí z cíle práce a z potřeby postupně připravit teoretický a metodický rámec pro budoucí porovnání nástrojů: od vymezení databázových systémů a jejich vývoje, přes vysvětlení, jak nástroje hodnotit podle více kritérií, až po volbu kritérií a postupu porovnání. Metoda AHP přitom umožňuje rozdělit rozhodování na menší přehledné části a systematicky porovnat jak jednotlivá kritéria, tak hodnocené nástroje.

Tomuto zaměření odpovídají následující výzkumné otázky:
- **VO1:** Jaké klíčové pojmy, modely a postupy se využívají při návrhu a vývoji databázových systémů?
- **VO2:** Jaké principy a postupy nabízí metoda AHP pro porovnání alternativ podle více kritérií?
- **VO3:** Jaká hodnoticí kritéria a jaký postup zvolit pro praktické porovnání nástrojů a jak jejich volbu zdůvodnit?

Odpovědi na uvedené výzkumné otázky postupně tvoří obsah jednotlivých kapitol.

# 3 Metodika práce

Zpracování práce probíhalo v několika navazujících krocích. Nejprve byly vymezeny oblasti, které je nutné vysvětlit tak, aby bylo možné nástroje později porovnat a navrhnout vhodná hodnoticí kritéria. Jednalo se o oblast databázových systémů, datové modelování, návrhu databáze, vícekriteriální rozhodování a metody AHP. K těmto oblastem byly potom dohledány odborné zdroje.

Zdroje byly vybírány tak, aby pokryly jednak celou teoretickou část práce, ale zároveň také výběr konkrétních nástrojů. Pro databázové systémy byla jako hlavní zdroj použita publikace Pokorného a Valenty (2020). Pro datové modelování a návrh relačních databází byla využita publikace Chlapka, Kučery a Palovské (2019). Metoda AHP byla zpracována podle prací Saatyho (1990, 2008) a učebního textu Soukopové (2016).

Dalším krokem byl výběr nástrojů, které budou v práci porovnávány. Pro jejich výběr byla využita studie Carvalho et al. (2022), protože se zabývá podobným tématem a porovnávala nástroje pro datové modelování jinou metodou. Dále byly použity oficiální dokumentace vybraných nástrojů. Z nich byly převzaty informace o funkcích, podporovaných databázových platformách, licenčních podmínkách a další informace. Jako podpůrný zdroj byl použit také článek Simanavičienė a Vdovinskienė (2023), který ukazuje použití metody AHP při výběru softwaru.

Na základě prostudovaných zdrojů byly následně vybrány nástroje a navržena hodnoticí kritéria. V další části práce budou nástroje hodnoceny podle jednotného postupu. Bude sledována například tvorba modelu, převod do logického a fyzického návrhu, generování SQL skriptu, reverzní inženýrství, použitelnost a licenční podmínky. Výsledky budou následně zpracovány metodou AHP.

Samotné porovnání nástrojů proběhne metodou AHP. Volba této metody vychází z přehledových studií vícekriteriálního rozhodování (MCDM), které AHP označují za jeden z nejvhodnějších přístupů pro hodnocení softwarových systémů, a to zejména díky její schopnosti kombinovat kvantitativní i kvalitativní kritéria (Velasquez a Hester, 2013; Ishizaka a Labib, 2011). Metoda AHP rozloží rozhodovací problém do hierarchie složené z cíle, kritérií a hodnocených nástrojů. Kritéria i nástroje se vzájemně porovnávají po dvojicích na Saatyho škále a z výsledků se vypočítají váhy a celkové pořadí nástrojů. Součástí bude také analýza citlivosti sledující, jak se pořadí mění při změně vah kritérií. Pro usnadnění výpočtů může vzniknout jednoduchá podpůrná aplikace.

# 4 Databázové systémy

## 4.1 Základní pojmy

Základem je rozlišit pojmy data, informace, databáze a systém řízení báze dat.
Data lze chápat jako jednotlivá fakta nebo zaznamenané hodnoty, které samy o sobě nemusí nést širší význam.
Informace vznikají interpretací dat v určitém kontextu.
Databáze pak představuje organizovanou kolekci vzájemně souvisejících dat, která jsou ukládána tak, aby s nimi bylo možné efektivně pracovat (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Watt a Eng, 2014).

****
Při práci s databázemi je nutné rozlišovat některé základní pojmy, jako jsou data, informace, databáze a systém řízení báze dat.
Pod pojmem data si lze představit jednotlivá fakta nebo zaznamenané hodnoty (Elmasri a Navathe, 2016; Watt a Eng, 2014). Tyto hodnoty samy o sobě nemusí být nositeli žádného širšího významu. Informace pak vznikají právě přiřazením významu datům v určitém kontextu (Elmasri a Navathe, 2016; Watt a Eng, 2014).
Pojem databáze pak představuje organizovanou sbírku vzájemně souvisejících dat, která jsou uložena tak, aby s nimi bylo možné dále efektivně pracovat (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Watt a Eng, 2014).
****


> **Zdrojové úryvky k odstavci výše**
>
> **„Data lze chápat jako jednotlivá fakta nebo zaznamenané hodnoty, které samy o sobě nemusí nést širší význam."**
>
> - *Elmasri a Navathe (2016, s. 4)*: „Data are known facts that can be recorded and that have implicit meaning."
> - *Watt a Eng (2014)* — online, bez PDF. Z textu kap. 1: „Data: Raw, unorganized facts that need to be processed. Data can be something simple and seemingly random and useless until it is organized."
>
> **„Informace vznikají interpretací dat v určitém kontextu."**
>
> - *Elmasri a Navathe (2016, s. 4)*: „...information, or processed data..."
> - *Watt a Eng (2014)* — online. Z textu kap. 1: „Information: When data is processed, organized, structured or presented in a given context so as to make it useful, it is called information."
>
> **„Databáze pak představuje organizovanou kolekci vzájemně souvisejících dat..."**
>
> - *Pokorný a Valenta (2020, s. 16)*: „Základem databázového přístupu je oddělení definice dat a jejich údržby od uživatelských programů. Data již nejsou organizována v izolovaných souborech, ale v komplikovanější, centrálně zpracovávané struktuře dat zvané databáze (DB). Principiálně databáze zahrnuje: datové prvky a vztahy mezi nimi, integritní omezení, schéma."
> - *Elmasri a Navathe (2016, s. 4)*: „A database is a logically coherent collection of related data with some inherent meaning."
> - *Watt a Eng (2014)* — online. Z textu kap. 1: „A *database* is a set of related data and the way it is organized."

---

Systém řízení báze dat, běžně označovaný zkratkou DBMS, je specializovaný software, který zajišťuje definici, ukládání, manipulaci, zabezpečení a správu dat uložených v databázi.
Databázový systém v širším smyslu zahrnuje nejen samotnou databázi a DBMS, ale také uživatele, aplikační software, pravidla provozu a další prostředky potřebné pro práci s daty.
Tento výčet funkcí — definici databáze, manipulaci s daty, souběžný přístup, ochranu dat a zotavení z chyb — shodně uvádějí jako základní služby DBMS Elmasri a Navathe i Pokorný a Valenta (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
****
Systém řízení báze dat, běžně označovaný jako DBMS, je specializovaný software, který zajišťuje definici, ukládání, manipulaci, zabezpečení a správu dat uložených v databázi (Pokorný a Valenta, 2020).
Spojení databáze s DBMS vytvoří databázový systém (DBS) (Elmasri a Navathe, 2016). DBMS v rámci tohoto systému zajišťuje transakční zpracování, obnovení dat po pádu, souběžný přístup více uživatelů i řízení ochrany dat (Pokorný a Valenta, 2020).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„DBMS je specializovaný software, který zajišťuje definici, ukládání, manipulaci, zabezpečení a správu dat..."**
>
> - *Pokorný a Valenta (2020, s. 17)*: „Centrální správa databáze je organizována prostřednictvím speciálního programového vybavení, které se nazývá systém řízení bází dat, anglicky DataBase Management System (DBMS)."
> - *Pokorný a Valenta (2020, s. 17)*: „K databázové technologii patří techniky transakčního zpracování, řízení souběžného přístupu více uživatelů, řízení zotavení z chyb, řízení ochrany dat, jazykové prostředky, odolnost proti chybám, řízení katalogu dat a paměti. Všechny tyto služby poskytuje DBMS."
> - *Elmasri a Navathe (2016, s. 4)*: „A database management system (DBMS) is a computerized system that enables users to create and maintain a database. The DBMS is a general-purpose software system that facilitates the processes of defining, constructing, manipulating, and sharing databases among various users and applications."
>
> **„Databázový systém v širším smyslu zahrnuje nejen samotnou databázi a DBMS, ale také uživatele, aplikační software..."**
>
> - *Pokorný a Valenta (2020, s. 17)*: „Ten [DBMS] spolu s nějakou databází tvoří databázový systém (DBS). Tyto tři základní pojmy lze zjednodušeně vyjádřit rovnicí DB + DBMS = DBS."
> - *Elmasri a Navathe (2016, s. 5)*: „The database and DBMS software together is called a database system."
>
> **„Tento výčet funkcí — definici databáze, manipulaci s daty, souběžný přístup, ochranu dat a zotavení z chyb..."**
>
> - *Pokorný a Valenta (2020, s. 17)*: „K databázové technologii patří techniky transakčního zpracování, řízení souběžného přístupu více uživatelů, řízení zotavení z chyb, řízení ochrany dat, jazykové prostředky, odolnost proti chybám, řízení katalogu dat a paměti. Všechny tyto služby poskytuje DBMS."
> - *Elmasri a Navathe (2016, s. 4)*: „...defining, constructing, manipulating, and sharing databases... Protecting the database includes system protection against hardware or software malfunction (crash) and security protection against unauthorized or malicious access."

---

Tradiční souborový přístup k ukládání dat se potýkal s řadou problémů, mezi něž patřila zejména vysoká redundance dat, nekonzistence a závislost aplikačních programů na fyzické struktuře souborů. Databázový přístup tyto nedostatky odstraňuje tím, že integruje data do jednoho logického celku a odděluje definici dat od samotných aplikací. Díky tomu je zajištěna sdílenost dat mezi různými uživateli, vyšší bezpečnost a možnost centrálního řízení integritních omezení (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

****
Původně se používal především jednoduchý souborový přístup, který měl však řadu problémů a omezení, například v podobě nekonzistentnosti dat při aktualizaci, závislosti na aplikačním programu a na fyzické struktuře, často spojené s redundancí dat (Elmasri a Navathe, 2016). Databázový přístup tyto nedostatky odstraňuje, a to tím, že integruje data do jednoho logického celku a odděluje definici dat od samotných aplikací (Pokorný a Valenta, 2020). Oddělením byla získána vyšší bezpečnost, možnost centrálního řízení integritních omezení a sdílenost dat mezi více uživateli (Pokorný a Valenta, 2020).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Tradiční souborový přístup k ukládání dat se potýkal s řadou problémů, mezi něž patřila zejména vysoká redundance dat..."**
>
> - *Pokorný a Valenta (2020, s. 15)*: „V souborovém přístupu má každá aplikace své vlastní soubory. To vede k redundanci (nadbytečnosti) dat, což přináší potíže s jejich konzistencí při aktualizaci... Další nevýhodou je těsná vazba mezi daty a programem."
> - *Elmasri a Navathe (2016, s. 6)*: „In traditional file processing, each user group maintains its own files... This redundancy leads to several problems: duplication of effort, wasted storage space, and inconsistency of data."
>
> **„Databázový přístup tyto nedostatky odstraňuje tím, že integruje data do jednoho logického celku..."**
>
> - *Pokorný a Valenta (2020, s. 16)*: „Základem databázového přístupu je oddělení definice dat a jejich údržby od uživatelských programů. Data již nejsou organizována v izolovaných souborech, ale v komplikovanější, centrálně zpracovávané struktuře dat zvané databáze."
> - *Elmasri a Navathe (2016, s. 9)*: „In the database approach, a single repository of data is maintained that is defined once and then accessed by various users... Program-data independence: The structure of data files is stored in the DBMS catalog separately from the access programs."

---

## 4.2 Schéma databáze, instance a metadata

V teorii databází je třeba rozlišovat schéma databáze a instanci databáze. Schéma databáze představuje popis struktury uložených dat, tedy určení entit, atributů, vazeb a omezení, která mají data splňovat. Instance databáze naopak vyjadřuje konkrétní aktuální obsah databáze v určitém čase. Toto rozlišení odděluje relativně stabilní strukturální návrh od proměnlivých datových hodnot (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

****
V teorii databází je třeba rozlišovat mezi schématem databáze a instancí databáze.
Schéma databáze představuje popis struktury uložených dat, zahrnuje určení entit, atributů, vazeb a integritních omezení, která mají data splňovat (Pokorný a Valenta, 2020).
Pojem instance databáze naopak vyjadřuje konkrétní aktuální obsah databáze v určitém čase.
Toto rozlišení odděluje relativně stabilní strukturální návrh od proměnlivých datových hodnot (Elmasri a Navathe, 2016).
****


> **Zdrojové úryvky k odstavci výše**
>
> **„Schéma databáze představuje popis struktury uložených dat, tedy určení entit, atributů, vazeb a omezení..."**
>
> - *Pokorný a Valenta (2020, s. 16–17)*: „Schéma databáze není nic jiného, než popis dat na úrovni srozumitelné uživateli databáze a odpovídající používané vrstvě software. Běžně se pod schéma databáze zahrnují i IO [integritní omezení]."
> - *Pokorný a Valenta (2020, s. 16)*: „Principiálně databáze zahrnuje: datové prvky a vztahy mezi nimi, integritní omezení, schéma."
> - *Elmasri a Navathe (2016, s. 29)*: „The description of a database is called the database schema, which is specified during database design and is not expected to change frequently. [...] Each object in the schema — for example, STUDENT or COURSE — is called a schema construct."
>
> **„Instance databáze naopak vyjadřuje konkrétní aktuální obsah databáze v určitém čase."**
>
> - *Pokorný a Valenta (2020, s. 17)*: „Je možné hovořit o stavu databáze. Stav databáze se mění v čase v souladu s její aktualizací. Pokud data splňují definovaná IO, říkáme, že databáze je v konzistentním stavu."
> - *Elmasri a Navathe (2016, s. 30)*: „The actual data stored in a database at a particular moment in time is called a database state or snapshot."
>
> **„Toto rozlišení odděluje relativně stabilní strukturální návrh od proměnlivých datových hodnot."**
>
> - *Pokorný a Valenta (2020, s. 17)*: „Z toho, co bylo dosud řečeno, lze shrnout, že databáze je definovaná pomocí jistého schématu a existuje nezávisle na aplikačních programech. Schéma (databáze) umožňuje do jisté míry porozumět datům v databázi."
> - *Elmasri a Navathe (2016, s. 29–30)*: „When we define a new database, we specify its database schema only to the DBMS. [...] At any point in time, the database has a current database state that refers to the data currently stored in the database."

---

S databázovým systémem úzce souvisejí také metadata. Metadata jsou data o datech, tedy informace popisující strukturu databáze, význam atributů, integritní omezení nebo přístupová práva. Metadata bývají ukládána v systémovém katalogu, který slouží jako centrální zdroj informací o databázových objektech (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

****
S databázovým systémem souvisí také pojem metadata.
Metadata jsou data o datech. Tato data tedy popisují strukturu databáze, význam atributů, integritní omezení nebo například přístupová práva.
Metadata bývají ukládána v systémovém katalogu, který slouží jako centrální zdroj informací o databázových objektech (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Metadata jsou data o datech, tedy informace popisující strukturu databáze..."**
>
> - *Pokorný a Valenta (2020, s. 18–19)*: „Veškeré definice obsažené ve schématu (vzhledem k datům z databáze jde o metadata) jsou organizovány v modulu DBMS, který se nazývá systémový katalog. Přístup k systémovému katalogu je elegantně řešen v jazyku SQL, kde stejnými prostředky jako k uživatelským datům lze přistupovat i k systémovému katalogu."
> - *Elmasri a Navathe (2016, s. 6)*: „The information stored in the catalog is called meta-data, and it describes the structure of the primary database."
>
> **„Metadata bývají ukládána v systémovém katalogu, který slouží jako centrální zdroj informací o databázových objektech."**
>
> - *Pokorný a Valenta (2020, s. 18–19)*: „Veškeré definice obsažené ve schématu (vzhledem k datům z databáze jde o metadata) jsou organizovány v modulu DBMS, který se nazývá systémový katalog."
> - *Elmasri a Navathe (2016, s. 6)*: „This definition is stored in the DBMS catalog... The DBMS catalog stores the schema and is called metadata — it is data about data."

---

Správa a údržba schématu databáze je klíčovou rolí správce databáze (DBA), přičemž změny schématu v průběhu životního cyklu systému musí být pečlivě kontrolovány. Metadata uložená v systémovém katalogu jsou využívána nejen samotným DBMS pro optimalizaci dotazů a kontrolu přístupových práv, ale také externími návrhovými nástroji. Tyto nástroje dokážou metadata z katalogu načíst a vizualizovat je ve formě diagramů, což usnadňuje pochopení existující struktury databáze a její další rozvoj (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

****
Správa a údržba schématu databáze je klíčovou rolí správce databáze (DBA), přičemž změny schématu v průběhu životního cyklu systému musí být pečlivě kontrolovány. Metadata uložená v systémovém katalogu jsou využívána nejen samotným DBMS pro optimalizaci dotazů a kontrolu přístupových práv, ale také externími návrhovými nástroji. Tyto nástroje dokážou metadata z katalogu načíst a vizualizovat je ve formě diagramů. Tato vizualizace pak usnadňuje pochopení existující struktury databáze a její další rozvoj (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Správa a údržba schématu databáze je klíčovou rolí správce databáze (DBA)..."**
>
> - *Pokorný a Valenta (2020, s. 18)*: „Správce databáze (DBA — Database Administrator) je odpovědný za návrh schématu, definici integritních omezení, autorizaci přístupu a dohled nad výkonem systému."
> - *Elmasri a Navathe (2016, s. 17)*: „The database administrator (DBA) is responsible for authorizing access to the database, coordinating and monitoring its use, and acquiring software and hardware resources as needed."
>
> **„Metadata uložená v systémovém katalogu jsou využívána [...] také externími návrhovými nástroji. Tyto nástroje dokážou metadata z katalogu načíst..."**
>
> - *Pokorný a Valenta (2020, s. 18–19)*: „Veškeré definice obsažené ve schématu (vzhledem k datům z databáze jde o metadata) jsou organizovány v modulu DBMS, který se nazývá systémový katalog."
> - *Elmasri a Navathe (2016, s. 9)*: „The information stored in the catalog is called metadata, and it describes the structure of the primary database... The DBMS software uses the catalog to guide its operations, but users and database design tools can also access it to understand the schema."

---

## 4.3 Funkce DBMS a víceúrovňová architektura

DBMS obvykle poskytuje několik základních skupin funkcí: definici dat, manipulaci s daty, řízení souběžného přístupu více uživatelů, ochranu dat a obnovu po chybě. V souvislosti s těmito funkcemi se používají pojmy DDL pro jazyk definice dat, DML pro jazyk manipulace s daty a transakce pro logický celek operací, který má být proveden buď celý, nebo vůbec (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Watt a Eng, 2014).

****
DBMS obvykle poskytuje několik základních skupin funkcí: definici dat, manipulaci s daty, řízení souběžného přístupu více uživatelů, ochranu dat a obnovu po chybě (Pokorný a Valenta, 2020). Pro tyto funkce se používají pojmy jako DDL pro jazyk definice dat, DML pro jazyk manipulace s daty a transakce pro logický celek operací, který má být proveden buď celý, nebo vůbec (Elmasri a Navathe, 2016; Watt a Eng, 2014).

****

> **Zdrojové úryvky k odstavci výše**
>
> **„DBMS obvykle poskytuje několik základních skupin funkcí: definici dat, manipulaci s daty, řízení souběžného přístupu, ochranu dat a obnovu po chybě."**
>
> - *Pokorný a Valenta (2020, s. 17)*: „K databázové technologii patří techniky transakčního zpracování, řízení souběžného přístupu více uživatelů, řízení zotavení z chyb, řízení ochrany dat, jazykové prostředky, odolnost proti chybám, řízení katalogu dat a paměti. Všechny tyto služby poskytuje DBMS."
> - *Elmasri a Navathe (2016, s. 4)*: „...defining, constructing, manipulating, and sharing databases... Protecting the database includes system protection against hardware or software malfunction and security protection against unauthorized or malicious access."
>
> **„DDL pro jazyk definice dat, DML pro jazyk manipulace s daty."**
>
> - *Pokorný a Valenta (2020, s. 18)*: „Jazyk pro definici dat (JDD) slouží k vytvoření všech definic dat v databázi, které jsou potřebné v dané aplikační doméně. Popis dat jedné databáze se nazývá (logické) schéma databáze. — Jazyk pro manipulaci dat (JMD) se používá jednak k aktualizaci dat (tj. k přidávání, k odstraňování a ke změnám dat v databázi), jednak k výběru dat podle daných požadavků."
> - *Elmasri a Navathe (2016, s. 43–44)*: „Once the database design is completed, the next step is to specify it using a special language called the data definition language (DDL)... data manipulation language (DML) [...] is used for retrieval, insertion, deletion, and modification of the data."
>
> **„Transakce pro logický celek operací, který má být proveden buď celý, nebo vůbec."**
>
> - *Pokorný a Valenta (2020, s. 19)*: „Transakce představuje logickou jednotku práce s databází. Jde vlastně o program, který se buď provede celý nebo se neprovede vůbec. Snahou samozřejmě je, aby transakce převedla databázi z jednoho konzistentního stavu do druhého."
> - *Elmasri a Navathe (2016, s. 45)*: „A transaction is an executing program or process that includes one or more database accesses, such as reading or updating of database records."

---

Dalším důležitým konceptem je víceúrovňová architektura DBMS, spojovaná s modelem ANSI/SPARC. Tato architektura rozlišuje externí, konceptuální a interní úroveň pohledu na data. Externí úroveň odpovídá pohledům jednotlivých skupin uživatelů, konceptuální úroveň představuje globální logický model celé databáze a interní úroveň popisuje fyzické uložení dat. Hlavním smyslem tohoto členění je podpora datové nezávislosti, tedy oddělení aplikací a uživatelských pohledů od fyzické implementace databáze (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

****
Další významnou myšlenkou bylo chápat DBMS jako víceúrovňový systém podle modelu ANSI/SPARC. Tento přístup představuje databázi jako hierarchii abstrakcí, které oddělují externí, konceptuální a interní rovinu. Ve zprávě výboru ANSI/X3/SPARC z roku 1975 se toto členění upřesnuje takto:
externí úroveň odpovídá pohledům jednotlivých skupin uživatelů, konceptuální úroveň představuje globální logický model celé databáze a interní úroveň popisuje fyzické uložení dat.
Hlavním smyslem tohoto členění je podpora datové nezávislosti, tedy oddělení aplikací a uživatelských pohledů od fyzické implementace databáze (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
****
> **Zdrojové úryvky k odstavci výše**
>
> **„Víceúrovňová architektura DBMS, spojovaná s modelem ANSI/SPARC."**
>
> - *Pokorný a Valenta (2020, s. 27)*: „Na databázovou technologii se můžeme dívat z několika různých úhlů pohledů. Jeden z nich je budovat databáze jako implementaci hierarchie jistých abstrakcí. Takovýto přístup se objevuje již v r. 1975 ve zprávě výboru ANSI/X3/SPARC (Standards Planning and Requirements Committee of the American National Standards Institute on Computers and Information Processing), kde byla použita tříúrovňová hierarchie obsahující: externí schémata, konceptuální schéma a fyzické schéma."
> - *Elmasri a Navathe (2016, s. 33)*: „This architecture [...] is called the three-schema architecture (also ANSI/SPARC architecture). Its goal is to separate the user applications from the physical database."
>
> **„Externí úroveň odpovídá pohledům jednotlivých skupin uživatelů."**
>
> - *Pokorný a Valenta (2020, s. 27)*: „Původní idea architektury předpokládala, že externí schémata (E-schéma), která mohou být popsána v různých konceptuálních modelech, obsahují informace potřebné pro jednotlivé kategorie uživatelů (rolí) pro provoz jejich aplikací. Např. mzdová účtárna vidí typ entity HEREC jiným způsobem, než personální oddělení."
> - *Elmasri a Navathe (2016, s. 33)*: „The external level includes a number of external schemas or user views. Each external schema describes the part of the database that a particular user group is interested in and hides the rest of the database from that user group."
>
> **„Konceptuální úroveň představuje globální logický model celé databáze."**
>
> - *Pokorný a Valenta (2020, s. 27)*: „Konceptuální schéma představuje unifikovaný konceptuální pohled na objekty a jejich vztahy ze všech aplikací (v rámci budovaného IS) a slouží nejen k popisu toho, ‚o čem' IS je, ale také jako jeden ze zdrojových dokumentů pro implementaci IS v prostředí příslušného DBMS."
> - *Elmasri a Navathe (2016, s. 33)*: „The conceptual level has a conceptual schema, which describes the structure of the whole database for a community of users. The conceptual schema hides the details of physical storage structures and concentrates on describing entities, data types, relationships, user operations, and constraints."
>
> **„Interní úroveň popisuje fyzické uložení dat."**
>
> - *Pokorný a Valenta (2020, s. 27)*: „Výše zmiňovaná zpráva ANSI/X3/SPARC používala pojem interního schématu, který zahrnoval jak databázový (nebo též logický), tak i fyzický pohled na data."
> - *Elmasri a Navathe (2016, s. 33)*: „The internal level has an internal schema, which describes the physical storage structure of the database."
>
> **„Hlavním smyslem tohoto členění je podpora datové nezávislosti."**
>
> - *Pokorný a Valenta (2020, s. 18)*: „Nezávislost dat většinou znamená, že programy, které přistupují k datům, jsou nezávislé na tom, jak a kde jsou data uložená. Tento rys patří k největším přednostem databázových systémů."
> - *Pokorný a Valenta (2020, s. 28)*: „Náhled na data pomocí hierarchie schémat je zásadního významu, umožňuje totiž jasně vymezit pojmy a odpovídající problémy. Z hlediska aplikací například umožní realizovat nezávislost aplikací na fyzických datech. Aplikace totiž pracují s daty pouze na logické úrovni."
> - *Elmasri a Navathe (2016, s. 34)*: „The goal of the three-schema architecture is to separate the user applications from the physical database. [...] The capacity to change the schema at one level of a database system without having to change the schema at the next higher level is called data independence."

---

Pro navazující komparaci nástrojů je tato architektura důležitá proto, že návrhové nástroje nepokrývají všechny úrovně databázového systému stejným způsobem. Některé se zaměřují především na konceptuální nebo logický model, jiné podporují i fyzické prvky konkrétního DBMS, například datové typy, indexy nebo generování SQL skriptů. Při hodnocení nástrojů proto není vhodné sledovat pouze možnost vytváření diagramů, ale také podporu přechodu mezi jednotlivými úrovněmi návrhu a implementace (Elmasri a Navathe, 2016; Rosenthal a Reiner, 1994).

****
Pro budoucí porovnání nástrojů v této práci je toto rozdělení důležité proto, že návrhové nástroje nepokrývají všechny úrovně databázového systému stejným způsobem (Rosenthal a Reiner, 1994). Některé se zaměřují především na konceptuální nebo logický model, jiné podporují i fyzické prvky konkrétního DBMS, například datové typy, indexy nebo generování SQL skriptů (Carvalho et al., 2022). Při hodnocení nástrojů proto bude vhodné sledovat nejen možnosti vytváření diagramů, ale také podporu přechodu mezi jednotlivými úrovněmi návrhu a implementace (Rosenthal a Reiner, 1994).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Návrhové nástroje nepokrývají všechny úrovně databázového systému stejným způsobem."**
>
> - *Rosenthal a Reiner (1994, s. 172)*: „A data model is a set of constructs for expressing how data is structured, constrained, and manipulated. *Different data models are required for different types of designs*: conceptual schemas, logical schemas (suited to a particular data model or DBMS interface), and physical schemas that capture implementation detail. A database design system needs to represent and manipulate all of these."
> - *Rosenthal a Reiner (1994, s. 168)*: „Conceptual design is done in the Entity-Relationship (ER) model, and the system handles multiple logical-level data models (relational, network, and hierarchical)."
>
> **„Některé se zaměřují na konceptuální nebo logický model, jiné podporují i fyzické prvky."**
>
> - *Carvalho et al. (2022, s. 3358)*: „Another relevant characteristic is that some tools have a visual representation of the conceptual data model, but others only show the physical data model. However, some have both types of visualization. On the one hand, the conceptual data model only describes the data and its relations. On the other, the physical data model displays table structures, including column name, data type, and the constraints."
>
> **„Při hodnocení nástrojů [...] také podporu přechodu mezi jednotlivými úrovněmi návrhu a implementace."**
>
> - *Rosenthal a Reiner (1994, s. 168–170)*: V tabulce nástrojů (Fig. 1) jsou pro každý krok návrhu (Requirements → Conceptual Design → Logical Design → Physical Design) vypsány automatizované nástroje. Autoři tak explicitně rozlišují, které nástroje pokrývají která pásma návrhu.

---

## 4.4 Fáze návrhu databáze

Návrh databáze je jednou z klíčových etap vývoje databázového systému a sám probíhá v několika na sebe navazujících fázích. Přímý přechod k fyzické implementaci tabulek v konkrétním systému může vést k chybám v návrhu, zbytečné redundanci a problémům s budoucí rozšiřitelností. Proto se v literatuře běžně rozlišuje konceptuální, logický a fyzický návrh (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Rosenthal a Reiner, 1994).

****
Návrh databáze představuje jednu z klíčových etap vývoje databázového systému a probíhá v několika na sebe navazujících fázích. Přímý přechod k fyzické implementaci tabulek v konkrétním systému může vést k chybám v návrhu, nadbytečné redundanci a omezené rozšiřitelnosti. Z tohoto důvodu se v literatuře standardně rozlišuje konceptuální, logický a fyzický návrh (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Rosenthal a Reiner, 1994).

****
> **Zdrojové úryvky k odstavci výše**
>
> **„Návrh databáze probíhá v několika na sebe navazujících fázích."**
>
> - *Rosenthal a Reiner (1994, abstraktu)*: „We describe the tools and theory of a comprehensive system for database design, and show how they work together to support multiple conceptual and logical design processes."
> - *Elmasri a Navathe (2016, s. 61–63)*: V kapitole 3 (sekce 3.2 „A Brief Review of the Database Design Process“) autoři popisují fáze návrhu databáze: requirements collection and analysis, conceptual database design, logical database design (data model mapping) a physical database design.
>
> **„Přímý přechod k fyzické implementaci může vést k chybám v návrhu."**
>
> - *Carvalho et al. (2022, s. 3351)*: „The result of a proper and rigorous CM design is a functionally richer, less error-prone, adequately attuned, able to adapt to varying user requirements, and less expensive system. Thus, designing the CM at the beginning of the development cycle should be mandatory."
>
> **„Proto se v literatuře běžně rozlišuje konceptuální, logický a fyzický návrh."**
>
> - *Rosenthal a Reiner (1994, s. 172)*: „Different data models are required for different types of designs: conceptual schemas, logical schemas (suited to a particular data model or DBMS interface), and physical schemas that capture implementation detail."
> - *Elmasri a Navathe (2016, s. 61)*: „The database design process [...] consists of two parallel activities: the design of the data content (data structure and constraints) and the design of the database applications... The database design process is typically divided into phases: requirements collection, conceptual design, logical design, and physical design."

---

Konceptuální návrh zachycuje strukturu aplikační domény bez vazby na konkrétní databázový systém. V této fázi jsou identifikovány entity, vztahy mezi nimi, atributy a základní omezení. Cílem je vytvořit model reality, který bude dostatečně přesný a současně technologicky nezávislý (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
****
Konceptuální návrh zachycuje strukturu aplikační domény bez vazby na konkrétní databázový systém (Carvalho et al., 2022; Rosenthal a Reiner, 1994).
V této fázi jsou identifikovány entity, vztahy mezi nimi, atributy a základní integritní omezení. Výsledkem je konceptuální schéma, které věrně popisuje realitu a je nezávislé na zvoleném DBMS (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
****
> **Zdrojové úryvky k odstavci výše**
>
> **„Konceptuální návrh zachycuje strukturu aplikační domény bez vazby na konkrétní databázový systém."**
>
> - *Rosenthal a Reiner (1994, s. 168)*: „Conceptual design is done in the Entity-Relationship (ER) model."
> - *Carvalho et al. (2022, s. 3351)*: „CM [Conceptual Model] describes the physical or social aspects of the world abstractly. [...] It will be easier to follow and adapt to user requirements and explore existing relationships between the concepts."
>
> **„V této fázi jsou identifikovány entity, vztahy, atributy a základní omezení."**
>
> - *Pokorný a Valenta (2020, s. 29)*: „Modelování entit a vztahů mezi entitami představuje velmi přirozený, ale také zjednodušený pohled na svět. Entita a vztah se objevují i v názvu asi nejčastěji používaného konceptuálního modelu — E-R modelu."
> - *Rosenthal a Reiner (1994, s. 170)*: „Entity-Relationship Schema Synthesizer: creates conceptual design from FDs via normalization and entity creation, key creation, relationship synthesis, and constraint inference."
>
> **„Cílem je vytvořit model reality, který bude dostatečně přesný a současně technologicky nezávislý."**
>
> - *Carvalho et al. (2022, s. 3351)*: „The result of a proper and rigorous CM design is a functionally richer, less error-prone, adequately attuned, able to adapt to varying user requirements, and less expensive system."

---

Na konceptuální návrh navazuje logický návrh. V této fázi se konceptuální model převádí do zvoleného datového modelu, v případě této práce zejména do modelu relačního. Dochází k návrhu relací, atributů, klíčů, cizích klíčů a integritních omezení. Výsledkem je logické schéma databáze, které lze implementovat v konkrétním DBMS (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
****
Na konceptuální návrh navazuje logický návrh.
V této části se konceptuální model převádí do zvoleného datového modelu, v případě této práce jde zejména o model relační (Rosenthal a Reiner, 1994).
Dochází k návrhu relací, atributů, klíčů, cizích klíčů a integritních omezení (Pokorný a Valenta, 2020).
Výsledkem je pak logické schéma databáze, které lze implementovat v konkrétním DBMS (Pokorný a Valenta, 2020).
****
> **Zdrojové úryvky k odstavci výše**
>
> **„V logickém návrhu se konceptuální model převádí do zvoleného datového modelu."**
>
> - *Rosenthal a Reiner (1994, s. 168)*: „The system handles multiple logical-level data models (relational, network, and hierarchical)."
> - *Rosenthal a Reiner (1994, s. 170)*: „Logical Design: ER→Relational Schema Translator; ER→Network Schema Translator."
> - *Rosenthal a Reiner (1994, s. 172)*: „logical schemas (suited to a particular data model or DBMS interface)"
>
> **„Výsledkem je logické schéma databáze, které lze implementovat v konkrétním DBMS."**
>
> - *Pokorný a Valenta (2020, s. 28)*: „Součástí návrhu schématu databáze je jeho realizace ve zvoleném DBMS. To znamená převod konceptuálního schématu do databázového schématu konkrétního DBMS."

---

Fyzický návrh se soustředí na způsob uložení dat v konkrétním databázovém systému. Řeší se zde organizace datových souborů, indexy, výkonové aspekty, optimalizace přístupu a další technické detaily. Na rozdíl od konceptuálního a logického návrhu je fyzický návrh silně závislý na konkrétní technologii (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
****
Ve fyzickém návrhu se řeší způsob uložení dat v konkrétním databázovém systému.
Řeší se zde organizace datových souborů, indexy, výkonové aspekty, optimalizace přístupu a další technické detaily (Rosenthal a Reiner, 1994).
Na rozdíl od konceptuálního a logického návrhu je fyzický návrh silně závislý na konkrétní technologii (Pokorný a Valenta, 2020).
****
> **Zdrojové úryvky k odstavci výše**
>
> **„Fyzický návrh se soustředí na způsob uložení dat; řeší indexy, výkonové aspekty, optimalizaci přístupu."**
>
> - *Rosenthal a Reiner (1994, s. 172)*: „physical schemas that capture implementation detail"
> - *Rosenthal a Reiner (1994, s. 170)*: „Physical Design: Physical Record Access tool (index selection); Schema Generator."
> - *Pokorný a Valenta (2020, s. 18–19)*: „Jsou-li v logickém schématu popsány záznamy a jejich vazby především z uživatelského hlediska, ve fyzickém schématu se řeší problém uložení dat na vnější paměti, metody přístupu k nim, způsoby indexace apod."

---

Mezi jednotlivými fázemi návrhu existuje zpětná vazba. Pokud se při fyzickém návrhu ukáže, že některé části modelu vedou k výkonovým problémům, je nutné vrátit se zpět k návrhu logickému. Podobně změna požadavků uživatelů může vyvolat úpravu konceptuálního modelu a následně i všech dalších úrovní. Návrh databáze proto nelze chápat jako striktně lineární proces, nýbrž jako proces iterativní (Rosenthal a Reiner, 1994).
****
Mezi jednotlivými kroky návrhu existuje zpětná vazba. Pokud se při fyzickém návrhu ukáže, že některé části modelu vedou například k výkonovým problémům, je nutné vrátit se zpět k návrhu logickému.
Podobně může změna požadavků uživatelů vyvolat úpravu konceptuálního modelu a následně i všech dalších úrovní.
Návrh databáze proto nelze chápat jako striktně lineární proces, nýbrž jako proces iterativní (Rosenthal a Reiner, 1994).

****
> **Zdrojové úryvky k odstavci výše**
>
> **„Mezi fázemi návrhu existuje zpětná vazba; návrh je iterativní."**
>
> - *Rosenthal a Reiner (1994, s. 169)*: „As a design progresses, details are accumulated, errors are fixed, and the schema gradually reorganized. Ideally, each change makes the schema a more accurate model of the external world. Once accuracy has been attained, however, conceptual and logical schema changes are generally still necessary for several reasons: *convenience* (so that schema objects will match organizational units or existing definitions), *implementability* (to use only the structures permitted in a target DBMS), and *performance* (since most DBMS's logical schemas partially determine physical implementation)."
> - *Carvalho et al. (2022, s. 3351)*: „The process of data modeling is not simple, meaning it usually demands multiple iterations."

---

Rozdělení návrhu do konceptuální, logické a fyzické úrovně tvoří v této práci základ pro formulaci pozdějších hodnoticích kritérií. Nástroj určený pro návrh databázového systému by měl umožnit srozumitelně zachytit požadavky, převést je do konzistentního schématu a podle potřeby podpořit i samotnou technickou implementaci v konkrétním databázovém prostředí. Rozsah podpory jednotlivých fází návrhu tvoří jeden z praktických rozdílů mezi porovnávanými nástroji (Carvalho et al., 2022; Rosenthal a Reiner, 1994).
****
Rozdělení návrhu databáze na konceptuální, logickou a fyzickou úroveň tvoří vhodný výchozí bod pro pozdější definici hodnoticích kritérií. Nástroj určený pro návrh databázového systému by měl umožnit zachytit požadavky, převést je do konzistentního schématu a podle potřeby podpořit technickou implementaci v konkrétním databázovém prostředí (Rosenthal a Reiner, 1994). Právě míra podpory těchto kroků představuje jeden z praktických rozdílů mezi porovnávanými nástroji (Carvalho et al., 2022; Rosenthal a Reiner, 1994).
****
> **Zdrojové úryvky k odstavci výše**
>
> **„Nástroj by měl umožnit zachytit požadavky, převést je do schématu a podpořit technickou implementaci."**
>
> - *Rosenthal a Reiner (1994, abstraktu)*: „We describe the tools and theory of a comprehensive system for database design, and show how they work together to support multiple conceptual and logical design processes."
> - *Rosenthal a Reiner (1994, s. 168)*: „The DDEW tool suite supports multiple design methodologies, including synthetic and analytic techniques for design from scratch, reverse engineering of existing schemas, and pairwise integration of schemas."
>
> **„Míra podpory těchto fází představuje jeden z praktických rozdílů mezi porovnávanými nástroji."**
>
> - *Carvalho et al. (2022, s. 3358)*: „Another relevant characteristic is that some tools have a visual representation of the conceptual data model, but others only show the physical data model. However, some have both types of visualization."
> - *Carvalho et al. (2022, s. 3351–3352)*: „We provide a brief description of the key features, such as the release year; real-time collaboration options; generation of the physical model; the presence of Reverse Engineering (auto-generation of ER from SQL) and Forward Engineering; supported DBMS and data types; different constraints; the incorporation of CM; finally, the pros and cons are analyzed."

Normální formy# 5 Datové modely

Datový model představuje formalizovaný prostředek pro popis dat, jejich struktury a vztahů mezi nimi. Datové modely umožňují zachytit realitu tak, aby s ní bylo možné systematicky pracovat při návrhu databází i při jejich následné implementaci (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
****
Datový model poskytuje formalizovaný nástroj, který slouží k popisu dat, jejich struktur a vztahů mezi nimi. Definuje datové objekty a jejich vzájemné vztahy včetně omezení, která se jich týkají (Pokorný a Valenta, 2020). Datový model je zjednodušený popis reality, který je vytvořen tak, aby se podle něj dala navrhnout a implementovat databáze (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Datový model představuje formalizovaný prostředek pro popis dat, jejich struktury a vztahů mezi nimi.”**
>
> - *Elmasri a Navathe (2016, s. 29)*: „A *data model*—a collection of concepts that can be used to describe the structure of a database—provides the necessary means to achieve this abstraction. By *structure of a database* we mean the data types, relationships, and constraints that apply to the data.”
> - *Pokorný a Valenta (2020, s. 22)*: „Datový model je prostředek k definici struktury databáze, tedy k definování, které datové objekty jsou v databázi a jaké jsou mezi nimi vztahy a omezení.”

---

## 5.1 Konceptuální modelování a ER/EER model

### 5.1.1 Konceptuální modelování a základní pojmy ER modelu

Konceptuální modelování slouží k zachycení požadavků aplikační domény bez ohledu na konkrétní databázovou technologii. Jeho cílem je vytvořit srozumitelný a logicky konzistentní model reality. V praxi se pro tuto fázi velmi často používá entitně-relační model (ER model), případně jeho rozšířená varianta EER (Chen, 1976; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
****
Konceptuální modelování slouží pro zachycení požadavků aplikační domény, kterou má aplikace pokrývat, ale bez ohledu na konkrétní databázovou technologii. Jeho cílem je vytvořit přehledný a věrný model reálného světa (Carvalho et al., 2022). V praxi se pro tuto fázi velmi často používá entitně-relační model (ER model), případně jeho rozšířená varianta EER (Chen, 1976; Elmasri a Navathe, 2016).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Konceptuální modelování slouží k zachycení požadavků aplikační domény bez ohledu na konkrétní databázovou technologii.”**
>
> - *Carvalho et al. (2022, s. 3351)*: „CM [Conceptual Model] describes the physical or social aspects of the world abstractly. [...] It will be easier to follow and adapt to user requirements and explore existing relationships between the concepts.”
> - *Elmasri a Navathe (2016, s. 30)*: „*High-level* or *conceptual data models* provide concepts that are close to the way many users perceive data...”
>
> **„V praxi se pro tuto fázi velmi často používá entitně-relační model (ER model), případně jeho rozšířená varianta EER.”**
>
> - *Chen (1976, s. 9)*: „The entity-relationship model can be used as a basis for unification of different views of data: the network model, the relational model, and the entity set model.”
> - *Elmasri a Navathe (2016, s. 59)*: „The *Entity-Relationship (ER) model* is a popular high-level conceptual data model. This model and its variations are frequently used for the conceptual design of database applications...”

---
Základními pojmy ER modelu jsou entita, entitní množina, vztah a atribut. Entita je objekt reálného světa, který je schopen samostatné existence a lze jej jednoznačně odlišit od ostatních objektů. Entitní množina je množina entit stejného typu, které mají společné vlastnosti. Vztah vyjadřuje vazbu mezi entitami nebo entitními množinami a atribut představuje vlastnost entity nebo vztahu (Chen, 1976).
****
Základními pojmy ER modelu jsou entita, entitní množina, vztah a atribut. Za entitu je považován objekt, který je schopen samostatné existence a lze jej jednoznačně odlišit od ostatních objektů (Chen, 1976). Entitní množina je pak množina entit, které jsou stejného typu a mají společné vlastnosti (Chen, 1976). Vztah vyjadřuje vazbu mezi entitami nebo entitními množinami a atribut představuje vlastnost entity nebo vztahu (Chen, 1976).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Entita je objekt reálného světa, který je schopen samostatné existence a lze jej jednoznačně odlišit od ostatních objektů.”**
>
> - *Chen (1976, s. 9)*: „An *entity* is a 'thing' which can be distinctly identified.”
>
> **„Entitní množina je množina entit stejného typu, které mají společné vlastnosti.”**
>
> - *Chen (1976, s. 9)*: „An *entity set* is a set of entities of the same type that share the same properties, or attributes.”
>
> **„Vztah vyjadřuje vazbu mezi entitami nebo entitními množinami.”**
>
> - *Chen (1976, s. 9–10)*: „A *relationship* is an association among several entities.”
>
> **„Atribut představuje vlastnost entity nebo vztahu.”**
>
> - *Chen (1976, s. 10)*: „The information about an entity is obtained by observation or measurement, and is expressed by a set of *attribute-value* pairs.”

---
Vztahy mezi entitami se popisují mimo jiné pomocí kardinality a participace. Kardinalita určuje, kolik entit jedné množiny může být ve vztahu k entitě jiné množiny. Typickými případy jsou vazby 1:1, 1:N a M:N. Participace vyjadřuje, zda je účast entity ve vztahu povinná nebo nepovinná. Tyto pojmy jsou důležité nejen na konceptuální úrovni, ale i pro následnou transformaci do relačního modelu (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
****
Vztahy mezi entitami lze popsat například kardinalitou a participací. Kardinalita udává, kolik entit jedné množiny může být ve vztahu k entitě jiné množiny (Elmasri a Navathe, 2016). Typickými případy jsou vazby 1:1, 1:N a M:N. Participace vyjadřuje, zda je účast entity ve vztahu povinná nebo nepovinná. Tyto pojmy jsou důležité nejen na konceptuální úrovni, ale i pro následnou transformaci do relačního modelu (Pokorný a Valenta, 2020).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Kardinalita určuje, kolik entit jedné množiny může být ve vztahu k entitě jiné množiny.”**
>
> - *Elmasri a Navathe (2016, s. 73)*: „The *cardinality ratio* for a binary relationship specifies the maximum number of relationship instances that an entity can participate in.”
> - *Pokorný a Valenta (2020, s. 33)*: „Mohutnost (cardinality) binárního vztahu nám říká, kolik entit jednoho typu může být asociováno s jednou entitou druhého (druhé) entitní množiny.”
>
> **„Participace vyjadřuje, zda je účast entity ve vztahu povinná nebo nepovinná.”**
>
> - *Elmasri a Navathe (2016, s. 74)*: „The *participation constraint* specifies whether the existence of an entity depends on its being related to another entity via the relationship type. This constraint specifies the minimum number of relationship instances that each entity can participate in, and is sometimes called the *minimum cardinality constraint*... There are two types of participation constraints—*total* and *partial*.”

---

### 5.1.2 Atributy, EER model a notace

Atributy jsou svázány s doménami, tedy s množinami přípustných hodnot. Rozlišují se jednoduché a složené atributy, případně další typy atributů. Pro jednoznačnou identifikaci entit slouží kandidátní a primární klíče. Rozšířený ER model (EER) doplňuje základní ER model o supertřídy, podtřídy a dědičnost atributů. EER model je vhodný tam, kde je třeba přesněji vystihnout specializaci nebo generalizaci objektů (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). V praxi se ER/EER model vyjadřuje různými grafickými notacemi; mezi nejčastější patří Chenova notace, Crow's Foot a UML (Elmasri a Navathe, 2016; Carvalho et al., 2022).
****
Atributy jsou svázány s doménami, tedy s množinami přípustných hodnot (Elmasri a Navathe, 2016). Rozlišujeme jednoduché a složené atributy, případně i další typy (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Pro jednoznačnou identifikaci entit slouží kandidátní a primární klíče (Elmasri a Navathe, 2016).

Rozšířený ER model (EER) doplňuje základní ER model o supertřídy, podtřídy a dědičnost atributů (Pokorný a Valenta, 2020). EER model je vhodný především tam, kde je potřeba přesněji vystihnout specializaci nebo generalizaci objektů (Elmasri a Navathe, 2016). V praxi se ER/EER model vyjadřuje různými grafickými notacemi, přičemž mezi nejčastější patří Chenova notace, Crow's Foot a UML (Elmasri a Navathe, 2016; Carvalho et al., 2022).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Atributy jsou svázány s doménami, tedy s množinami přípustných hodnot.”**
>
> - *Elmasri a Navathe (2016, s. 65)*: „Each simple attribute of an entity type is associated with a *value set* (or *domain*) of values. The value set specifies the set of values that may be assigned to that attribute for each individual entity.”
>
> **„Rozlišují se jednoduché a složené atributy, případně další typy atributů.”**
>
> - *Elmasri a Navathe (2016, s. 66)*: „*Composite* attributes can be divided into smaller subparts, which represent more basic attributes with independent meanings. [...] *Simple* (or *atomic*) attributes are not divisible into smaller components.”
> - *Pokorný a Valenta (2020, s. 31)*: „Atribut může být jednoduchý nebo složený.”
>
> **„Rozšířený ER model (EER) doplňuje základní ER model o supertřídy, podtřídy a dědičnost atributů.”**
>
> - *Elmasri a Navathe (2016, s. 107)*: „The *enhanced* (or *extended*) *entity-relationship* (*EER*) *model* includes all of the original ER model concepts, plus the concepts of subclass/superclass, specialization/generalization, and union types (categories).”

---

Pro hodnocení databázových návrhových nástrojů je podpora konceptuálního modelování významná z praktického hlediska. Nástroj by měl umožnit vyjádřit entity, vztahy, kardinality a omezení způsobem, který je srozumitelný analytikům i vývojářům. Jednotlivé nástroje se přitom mohou lišit použitou notací, úrovní podpory EER prvků a možností následného převodu modelu do relačního schématu (Carvalho et al., 2022; Rosenthal a Reiner, 1994).
****
Pro hodnocení databázových nástrojů je podpora konceptuálního modelování významná hlavně z praktického hlediska. Nástroj by měl umožnit vyjádřit entity, vztahy, kardinality a omezení způsobem, který je srozumitelný jak analytikům, tak i vývojářům (Rosenthal a Reiner, 1994).
Jednotlivé nástroje se přitom mohou lišit použitou notací, úrovní podpory EER prvků a možností následného převodu modelu do relačního schématu (Carvalho et al., 2022; Rosenthal a Reiner, 1994).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Nástroj by měl umožnit vyjádřit entity, vztahy, kardinality a omezení způsobem, který je srozumitelný analytikům i vývojářům.”**
>
> - *Rosenthal a Reiner (1994, s. 168)*: „Conceptual design is done in the Entity-Relationship (ER) model.”
>
> **„Jednotlivé nástroje se přitom mohou lišit použitou notací, úrovní podpory EER prvků a možností následného převodu modelu do relačního schématu.”**
>
> - *Carvalho et al. (2022, s. 3358)*: „Another relevant characteristic is that some tools have a visual representation of the conceptual data model, but others only show the physical data model. However, some have both types of visualization.”
> - *Carvalho et al. (2022, s. 3351–3352)*: „We provide a brief description of the key features, such as [...] the presence of Reverse Engineering (auto-generation of ER from SQL) and Forward Engineering [...] finally, the pros and cons are analyzed.”

---

## 5.2 Relační model

Relační model je založen na relacích, které jsou v praxi reprezentovány tabulkami. Každá relace má své schéma, tedy jméno relace, seznam atributů a jejich domén. Konkrétní řádky tabulky odpovídají n-ticím. Relační model pracuje s atomickými hodnotami a s přesně vymezenými atributy (Codd, 1970; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
****
Relační model je založen na relacích, které jsou v praxi neformálně reprezentovány tabulkami.
Každá relace má své schéma, tedy jméno relace, seznam atributů a jejich domén (Pokorný a Valenta, 2020).
Konkrétní řádky tabulky odpovídají n-ticím.
Relační model pracuje s atomickými hodnotami a s přesně vymezenými atributy (Codd, 1970; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

****

> **Zdrojové úryvky k odstavci výše**
>
> **„Relační model je založen na relacích, které jsou v praxi reprezentovány tabulkami."**
>
> - *Codd (1970, s. 377)*: „The term *relation* is used here in its accepted mathematical sense. Given sets S1, S2, ..., Sn (not necessarily distinct), R is a relation on these n sets if it is a set of n-tuples each of which has its first element from S1, its second element from S2, and so on."
> - *Elmasri a Navathe (2016, s. 141)*: „The *relational model* represents the database as a collection of *relations*. Informally, each relation resembles a *table* of values.“
>
> **„Každá relace má své schéma, tedy jméno relace, seznam atributů a jejich domén."**
>
> - *Elmasri a Navathe (2016, s. 142)*: „A *relation schema* $R$, denoted by $R(A_1, A_2, \dots, A_n)$, is made up of a relation name $R$ and a list of attributes, $A_1, A_2, \dots, A_n$. Each attribute $A_i$ is the name of a role played by some domain $D$ in the relation schema $R$.“
> - *Pokorný a Valenta (2020, s. 48)*: „Schéma relace obsahuje jméno relace a seznam jmen atributů spolu s jejich doménami."
>
> **„Relační model pracuje s atomickými hodnotami."**
>
> - *Codd (1970, s. 381)*: „Each column in a relation contains values from a single domain. [...] the values in the columns are atomic (nondecomposable)."

---

Klíče jsou v relačním modelu zásadní. Primární klíč slouží k jednoznačné identifikaci řádku tabulky (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Cizí klíč umožňuje vyjádřit vazbu mezi tabulkami a je základem referenční integrity. Mezi obecné vlastnosti relačních tabulek patří nezávislost na pořadí řádků a sloupců a požadavek na neduplicitu řádků (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Watt a Eng, 2014).
****
Klíče jsou v relačním modelu zásadní.
Primární klíč slouží k jednoznačné identifikaci řádku tabulky (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
Cizí klíč umožňuje vyjádřit vazbu mezi tabulkami a je základem referenční integrity (Watt a Eng, 2014).
Mezi obecné vlastnosti relačních tabulek patří nezávislost na pořadí řádků a sloupců a požadavek na neduplicitu řádků (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

****

> **Zdrojové úryvky k odstavci výše**
>
> **„Primární klíč slouží k jednoznačné identifikaci řádku tabulky."**
>
> - *Elmasri a Navathe (2016, s. 146)*: „Usually, one of the candidate keys is designated to be the *primary key* of the relation. This is the candidate key whose values are used to identify tuples in the relation.“
> - *Pokorný a Valenta (2020, s. 49)*: „Primárním klíčem relace R rozumíme takový kandidátní klíč relace R, který byl vybrán jako identifikátor n-tic."
>
> **„Cizí klíč umožňuje vyjádřit vazbu mezi tabulkami a je základem referenční integrity."**
>
> - *Elmasri a Navathe (2016, s. 149)*: „A set of attributes *FK* in relation schema *R1* is a *foreign key* of *R1* that references relation *R2* if [...] the values of *FK* in each tuple *t1* in the current state *r1(R1)* either occur as values of *PK* for some tuple *t2* in the current state *r2(R2)* or are *NULL*.“
> - *Watt a Eng (2014)* — online, kap. 8: „A *foreign key* is an attribute that references the primary key of another table. It creates a link between two tables and enforces *referential integrity*."
>
> **„Mezi obecné vlastnosti relačních tabulek patří nezávislost na pořadí řádků a sloupců a požadavek na neduplicitu řádků."**
>
> - *Elmasri a Navathe (2016, s. 143)*: „The tuples in a relation [...] are not considered to be ordered. [...] All values in a column are of the same data type. [...] Each tuple should be distinct; there should be no duplicate tuples.“
> - *Codd (1970, s. 377)*: „A relation of degree 1 is commonly called a unary relation [...]. Relations of arbitrary degree are permitted [...]. Unlike a mathematical relation, a relation stored in a computer is often considered to be ordered; that is, there is a first tuple, a second tuple, and so on."

---

Relační model je pro tuto práci důležitý také proto, že většina běžně používaných návrhových nástrojů pro databáze směřuje k tvorbě relačního schématu a k práci s SQL databázemi. Při jejich porovnání proto bude podstatné, zda nástroj podporuje definici primárních a cizích klíčů, integritních omezení, datových typů a generování nebo zpětné načítání databázového schématu (Carvalho et al., 2022).
****
Relační model je pro tuto práci důležitý také proto, že většina běžně používaných návrhových nástrojů pro databáze směřuje k tvorbě relačního schématu a k práci s SQL databázemi. Při jejich porovnání proto bude důležité, zda nástroj podporuje definici primárních a cizích klíčů, integritních omezení, datových typů a generování nebo zpětné načítání databázového schématu (Carvalho et al., 2022).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Při jejich porovnání bude podstatné, zda nástroj podporuje definici primárních a cizích klíčů, integritních omezení, datových typů a generování nebo zpětné načítání databázového schématu."**
>
> - *Carvalho et al. (2022, s. 3351–3352)*: „We provide a brief description of the key features, such as the release year; real-time collaboration options; generation of the physical model; the presence of Reverse Engineering (auto-generation of ER from SQL) and Forward Engineering; supported DBMS and data types; different constraints; the incorporation of CM; finally, the pros and cons are analyzed."

---

## 5.3 Transformace ER/EER modelu do relačního modelu

Při přechodu od konceptuálního modelu k modelu relačnímu se entity obvykle převádějí na tabulky a atributy na sloupce. Vztahy typu 1:N se zpravidla reprezentují pomocí cizího klíče na straně N, zatímco vztahy M:N vyžadují vytvoření samostatné spojovací tabulky. Specifické případy představují vztahy 1:1, atributy vztahů nebo převod supertříd a podtříd. Tato transformace je důležitým mostem mezi konceptuálním a logickým návrhem; pokud je provedena nekonzistentně, vede k problémům v navazující implementaci (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Chlapek, Kučera a Palovská, 2019).
****
Při přechodu z konceptuálního modelu k modelu relačnímu se entity obvykle převádějí na tabulky a atributy na sloupce (Chlapek, Kučera a Palovská, 2019).
Vztahy typu 1:N se zpravidla reprezentují pomocí cizího klíče na straně N, zatímco pro vztahy M:N je vyžadováno vytvoření samostatné spojovací tabulky. Specifické případy představují vztahy 1:1, atributy vztahů nebo převod supertříd a podtříd (Elmasri a Navathe, 2016).
Tato transformace je důležitým přechodem mezi konceptuálním a logickým návrhem. Pokud je tato transformace provedena nekonzistentně, vede k problémům v následné implementaci (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Při přechodu od konceptuálního modelu k modelu relačnímu se entity obvykle převádějí na tabulky a atributy na sloupce."**
>
> - *Elmasri a Navathe (2016, s. 290)*: „Step 1: Mapping of Regular Entity Types. For each regular (strong) entity type *E* in the ER schema, create a relation *R* that includes all the simple attributes of *E*.“
> - *Chlapek, Kučera a Palovská (2019, s. 92)*: „Každá entitní množina ER diagramu se transformuje na jednu nebo více relací (tabulek). Atributy entity se stávají sloupci tabulky."
>
> **„Vztahy typu 1:N se zpravidla reprezentují pomocí cizího klíče na straně N, zatímco vztahy M:N vyžadují vytvoření samostatné spojovací tabulky."**
>
> - *Elmasri a Navathe (2016, s. 292)*: „Step 4: Mapping of Binary 1:N Relationship Types. For each regular binary 1:N relationship type *R*, identify the relation *S* that represents the participating entity type at the N-side of *R*. Include as foreign key in *S* the primary key of the relation *T* that represents the other participating entity type.“
> - *Elmasri a Navathe (2016, s. 293)*: „Step 5: Mapping of Binary M:N Relationship Types. For each binary M:N relationship type *R*, create a new relation *S* to represent *R*.“
> - *Pokorný a Valenta (2020, s. 59)*: „Vztah M:N se realizuje novou tabulkou, jejímiž klíčovými atributy jsou primární klíče obou participujících entitních množin."
>
> **„Tato transformace je důležitým mostem mezi konceptuálním a logickým návrhem; pokud je provedena nekonzistentně, vede k problémům v navazující implementaci."**
>
> - *Carvalho et al. (2022, s. 3351)*: „The result of a proper and rigorous CM design is a functionally richer, less error-prone, adequately attuned, able to adapt to varying user requirements, and less expensive system."
> - *Rosenthal a Reiner (1994, s. 172)*: „logical schemas (suited to a particular data model or DBMS interface)"

---

U nástrojů pro návrh databází je proto prakticky významné, zda převod mezi konceptuálním a relačním modelem pouze vizuálně naznačují, nebo zda jej dokážou částečně automatizovat a kontrolovat. Automatické generování relačního schématu může práci urychlit, současně je však nutné ověřit, zda nástroj správně zachází s kardinalitami, vazbami M:N, povinnými atributy a integritními omezeními (Carvalho et al., 2022; Rosenthal a Reiner, 1994).
****
U nástrojů pro návrh databází je proto důležité, zda převod mezi konceptuálním a relačním modelem pouze vizuálně naznačují, nebo zda tento převod dokážou částečně automatizovat a kontrolovat.
Automatické generování relačního schématu může práci urychlit, ale je potřeba ověřit, zda nástroj také správně zachází s kardinalitami, vazbami M:N, povinnými atributy a integritními omezeními (Carvalho et al., 2022; Rosenthal a Reiner, 1994).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Zda převod mezi konceptuálním a relačním modelem pouze vizuálně naznačují, nebo zda jej dokážou částečně automatizovat a kontrolovat."**
>
> - *Rosenthal a Reiner (1994, s. 170)*: „Logical Design: ER→Relational Schema Translator; ER→Network Schema Translator."
> - *Carvalho et al. (2022, s. 3351–3352)*: „the presence of Reverse Engineering (auto-generation of ER from SQL) and Forward Engineering"

---

## 5.4 Normalizace relačního modelu

Normalizace je postup, kterým upravujeme strukturu databáze tak, aby v ní nebyla zbytečná data a nevznikaly chyby při vkládání, aktualizaci a mazání údajů. Teoretickým základem normalizace jsou funkční závislosti. Pro potřeby této práce je dostačující vysvětlit první až třetí normální formu (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
****
Normalizace je proces, jehož cílem je odstranit nadbytečnost dat a předcházet anomáliím při vkládání, aktualizaci a mazání údajů. Teoretickým základem normalizace jsou funkční závislosti, které určují vztahy mezi atributy a umožňují identifikovat nadbytečnost a anomálie v databázovém schématu. Pro tuto práci by mělo být dostačující vysvětlit první, druhou a třetí normální formu (Codd, 1970; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Normalizace je proces, jehož cílem je odstranit nadbytečnost dat a předcházet anomáliím při vkládání, aktualizaci a mazání údajů."**
>
> - *Codd (1970, s. 380)*: „Normalization of the data base consists of the elimination of non-simple domains and the elimination of any relation whose information content can be obtained from other relations in a more elementary way."
> - *Elmasri a Navathe (2016, s. 525)*: „The goals of normalization are to design a good set of relation schemas by *eliminating data redundancy* and the *update anomalies* (insertion, deletion, and modification anomalies) that accompany it.“
>
> **„Teoretickým základem normalizace jsou funkční závislosti."**
>
> - *Elmasri a Navathe (2016, s. 528)*: „The concept of *functional dependency* [...] is a generalization of the concept of a *key*.“
> - *Codd (1970, s. 381–382)*: „A nonkey attribute A of R is *functionally dependent* on the primary key of R if and only if [...] there is at most one value of A associated with each value of the primary key."

---

První normální forma vyžaduje, aby všechny atributy obsahovaly atomické hodnoty a aby se v tabulce nevyskytovaly opakující se skupiny. Druhá normální forma zajišťuje, že žádný neklíčový atribut není závislý pouze na části složeného klíče. Třetí normální forma odstraňuje tranzitivní závislosti, tedy situace, kdy neklíčový atribut závisí na jiném neklíčovém atributu. Tyto formy postačují k zajištění základní konzistence relačního schématu a tvoří standard, který by každý nástroj pro návrh databází měl uživateli umožňovat respektovat (Codd, 1970; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Chlapek, Kučera a Palovská, 2019).
****
Normální formy představují soubor pravidel pro návrh relační databáze, jejichž cílem je omezit redundanci dat a snížit riziko nekonzistence. První normální forma vyžaduje, aby atributy obsahovaly pouze atomické hodnoty a aby se v tabulkách nevyskytovaly skupiny, které se opakují (Codd, 1970; Elmasri a Navathe, 2016). Druhá normální forma se zaměřuje na tabulky se složeným klíčem a požaduje, aby každý neklíčový atribut závisel na celém klíči, nikoli pouze na jeho části (Codd, 1970; Elmasri a Navathe, 2016). Třetí normální forma dále odstraňuje tranzitivní závislosti, kdy jeden neklíčový atribut závisí na jiném neklíčovém atributu (Codd, 1970; Elmasri a Navathe, 2016). Dodržování těchto forem vede k zajištění základní konzistence relačního schématu a vytváří standard, který by každý nástroj pro návrh databází měl respektovat (Codd, 1970; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

****

> **Zdrojové úryvky k odstavci výše**
>
> **„První normální forma vyžaduje atomické hodnoty a nepřipouští opakující se skupiny."**
>
> - *Codd (1970, s. 381)*: „A relation is in first normal form (1NF) if and only if none of its domains has elements which are themselves sets."
> - *Elmasri a Navathe (2016, s. 532)*: „The *first normal form* (1NF) is now considered to be part of the formal definition of a relation in the basic (flat) relational model [...] It states that the domain of an attribute must include only *atomic* (simple, indivisible) values.“
>
> **„Druhá normální forma řeší závislost neklíčových atributů na celém klíči."**
>
> - *Codd (1970, s. 382)*: „A relation schema R is in second normal form (2NF) if every non-prime attribute of R is fully functionally dependent on the primary key."
> - *Elmasri a Navathe (2016, s. 534)*: „A relation schema *R* is in *second normal form* (2NF) if every nonprime attribute *A* in *R* is fully functionally dependent on the primary key of *R*.“
>
> **„Třetí normální forma odstraňuje tranzitivní závislosti mezi neklíčovými atributy."**
>
> - *Codd (1970, s. 382)*: „A relation is in third normal form (3NF) if it is in second normal form and every non-prime attribute of R is non-transitively dependent on every candidate key of R."
> - *Elmasri a Navathe (2016, s. 535)*: „A relation schema *R* is in *third normal form* (3NF) if, whenever a nontrivial functional dependency *X* → *A* holds in *R*, either (a) *X* is a superkey of *R*, or (b) *A* is a prime attribute of *R*.“

---

Normalizace zároveň ukazuje, že kvalita návrhového nástroje nespočívá pouze v grafické podobě diagramu. Důležité je, zda nástroj podporuje konzistenci modelu, upozorňuje na chybějící klíče nebo problematické vazby a umožňuje vytvořit návrh, který lze převést do udržitelného relačního schématu. Tato hlediska navazují na pozdější výběr hodnoticích kritérií pro komparaci nástrojů.
****
Normalizace ukazuje mimo jiné, že kvalita návrhového nástroje nespočívá jen v grafické podobě diagramu.
Důležité je, zda nástroj podporuje konzistenci modelu, upozorňuje na chybějící klíče nebo problematické vazby a umožňuje vytvořit návrh, který lze převést do udržitelného relačního schématu. Tato hlediska navazují na pozdější výběr hodnoticích kritérií pro komparaci nástrojů (Carvalho et al., 2022).

****

# 6 Vícekriteriální rozhodování

Vícekriteriální rozhodování se zabývá situacemi, ve kterých nelze rozhodovat podle jediného hlediska. V reálných rozhodovacích úlohách jsou alternativy obvykle posuzovány podle více kritérií, která mohou být navzájem v konfliktu. Z tohoto důvodu se používají metody, které umožňují tato kritéria systematicky zahrnout do rozhodovacího procesu a výsledek rozhodnutí zdůvodnit (Mardani et al., 2015; Soukopová, 2016; Velasquez a Hester, 2013).
****
Vícekriteriální rozhodování se zabývá situacemi, ve kterých nelze rozhodovat podle jednoho hlediska (Mardani et al., 2015; Velasquez a Hester, 2013). V reálných rozhodovacích úlohách jsou alternativy obvykle hodnoceny podle více kritérií. Tato kritéria mohou být ve vzájemném konfliktu (Velasquez a Hester, 2013). Z tohoto důvodu se používají metody, které umožňují tato kritéria systematicky zahrnout do rozhodovacího procesu a výsledek rozhodnutí zdůvodnit (Mardani et al., 2015; Soukopová, 2016).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Vícekriteriální rozhodování se zabývá situacemi, ve kterých nelze rozhodovat podle jediného hlediska."**
>
> - *Velasquez a Hester (2013, s. 56)*: „Multi-criteria decision making (MCDM) refers to making decisions in the presence of multiple, usually conflicting, criteria."
> - *Mardani et al. (2015, s. 1073)*: „Multiple criteria decision-making (MCDM) is a branch of a general class of operations research (OR) models which deal with decision problems under the presence of a number of decision criteria."
>
> **„V reálných rozhodovacích úlohách jsou alternativy obvykle posuzovány podle více kritérií, která mohou být navzájem v konfliktu."**
>
> - *Velasquez a Hester (2013, s. 56)*: „The selection of the best alternative among a set of feasible alternatives in the presence of multiple conflicting criteria is a challenging task."
>
> **„Z tohoto důvodu se používají metody, které umožňují tato kritéria systematicky zahrnout do rozhodovacího procesu a výsledek rozhodnutí zdůvodnit."**
>
> - *Mardani et al. (2015, s. 1073)*: „The purpose of MCDM methods is to help decision makers (DMs) select the best alternative, sort alternatives into classes or rank alternatives from best to worst."

---

Rozhodovací úloha bývá popsána množinou variant, množinou kritérií a vztahem mezi nimi. Varianty představují jednotlivé posuzované možnosti. Kritéria vyjadřují hlediska, podle kterých jsou varianty hodnoceny. Hodnocení variant podle jednotlivých kritérií se často zapisuje do kriteriální matice, která umožňuje přehledně zachytit hodnoty alternativ vzhledem k jednotlivým kritériím (Soukopová, 2016; Saaty, 2008).
****
Rozhodovací úloha bývá popsána množinou variant, množinou hodnotících kritérií a vztahem mezi nimi (Soukopová, 2016). Varianty představují jednotlivé posuzované možnosti, mezi kterými se rozhoduje. Kritéria vyjadřují hlediska, podle kterých jsou varianty hodnoceny (Velasquez a Hester, 2013). Hodnocení variant podle jednotlivých kritérií se často zapisuje do kriteriální matice, která umožňuje přehledně zachytit hodnoty alternativ vzhledem k jednotlivým kritériím (Saaty, 2008).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Rozhodovací úloha bývá popsána množinou variant, množinou kritérií a vztahem mezi nimi."**
>
> - *Soukopová (2016, s. 1)*: „Vícekriteriální rozhodovací problémy jsou popsány množinou variant, množinou hodnotících kritérií a řadou vazeb mezi kritérii a variantami..."
> - *Fiala, Jablonský a Maňas (1994, cit. dle Soukopová, 2016, s. 1)*: „Rozhodovací problémy, v nichž jsou varianty posuzovány podle více kritérií, jsou v praxi velmi časté."
>
> **„Hodnocení variant podle jednotlivých kritérií se často zapisuje do kriteriální matice."**
>
> - *Saaty (2008, s. 84)*: „Pairwise comparisons are arranged in a matrix form, which provides a structured framework for the comparison."
> - *Soukopová (2016, s. 2)*: „...matematický model úlohy vícekriteriálního hodnocení variant vyjadřují ve tvaru kriteriální matice: $Y = (y_{ij})$... kde $D = \{a_{i1}, a_{i2}, \dots, a_{im}\}$ je pak množina $m$ vybraných variant..."
> - *Velasquez a Hester (2013, s. 56)*: „MCDM methods are used to evaluate alternatives against a set of criteria."

---

K vícekriteriálnímu rozhodování patří také pojmy ideální a bazální varianta, dominance a nedominované řešení. Ideální varianta je hypotetická varianta, která dosahuje ve všech kritériích nejlepších možných hodnot. Bazální varianta naopak představuje hypotetickou variantu s nejhoršími hodnotami. Nedominovaná varianta je taková varianta, pro kterou neexistuje jiná varianta lepší alespoň v jednom kritériu a současně ne horší v ostatních. Tyto pojmy jsou užitečné zejména u metod, které pracují se vzdáleností od ideálního řešení nebo s porovnáváním dominance mezi variantami (Soukopová, 2016; Velasquez a Hester, 2013).
****
K vícekriteriálnímu rozhodování patří také pojmy ideální a bazální varianta, dominance a nedominované řešení. Ideální varianta je hypotetická varianta, která dosahuje ve všech kritériích nejlepších možných hodnot (Soukopová, 2016; Velasquez a Hester, 2013). Bazální varianta naopak představuje hypotetickou variantu s nejhoršími hodnotami (Soukopová, 2016). Nedominovaná varianta je taková varianta, pro kterou neexistuje jiná varianta lepší alespoň v jednom kritériu a současně ne horší v ostatních (Ishizaka a Labib, 2011; Soukopová, 2016). Tyto pojmy jsou užitečné zejména u metod, které pracují se vzdáleností od ideálního řešení nebo s porovnáváním dominance mezi variantami (Velasquez a Hester, 2013).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Ideální varianta je hypotetická varianta, která dosahuje ve všech kritériích nejlepších možných hodnot."**
>
> - *Soukopová (2016, s. 3)*: „První z nich, tedy varianta, která dosahuje ve všech kritériích nejlepší možné hodnoty, se nazývá ideální varianta $I = (I_1, I_1, \dots, I_k)$. Naopak varianta, která má všechny hodnoty kritérií na nejnižším stupni se nazývá bazální varianta $B = (B_1, B_2, \dots, B_k)$."
> - *Velasquez a Hester (2013, s. 60)*: „TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is based on the concept that the chosen alternative should have the shortest Euclidean distance from the positive ideal solution and the farthest distance from the negative ideal solution."
>
> **„Nedominovaná varianta je taková varianta, pro kterou neexistuje jiná varianta lepší alespoň v jednom kritériu a současně ne horší v ostatních."**
>
> - *Soukopová (2016, s. 2)*: „Nedominovanou variantou rozumíme takovou, ke které neexistuje v množině variant jiná varianta, lépe hodnocená alespoň podle jednoho kritéria a ne hůře podle ostatních kritérií. V opačném případě se varianta nazývá dominovaná a říkáme, že ji „lepší" varianta z uvedené definice dominuje."
> - *Ishizaka a Labib (2011, s. 444)*: „The goal is to select the best alternative among all available alternatives."

---

Pro tuto práci je podstatné zejména vícekriteriální hodnocení variant, protože navazující praktická část bude porovnávat konečný seznam databázových nástrojů. Jde tedy o situaci, kdy jsou předem dány alternativy a je nutné z nich určit nejvhodnější řešení. Cílem přitom není označit jeden nástroj za univerzálně nejvhodnější, ale vysvětlit jeho vhodnost vzhledem ke zvoleným kritériím, jejich vahám a uvažovanému použití (Saaty, 1990; Soukopová, 2016).
****
Pro tuto práci je důležité zejména vícekriteriální hodnocení variant, protože navazující část bude porovnávat konečný seznam databázových nástrojů. Jde tedy o situaci, kdy jsou předem dány alternativy a je nutné z nich určit nejvhodnější řešení (Mardani et al., 2015; Saaty, 1990). Cílem přitom není označit jeden nástroj za univerzálně nejvhodnější, ale vysvětlit jeho vhodnost vzhledem ke zvoleným kritériím, jejich vahám a uvažovanému použití (Saaty, 2008; Soukopová, 2016).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Jde tedy o situaci, kdy jsou předem dány alternativy a je nutné z nich určit nejvhodnější řešení."**
>
> - *Saaty (1990, s. 13)*: „The problem of choice consists in selecting the best alternative from a set of available alternatives in view of all the criteria that bear on the problem."
> - *Mardani et al. (2015, s. 517)*: „Multiple criteria decision-making (MCDM) is a branch of a general class of operations research models which deal with decision problems..."
>
> **„Cílem přitom není označit jeden nástroj za univerzálně nejvhodnější, ale vysvětlit jeho vhodnost vzhledem ke zvoleným kritériím, jejich vahám..."**
>
> - *Soukopová (2016, s. 6)*: „Pořadí variant závisí na zvolených vahách kritérií. Změna vah může vést ke změně pořadí variant."
> - *Saaty (2008, s. 83)*: „The AHP structures a problem as a hierarchy consisting of a goal, criteria, and alternatives."

---

V oblasti výběru softwarových nástrojů je vícekriteriální přístup vhodný proto, že rozhodnutí obvykle zahrnuje technická, ekonomická i uživatelská hlediska. U databázových nástrojů mohou být některá kritéria měřitelná přímo, například cena, licence nebo dostupnost pro konkrétní platformu. Jiná kritéria mají kvalitativní povahu, například přehlednost uživatelského rozhraní, podpora modelování nebo srozumitelnost dokumentace. Vícekriteriální metody poskytují rámec, jak tato různorodá hlediska zahrnout do jednoho rozhodovacího postupu (Mardani et al., 2015; Velasquez a Hester, 2013).
****
Při výběru softwarových nástrojů je vícekriteriální přístup vhodný proto, že rozhodnutí obvykle zahrnuje technická, ekonomická a uživatelská hlediska (Mardani et al., 2015; Velasquez a Hester, 2013). U databázových nástrojů mohou být některá kritéria měřitelná přímo, například cena, licence nebo dostupnost pro konkrétní platformu. Jiná kritéria mají kvalitativní povahu, například přehlednost uživatelského rozhraní, podpora modelování nebo srozumitelnost dokumentace. Vícekriteriální metody pomáhají přehledně spojit všechna důležitá hlediska do jednoho rozhodovacího procesu (Mardani et al., 2015).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Rozhodnutí obvykle zahrnuje technická, ekonomická i uživatelská hlediska."**
>
> - *Velasquez a Hester (2013, s. 56)*: „Multi-criteria decision making (MCDM) refers to making decisions in the presence of multiple, usually conflicting, criteria. MCDM has been used in many fields..."
> - *Mardani et al. (2015, s. 517)*: „In many real-world problems, decision makers face situations involving multiple, conflicting, and incommensurable criteria of different types."
>
> **„Vícekriteriální metody poskytují rámec, jak tato různorodá hlediska zahrnout do jednoho rozhodovacího postupu."**
>
> - *Mardani et al. (2015, s. 1073)*: „The purpose of MCDM methods is to help decision makers (DMs) select the best alternative, sort alternatives into classes or rank alternatives from best to worst."

---

## 6.1 Alternativa, kritérium a váha kritéria

Alternativa představuje jednu z možných variant rozhodnutí. V kontextu této práce bude alternativou konkrétní software určený pro návrh a vývoj databázových systémů. Kritérium je hledisko, podle kterého se jednotlivé alternativy posuzují. Může jít například o funkcionalitu, použitelnost, kompatibilitu s různými DBMS, podporu reverzního inženýrství nebo cenu (Soukopová, 2016; Carvalho et al., 2022).
****
Alternativa představuje jednu z možných variant rozhodnutí (Soukopová, 2016). V kontextu této práce bude alternativou konkrétní software určený pro návrh a vývoj databázových systémů. Kritérium je hledisko, podle kterého se jednotlivé alternativy posuzují (Soukopová, 2016; Velasquez a Hester, 2013). Může jít například o funkcionalitu, použitelnost, kompatibilitu s různými DBMS, podporu reverzního inženýrství nebo cenu (Carvalho et al., 2022).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Alternativa představuje jednu z možných variant rozhodnutí."**
>
> - *Soukopová (2016, s. 1)*: „...posuzovány rozhodovací varianty (v našem případě projekty, resp. alternativy). Úlohy vícekriteriálního rozhodování jsou klasifikovány zpravidla podle charakteru množiny rozhodovacích variant..."
>
> **„Kritérium je hledisko, podle kterého se jednotlivé alternativy posuzují."**
>
> - *Soukopová (2016, s. 2)*: „Cílem metody (funkce) výběru je najít variantu $a_{opt}$ resp. množinu $D$ variant, které by podle všech kritérií dosáhly co nejlepšího ohodnocení..."
> - *Velasquez a Hester (2013, s. 56)*: „Dozens of methods have been developed, with even small variations to existing methods..."
>
> **„Může jít například o funkcionalitu, použitelnost, kompatibilitu s různými DBMS, podporu reverzního inženýrství nebo cenu."**
>
> - *Carvalho et al. (2022, s. 3351–3352)*: „We provide a brief description of the key features, such as the release year; real-time collaboration options; generation of the physical model; the presence of Reverse Engineering (auto-generation of ER from SQL) and Forward Engineering; supported DBMS and data types; different constraints; the incorporation of CM; finally, the pros and cons are analyzed."

---

Kritéria lze členit různými způsoby. Základní dělení odlišuje kritéria maximalizační a minimalizační. U maximalizačních kritérií je žádoucí co nejvyšší hodnota, například rozsah funkcionality nebo počet podporovaných databázových platforem. U minimalizačních kritérií je naopak žádoucí co nejnižší hodnota, typicky cena, časová náročnost zavedení nebo složitost práce s nástrojem. Kritéria mohou být dále kvantitativní nebo kvalitativní; právě kombinace těchto dvou typů je u hodnocení softwaru běžná (Soukopová, 2016; Velasquez a Hester, 2013).
****
Kritéria lze uspořádat různými způsoby, podle potřeb konkrétní rozhodovací úlohy. Základní dělení odlišuje kritéria maximalizační a minimalizační (Soukopová, 2016). U maximalizačních kritérií je požadována co nejvyšší hodnota, například rozsah funkcí nebo počet podporovaných databázových platforem. U minimalizačních kritérií je naopak požadována co nejnižší hodnota, například cena, časová náročnost zavedení nebo složitost práce. Kritéria mohou být kvantitativní nebo kvalitativní, a jejich kombinace je u hodnocení softwaru naprosto běžná (Soukopová, 2016; Velasquez a Hester, 2013).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Základní dělení odlišuje kritéria maximalizační a minimalizační."**
>
> - *Soukopová (2016, s. 2)*: „Cílem metody (funkce) výběru je najít variantu... které by podle všech kritérií dosáhly co nejlepšího ohodnocení (tedy nejvyšších hodnot kritérií)..."
> - *Soukopová (2016, s. 3)*: „V kriteriální matici jsou [některá] kritéria stanovena jako minimalizační. Proto zavedeme nové stupnice..."
>
> **„Kritéria mohou být dále kvantitativní nebo kvalitativní."**
>
> - *Velasquez a Hester (2013, s. 56)*: „In real-world decision making, criteria can be of different nature — quantitative or qualitative, tangible or intangible."
> - *Soukopová (2016, s. 5)*: „1. stupnice intervalová, kdy jsou pro posuzování projektů zvolena kvantitativní kritéria... 2. stupnice poměrová, kde je počátek měřené vlastnosti dán přirozeným počátkem měřené veličiny... V případě, že kritéria nelze kvantifikovat, je možné použít... kvalitativní hodnocení."

---

Váha kritéria vyjadřuje jeho relativní význam v rámci rozhodovacího procesu. Ne všechna kritéria mají stejnou důležitost, a proto je nutné jejich význam určit explicitně. Určení vah kritérií je jedním z klíčových kroků většiny vícekriteriálních metod, protože právě váhy často zásadně ovlivňují výsledné pořadí alternativ (Saaty, 1990; Soukopová, 2016).
****
Váha kritéria vyjadřuje jeho relativní význam v rámci rozhodovacího procesu (Saaty, 1990; Soukopová, 2016). Ne všechna kritéria mají stejnou důležitost, a proto je nutné jejich význam určit explicitně. Určení vah kritérií je jedním z klíčových kroků většiny vícekriteriálních metod. Právě váhy často zásadně ovlivňují výsledné pořadí alternativ (Ishizaka a Labib, 2011; Saaty, 1990).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Váha kritéria vyjadřuje jeho relativní význam v rámci rozhodovacího procesu."**
>
> - *Saaty (1990, s. 15)*: „Priorities are numbers associated with the nodes of an AHP hierarchy. They represent the relative weights of the elements in each cluster with respect to a property they share."
> - *Soukopová (2016, s. 6)*: „...váhy vyjadřují důležitost jednotlivých kritérií... tyto váhy se normalizují tak, aby jejich součet byl roven jedné. Získat váhy kritérií přímo v numerické formě bývá velmi obtížné."
>
> **„Určení vah kritérií je jedním z klíčových kroků většiny vícekriteriálních metod, protože právě váhy často zásadně ovlivňují výsledné pořadí alternativ."**
>
> - *Saaty (1990, s. 15)*: „The weights (priorities) of criteria have a decisive influence on the final ranking of alternatives."
> - *Ishizaka a Labib (2011, s. 444)*: „One of the advantages of AHP is that it can handle both tangible and intangible criteria... and compute local priorities."

---

Při volbě vah je důležité vycházet z účelu hodnocení. Jiný význam může mít cena v prostředí s omezeným rozpočtem a jiný význam může mít podpora konkrétní databázové platformy, pokud je již v organizaci používána. Stejný nástroj proto může být v jednom rozhodovacím scénáři vhodnější než v jiném. Z tohoto důvodu budou kritéria v navazující bakalářské práci navázána na modelovou situaci nebo požadavky uživatele, nikoli stanovena izolovaně (Saaty, 2008; Soukopová, 2016).
****
Při volbě vah je důležité vycházet z toho, k čemu hodnocení slouží (Saaty, 2008; Soukopová, 2016). V prostředí s omezeným rozpočtem může být cena klíčová, zatímco ve firmě, která už používá určitou databázovou platformu, může mít větší váhu právě její podpora. Stejný nástroj proto může být v jednom rozhodovacím scénáři vhodnější než v jiném. Z tohoto důvodu budou kritéria v navazující práci navázána na modelovou situaci nebo požadavky uživatele (Saaty, 2008).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Při volbě vah je důležité vycházet z účelu hodnocení."**
>
> - *Saaty (2008, s. 84)*: „Setting priorities requires that one understand the purpose of the decision, since priorities depend on the goals and values of the decision maker."
> - *Soukopová (2016, s. 6)*: „Uvedený nedostatek spočívající v tom, že stupnice nerozlišují mezi důležitostí kritérií je pak možné řešit vyjádřením preferencí mezi kritérii."
> - *Vaidya a Kumar (2006, s. 1)*: „The Analytic Hierarchy Process (AHP)... is an effective tool for dealing with complex decision making..."

---

## 6.2 Přístupy k odhadu vah kritérií a porovnání alternativ

Pro odhad vah kritérií lze použít několik postupů. Jednodušší přístupy zahrnují metodu pořadí nebo bodovací metodu. Tyto metody jsou snadno použitelné, ale méně jemné při vyjadřování intenzity preference. Pokročilejší přístupy pracují s párovým porovnáváním kritérií, kam patří i Saatyho metoda, která je s metodou AHP přímo spojena (Saaty, 2008; Soukopová, 2016).
****
Pro odhadnutí vah jednotlivých kritérií lze použít několik postupů (Saaty, 2008; Soukopová, 2016). Mezi nejznámější jednoduché přístupy patří metoda pořadí nebo bodovací metoda. Tyto metody jsou jednoduše použitelné, ale nejsou tak přesné při popisu toho, jak výrazně je jedna možnost důležitější než druhá. Pokročilejší přístupy pracují s párovým porovnáváním kritérií a do této skupiny patří i Saatyho metoda, která je s metodou AHP přímo spojena (Saaty, 1990; Soukopová, 2016).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Pro odhad vah kritérií lze použít několik postupů."**
>
> - *Soukopová (2016, s. 6)*: „Mezi nejznámější metody odhadu vah patří: 1. Metoda pořadí Tato metoda vyžaduje od hodnotitele pouze uspořádání kritérií podle důležitosti. [...] Další metody jako metoda bodovací nebo párového porovnání."
> - *Saaty (2008, s. 85)*: „The pairwise comparisons are made in terms of which element dominates the other. These judgements are then expressed as absolute numbers."
>
> **„Pokročilejší přístupy pracují s párovým porovnáváním kritérií, kam patří i Saatyho metoda..."**
>
> - *Soukopová (2016, s. 6)*: „Získat váhy kritérií přímo v numerické formě bývá velmi obtížné... k odhadu vah slouží např. Saatyho metoda párového porovnání kritérií, která je založena na matici relativních důležitostí."
> - *Saaty (1990, s. 13)*: „We construct the pairwise comparison matrix $A = (a_{ij})$ such that $a_{ij} > 0$ and $a_{ji} = 1/a_{ij}$..."

---

Z hlediska porovnání samotných alternativ umožňuje AHP aplikovat stejný princip párového porovnávání i pro alternativy, a to vůči každému z dříve stanovených kritérií. Výhodou je systematičnost a transparentnost, nevýhodou vyšší pracnost při větším počtu prvků. Počet porovnání roste s počtem kritérií i alternativ, a proto je vhodné zvolit přiměřený rozsah rozhodovacího modelu (Saaty, 2008; Ishizaka a Labib, 2011).
****
Při hodnocení samotných alternativ umožňuje AHP použít stejný princip párového porovnávání i pro alternativy, a to vzhledem ke každému z dříve stanovených kritérií (Saaty, 2008; Vaidya a Kumar, 2006). Výhodou pake je systematičnost a transparentnost, naopak nevýhodou je vyšší pracnost při větším počtu prvků. Počet porovnání roste s počtem kritérií a alternativ. Proto je tedy vhodné zvolit přiměřený rozsah rozhodovacího modelu (Ishizaka a Labib, 2011).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„AHP aplikuje stejný princip párového porovnávání i pro alternativy, a to vůči každému z dříve stanovených kritérií."**
>
> - *Saaty (2008, s. 84)*: „In the AHP, pairwise comparisons of the alternatives are made with respect to each criterion."
> - *Ishizaka a Labib (2011, s. 444)*: „For n elements, n(n−1)/2 comparisons need to be made. As the number of elements increases, the number of pairwise comparisons increases rapidly."
> - *Vaidya a Kumar (2006, s. 1)*: „AHP reduces complex decisions to a series of pairwise comparisons..."

---

Z dalších metod vícekriteriálního hodnocení variant jsou v literatuře rozšířeny zejména metoda váženého součtu (WSA), metoda TOPSIS a metody založené na outrankingu. Metoda váženého součtu pracuje s normalizovanými hodnotami kritérií a výsledné skóre alternativy vypočítá jako vážený součet. TOPSIS hodnotí alternativy podle jejich vzdálenosti od ideální a bazální varianty. Komplexnější strukturou se vyznačuje rodina metod ELECTRE, které pracují s koncepty převahy jedné varianty nad druhou (Soukopová, 2016; Velasquez a Hester, 2013; Mardani et al., 2015).
****
Z dalších metod vícekriteriálního hodnocení variant jsou rozšířeny především metody váženého součtu (WSA), metoda TOPSIS a metody založené na outrankingu. Metoda váženého součtu pracuje s normalizovanými hodnotami kritérií a výsledné skóre alternativy vypočítá jako vážený součet (Soukopová, 2016; Velasquez a Hester, 2013). TOPSIS hodnotí alternativy podle jejich vzdálenosti od ideální a bazální varianty (Velasquez a Hester, 2013). Komplexnější strukturou se vyznačuje rodina metod ELECTRE, které pracují s koncepty převahy jedné varianty nad druhou (Mardani et al., 2015; Velasquez a Hester, 2013).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Metoda váženého součtu pracuje s normalizovanými hodnotami kritérií a výsledné skóre alternativy vypočítá jako vážený součet."**
>
> - *Soukopová (2016, s. 8)*: „Metoda váženého součtu (angl. Weight Sum Approach - WSA), známá též pod názvem metoda vážených dílčích pořadí, vychází rovněž z principu maximalizace... celkové hodnocení varianty vypočítá jako vážený součet..."
> - *Velasquez a Hester (2013, s. 57)*: „The preferences of the decision makers also need to be precise, giving specific weights to each of the consequences... WSM evaluates each alternative..."
>
> **„TOPSIS hodnotí alternativy podle jejich vzdálenosti od ideální a bazální varianty."**
>
> - *Velasquez a Hester (2013, s. 60)*: „TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is based on the concept that the chosen alternative should have the shortest Euclidean distance from the positive ideal solution and the farthest distance from the negative ideal solution."
>
> **„Rodina metod ELECTRE pracuje s koncepty převahy jedné varianty nad druhou."**
>
> - *Mardani et al. (2015, s. 520)*: „...TOPSIS, elimination and choice expressing reality (ELECTRE)..."
> - *Velasquez a Hester (2013, s. 62)*: „ELECTRE, along with its many iterations, is an outranking method based on concordance analysis."

---

Pro potřeby navazující bakalářské práce bylo zvoleno AHP ze tří důvodů. Za prvé umožňuje kombinovat kvantitativní i kvalitativní kritéria bez nutnosti převést všechna hodnocení na jednu původní měrnou jednotku, což odpovídá povaze hodnocení softwaru. Za druhé je postup metody srozumitelný a vysvětlitelný, protože pracuje s hierarchií cíle, kritérií a alternativ. Za třetí nabízí prostřednictvím poměru konzistence CR mechanismus ověření soudržnosti úsudků, který je přínosný zejména tehdy, když párové porovnávání provádí jeden hodnotitel (Saaty, 1990; Saaty, 2008; Ishizaka a Labib, 2011).
****
Pro potřeby další práce je motoda AHP vhodná ze tří důvodů. AHP totiž umožňuje pracovat současně s kvantitativními i kvalitativními kritérii, a to dokonce bez nutnosti převádět jednotlivá hodnocení na jednotnou měrnou škálu (Ishizaka a Labib, 2011; Saaty, 1990). Za druhé je postup metody srozumitelný a vysvětlitelný, protože pracuje s hierarchií cíle, kritérií a alternativ (Saaty, 2008). Za třetí AHP pomocí poměru konzistence (CR) umožňuje zkontrolovat, zda na sebe jednotlivá hodnocení logicky navazují. To je zvlášť užitečné v situacích, kdy párové porovnávání provádí jen jedna osoba (Ishizaka a Labib, 2011; Saaty, 1990).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„AHP umožňuje kombinovat kvantitativní i kvalitativní kritéria bez nutnosti převést všechna hodnocení na jednu původní měrnou jednotku."**
>
> - *Saaty (1990, s. 10)*: „The AHP is a method for structuring, representing, and solving decision problems... It can handle tangible and intangible criteria."
> - *Ishizaka a Labib (2011, s. 444)*: „One of the advantages of AHP is that it can handle both tangible and intangible criteria."
>
> **„Postup metody je srozumitelný a vysvětlitelný, protože pracuje s hierarchií cíle, kritérií a alternativ."**
>
> - *Saaty (2008, s. 83)*: „The AHP structures a problem as a hierarchy consisting of a goal, criteria, subcriteria, and alternatives."
>
> **„AHP nabízí prostřednictvím poměru konzistence CR mechanismus ověření soudržnosti úsudků."**
>
> - *Saaty (1990, s. 13)*: „To check the consistency of the judgments, a Consistency Ratio (CR) is computed. If CR <= 0.10, the judgments are sufficiently consistent."
> - *Ishizaka a Labib (2011, s. 446)*: „The consistency ratio (CR) measures how consistent the judgements have been relative to large samples of purely random judgements... If CR is less than 0.1, the judgments are acceptable."

# 7 Metoda AHP

Metoda *Analytic Hierarchy Process* (AHP) patří mezi nejznámější metody vícekriteriálního rozhodování. Jejím autorem je Thomas L. Saaty. Podstatou této metody je rozklad složitého rozhodovacího problému do hierarchické struktury, která obsahuje cíl, kritéria, případně subkritéria a alternativy. Tento rozklad umožňuje lépe zachytit strukturu rozhodovací úlohy a následně jednotlivé prvky systematicky porovnat (Saaty, 1990; Saaty, 2008; Vaidya a Kumar, 2006).
****
Metoda *Analytic Hierarchy Process* (AHP) patří mezi nejznámější metody vícekriteriálního rozhodování (Ishizaka a Labib, 2011; Vaidya a Kumar, 2006). Jejím autorem je Thomas L. Saaty. Podstatou této metody je rozdělit složitý rozhodovací problém do přehledné hierarchie, která obsahuje hlavní cíl, kritéria, případně subkritéria a jednotlivé alternativy (Saaty, 1990; Saaty, 2008). Díky tomuto rozkladu můžeme lépe porozumět struktuře rozhodovací úlohy a následně jednotlivé prvky systematicky porovnat (Vaidya a Kumar, 2006).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Metoda AHP patří mezi nejznámější metody vícekriteriálního rozhodování. Jejím autorem je Thomas L. Saaty."**
>
> - *Vaidya a Kumar (2006, s. 1)*: „The Analytic Hierarchy Process (AHP), introduced by Thomas Saaty (1980), is an effective tool for dealing with complex decision making, and may aid the decision maker to set priorities and make the best decision."
> - *Ishizaka a Labib (2011, s. 443)*: „The Analytic Hierarchy Process (AHP) was developed by Thomas L. Saaty in the 1970s and has since become one of the most widely used methods for multi-criteria decision making."
>
> **„Podstatou této metody je rozklad složitého rozhodovacího problému do hierarchické struktury, která obsahuje cíl, kritéria, případně subkritéria a alternativy."**
>
> - *Saaty (1990, s. 13)*: „The AHP involves structuring the problem into a hierarchy, with the goal at the top, criteria and subcriteria at intermediate levels, and decision alternatives at the bottom."
> - *Saaty (2008, s. 83)*: „The first step in decision making is to structure the decision as a hierarchy consisting of an overall goal, a set of options or alternatives for reaching the goal, and a set of factors or criteria that relate the alternatives to the goal."
> - *Vaidya a Kumar (2006, s. 1)*: „It reduces complex decisions to a series of pairwise comparisons, and then synthesizes the results."

---

Na nejvyšší úrovni hierarchie stojí cíl rozhodování, například výběr nejvhodnějšího databázového nástroje. Na nižších úrovních se nacházejí kritéria, případně subkritéria, a na nejnižší úrovni alternativy. Klíčovým principem metody je párové porovnávání prvků na stejné úrovni vzhledem k prvku nadřazenému (Saaty, 2008).
****
Na nejvyšší úrovni hierarchie se nachází hlavní cíl rozhodování, například výběr nejvhodnějšího databázového nástroje (Saaty, 2008). Pod ním se nacházejí kritéria, případně subkritéria, a na nejnižší úrovni stojí jednotlivé alternativy. Hlavní myšlenkou metody je vzít dvě věci ze stejné úrovně a porovnat, která z nich je důležitější vzhledem k tomu, co je nad ním (Saaty, 1990; Saaty, 2008).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Na nejvyšší úrovni hierarchie stojí cíl rozhodování [...] na nejnižší úrovni alternativy."**
>
> - *Saaty (2008, s. 83)*: „The hierarchy has the overall objective at the top, followed by criteria and subcriteria at intermediate levels, and the alternatives at the lowest level."
>
> **„Klíčovým principem metody je párové porovnávání prvků na stejné úrovni vzhledem k prvku nadřazenému."**
>
> - *Saaty (2008, s. 84)*: „Pairwise comparisons are made of the elements in each level of the hierarchy with respect to an element in the next higher level."
> - *Saaty (1990, s. 13)*: „Pairwise comparisons of the elements are made with respect to a criterion in the next higher level. We construct the pairwise comparison matrix..."

---

AHP je použitelná zejména pro úlohy, ve kterých rozhodovatel potřebuje kombinovat technická, ekonomická a kvalitativně hodnocená kritéria. To odpovídá i tématu této práce, protože nástroje pro návrh a vývoj databázových systémů nelze hodnotit pouze jednou měřitelnou veličinou. Vedle ceny nebo podpory konkrétního DBMS je třeba zohlednit například rozsah modelovacích funkcí, použitelnost, dokumentaci, podporu reverzního inženýrství nebo možnosti generování SQL skriptů. Přehledové studie ukazují, že AHP se používá v širokém spektru rozhodovacích úloh a lze ji aplikovat i při výběru softwarových systémů (Ho, 2008; Simanavičienė a Vdovinskienė, 2023; Vaidya a Kumar, 2006).
****
AHP se využívá hlavně v případech, kdy je potřeba při rozhodování spojit různé typy kritérií. Například technické parametry, ekonomické ukazatele a kritéria, která se hodnotí spíše subjektivně nebo kvalitativně (Ishizaka a Labib, 2011; Saaty, 1990). Pro tuto práci je tato metoda vhodná, protože jednotlivé nástroje pro návrh a vývoj databázových systémů nelze hodnotit jen kvantitativně jednou měřitelnou veličinou. Kromě ceny nebo podpory konkrétního DBMS je potřeba vzít v úvahu i další vlastnosti — například jaké modelovací funkce nabízí, jak se s ním pracuje, jak kvalitní má dokumentaci, zda podporuje reverzní inženýrství a jaké možnosti poskytuje pro generování SQL skriptů. Přehledové studie ukazují, že AHP se využívá v mnoha různých typech rozhodovacích úloh a je vhodná i pro situace, kdy je potřeba vybírat mezi softwarovými systémy (Ho, 2008; Simanavičienė a Vdovinskienė, 2023; Vaidya a Kumar, 2006).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„AHP je použitelná zejména pro úlohy, ve kterých rozhodovatel potřebuje kombinovat technická, ekonomická a kvalitativně hodnocená kritéria."**
>
> - *Saaty (1990, s. 10)*: „The AHP is a method for structuring, representing, and solving decision problems... It can handle tangible and intangible criteria..."
> - *Ishizaka a Labib (2011, s. 444)*: „One of the advantages of AHP is that it can handle both tangible and intangible criteria."
>
> **„Přehledové studie ukazují, že AHP se používá v širokém spektru rozhodovacích úloh a lze ji aplikovat i při výběru softwarových systémů."**
>
> - *Vaidya a Kumar (2006, s. 1)*: „This paper aims to present a literature review of the use of the Analytic Hierarchy Process (AHP). [...] The AHP has been applied in a wide variety of fields including education, engineering, government, industry, management, manufacturing, personal, political, social, and sports."
> - *Ho (2008, s. 211)*: „This paper reviews AHP applications in the literature published between 1997 and 2006... The applications cover a broad range including selection, evaluation, benefit-cost analysis, planning and development, priority and ranking, and resource allocation."
> - *Simanavičienė a Vdovinskienė (2023, s. 1)*: „The paper aims to evaluate and select the most appropriate software package... using the Analytic Hierarchy Process..."

---

Typický postup AHP lze shrnout do několika kroků. Nejprve je vymezen cíl rozhodování a sestavena hierarchie kritérií a alternativ. Poté se provedou párová porovnání kritérií vzhledem k cíli a párová porovnání alternativ vzhledem ke každému kritériu. Z těchto porovnání se vypočítají lokální priority, ověří se konzistence úsudků a nakonec se lokální váhy agregují do celkového pořadí alternativ (Saaty, 1990; Saaty, 2008; Ishizaka a Labib, 2011).
****
Typický postup AHP lze shrnout do několika kroků. Nejprve je vymezen cíl rozhodování a sestavena hierarchie kritérií a alternativ (Saaty, 2008). Potom se provedou párová porovnání kritérií vzhledem k cíli a párová porovnání alternativ vzhledem ke každému kritériu (Saaty, 1990). Z těchto porovnání se vypočítají lokální priority, ověří se konzistence úsudků. Nakonec se lokální váhy agregují do celkového pořadí alternativ (Ishizaka a Labib, 2011; Saaty, 2008).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Typický postup AHP lze shrnout do několika kroků."**
>
> - *Ishizaka a Labib (2011, s. 444)*: „The AHP process can be summarised in the following steps: (1) model the problem as a hierarchy... (2) collect pairwise comparison data... (3) compute the local priorities... (4) check the consistency... (5) aggregate..."
> - *Saaty (2008, s. 84)*: „The steps of AHP are: define the problem and determine the goal; structure the decision hierarchy; construct a set of pairwise comparison matrices; synthesize the judgements to yield a set of priorities."
> - *Saaty (1990, s. 13)*: „First, structure the problem into a hierarchy. Next, construct pairwise comparison matrices. Then, synthesize the judgments..."

---

## 7.1 Saatyho škála a párové porovnání

Při párovém porovnávání se používá Saatyho škála. Základní hodnoty této škály jsou 1, 3, 5, 7 a 9, přičemž vyjadřují stejnou důležitost, mírnou, silnou, velmi silnou až absolutní preferenci. Sudé hodnoty 2, 4, 6, 8 lze chápat jako mezistupně. Pokud je jeden prvek méně významný než druhý, použije se převrácená hodnota. Hodnota 1 tedy znamená rovnocennost dvou prvků, zatímco hodnota 9 vyjadřuje krajní převahu jednoho prvku nad druhým (Saaty, 1990; Saaty, 2008).
****
Při párovém porovnávání se používá Saatyho škála. Základní hodnoty této škály jsou 1, 3, 5, 7 a 9, přičemž vyjadřují stejnou důležitost, mírnou, silnou, velmi silnou až absolutní preferenci (Saaty, 1990; Saaty, 2008). Sudé hodnoty 2, 4, 6, 8 jsou chápány jako mezistupně. Pokud je jeden prvek méně významný než druhý, použije se převrácená hodnota (Ishizaka a Labib, 2011; Saaty, 1990). Hodnota 1 tedy znamená rovnocennost dvou prvků, zatímco hodnota 9 vyjadřuje krajní převahu jednoho prvku nad druhým.
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Základní hodnoty Saatyho škály jsou 1, 3, 5, 7 a 9, přičemž vyjadřují stejnou důležitost, mírnou, silnou, velmi silnou až absolutní preferenci."**
>
> - *Saaty (2008, s. 86)*: „Table 1 shows the fundamental scale of absolute numbers... 1 - Equal importance... 3 - Moderate importance... 5 - Strong importance... 7 - Very strong... 9 - Extreme..."
> - *Saaty (1990, s. 13)*: „Table 1: The Fundamental Scale... 1 Equal importance, 3 Moderate importance, 5 Strong importance, 7 Very strong importance, 9 Extreme importance, with 2, 4, 6, 8 as intermediate values."
>
> **„Pokud je jeden prvek méně významný než druhý, použije se převrácená hodnota."**
>
> - *Saaty (1990, s. 13)*: „Reciprocals of above: If activity i has one of the above nonzero numbers assigned to it when compared with activity j, then j has the reciprocal value when compared with i."
> - *Ishizaka a Labib (2011, s. 445)*: „The matrix is reciprocal... if element A is preferred with intensity X, then B is preferred with intensity 1/X."

---

Výsledkem párového porovnání je čtvercová reciproční matice, označovaná jako Saatyho matice. Reciproční povaha matice znamená, že pokud je prvek A vůči prvku B hodnocen hodnotou 5, pak opačné porovnání B vůči A má hodnotu 1/5. Hlavní diagonála matice obsahuje hodnoty 1, protože každý prvek je sám se sebou stejně důležitý (Saaty, 1990).
****
Výsledkem párového porovnání je čtvercová reciproční matice, označovaná jako Saatyho matice (Saaty, 1990). Reciproční povaha matice znamená, že pokud je prvek A vůči prvku B hodnocen hodnotou 5, pak opačné porovnání B vůči A má hodnotu 1/5 (Ishizaka a Labib, 2011; Saaty, 2008). Hlavní diagonála matice obsahuje hodnoty 1, protože každý prvek je sám se sebou stejně důležitý.
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Výsledkem párového porovnání je čtvercová reciproční matice."**
>
> - *Saaty (1990, s. 13)*: „We construct the pairwise comparison matrix $A = (a_{ij})$ such that $a_{ij} > 0$ and $a_{ji} = 1/a_{ij}$ (reciprocal condition), and $a_{ii} = 1$."
>
> **„Reciproční povaha matice znamená, že pokud je prvek A vůči prvku B hodnocen hodnotou 5, pak opačné porovnání B vůči A má hodnotu 1/5."**
>
> - *Saaty (2008, s. 85)*: „If element A has one of the above numbers assigned to it when compared with element B, then B has the reciprocal value when compared with A."
> - *Ishizaka a Labib (2011, s. 445)*: „The matrix is reciprocal, meaning $a_{ij} = 1/a_{ji}$."

---

Z této matice se následně vypočítají lokální váhy. V literatuře se používá více postupů výpočtu, například metoda vlastního vektoru nebo výpočet založený na geometrickém průměru řádků. Výsledkem je vektor priorit, jehož hodnoty vyjadřují relativní význam porovnávaných prvků. U kritérií tyto hodnoty představují jejich váhy, u alternativ pak jejich lokální hodnocení vzhledem ke konkrétnímu kritériu (Saaty, 2008; Ishizaka a Labib, 2011).
****
Z této matice se následně vypočítají lokální váhy. V odborné literatuře se objevují různé způsoby výpočtu AHP. Například postup založený na vlastním vektoru nebo metoda využívající geometrický průměr řádků (Ishizaka a Labib, 2011; Saaty, 1990). Výsledkem výpočtu je vektor priorit. Hodnoty vektoru priorit vyjadřují relativní význam porovnávaných prvků (Saaty, 1990; Saaty, 2008). U kritérií tyto hodnoty představují jejich váhy, u alternativ pak jejich lokální hodnocení vzhledem ke konkrétnímu kritériu.
****

> **Zdrojové úryvky k odstavci výše**
>
> **„V literatuře se používá více postupů výpočtu, například metoda vlastního vektoru nebo výpočet založený na geometrickém průměru řádků."**
>
> - *Saaty (1990, s. 13)*: „To derive the priority vector from a pairwise comparison matrix, Saaty proposed using the principal eigenvector of the matrix."
> - *Ishizaka a Labib (2011, s. 445)*: „An alternative approach to compute the priority vector is the geometric mean method (GMM)... calculating the geometric mean of each row and then normalising the results."
>
> **„Výsledkem je vektor priorit, jehož hodnoty vyjadřují relativní význam porovnávaných prvků."**
>
> - *Saaty (2008, s. 86)*: „The resulting priority vector gives the relative importance of the elements being compared."
> - *Saaty (1990, s. 15)*: „Priorities are numbers associated with the nodes of an AHP hierarchy."

---

Pro tuto práci je důležité, že párové porovnávání umožňuje hodnotiteli vyjadřovat preference postupně a přehledně. Místo přímého přiřazení přesných vah všem kritériím hodnotitel vždy posuzuje pouze dvojici prvků. To je užitečné zejména u kritérií, která nejsou přímo měřitelná, například přehlednost prostředí nebo kvalita podpory modelování (Saaty, 2008; Simanavičienė a Vdovinskienė, 2023).
****
Pro tuto práci je důležité, že párové porovnávání umožňuje hodnotiteli vyjadřovat preference postupně a přehledně. Místo toho, aby musel hned přímo přiřazovat přesné váhy všem kritériím, posuzuje vždy jen dvojici prvků a rozhoduje, který z nich je vzhledem k danému cíli nebo kritériu důležitější (Saaty, 2008). To je užitečné zejména u kritérií, která nejsou přímo měřitelná, například přehlednost prostředí nebo kvalita podpory modelování (Saaty, 1990; Simanavičienė a Vdovinskienė, 2023).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Místo přímého přiřazení přesných vah všem kritériím hodnotitel vždy posuzuje pouze dvojici prvků."**
>
> - *Saaty (2008, s. 85)*: „In making the judgements, one compares two elements at a time... this reduces the complexity of the decision and allows for a more focused and consistent assessment."
>
> **„To je užitečné zejména u kritérií, která nejsou přímo měřitelná."**
>
> - *Saaty (1990, s. 10)*: „The AHP is a method for structuring, representing, and solving decision problems... It can handle tangible and intangible criteria..."
> - *Simanavičienė a Vdovinskienė (2023, s. 1)*: „The paper aims to evaluate and select the most appropriate software package... using the Analytic Hierarchy Process..."

---

## 7.2 Kontrola konzistence

Protože párové porovnávání vychází z lidského úsudku, není vždy dokonale konzistentní. Součástí metody AHP je proto kontrola konzistence. K tomu slouží *Consistency Index* (CI), *Random Consistency Index* (RI) a *Consistency Ratio* (CR). V praxi se uvádí, že hodnota CR menší než 0,1 značí přijatelnou úroveň konzistence; vyšší hodnoty obvykle vedou k přehodnocení porovnání (Saaty, 1990; Saaty, 2008).
****
Protože párové porovnávání vychází z lidského úsudku, není vždy dokonale konzistentní. Součástí metody AHP je proto kontrola konzistence. K tomu slouží *Consistency Index* (CI), *Random Consistency Index* (RI) a *Consistency Ratio* (CR) (Ishizaka a Labib, 2011; Saaty, 1990). V praxi se uvažuje, že hodnota CR menší než 0,1 značí přijatelnou úroveň konzistence. Vyšší hodnoty konzistence obvykle vedou k přehodnocení porovnání (Saaty, 1990; Saaty, 2008).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„K tomu slouží Consistency Index (CI), Random Consistency Index (RI) a Consistency Ratio (CR)."**
>
> - *Saaty (1990, s. 13)*: „The consistency index is $CI = (\lambda_{max} - n)/(n - 1)$... The consistency ratio is $CR = CI / RI$."
> - *Ishizaka a Labib (2011, s. 446)*: „The consistency ratio (CR) measures how consistent the judgements have been relative to large samples of purely random judgements... If CR is less than 0.1, the judgments are acceptable."
>
> **„V praxi se uvádí, že hodnota CR menší než 0,1 značí přijatelnou úroveň konzistence."**
>
> - *Saaty (1990, s. 13)*: „If the ratio (called the consistency ratio CR) of CI to that from random matrices is significantly small (carefully specified to be about 10% or less), we accept the estimate of w. Otherwise, we accept that there is inconsistency."
> - *Saaty (2008, s. 87)*: „A consistency ratio of 0.10 or less is considered acceptable."

---

Konzistence znamená, že jednotlivé úsudky by si neměly navzájem odporovat. Pokud je například kritérium A výrazně důležitější než kritérium B a kritérium B je důležitější než kritérium C, potom by mělo být kritérium A zároveň důležitější než kritérium C. Menší odchylky jsou při rozhodování přirozené, příliš vysoká nekonzistence však snižuje důvěryhodnost výsledků (Ishizaka a Labib, 2011; Saaty, 2008).
****
Konzistence ověřuje, zda jsou jednotlivé úsudky hodnotící osoby vzájemně logické a v souladu a zda si jednotlivé úsudky navzájem neodporují (Ishizaka a Labib, 2011; Saaty, 2008). Pokud je například kritérium A výrazně důležitější než kritérium B a kritérium B je důležitější než kritérium C, potom by mělo být kritérium A zároveň důležitější než kritérium C. Menší odchylky jsou při rozhodování přirozené, příliš vysoká nekonzistence však snižuje důvěryhodnost výsledků (Saaty, 1990; Saaty, 2008).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Konzistence znamená, že jednotlivé úsudky by si neměly navzájem odporovat."**
>
> - *Saaty (2008, s. 87)*: „A matrix of comparisons is consistent if $a_{ik} = a_{ij} \cdot a_{jk}$ for all $i, j, k$."
> - *Ishizaka a Labib (2011, s. 446)*: „Perfect consistency requires that if A is preferred to B with intensity 3 and B to C with intensity 2, then A should be preferred to C with intensity 6."
>
> **„Menší odchylky jsou při rozhodování přirozené, příliš vysoká nekonzistence však snižuje důvěryhodnost výsledků."**
>
> - *Saaty (2008, s. 87)*: „Some inconsistency is inevitable in human judgment; the purpose of the CR is to distinguish between an acceptable level of inconsistency and one that leads to unreliable priorities."
> - *Saaty (1990, s. 13)*: „We must expect some inconsistency, but we must make sure it is not too large..."

---

Možnost kontroly konzistence je jedním z důvodů, proč je AHP pro tuto práci vhodnější než jednodušší bodovací postup. Při hodnocení databázových nástrojů bude část úsudků založena na kvalitativním posouzení, například u použitelnosti nebo přehlednosti práce s modelem. Ukazatel CR umožňuje ověřit, zda jsou tato porovnání vnitřně soudržná, a případně se k problematickým porovnáním vrátit (Saaty, 1990; Ishizaka a Labib, 2011).
****
Možnost ověřit konzistenci je například důvodem, proč je AHP pro tuto práci vhodnější než jednodušší bodovací postup. Při hodnocení databázových nástrojů bude část úsudků založena na kvalitativním posouzení, například u použitelnosti nebo přehlednosti práce s modelem. Ukazatel CR umožňuje ověřit, zda jsou tato porovnání vnitřně soudržná, a případně se k problematickým porovnáním vrátit (Ishizaka a Labib, 2011; Saaty, 1990; Saaty, 2008).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Ukazatel CR umožňuje ověřit, zda jsou tato porovnání vnitřně soudržná, a případně se k problematickým porovnáním vrátit."**
>
> - *Saaty (1990, s. 13)*: „If the CR exceeds 0.10, the decision maker should revise his or her pairwise comparisons."
> - *Ishizaka a Labib (2011, s. 446)*: „If the CR exceeds 0.1, the decision maker should revise the pairwise comparisons to improve consistency."
> - *Saaty (2008, s. 87)*: „If the CR is much larger than 0.10, we must take steps to improve consistency by revising the comparisons."

---

## 7.3 Výhody a omezení AHP

Výhodou AHP je možnost kombinovat kvantitativní i kvalitativní kritéria a transparentně zdůvodnit, jak bylo dosaženo výsledného pořadí alternativ. Metoda současně umožňuje analýzu citlivosti, tedy sledování dopadu změny vah kritérií na výsledné pořadí. To je důležité zejména tehdy, když jsou výsledky citlivé na malé změny preferencí a kdy je třeba ověřit stabilitu doporučení (Saaty, 2008; Ishizaka a Labib, 2011; Ho, 2008).
****
Výhodou metody AHP je možnost kombinovat kvantitativní i kvalitativní kritéria a zdůvodnit, jak bylo dosaženo výsledného pořadí alternativ (Ishizaka a Labib, 2011; Vaidya a Kumar, 2006). Metoda současně umožňuje analýzu citlivosti, tedy sledování dopadu změny vah kritérií na výsledné pořadí (Ho, 2008; Saaty, 2008). To je důležité zejména tehdy, když jsou výsledky citlivé na malé změny preferencí a kdy je třeba ověřit stabilitu doporučení.
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Výhodou AHP je možnost kombinovat kvantitativní i kvalitativní kritéria a transparentně zdůvodnit výsledné pořadí alternativ."**
>
> - *Vaidya a Kumar (2006, s. 1)*: „AHP is an effective tool for dealing with complex decision making [...] It reduces complex decisions to a series of pairwise comparisons, and then synthesizes the results."
> - *Ishizaka a Labib (2011, s. 444)*: „One of the advantages of AHP is that it can handle both tangible and intangible criteria and provides an explicit rationale for the final ranking."
>
> **„Metoda současně umožňuje analýzu citlivosti, tedy sledování dopadu změny vah kritérií na výsledné pořadí."**
>
> - *Saaty (2008, s. 88)*: „Sensitivity analysis allows the decision maker to examine how the final ranking changes when the weights of the criteria change."
> - *Ho (2008, s. 213)*: „Sensitivity analysis is often performed to examine the stability of the results under different weighting scenarios."

---

Nevýhodou je vyšší pracnost při větším počtu kritérií a alternativ a určitá míra subjektivity, která je s párovým porovnáváním spjata. Pokud je v modelu mnoho prvků, počet potřebných porovnání rychle roste a hodnotitel může být zatížen opakováním podobných rozhodnutí. Proto je vhodné udržet počet kritérií i alternativ v přiměřeném rozsahu a jasně vymezit význam jednotlivých kritérií (Saaty, 2008; Ishizaka a Labib, 2011).
****
Nevýhodou metody je pracnost při větším počtu kritérií a alternativ a jistá míra subjektivity, která je s párovým porovnáváním spojena (Ishizaka a Labib, 2011; Saaty, 2008). Pokud je v modelu mnoho prvků, počet potřebných porovnání rychle roste.  Hodnotitel pak může být zatížen opakováním podobných rozhodnutí (Ishizaka a Labib, 2011). Proto je vhodné udržet počet kritérií i alternativ v přiměřeném rozsahu a jasně vymezit význam jednotlivých kritérií.
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Nevýhodou je vyšší pracnost při větším počtu kritérií a alternativ."**
>
> - *Ishizaka a Labib (2011, s. 444)*: „For n elements, n(n−1)/2 comparisons need to be made. As the number of elements increases, the number of pairwise comparisons increases rapidly, which can be burdensome for the decision maker."
> - *Saaty (2008, s. 85)*: „The judgements in AHP are subjective, reflecting the experience and values of the decision maker."
> - *Vaidya a Kumar (2006, s. 1)*: „It reduces complex decisions to a series of pairwise comparisons..."

---

V literatuře se v souvislosti s AHP diskutuje také jev tzv. rank reversal, tedy možná změna pořadí alternativ při přidání nebo odebrání varianty z modelu. Tento problém neznamená, že AHP nelze použít, ale ukazuje, že výsledky je třeba interpretovat s ohledem na zvolený soubor alternativ a nastavení modelu. U navazující praktické části proto bude důležité jasně zdůvodnit, proč byly vybrány právě dané nástroje a jaké požadavky reprezentují (Saaty, 2008; Vaidya a Kumar, 2006).
****
V odborné literatuře se diskutuje jev *rank reversal*, tedy možná změna pořadí alternativ při přidání nebo odebrání varianty z modelu (Ishizaka a Labib, 2011; Saaty, 2008; Vaidya a Kumar, 2006). Tento problém neznamená, že AHP nelze použít, ale ukazuje, že výsledky je třeba interpretovat s ohledem na zvolený soubor alternativ a nastavení modelu. U navazující praktické části proto bude důležité jasně zdůvodnit, proč byly vybrány právě dané nástroje a jaké požadavky reprezentují.
****

> **Zdrojové úryvky k odstavci výše**
>
> **„V literatuře se v souvislosti s AHP diskutuje jev tzv. rank reversal, tedy možná změna pořadí alternativ při přidání nebo odebrání varianty z modelu."**
>
> - *Vaidya a Kumar (2006, s. 1)*: „One of the main criticisms of AHP is the phenomenon of rank reversal — the ranking of alternatives can change when a new alternative is added or an existing one is removed."
> - *Saaty (2008, s. 88)*: „Rank reversal can occur when a new alternative is introduced or removed from the set..."
> - *Ishizaka a Labib (2011, s. 450)*: „Rank reversal is the change in the relative ranking of alternatives when a new alternative is added or deleted."

---

V kontextu výběru databázového nástroje je AHP přínosná také tím, že umožňuje oddělit váhy kritérií od hodnocení alternativ. Nejprve lze stanovit, jak důležitá je například funkcionalita, použitelnost, kompatibilita, cena nebo podpora vývojového procesu, a teprve poté hodnotit jednotlivé nástroje vůči těmto kritériím. Díky tomu je výsledek lépe kontrolovatelný než prosté celkové dojmové hodnocení softwaru (Saaty, 1990; Simanavičienė a Vdovinskienė, 2023).
****
V kontextu výběru databázového nástroje je AHP přínosná tím, že umožní oddělit stanovení vah kritérií od samotného hodnocení alternativ. Nejprve lze stanovit, jak důležitá je například funkcionalita, použitelnost, kompatibilita, cena nebo podpora vývojového procesu, a teprve poté hodnotit jednotlivé nástroje vůči těmto kritériím (Saaty, 1990). Díky tomu je výsledek lépe kontrolovatelný než prosté celkové dojmové hodnocení softwaru (Simanavičienė a Vdovinskienė, 2023).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„AHP umožňuje oddělit váhy kritérií od hodnocení alternativ."**
>
> - *Saaty (1990, s. 13)*: „The AHP first determines the weights of the criteria through pairwise comparisons with respect to the goal, and then evaluates the alternatives with respect to each criterion separately."
> - *Simanavičienė a Vdovinskienė (2023, s. 1)*: „The paper aims to evaluate and select the most appropriate software package... using the Analytic Hierarchy Process..."
> - *Ebrahimi a Taheri (2015, s. 1)*: „...selection of Database Management System using Analytic Hierarchy Process..."

# 8 Nástroje pro návrh a vývoj databází

Výběr nástrojů pro porovnání vycházel nejprve z přehledu dostupných nástrojů pro návrh a vývoj databází. Jako jeden z podkladů byla využita studie Carvalho et al. (2022), která hodnotila sedmnáct nástrojů pro datové modelování. V této studii je vidět, že nabídka těchto nástrojů je velmi široká a obsahuje nástroje online i desktopové, bezplatné i komerční a také nástroje zaměřené na různé databázové platformy. Příkladem online nástroje je ONDA vyvinutý na Univerzitě v Coimbře (Laranjeiro a Pinto, 2024); do užšího výběru však zařazen nebyl, protože práce se soustředí na plnohodnotné desktopové nástroje. Dalším podkladem byly oficiální online dokumentace vybraných nástrojů, ze kterých byly ověřeny jejich základní funkce, podporované databázové platformy a licenční podmínky. Pro posouzení významu jednotlivých databázových platforem byl využit také žebříček DB-Engines (2026).

Na základě těchto podkladů byly pro další práci vybrány čtyři nástroje: Oracle SQL Developer Data Modeler, DBeaver Community Edition, MySQL Workbench Community Edition a pgModeler. Při výběru bylo zohledněno, zda nástroj podporuje návrh databáze, zda je dostupný v bezplatné nebo volně testovatelné verzi a zda vhodně doplňuje ostatní vybrané nástroje. Oracle SQL Developer Data Modeler je zaměřený hlavně na Oracle Database, MySQL Workbench na MySQL, pgModeler na PostgreSQL a DBeaver představuje univerzálnější nástroj podporující více DBMS. Tři z těchto nástrojů jsou uvedeny také ve studii Carvalho et al. (2022). Díky tomu bude možné pozdější výsledky alespoň částečně porovnat s již publikovanou studií.

Volba databázových platforem vychází také z jejich rozšířenosti. Oracle Database, MySQL a PostgreSQL patří podle žebříčku DB-Engines (2026) mezi významné relační databázové systémy. Do úvahy byl brán i Microsoft SQL Server, ten však nebyl zařazen, protože pro zvolený postup práce lépe odpovídají nástroje dostupné bezplatně nebo ve volně použitelné komunitní verzi. U univerzálních nástrojů bude při hodnocení sledováno také to, zda umožňují práci s více databázovými platformami, případně i s nerelačními databázemi.

Základní charakteristiky vybraných nástrojů shrnuje tabulka 1.

| Nástroj | Vydavatel | Licence | Primární DBMS | Klíčové funkce |
|---|---|---|---|---|
| Oracle SQL Developer Data Modeler | Oracle Corporation | Freeware | Oracle Database | Logický, relační, fyzický a multidimenzionální model; forward/reverse engineering |
| DBeaver Community Edition | DBeaver Corp. | Open-source (Apache 2.0) | Multi-DBMS | ER diagramy, SQL editor, prohlížeč dat, DDL export |
| MySQL Workbench Community Edition | Oracle Corporation | Open-source (GPLv2) | MySQL | EER modelování, forward/reverse engineering, synchronizace s živou databází |
| pgModeler | Raphael Araújo e Silva | Open-source (GPLv3) | PostgreSQL | Grafický návrh schémat, generování SQL, reverzní inženýrství, validace modelu |

*Tabulka 1 – Základní charakteristiky vybraných nástrojů (zdroje: Oracle, 2026; DBeaver, 2026; MySQL, 2026; pgModeler, 2026)*

## 8.1 Oracle SQL Developer Data Modeler

Oracle SQL Developer Data Modeler je bezplatný grafický nástroj společnosti Oracle pro modelování dat. Podporuje logické, relační, fyzické, multidimenzionální a typové modely, nabízí forward i reverse engineering a integraci se širším portfoliem Oracle SQL Developer. Jako primární databázová platforma je preferován Oracle Database, nástroj však umožňuje pracovat i s dalšími systémy (Oracle, 2026). Pro účely této práce bude testována verze 24.3.

## 8.2 DBeaver Community Edition

DBeaver je open-source univerzální databázový nástroj s podporou širokého spektra DBMS (PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, SQLite a další). Nabízí editor SQL, prohlížeč dat, vizualizaci databázových struktur pomocí ER diagramů a generování DDL skriptů. Pokročilejší funkce, například datové generátory nebo vizuální dotazování, jsou dostupné v komerční edici (DBeaver, 2026). Pro účely této práce bude testována verze 26.0 Community Edition.

## 8.3 MySQL Workbench Community Edition

MySQL Workbench je oficiální nástroj společnosti Oracle pro práci s databází MySQL. Sjednocuje v jednom prostředí návrh databáze (EER diagramy), správu serveru, modelování, forward i reverse engineering a SQL vývoj. Podporuje synchronizaci modelu s živou databází a export modelu do DDL skriptu (MySQL, 2026). Pro účely této práce bude testována verze 8.0.

## 8.4 pgModeler

pgModeler, jehož název vychází z označení PostgreSQL Database Modeler, je open-source nástroj zaměřený přímo na databázi PostgreSQL. Umožňuje grafický návrh schémat, generování SQL skriptů, reverzní inženýrství, validaci modelu a porovnávání modelu s živou databází (pgModeler, 2026). Cílovou databázovou platformou nástroje je PostgreSQL, jehož oficiální dokumentace popisuje podporované datové typy a syntaxi SQL, vůči nimž pgModeler generované skripty validuje (PostgreSQL, 2026). Pro účely této práce bude testována aktuální stabilní verze ke dni testování.

# 9 Návrh hodnoticích kritérií

Při vytváření kritérií pro hodnocení je potřeba zohlednit, že nástroje budou porovnávány podle toho, jak dokážou podpořit návrh a vývoj databáze, nikoliv pouze podle toho, jak zvládají její provoz a správu. Hodnoticí kritéria vycházejí ze studie Carvalho et al. (2022). Tato práce porovnávala nástroje pro datové modelování podle kategorií jako: funkcionalita, provozní vlastnosti softwaru, dokumentace a komunitní podpora. Tato práce toto členění přebírá a rozšiřuje ho o kritéria specifická pro návrh databázových systémů. U kritérií, která nejdou vyjádřit číselně, se použije kvalitativní hodnocení podle zkušenosti a každé porovnání se krátce zdůvodní.

Přehled osmi navržených pracovních kritérií uvádí tabulka 2.

| ID | Název kritéria | Typ kritéria | Způsob a zdroj hodnocení |
|---|---|---|---|
| K1 | Funkcionalita | maximalizační | testovací scénář a dokumentace nástroje |
| K2 | Použitelnost | maximalizační | kvalitativní hodnocení v testovacím scénáři |
| K3 | Kompatibilita s DBMS | maximalizační | počet oficiálně podporovaných DBMS |
| K4 | Forward engineering | maximalizační | testovací scénář (generování DDL) |
| K5 | Reverse engineering | maximalizační | testovací scénář (import z existující DB) |
| K6 | Dokumentace a komunitní podpora | maximalizační | kvalitativní hodnocení |
| K7 | Import a export modelu | maximalizační | testovací scénář a podporované formáty |
| K8 | Cena a licence | minimalizační | typ licence, omezení bezplatné verze, celková cena |

*Tabulka 2 – Přehled navržených hodnoticích kritérií (vlastní zpracování na základě Carvalho et al., 2022)*

Význam jednotlivých kritérií je blíže popsán níže.

**K1 Funkcionalita.** Rozsah funkcí nástroje — typy modelů (konceptuální, logický, fyzický), validace, dokumentace a podpora objektů jako tabulky, pohledy, indexy nebo triggery.

**K2 Použitelnost.** Vyjadřuje, jak snadno se s nástrojem pracuje – jak rychle se v něm uživatel zorientuje, nakolik je prostředí editoru modelu přehledné a jak náročné je provést běžné úkony.

**K3 Kompatibilita s DBMS.** Udává, kolik databázových systémů nástroj oficiálně podporuje.

**K4 Forward engineering.** Sleduje, jak nástroj generuje DDL skript nebo schéma databáze z navrženého modelu.

**K5 Reverse engineering.** Týká se schopnosti nástroje sestavit model z již existující databáze.

**K6 Dokumentace a komunitní podpora.** Posuzuje rozsah a aktuálnost oficiální dokumentace i dostupnost komunitní podpory a aktualizací.

**K7 Import a export modelu.** Zaměřuje se na podporované formáty importu a exportu a na propojení s verzovacími systémy.

**K8 Cena a licence.** Bere v úvahu typ licence (open source, freeware, komerční), omezení bezplatné verze a celkové náklady na zavedení.

# 10 Závěry a doporučení

Cíl práce, tedy zpracování teoretických a metodických východisek pro praktickou část, byl naplněn. Odpovědi na výzkumné otázky lze stručně shrnout takto:

- **K VO1:** Byly vymezeny klíčové pojmy databázových systémů (data, DBMS, schéma, instance, metadata), popsány fáze návrhu databáze (konceptuální, logický, fyzický) a vysvětleny datové modely používané v praxi, zejména ER/EER a relační model spolu s normalizací.
- **K VO2:** Metoda AHP byla popsána jak z hlediska principu (hierarchie cíl–kritéria–alternativy), tak z hlediska postupu (párové porovnání s využitím Saatyho škály, výpočet vah, kontrola konzistence pomocí CR). Bylo zdůvodněno, proč je AHP vhodná pro porovnání softwarových nástrojů.
- **K VO3:** Bylo navrženo osm hodnoticích kritérií (K1–K8) a metodický rámec navazující komparace, zahrnující sestavení hierarchie, párové porovnání kritérií, testovací scénář nad nainstalovanými nástroji, syntézu priorit a analýzu citlivosti.

Tento navržený teoretický a metodický rámec tvoří přímý základ pro navazující praktickou komparaci v bakalářské práci. Pro realizaci této praktické části se doporučuje: a) provést testovací scénář na všech čtyřech nástrojích v jednom kalendářním týdnu, aby se minimalizovaly rozdíly ve zkušenostech hodnotitele; b) při hodnocení kvalitativních kritérií (K2, K6) doplnit slovní zdůvodnění každého párového porovnání; c) zařadit analýzu citlivosti minimálně pro váhy K1 a K8; d) zvážit modelový scénář dvou typových firem (malé a střední) s odlišnými váhami kritérií a porovnat výsledné pořadí mezi scénáři. Vedle toho bude v bakalářské práci detailně rozpracován jednotný testovací scénář a případný výpočet vah v excelovém modelu či jednoduché podpůrné aplikaci.


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Seznam zdrojů

## Tištěné zdroje

CARVALHO, Gonçalo, Sergii MYKOLYSHYN, Bruno CABRAL, Jorge BERNARDINO a Vasco PEREIRA. Comparative Analysis of Data Modeling Design Tools. *IEEE Access*. 2022, **10**, 3351-3365. ISSN 2169-3536. DOI: 10.1109/ACCESS.2021.3139071.

CHEN, Peter Pin-Shan. The entity-relationship model—toward a unified view of data. *ACM Transactions on Database Systems*. 1976, **1**(1), 9–36. ISSN 0362-5915. DOI: 10.1145/320434.320440.

CHLAPEK, Dušan, Jan KUČERA a Helena PALOVSKÁ. *Datové modelování a návrh relační databáze: Sbírka řešených úloh*. Praha: Vysoká škola ekonomická v Praze, Nakladatelství Oeconomica, 2019. ISBN 978-80-245-2331-6.

CODD, Edgar F. A relational model of data for large shared data banks. *Communications of the ACM*. 1970, **13**(6), 377–387. ISSN 0001-0782. DOI: 10.1145/362384.362685.

ELMASRI, Ramez a Shamkant B. NAVATHE. *Fundamentals of Database Systems*. 7th ed. Boston: Pearson, 2016. ISBN 978-0-13-397077-7.

HO, William. Integrated analytic hierarchy process and its applications – a literature review. *European Journal of Operational Research*. 2008, **186**(1), 211–228. ISSN 0377-2217. DOI: 10.1016/j.ejor.2007.01.004.

ISHIZAKA, Alessio a Ashraf LABIB. Review of the main developments in the Analytic Hierarchy Process. *Expert Systems with Applications*. 2011, **38**(11), 14336–14345. ISSN 0957-4174. DOI: 10.1016/j.eswa.2011.04.143.

MARDANI, Abbas, Ahmad JUSOH, Khalil MD NOR, Zainab KHALIFAH, Norhayati ZAKWAN a Alireza VALIPOUR. Multiple criteria decision-making techniques and their applications – a review of the literature from 2000 to 2014. *Economic Research – Ekonomska Istraživanja*. 2015, **28**(1), 516–571. ISSN 1331-677X. DOI: 10.1080/1331677X.2015.1075139.

POKORNÝ, Jaroslav a Michal VALENTA. *Databázové systémy*. Praha: České vysoké učení technické v Praze, 2020. ISBN 978-80-01-06708-6.

ROSENTHAL, Arnon a David REINER. Tools and Transformations — Rigorous and Otherwise — for Practical Database Design. *ACM Transactions on Database Systems*. 1994, **19**(2), 167-211. ISSN 0362-5915. DOI: 10.1145/176567.176568.

SAATY, Thomas L. How to make a decision: The Analytic Hierarchy Process. *European Journal of Operational Research*. 1990, **48**(1), 9-26. ISSN 0377-2217.

SAATY, Thomas L. Decision making with the analytic hierarchy process. *International Journal of Services Sciences*. 2008, **1**(1), 83-98. ISSN 1753-1454.

SIMANAVIČIENĖ, Rūta a Sonata VDOVINSKIENĖ. Selection of Computer-Aided Design Software Systems Using the AHP Method. *Baltic Journal of Modern Computing*. 2023, **11**(2), 272-284. ISSN 2255-8950. DOI: 10.22364/bjmc.2023.11.2.04.

VAIDYA, Omkarprasad S. a Sushil KUMAR. Analytic hierarchy process: An overview of applications. *European Journal of Operational Research*. 2006, **169**(1), 1–29. ISSN 0377-2217. DOI: 10.1016/j.ejor.2004.04.028.

VELASQUEZ, Mark a Patrick T. HESTER. An Analysis of Multi-Criteria Decision Making Methods. *International Journal of Operations Research*. 2013, **10**(2), 56–66. ISSN 1813-713X.

## Internetové zdroje

DBEAVER. *DBeaver Documentation* [online]. DBeaver Corp., 2026 [cit. 2026-06-09]. Dostupné z: <https://dbeaver.com/docs/dbeaver/>

DB-ENGINES. *DB-Engines Ranking* [online]. solid IT gmbh, 2026 [cit. 2026-06-14]. Dostupné z: <https://db-engines.com/en/ranking>

LARANJEIRO, Nuno a Alexandre Miguel PINTO. *ONDA: ONLine Database Architect* [online]. arXiv:2401.16552, 2024 [cit. 2026-06-15]. DOI: 10.48550/arXiv.2401.16552. Dostupné z: <https://doi.org/10.48550/arXiv.2401.16552>

MYSQL. *MySQL Workbench Manual* [online]. Oracle Corporation, 2026 [cit. 2026-06-09]. Dostupné z: <https://dev.mysql.com/doc/workbench/en/>

ORACLE. *Oracle SQL Developer Data Modeler* [online]. Oracle Corporation, 2026 [cit. 2026-06-09]. Dostupné z: <https://www.oracle.com/database/sqldeveloper/technologies/sql-data-modeler/>

PGMODELER. *pgModeler – PostgreSQL Database Modeler* [online]. Raphael Araújo e Silva, 2026 [cit. 2026-06-09]. Dostupné z: <https://pgmodeler.io/>

POSTGRESQL. *PostgreSQL Documentation* [online]. The PostgreSQL Global Development Group, 2026 [cit. 2026-06-09]. Dostupné z: <https://www.postgresql.org/docs/>

SOUKOPOVÁ, Jana. *Vícekriteriální metody hodnocení* [online]. Brno: Masarykova univerzita, Ekonomicko-správní fakulta, 2016. Učební text [cit. 2026-06-09]. Dostupné z: <https://is.muni.cz/el/1456/jaro2016/BPE_VIMP/um/>

WATT, Adrienne a Nelson ENG. *Database Design* [online]. 2nd ed. Victoria: BCcampus, 2014 [cit. 2026-06-18]. Dostupné z: <https://opentextbc.ca/dbdesign01/>

## Zdroje nenásledované v textu [potenciálně pro BP]

`[101]` CATAK, F. Ozgur, Servet KARABAS a Serkan YILDIRIM. Fuzzy Analytic Hierarchy Based DBMS Selection in Turkish National Identity Card Management Project. *International Journal of Information Sciences and Techniques*. 2012, **2**(4), 29–38. DOI: 10.5121/ijist.2012.2403. — `literatura/AHP/`

`[102]` EBRAHIMI, M. a M. TAHERI. Selection of Database Management System with Fuzzy-AHP for Electronic Medical Record. *I.J. Information Engineering and Electronic Business*. 2015, (5), 1–6. DOI: 10.5815/ijieeb.2015.05.01. — `literatura/AHP/`
