# 4 Databázové systémy

## 4.1 Základní pojmy

Základem je rozlišit pojmy data, informace, databáze a systém řízení báze dat.
Data lze chápat jako jednotlivá fakta nebo zaznamenané hodnoty, které samy o sobě nemusí nést širší význam.
Informace vznikají interpretací dat v určitém kontextu.
Databáze pak představuje organizovanou kolekci vzájemně souvisejících dat, která jsou ukládána tak, aby s nimi bylo možné efektivně pracovat (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Watt a Eng, 2014).

****
Při práci s databázemi je nutné rozlišovat některé základní pojmy jako jsou data, informace, databáze a systém řízení báze dat.
Pod pojmem data si jde představit jednotlivá fakta nebo zaznamenané hodnoty (Elmasri a Navathe, 2016; Watt a Eng, 2014). Tyto hodnoty samy o sobě nemusí být nositelem žádného širšího významu. Informace pak vznikají právě přiřazením významu datům v určitém kontextu. (Elmasri a Navathe, 2016; Watt a Eng, 2014)
Pojem databáze pak představuje organizovanou sbírku vzájemně souvisejících dat, které jsou uloženy tak, aby s nimi bylo možné dále efektivně pracovat. (Elmasri a Navathe, 2016, s. 4; Pokorný a Valenta, 2020; Watt a Eng, 2014).
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
Systém řízení báze dat, běžně označovaný jako DBMS, je specializovaný software, který zajišťuje definici, ukládání, manipulaci, zabezpečení a správu dat uložených v databázi. (Pokorný a Valenta, 2020)
Spojení databáze s DBMS vytvoří databázový systém (DBS). (Elmasri a Navathe, 2016) DBMS v rámci tohoto systému zajišťuje transakční zpracování, obnovení dat po pádu, souběžný přístup více uživatelů i řízení ochrany dat. (Pokorný a Valenta, 2020)
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
Původně se používal především jednoduchý souborový přístup, který měl však řadu problémů a omezení. Například v podobě nekonzistentnosti dat při aktualizaci, závislosti na aplikačním programu a na fyzické struktuře, často spojené s redundancí dat. (Elmasri a Navathe, 2016) Databázový přístup tyto nedostatky odstraňuje, a to tím, že integruje data do jednoho logického celku a odděluje definici dat od samotných aplikací (Pokorný a Valenta, 2020). Oddělením byla získána vyšší bezpečnost, možnost centrálního řízení integritních omezení a sdílenost dat mezi více uživateli. (Pokorný a Valenta, 2020)
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
Schéma databáze představuje popis struktury uložených dat, zahrnuje určení entit, atributů, vazeb a integritních omezení, která mají data splňovat. (Pokorný a Valenta, 2020)
Pojem instance databáze naopak vyjadřuje konkrétní aktuální obsah databáze v určitém čase.
Toto rozlišení odděluje relativně stabilní strukturální návrh od proměnlivých datových hodnot. (Elmasri a Navathe, 2016)
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
Metadata jsou data o datech. Tyto data tedy popisují strukturu databáze, význam atributů, integritní omezení nebo například přístupová práva.
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
Správa a údržba schématu databáze je klíčovou rolí správce databáze (DBA), přičemž změny schématu v průběhu životního cyklu systému musí být pečlivě kontrolovány. Metadata uložená v systémovém katalogu jsou využívána nejen samotným DBMS pro optimalizaci dotazů a kontrolu přístupových práv, ale také externími návrhovými nástroji. Tyto nástroje dokážou metadata z katalogu načíst a vizualizovat je ve formě diagramů, což usnadňuje pochopení existující struktury databáze a její další rozvoj (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
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
DBMS obvykle poskytuje několik základních skupin funkcí: definici dat, manipulaci s daty, řízení souběžného přístupu více uživatelů, ochranu dat a obnovu po chybě (Pokorný a Valenta, 2020). V souvislosti s těmito funkcemi se používají pojmy DDL pro jazyk definice dat, DML pro jazyk manipulace s daty a transakce pro logický celek operací, který má být proveden buď celý, nebo vůbec (Elmasri a Navathe, 2016; Watt a Eng, 2014).

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
Dalším důležitým konceptem je víceúrovňová architektura DBMS, která je spojovaná s modelem ANSI/SPARC.
Myšlenkou bylo podívat se na stavbu databáze jako implementaci hierarchie jistých abstrakcí. Ve zprávě výboru ANSI/X3/SPARC z roku 1975 se objevuje rozdělení na externí, konceptuální a interní úroveň pohledu, kde
externí úroveň odpovídá pohledům jednotlivých skupin uživatelů, konceptuální úroveň představuje globální logický model celé databáze a interní úroveň popisuje fyzické uložení dat.
Hlavním smyslem tohoto členění je podpora datové nezávislosti, tedy oddělení aplikací a uživatelských pohledů od fyzické implementace databáze. (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020)
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
Pro následné porovnání nástrojů je tato architektura důležitá proto, že návrhové nástroje nepokrývají všechny úrovně databázového systému stejným způsobem.
(Rosenthal a Reiner, 1994)
Některé se zaměřují především na konceptuální nebo logický model, jiné podporují i fyzické prvky konkrétního DBMS, například datové typy, indexy nebo generování SQL skriptů. (Carvalho et al., 2022)
Při hodnocení nástrojů proto bude vhodné sledovat nejen možnosti vytváření diagramů, ale také podporu přechodu mezi jednotlivými úrovněmi návrhu a implementace
(Rosenthal a Reiner, 1994).
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
V této části se konceptuální model převádí do zvoleného datového modelu, v případě této práce jde zejména o model relační. (Rosenthal a Reiner, 1994)
Dochází k návrhu relací, atributů, klíčů, cizích klíčů a integritních omezení. (Pokorný a Valenta, 2020)
Výsledkem je pak logické schéma databáze, které lze implementovat v konkrétním DBMS. (Pokorný a Valenta, 2020)
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
Řeší se zde organizace datových souborů, indexy, výkonové aspekty, optimalizace přístupu a další technické detaily. (Rosenthal a Reiner, 1994)
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
Mezi jednotlivými částmi návrhu existuje zpětná vazba. Pokud se při fyzickém návrhu ukáže, že některé části modelu vedou například k výkonovým problémům, je nutné vrátit se zpět k návrhu logickému.
Podobně může změna požadavků uživatelů vyvolat úpravu konceptuálního modelu a následně i všech dalších úrovní.
Návrh databáze proto nelze chápat jako striktně lineární proces, nýbrž jako proces iterativní
(Rosenthal a Reiner, 1994).

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
Rozdělení návrhu databáze na konceptuální, logickou a fyzickou úroveň tvoří vhodný výchozí bod pro pozdější definici hodnoticích kritérií.
Nástroj určený pro návrh databázového systému by měl umožnit zachytávat požadavky, převést je do konzistentního schématu a podle potřeby podpořit i technickou implementaci v konkrétním databázovém prostředí. (Rosenthal a Reiner, 1994)
Právě míra podpory těchto kroků představuje jeden z praktických rozdílů mezi porovnávanými nástroji (Carvalho et al., 2022; Rosenthal a Reiner, 1994).
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
