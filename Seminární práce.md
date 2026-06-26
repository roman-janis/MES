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

# 5 Datové modely

## 5.1 Konceptuální modelování a ER/EER model

### 5.1.1 Konceptuální modelování a základní pojmy ER modelu

Datový model poskytuje formalizovaný nástroj, který slouží k popisu dat, jejich struktur a vztahů mezi nimi. Definuje datové objekty a jejich vzájemné vztahy včetně omezení, která se jich týkají (Pokorný a Valenta, 2020). Datový model je zjednodušený popis reality, který je vytvořen tak, aby se podle něj dala navrhnout databáze a později také implementovat. (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

Konceptuální modelování slouží pro zachycení požadavků aplikační domény, kterou mná aplikace pokrývat, ale bez ohledu na konkrétní databázovou technologii.
Jeho cílem je vytvořit přehledný a věrný model reálného světa (Carvalho et al., 2022).
V praxi se pro tuto fázi velmi často používá entitně-relační model (ER model), případně jeho rozšířená varianta EER (Chen, 1976; Elmasri a Navathe, 2016).

Základními pojmy ER modelu jsou entita, entitní množina, vztah a atribut.
Za entitu je považován objekt, který je schopen samostatné existence a lze jej jednoznačně odlišit od ostatních objektů (Chen, 1976).
Entitní množina je pak množina entit, které jsou stejného typu a mají společné vlastnosti (Chen, 1976).
Vztah vyjadřuje vazbu mezi entitami nebo entitními množinami a atribut představuje vlastnost entity nebo vztahu (Chen, 1976).

Vztahy mezi entitami lze popsat například kardinalitou a participací. Kardinalita udává, kolik entit jedné množiny může být ve vztahu k entitě jiné množiny (Elmasri a Navathe, 2016). Typickými případy jsou vazby 1:1, 1:N a M:N. Participace vyjadřuje, zda je účast entity ve vztahu povinná nebo nepovinná. Tyto pojmy jsou důležité nejen na konceptuální úrovni, ale i pro následnou transformaci do relačního modelu (Pokorný a Valenta, 2020).

### 5.1.2 Atributy, EER model a notace

Atributy jsou svázány s doménami, tedy s množinami přípustných hodnot (Elmasri a Navathe, 2016). Rozlišujeme jednoduché a složené atributy, případně i další typy (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
Pro jednoznačnou identifikaci entit slouží kandidátní a primární klíče (Elmasri a Navathe, 2016).

Rozšířený ER model (EER) doplňuje základní ER model o supertřídy, podtřídy a dědičnost atributů (Pokorný a Valenta, 2020). EER model je vhodný především tam, kde je potřeba přesněji vystihnout specializaci nebo generalizaci objektů (Elmasri a Navathe, 2016). V praxi se ER/EER model vyjadřuje různými grafickými notacemi, a mezi nejčastější patří Chenova notace, Crow's Foot a UML (Elmasri a Navathe, 2016; Carvalho et al., 2022).

Pro hodnocení databázových nástrojů je podpora konceptuálního modelování významná hlavně z praktického hlediska.
Nástroj by měl umožnit vyjádřit entity, vztahy, kardinality a omezení způsobem, který je srozumitelný jak analytikům, tak i vývojářům (Rosenthal a Reiner, 1994).
Jednotlivé nástroje se přitom mohou lišit použitou notací, úrovní podpory EER prvků a možností následného převodu modelu do relačního schématu (Carvalho et al., 2022; Rosenthal a Reiner, 1994).

## 5.2 Relační model

Relační model je založen na relacích, které jsou v praxi neformálně reprezentovány tabulkami.
Každá relace má své schéma, tedy jméno relace, seznam atributů a jejich domén (Pokorný a Valenta, 2020).
Konkrétní řádky tabulky odpovídají n-ticím.
Relační model pracuje s atomickými hodnotami a s přesně vymezenými atributy (Codd, 1970; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).


Klíče jsou v relačním modelu zásadní.
Primární klíč slouží k jednoznačné identifikaci řádku tabulky (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
Cizí klíč umožňuje vyjádřit vazbu mezi tabulkami a je základem referenční integrity (Watt a Eng, 2014).
Mezi obecné vlastnosti relačních tabulek patří nezávislost na pořadí řádků a sloupců a požadavek na neduplicitu řádků (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).


Relační model je pro tuto práci důležitý také proto, že většina běžně používaných návrhových nástrojů pro databáze směřuje k tvorbě relačního schématu a k práci s SQL databázemi. Při jejich porovnání proto bude důležité, zda nástroj podporuje definici primárních a cizích klíčů, integritních omezení, datových typů a generování nebo zpětné načítání databázového schématu (Carvalho et al., 2022).

## 5.3 Transformace ER/EER modelu do relačního modelu

Při přechodu z konceptuálního modelu k modelu relačnímu se entity obvykle převádějí na tabulky a atributy na sloupce (Chlapek, Kučera a Palovská, 2019).
Vztahy typu 1:N se zpravidla reprezentují pomocí cizího klíče na straně N, zatímco pro vztahy M:N je vyžadováno vytvoření samostatné spojovací tabulky. Specifické případy představují vztahy 1:1, atributy vztahů nebo převod supertříd a podtříd (Elmasri a Navathe, 2016).
Tato transformace je důležitým přechodem mezi konceptuálním a logickým návrhem. Pokud je tato transformace provedena nekonzistentně, vede k problémům v následné implementaci (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

U nástrojů pro návrh databází je proto důležité, zda převod mezi konceptuálním a relačním modelem pouze vizuálně naznačují, nebo zda tento převod dokážou částečně automatizovat a kontrolovat.
Automatické generování relačního schématu může práci urychlit, ale je potřeba ověřit, zda nástroj také správně zachází s kardinalitami, vazbami M:N, povinnými atributy a integritními omezeními (Carvalho et al., 2022; Rosenthal a Reiner, 1994).

## 5.4 Normalizace relačního modelu

Normalizace je proces, jehož cílem je odstranit nadbytečnost dat a předcházet anomáliím při vkládání, aktualizaci a mazání údajů.
Teoretickým základem normalizace jsou funkční závislosti.
Pro potřeby této práce je dostačující vysvětlit první až třetí normální formu (Codd, 1970; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

První normální forma vyžaduje atomické hodnoty a nepřipouští skupiny, které se opakují (Codd, 1970; Elmasri a Navathe, 2016).
Druhá normální forma řeší závislost neklíčových atributů na celém klíči (Codd, 1970; Elmasri a Navathe, 2016).
Třetí normální forma odstraňuje tranzitivní závislosti mezi neklíčovými atributy (Codd, 1970; Elmasri a Navathe, 2016).
Tyto formy postačují k zajištění základní konzistence relačního schématu a tvoří standard, který by každý nástroj pro návrh databází měl uživateli umožňovat respektovat (Codd, 1970; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).


Normalizace zároveň ukazuje, že kvalita návrhového nástroje nespočívá jen v grafické podobě diagramu.
Důležité je, zda nástroj podporuje konzistenci modelu, upozorňuje na chybějící klíče nebo problematické vazby a umožňuje vytvořit návrh,
který lze převést do udržitelného relačního schématu.
Tato hlediska navazují na pozdější výběr hodnoticích kritérií pro komparaci nástrojů (Carvalho et al., 2022).

# 6 Vícekriteriální rozhodování

## 6.1 Alternativa, kritérium a váha kritéria

## 6.2 Přístupy k odhadu vah kritérií a porovnání alternativ

# 7 Metoda AHP

## 7.1 Saatyho škála a párové porovnání

## 7.2 Kontrola konzistence

## 7.3 Výhody a omezení AHP
