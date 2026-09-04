# Nástroje pro návrh a vývoj databází

Výběr nástrojů pro porovnání vycházel nejprve z přehledu dostupných nástrojů pro návrh a vývoj databází. Jako jeden z podkladů byla využita studie Carvalho et al. (2022), která hodnotila sedmnáct nástrojů pro datové modelování. Ze studie vyplývá, že nabídka těchto nástrojů je velmi široká a obsahuje nástroje online i desktopové, bezplatné i komerční a také nástroje zaměřené na různé databázové platformy. Příkladem online nástroje je ONDA vyvinutý na Univerzitě v Coimbře (Laranjeiro a Pinto, 2024), který však do výběru zařazen nebyl, protože práce se soustředí na plnohodnotné desktopové nástroje. Dalším podkladem byla oficiální online dokumentace vybraných nástrojů, ze které byly ověřeny jejich základní funkce, podporované databázové platformy a licenční podmínky. Pro posouzení významu jednotlivých databázových platforem byl využit také žebříček DB-Engines (2026).

Na základě těchto podkladů byly pro další práci vybrány čtyři nástroje: Oracle SQL Developer Data Modeler, DBeaver Community Edition, MySQL Workbench Community Edition a pgModeler. Při výběru bylo zohledněno, zda vybraný nástroj podporuje návrh databáze, zda je dostupný v bezplatné nebo volně testovatelné verzi a zda vhodně doplňuje ostatní vybrané nástroje. Oracle SQL Developer Data Modeler je zaměřený hlavně na Oracle Database, MySQL Workbench na MySQL, pgModeler na PostgreSQL a DBeaver představuje univerzálnější nástroj podporující více DBMS. Tři z těchto nástrojů (Oracle SQL Developer Data Modeler, MySQL Workbench a pgModeler) jsou uvedeny také ve studii Carvalho et al. (2022), přičemž pgModeler v jejich hodnocení dosáhl ze všech sedmnácti posuzovaných nástrojů nejlepšího výsledku. DBeaver byl do výběru zařazen navíc jako univerzální nástroj podporující více DBMS, který v původní studii chybí. Díky tomu bude možné pozdější výsledky alespoň částečně porovnat s již publikovanou studií. Volba databázových platforem vychází také z jejich rozšířenosti. Oracle Database, MySQL a PostgreSQL patří podle žebříčku DB-Engines (2026) mezi významné relační databázové systémy. Do úvahy byl brán také Microsoft SQL Server, avšak nakonec nebyl zařazen, protože práce se zaměřuje na nástroje s velkou podporou databázového modelování a zároveň chce zachovat přiměřený počet alternativ pro AHP. U univerzálních nástrojů bude při hodnocení sledováno také to, zda umožňují práci s více databázovými platformami, případně i s nerelačními databázemi.

Základní charakteristiky vybraných nástrojů shrnuje tabulka 1.

| **Nástroj** | **Zaměření** | **Licence** | **Vybrané funkce** |
|:---|:---|:---|:---|
| Oracle SQL Developer Data Modeler | Oracle Database | bezplatný nástroj | logické, relační a fyzické modely, forward a reverse engineering |
| DBeaver Community Edition | více databázových systémů | open-source komunitní edice | SQL vývoj, správa dat, ER diagramy, generování DDL |
| MySQL Workbench Community Edition | MySQL | komunitní edice | EER diagramy, správa serveru, forward a reverse engineering |
| pgModeler | PostgreSQL | open-source / placená distribuce | návrh schémat, SQL export, reverse engineering, validace modelu |

<span id="_Toc234483571" class="anchor"></span>Tabulka 1: Základní charakteristiky vybraných nástrojů (vlastní zpracování podle Oracle, 2026; DBeaver, 2026; MySQL, 2026; pgModeler, 2026)

## Oracle SQL Developer Data Modeler

Oracle SQL Developer Data Modeler je bezplatný grafický nástroj společnosti Oracle pro modelování dat. Podporuje logické, relační, fyzické, multidimenzionální a typové modely, nabízí forward i reverse engineering a integraci se širším portfoliem Oracle SQL Developer. Jako primární databázová platforma je preferována Oracle Database, nástroj však umožňuje pracovat i s dalšími systémy (Oracle, 2026). Pro účely navazující práce bude testována verze 24.3.

## DBeaver Community Edition

DBeaver je open-source univerzální databázový nástroj s podporou širokého spektra DBMS (PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, SQLite a další). Nabízí editor SQL, prohlížeč dat, vizualizaci databázových struktur pomocí ER diagramů a generování DDL skriptů. Pokročilejší funkce, například datové generátory nebo vizuální dotazování, jsou dostupné v komerční edici (DBeaver, 2026). Pro účely navazující práce bude testována verze 26.0 Community Edition.

## MySQL Workbench Community Edition

MySQL Workbench je oficiální nástroj společnosti Oracle pro práci s databází MySQL. Sjednocuje v jednom prostředí návrh databáze (EER diagramy), správu serveru, modelování, forward i reverse engineering a SQL vývoj. Podporuje synchronizaci modelu s živou databází a export modelu do DDL skriptu (MySQL, 2026). Pro účely navazující práce bude testována verze 8.0.

## pgModeler

pgModeler, jehož název vychází z označení PostgreSQL Database Modeler, je open-source nástroj zaměřený přímo na databázi PostgreSQL. Umožňuje grafický návrh schémat, generování SQL skriptů, reverzní inženýrství, validaci modelu a porovnávání modelu s živou databází (pgModeler, 2026). Cílovou databázovou platformou nástroje je PostgreSQL, jehož oficiální dokumentace popisuje podporované datové typy a syntaxi SQL, vůči nimž pgModeler validuje generované skripty (PostgreSQL, 2026). Pro účely navazující práce bude testována stabilní verze 1.2.3.
