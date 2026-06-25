# 4 Databázové systémy

## 4.1 Základní pojmy

Při práci s databázemi je nutné rozlišovat některé základní pojmy jako jsou data, informace, databáze a systém řízení báze dat.
Pod pojmem data si jde představit jednotlivá fakta nebo zaznamenané hodnoty (Elmasri a Navathe, 2016; Watt a Eng, 2014). Tyto hodnoty samy o sobě nemusí být nositelem žádného širšího významu. Informace pak vznikají právě přiřazením významu datům v určitém kontextu. (Elmasri a Navathe, 2016; Watt a Eng, 2014)
Pojem databáze pak představuje organizovanou sbírku vzájemně souvisejících dat, které jsou uloženy tak, aby s nimi bylo možné dále efektivně pracovat. (Elmasri a Navathe, 2016, s. 4; Pokorný a Valenta, 2020; Watt a Eng, 2014).

Systém řízení báze dat, běžně označovaný jako DBMS, je specializovaný software, který zajišťuje definici, ukládání, manipulaci, zabezpečení a správu dat uložených v databázi. (Pokorný a Valenta, 2020)
Spojení databáze s DBMS vytvoří databázový systém (DBS). (Elmasri a Navathe, 2016) DBMS v rámci tohoto systému zajišťuje transakční zpracování, obnovení dat po pádu, souběžný přístup více uživatelů i řízení ochrany dat. (Pokorný a Valenta, 2020)

Původně se používal především jednoduchý souborový přístup, který měl záhy řadu problémů a omezení napříkald v podobě nekonzistentnosti dat při aktualizaci, závislosti na aplikačním programu a na fyzické struktuře, často spojené s redundancí dat. (Elmasri a Navathe, 2016) Databázový přístup tyto nedostatky odstraňuje, a to tím, že integruje data do jednoho logického celku a odděluje definici dat od samotných aplikací (Pokorný a Valenta, 2020).
Oddělením byla získána vyšší bezpečnost, možnost centrálního řízení integritních omezení a sdílenost dat mezi více uživateli. (Pokorný a Valenta, 2020)

## 4.2 Schéma databáze, instance a metadata

V teorii databází je třeba rozlišovat mezi schématem databáze a instancí databáze.
Schéma databáze představuje popis struktury uložených dat a běžně se pod něj zahrnují také integritní omezení, kteraá obsahují určení entit, atributů, vazeb a omezení, která mají data splňovat.
(Pokorný a Valenta, 2020)
Pojem instance databáze naopak vyjadřuje konkrétní aktuální obsah databáze v určitém čase.
Toto rozlišení odděluje relativně stabilní strukturální návrh od proměnlivých datových hodnot. (Elmasri a Navathe, 2016)

S databázovým systémem souvisí také pojem metadata.
Metadata jsou data o datech. Tyto data tedy popisují strukturu databáze, význam atributů, integritní omezení nebo například přístupová práva.
Metadata bývají ukládána v systémovém katalogu, který slouží jako centrální zdroj informací o databázových objektech (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

Správa a údržba schématu databáze je klíčovou rolí správce databáze (DBA), přičemž změny schématu v průběhu životního cyklu systému musí být pečlivě kontrolovány. Metadata uložená v systémovém katalogu jsou využívána nejen samotným DBMS pro optimalizaci dotazů a kontrolu přístupových práv, ale také externími návrhovými nástroji. Tyto nástroje dokážou metadata z katalogu načíst a vizualizovat je ve formě diagramů, což usnadňuje pochopení existující struktury databáze a její další rozvoj (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

## 4.3 Funkce DBMS a víceúrovňová architektura

Dalším důležitým konceptem je víceúrovňová architektura DBMS, která je spojovaná s modelem ANSI/SPARC.
Myšlenkou bylo podívat se na stavbu databáze jako implementaci hierarchie jistých abstrakcí. Ve zprávě výboru ANSI/X3/SPARC z roku 1975 se objevuje rozdělení na externí, konceptuální a interní úroveň pohledu, kde
externí úroveň odpovídá pohledům jednotlivých skupin uživatelů, konceptuální úroveň představuje globální logický model celé databáze a interní úroveň popisuje fyzické uložení dat.
Hlavním smyslem tohoto členění je podpora datové nezávislosti, tedy oddělení aplikací a uživatelských pohledů od fyzické implementace databáze. (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020)

Pro následné porovnání nástrojů je tato architektura důležitá proto, že návrhové nástroje nepokrývají všechny úrovně databázového systému stejným způsobem.
(Rosenthal a Reiner, 1994)
Některé se zaměřují především na konceptuální nebo logický model, jiné podporují i fyzické prvky konkrétního DBMS, například datové typy, indexy nebo generování SQL skriptů. (Carvalho et al., 2022)
Při hodnocení nástrojů proto bude vhodné sledovat nejen možnosti vytváření diagramů, ale také podporu přechodu mezi jednotlivými úrovněmi návrhu a implementace
(Rosenthal a Reiner, 1994).

## 4.4 Fáze návrhu databáze

Na konceptuální návrh navazuje v logický návrh.
V této části se konceptuální model převádí do zvoleného datového modelu, v případě této práce jde zejména o model relační. (Rosenthal a Reiner, 1994)
Dochází k návrhu relací, atributů, klíčů, cizích klíčů a integritních omezení. (Pokorný a Valenta, 2020)
Výsledkem je pak logické schéma databáze, které lze implementovat v konkrétním DBMS. (Pokorný a Valenta, 2020)

Ve fyzickém návrhu se řeší způsob uložení dat v konkrétním databázovém systému.
Řeší se zde organizace datových souborů, indexy, výkonové aspekty, optimalizace přístupu a další technické detaily. (Rosenthal a Reiner, 1994)
Na rozdíl od konceptuálního a logického návrhu je fyzický návrh silně závislý na konkrétní technologii (Pokorný a Valenta, 2020).

Mezi jednotlivými částmi návrhu existuje zpětná vazba. Pokud se při fyzickém návrhu ukáže, že některé části modelu vedou například k výkonovým problémům, je nutné vrátit se zpět k návrhu logickému.
Podobně může změna požadavků uživatelů vyvolat úpravu konceptuálního modelu a následně i včech dalších úrovní.
Návrh databáze proto nelze chápat jako striktně lineární proces, nýbrž jako proces iterativní
(Rosenthal a Reiner, 1994).


Z pohledu práce, právě členění návrhu databáze na konceptuální, logickou a fyzickou, představuje vhodný výchozí bod pro pozdější definici hodnoticích kritérií.
Nástroj určený pro návrh databázového systému by měl umožnit zachytávat požadavky, převést je do konzistentního schématu a podle potřeby podpořit i technickou implementaci v konkrétním databázovém prostředí. (Rosenthal a Reiner, 1994)
Právě míra podpory těchto kroků představuje jeden z praktických rozdílů mezi porovnávanými nástroji (Carvalho et al., 2022; Rosenthal a Reiner, 1994).
