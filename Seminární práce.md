# Univerzita Hradec Králové

## Fakulta informatiky a managementu

### Katedra informatiky a kvantitativních metod

&nbsp;

&nbsp;

&nbsp;

# Komparace nástrojů pro návrh a vývoj databázových systémů pomocí AHP

## Teoretická východiska — seminární práce

&nbsp;

Seminární práce v předmětu KRCR-MES Metodologický seminář

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

Prohlašuji, že jsem tuto seminární práci vypracoval samostatně a uvedl jsem všechny použité prameny a literaturu.

&nbsp;

&nbsp;

V Hradci Králové dne ………………………… &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ……………………………………

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Roman Janiš


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Poděkování

Tímto bych rád poděkoval vedoucímu bakalářské práce Ing. et Ing. Martinu Lněničkovi, Ph.D., za odborné vedení, věcné připomínky a konzultace, které přispěly ke zpracování této seminární práce.


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Abstrakt

Seminární práce představuje teoretická východiska bakalářské práce zaměřené na komparaci nástrojů pro návrh a vývoj databázových systémů s využitím metody vícekriteriálního rozhodování Analytic Hierarchy Process. V první části jsou vymezeny základní pojmy z oblasti databázových systémů, popsány fáze návrhu databáze a vysvětleny datové modely používané při návrhu, zejména entitně‑relační model a model relační. Druhá část je věnována vícekriteriálnímu rozhodování, vymezení pojmů alternativa, kritérium a váha kritéria a podrobnému výkladu metody AHP, včetně párového porovnávání, Saatyho škály a kontroly konzistence. Třetí část představuje nástroje, které budou předmětem navazující praktické komparace v bakalářské práci, navrhuje hodnoticí kritéria a popisuje metodický rámec dalšího postupu. Výstupem práce je teoretický a metodický základ, na který přímo naváže praktická část bakalářské práce.

**Klíčová slova:** databázový systém, návrh databází, datové modelování, vícekriteriální rozhodování, Analytic Hierarchy Process.

&nbsp;

# Abstract

**Title:** Comparison of Database Design and Development Tools Using AHP — Theoretical Background

This seminar paper presents the theoretical background of a bachelor thesis focused on the comparison of tools for the design and development of database systems using the Analytic Hierarchy Process, a multi‑criteria decision‑making method. The first part defines fundamental terms related to database systems, describes the phases of database design and explains the data models used in design, in particular the entity–relationship model and the relational model. The second part addresses multi‑criteria decision making, defines the terms alternative, criterion and criterion weight, and provides a detailed explanation of the AHP method, including pairwise comparison, Saaty's scale and consistency checking. The third part introduces the tools that will be the subject of the follow‑up practical comparison in the bachelor thesis, proposes evaluation criteria and describes the methodological framework of further work. The result is a theoretical and methodological foundation on which the practical part of the bachelor thesis will directly build.

**Keywords:** database system, database design, data modelling, multi‑criteria decision making, Analytic Hierarchy Process.


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
<w:p><w:pPr><w:pStyle w:val="Nadpisobsahu"/></w:pPr><w:r><w:t>Obsah</w:t></w:r></w:p>
<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/><w:instrText xml:space="preserve"> TOC \o "1-3" \h \z \u </w:instrText><w:fldChar w:fldCharType="separate"/><w:t>Pole obsahu — ve Wordu klikněte do pole pravým tlačítkem a zvolte „Aktualizovat pole", případně stiskněte F9.</w:t><w:fldChar w:fldCharType="end"/></w:r></w:p>
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# 1 Úvod

Návrh databáze je jednou z důležitých činností při tvorbě informačních systémů. Kvalita datového návrhu ovlivňuje spolehlivost, výkon a možnosti dalšího rozšiřování výsledné aplikace. Pokud při návrhu vzniknou chyby, jejich odstranění je v dalších etapách složité a nákladné. Při návrhu a vývoji databází se proto využívají různé softwarové nástroje, například nástroje pro datové modelování, tvorbu ER diagramů, generování SQL skriptů nebo správu databázových schémat, které se liší rozsahem funkcí, podporovanými databázovými platformami, možnostmi modelování, mírou automatizace nebo licenčními podmínkami. Nabídka těchto nástrojů je navíc široká a stále se proměňuje, mimo jiné v souvislosti s rostoucím významem nerelačních (NoSQL) databází (Jedlička, 2024).

Zvolit vhodný nástroj není v praxi jednoduché. Rozhodnutí nelze opřít pouze o jedno hledisko, například cenu nebo rozšířenost nástroje, protože do výběru vstupuje více kritérií, která se mohou navzájem dostávat do konfliktu. Vhodnější je proto využít postup, který umožní jednotlivé nástroje porovnat podle předem stanovených kritérií, nikoli pouze podle subjektivního dojmu. Takovým postupem je metoda vícekriteriálního rozhodování Analytic Hierarchy Process (AHP), na níž je tato práce postavena.

Tato seminární práce vytváří teoretický a metodický základ pro navazující praktické porovnání nástrojů a je členěna následovně. Nejprve jsou vymezeny pojmy z oblasti databázových systémů, datového modelování a návrhu databáze. Poté je vyložen princip vícekriteriálního rozhodování a metoda AHP. Závěrečná část představuje konkrétní nástroje a navrhuje hodnoticí kritéria, která budou využita v praktické části bakalářské práce. Výsledné porovnání má pomoci lépe posoudit, v jakých situacích je vhodné jednotlivé nástroje využít.

# 2 Cíl práce a výzkumné otázky

Cílem práce je porovnat vybrané nástroje pro návrh a vývoj databázových systémů z hlediska jejich funkcionality, použitelnosti a podpory návrhu databáze. K naplnění hlavního cíle jsou důležité tyto dílčí cíle:

- vymezit základní pojmy z oblasti databázových systémů, datového modelování a návrhu databáze,
- vysvětlit principy vícekriteriálního rozhodování, metodu AHP a její použitelnost pro porovnání softwarových nástrojů,
- vybrat a charakterizovat nástroje, které budou předmětem porovnávání, a navrhnout hodnoticí kritéria.

Výzkumné otázky vycházejí z hlavního cíle a sledují postupnou přípravu teoretického a metodického rámce — od vymezení základních pojmů, přes principy hodnocení nástrojů podle více kritérií, až po volbu kritérií a postupu pro vlastní porovnání.

Tomuto zaměření odpovídají následující výzkumné otázky:
- **VO1:** Jaké klíčové pojmy, modely a postupy se využívají při návrhu a vývoji databázových systémů?
- **VO2:** Jaké principy a postupy nabízí metoda AHP pro porovnání alternativ podle více kritérií?
- **VO3:** Jaká hodnoticí kritéria a jaký postup zvolit pro praktické porovnání nástrojů a jak jejich volbu zdůvodnit?

Odpovědi na uvedené výzkumné otázky tvoří obsah jednotlivých kapitol této práce a současně vytváří metodický rámec pro praktickou část bakalářské práce.

# 3 Metodika práce

Při zpracování práce byl nejprve vymezen okruh témat, která jsou potřebná pro pozdější porovnání nástrojů. Jednalo se zejména o témata: databázové systémy, datové modelování, návrh databáze, vícekriteriální rozhodování a metodu AHP. K těmto oblastem byla následně dohledána odborná literatura, ze které byly převzaty a vysvětleny základní pojmy využité v dalších částech práce.

Teoretická část týkající se databázových systémů vychází především z publikace Pokorného a Valenty (2020). Pro vysvětlení metody AHP byly využity práce Saatyho (1990, 2008) a doplňující české zdroje k vícekriteriálnímu rozhodování (Soukopová, 2016; Jandová, 2012; Vohradský, 2016). K oblasti datového modelování a návrhu relačních databází byly využity také české práce Chlapka, Kučery a Palovské (2019), Kašpara (2012) a Chotěnovského (2023); k nerelačním databázovým systémům pak práce Jedličky (2024). Použitelnost AHP pro výběr softwarových nástrojů dokládá v mezinárodním kontextu práce Simanavičienė a Vdovinskienė (2023), která se zabývá výběrem CAD systémů. Strukturu hodnoticích kategorií a výběr nástrojů metodicky podpořila srovnávací studie Carvalho et al. (2022). Pro popis konkrétních nástrojů byla využita jejich oficiální dokumentace.

**Práce se zdroji.** Citace jsou v textu uváděny harvardským způsobem, tedy ve tvaru autor a rok. Seznam zdrojů je zpracován podle normy ČSN ISO 690:2022. U webových zdrojů je uvedeno datum citace.

**Postup pro navazující praktickou komparaci.** V praktické části bakalářské práce budou vybrané nástroje nainstalovány a otestovány podle jednotného scénáře. U každého nástroje bude ověřena tvorba modelu, převod do logického a fyzického návrhu, generování SQL skriptu a případně také reverzní inženýrství z existující databáze. Získané poznatky budou použity jako podklad pro hodnocení nástrojů podle navržených kritérií metodou AHP.

# 4 Databázové systémy

## 4.1 Základní pojmy

Pro správné pochopení je nutné oddělit pojmy data, informace, databáze a systém řízení báze dat. Data lze chápat jako jednotlivá fakta nebo zaznamenané hodnoty, které samy o sobě nemusí nést širší význam. Informace vznikají interpretací dat v určitém kontextu. Databáze pak představuje organizovanou kolekci vzájemně souvisejících dat, která jsou ukládána tak, aby s nimi bylo možné efektivně pracovat (Pokorný a Valenta, 2020).

Systém řízení báze dat, běžně označovaný zkratkou DBMS, je specializovaný software, který zajišťuje definici, ukládání, manipulaci, zabezpečení a správu dat uložených v databázi. Databázový systém v širším smyslu zahrnuje nejen samotnou databázi a DBMS, ale také uživatele, aplikační software, pravidla provozu a další prostředky potřebné pro práci s daty. Pokorný a Valenta uvádějí, že databázové systémy poskytují služby spojené s definicí databáze, manipulací s daty, souběžným přístupem k datům, ochranou dat a zotavením z chyb (Pokorný a Valenta, 2020).

## 4.2 Schéma databáze, instance a metadata

Důležitou součástí teorie databázových systémů je rozlišení schématu databáze a instance databáze. Schéma databáze představuje popis struktury uložených dat, tedy určení entit, atributů, vazeb a omezení, která mají data splňovat. Instance databáze naopak vyjadřuje konkrétní aktuální obsah databáze v určitém čase. Toto rozlišení je důležité, protože odděluje relativně stabilní strukturální návrh od proměnlivých datových hodnot (Pokorný a Valenta, 2020).

S databázovým systémem úzce souvisejí také metadata. Metadata jsou data o datech, tedy informace popisující strukturu databáze, význam atributů, integritní omezení nebo přístupová práva. Metadata bývají ukládána v systémovém katalogu, který slouží jako centrální zdroj informací o databázových objektech (Pokorný a Valenta, 2020).

## 4.3 Funkce DBMS a víceúrovňová architektura

DBMS obvykle poskytuje několik základních skupin funkcí: definici dat, manipulaci s daty, řízení souběžného přístupu více uživatelů, ochranu dat a obnovu po chybě. V souvislosti s těmito funkcemi se používají pojmy DDL pro jazyk definice dat, DML pro jazyk manipulace s daty a transakce pro logický celek operací, který má být proveden buď celý, nebo vůbec (Pokorný a Valenta, 2020).

Významnou teoretickou oporou je víceúrovňová architektura DBMS spojovaná s modelem ANSI/SPARC. Tato architektura rozlišuje externí, konceptuální a interní úroveň pohledu na data. Externí úroveň odpovídá pohledům jednotlivých skupin uživatelů, konceptuální úroveň představuje globální logický model celé databáze a interní úroveň popisuje fyzické uložení dat. Hlavním smyslem tohoto členění je podpora datové nezávislosti, tedy oddělení aplikací a uživatelských pohledů od fyzické implementace databáze (Pokorný a Valenta, 2020).

## 4.4 Fáze návrhu databáze

Návrh databáze je proces, který probíhá v několika na sebe navazujících fázích. Není vhodné začínat přímo fyzickou implementací tabulek v konkrétním systému, protože takový postup často vede k chybám v návrhu, k zbytečné redundanci a k problémům s budoucí rozšiřitelností. Proto se v literatuře běžně rozlišuje konceptuální, logický a fyzický návrh (Pokorný a Valenta, 2020).

Konceptuální návrh zachycuje strukturu aplikační domény bez vazby na konkrétní databázový systém. V této fázi jsou identifikovány entity, vztahy mezi nimi, atributy a základní omezení. Cílem je vytvořit model reality, který bude dostatečně přesný a současně technologicky nezávislý.

Na konceptuální návrh navazuje logický návrh. V této fázi se konceptuální model převádí do zvoleného datového modelu, v případě této práce zejména do modelu relačního. Dochází k návrhu relací, atributů, klíčů, cizích klíčů a integritních omezení. Výsledkem je logické schéma databáze, které lze implementovat v konkrétním DBMS.

Fyzický návrh se soustředí na způsob uložení dat v konkrétním databázovém systému. Řeší se zde organizace datových souborů, indexy, výkonové aspekty, optimalizace přístupu a další technické detaily. Na rozdíl od konceptuálního a logického návrhu je fyzický návrh silně závislý na konkrétní technologii (Pokorný a Valenta, 2020).

Mezi jednotlivými fázemi návrhu existuje zpětná vazba. Pokud se při fyzickém návrhu ukáže, že některé části modelu vedou k výkonovým problémům, je nutné vrátit se zpět k návrhu logickému. Podobně změna požadavků uživatelů může vyvolat úpravu konceptuálního modelu a následně i všech dalších úrovní. Návrh databáze proto nelze chápat jako striktně lineární proces, nýbrž jako proces iterativní.

# 5 Datové modely

## 5.1 Konceptuální modelování a ER/EER model

Datový model představuje formalizovaný prostředek pro popis dat, jejich struktury a vztahů mezi nimi. Datové modely umožňují zachytit realitu tak, aby s ní bylo možné systematicky pracovat při návrhu databází i při jejich následné implementaci (Pokorný a Valenta, 2020).

Konceptuální modelování slouží k zachycení požadavků aplikační domény bez ohledu na konkrétní databázovou technologii. Jeho cílem je vytvořit srozumitelný a logicky konzistentní model reality. V praxi se pro tuto fázi velmi často používá entitně‑relační model (ER model), případně jeho rozšířená varianta EER (Pokorný a Valenta, 2020).

Základními pojmy ER modelu jsou entita, entitní množina, vztah a atribut. Entita je objekt reálného světa, který je schopen samostatné existence a lze jej jednoznačně odlišit od ostatních objektů. Entitní množina je množina entit stejného typu, které mají společné vlastnosti. Vztah vyjadřuje vazbu mezi entitami nebo entitními množinami a atribut představuje vlastnost entity nebo vztahu.

Vztahy mezi entitami se popisují mimo jiné pomocí kardinality a participace. Kardinalita určuje, kolik entit jedné množiny může být ve vztahu k entitě jiné množiny. Typickými případy jsou vazby 1:1, 1:N a M:N. Participace vyjadřuje, zda je účast entity ve vztahu povinná nebo nepovinná. Tyto pojmy jsou důležité nejen na konceptuální úrovni, ale i pro následnou transformaci do relačního modelu (Pokorný a Valenta, 2020).

Atributy jsou svázány s doménami, tedy s množinami přípustných hodnot. Rozlišují se jednoduché a složené atributy, případně další typy atributů. Pro jednoznačnou identifikaci entit slouží kandidátní a primární klíče. Rozšířený ER model (EER) doplňuje základní ER model o supertřídy, podtřídy a dědičnost atributů. EER model je vhodný tam, kde je třeba přesněji vystihnout specializaci nebo generalizaci objektů (Pokorný a Valenta, 2020). V praxi se ER/EER model vyjadřuje různými grafickými notacemi; mezi nejčastější patří Chenova notace, Crow's Foot a UML.

## 5.2 Relační model

Relační model je založen na relacích, které jsou v praxi reprezentovány tabulkami. Každá relace má své schéma, tedy jméno relace, seznam atributů a jejich domén. Konkrétní řádky tabulky odpovídají n‑ticím. Důležitou vlastností relačního modelu je práce s atomickými hodnotami a s přesně vymezenými atributy (Pokorný a Valenta, 2020).

V relačním modelu hrají zásadní roli klíče. Primární klíč slouží k jednoznačné identifikaci řádku tabulky. Cizí klíč umožňuje vyjádřit vazbu mezi tabulkami a je základem referenční integrity. Mezi obecné vlastnosti relačních tabulek patří nezávislost na pořadí řádků a sloupců a požadavek na neduplicitu řádků (Pokorný a Valenta, 2020).

## 5.3 Transformace ER/EER modelu do relačního modelu

Při přechodu od konceptuálního modelu k modelu relačnímu se entity obvykle převádějí na tabulky a atributy na sloupce. Vztahy typu 1:N se zpravidla reprezentují pomocí cizího klíče na straně N, zatímco vztahy M:N vyžadují vytvoření samostatné spojovací tabulky. Specifické případy představují vztahy 1:1, atributy vztahů nebo převod supertříd a podtříd. Tato transformace je důležitým mostem mezi konceptuálním a logickým návrhem; pokud je provedena nekonzistentně, vede k problémům v navazující implementaci (Pokorný a Valenta, 2020; Chlapek, Kučera a Palovská, 2019).

## 5.4 Normalizace relačního modelu

Normalizace je proces, jehož cílem je odstranit nadbytečnost dat a předcházet anomáliím při vkládání, aktualizaci a mazání údajů. Teoretickým základem normalizace jsou funkční závislosti. Pro potřeby této práce je dostačující vysvětlit první až třetí normální formu.

První normální forma vyžaduje atomické hodnoty a nepřipouští opakující se skupiny. Druhá normální forma řeší závislost neklíčových atributů na celém klíči. Třetí normální forma odstraňuje tranzitivní závislosti mezi neklíčovými atributy. Tyto formy postačují k zajištění základní konzistence relačního schématu a tvoří standard, který by každý nástroj pro návrh databází měl uživateli umožňovat respektovat (Pokorný a Valenta, 2020; Chlapek, Kučera a Palovská, 2019).

# 6 Vícekriteriální rozhodování

Vícekriteriální rozhodování se zabývá situacemi, ve kterých nelze rozhodovat podle jediného hlediska. V reálných rozhodovacích úlohách jsou alternativy obvykle posuzovány podle více kritérií, která mohou být navzájem v konfliktu. Právě proto je vhodné využít metody, které umožňují tato kritéria systematicky zahrnout do rozhodovacího procesu (Saaty, 2008).

Rozhodovací úloha bývá popsána množinou variant, množinou kritérií a vztahem mezi nimi. Varianty představují jednotlivé posuzované možnosti. Kritéria vyjadřují hlediska, podle kterých jsou varianty hodnoceny. Hodnocení variant podle jednotlivých kritérií se často zapisuje do kriteriální matice (Saaty, 2008).

V souvislosti s vícekriteriálním rozhodováním je vhodné vysvětlit pojmy ideální a bazální varianta, dominance a nedominované řešení. Ideální varianta je hypotetická varianta, která dosahuje ve všech kritériích nejlepších možných hodnot. Bazální varianta naopak představuje hypotetickou variantu s nejhoršími hodnotami. Nedominovaná varianta je taková varianta, pro kterou neexistuje jiná varianta lepší alespoň v jednom kritériu a současně ne horší v ostatních (Saaty, 2008).

Pro potřeby této práce je důležité zejména vícekriteriální hodnocení variant, neboť navazující praktická část bude porovnávat konečný seznam databázových nástrojů. Jde tedy o situaci, kdy jsou předem dány alternativy a je nutné z nich určit nejvhodnější řešení (Saaty, 1990).

## 6.1 Alternativa, kritérium a váha kritéria

Alternativa představuje jednu z možných variant rozhodnutí. V kontextu této práce bude alternativou konkrétní software určený pro návrh a vývoj databázových systémů. Kritérium je hledisko, podle kterého se jednotlivé alternativy posuzují. Může jít například o funkcionalitu, použitelnost, kompatibilitu s různými DBMS, podporu reverzního inženýrství nebo cenu.

Kritéria lze členit různými způsoby. Základní dělení odlišuje kritéria maximalizační a minimalizační. U maximalizačních kritérií je žádoucí co nejvyšší hodnota, například rozsah funkcionality. U minimalizačních kritérií je naopak žádoucí co nejnižší hodnota, typicky například cena nebo náročnost implementace. Kritéria mohou být dále kvantitativní nebo kvalitativní.

Váha kritéria vyjadřuje jeho relativní význam v rámci rozhodovacího procesu. Ne všechna kritéria mají stejnou důležitost, a proto je nutné jejich význam určit explicitně. Určení vah kritérií je jedním z klíčových kroků většiny vícekriteriálních metod (Saaty, 1990; Soukopová, 2016).

## 6.2 Přístupy k odhadu vah kritérií a porovnání alternativ

Pro odhad vah kritérií lze použít několik postupů. Jednodušší přístupy zahrnují metodu pořadí nebo bodovací metodu. Tyto metody jsou snadno použitelné, ale méně jemné při vyjadřování intenzity preference. Pokročilejší přístupy pracují s párovým porovnáváním kritérií, kam patří i Saatyho metoda, která je s metodou AHP přímo spojena (Saaty, 2008). Z hlediska porovnání samotných alternativ umožňuje AHP aplikovat stejný princip párového porovnávání i pro alternativy, a to vůči každému z dříve stanovených kritérií. Výhodou je systematičnost a transparentnost, nevýhodou vyšší pracnost při větším počtu prvků (Saaty, 2008).

Z dalších metod vícekriteriálního hodnocení variant jsou v literatuře rozšířeny zejména metoda váženého součtu (WSA), která pracuje s lineárně normalizovanými hodnotami kritérií a výsledné skóre alternativy vypočítá jako vážený součet normalizovaných hodnot, a metoda TOPSIS, jež hodnotí alternativy podle jejich vzdálenosti od ideální a bazální varianty. Komplexnější strukturou se vyznačuje rodina metod ELECTRE, které pracují s koncepty outrangování (Soukopová, 2016). Pro potřeby navazující bakalářské práce bylo zvoleno AHP ze dvou důvodů: za prvé umožňuje přirozeně kombinovat kvantitativní i kvalitativní kritéria bez nutnosti jejich normalizace na společnou škálu, což je při hodnocení softwaru žádoucí; za druhé nabízí prostřednictvím indexu konzistence CR vestavěný mechanismus ověření soudržnosti hodnotitelových úsudků, který je obzvláště přínosný v situaci, kdy párové porovnávání provádí jeden hodnotitel (Saaty, 1990; Saaty, 2008).

# 7 Metoda AHP

Metoda *Analytic Hierarchy Process* (AHP) patří mezi nejznámější metody vícekriteriálního rozhodování. Jejím autorem je Thomas L. Saaty. Podstatou této metody je rozklad složitého rozhodovacího problému do hierarchické struktury, která obsahuje cíl, kritéria, případně subkritéria a alternativy. Tento rozklad umožňuje lépe zachytit strukturu rozhodovací úlohy a následně jednotlivé prvky systematicky porovnat (Saaty, 1990; Saaty, 2008).

Na nejvyšší úrovni hierarchie stojí cíl rozhodování, například výběr nejvhodnějšího databázového nástroje. Na nižších úrovních se nacházejí kritéria, případně subkritéria, a na nejnižší úrovni alternativy. Klíčovým principem metody je párové porovnávání prvků na stejné úrovni vzhledem k prvku nadřazenému (Saaty, 2008).

## 7.1 Saatyho škála a párové porovnání

Při párovém porovnávání se používá Saatyho škála. Základní hodnoty této škály jsou 1, 3, 5, 7 a 9, přičemž vyjadřují stejnou důležitost, mírnou, silnou, velmi silnou až absolutní preferenci. Sudé hodnoty 2, 4, 6, 8 lze chápat jako mezistupně. Pokud je jeden prvek méně významný než druhý, použije se převrácená hodnota (Saaty, 1990).

Výsledkem párového porovnání je čtvercová reciproční matice, označovaná jako Saatyho matice. Z této matice se následně vypočítají lokální váhy. V literatuře se používá více postupů výpočtu, například metoda vlastního vektoru nebo výpočet založený na geometrickém průměru řádků (Saaty, 2008).

## 7.2 Kontrola konzistence

Protože párové porovnávání vychází z lidského úsudku, není vždy dokonale konzistentní. Součástí metody AHP je proto kontrola konzistence. K tomu slouží *Consistency Index* (CI), *Random Consistency Index* (RI) a *Consistency Ratio* (CR). V praxi se uvádí, že hodnota CR menší než 0,1 značí přijatelnou úroveň konzistence; vyšší hodnoty obvykle vedou k přehodnocení porovnání (Saaty, 1990; Saaty, 2008).

## 7.3 Výhody a omezení AHP

Výhodou AHP je možnost kombinovat kvantitativní i kvalitativní kritéria a transparentně zdůvodnit, jak bylo dosaženo výsledného pořadí alternativ. Metoda současně umožňuje analýzu citlivosti, tedy sledování dopadu změny vah kritérií na výsledné pořadí. Nevýhodou je vyšší pracnost při větším počtu kritérií a alternativ a určitá míra subjektivity, která je s párovým porovnáváním spjata (Saaty, 2008). V české odborné literatuře se v této souvislosti hovoří o problému udržení konzistence rozhodovatele při rozsáhlejším počtu párových srovnání a o riziku změny pořadí alternativ (tzv. rank reversal) při přidání nebo odebrání varianty z modelu (Jandová, 2012; Vohradský, 2016).

# 8 Nástroje pro návrh a vývoj databází

Výběr nástrojů pro praktickou komparaci proběhl ve dvou krocích. Nejprve byl vymezen okruh dostupných nástrojů pro návrh a vývoj databází; že je tato nabídka široká, dokládá srovnávací studie Carvalho et al. (2022), která hodnotila sedmnáct nástrojů pro datové modelování. Z tohoto okruhu byly nástroje vybírány podle několika hledisek: (1) zaměření na návrh a vývoj databáze, nikoli pouze na její správu či provoz; (2) dostupnost bezplatné nebo volně testovatelné verze, aby je bylo možné prakticky vyzkoušet; (3) pokrytí různých licenčních modelů (open‑source, freeware) a různé míry specializace (univerzální nástroj vs. nástroj vázaný na konkrétní DBMS); a (4) přítomnost alespoň části z nich v odborné literatuře, což umožní porovnat výsledky s existujícími studiemi. Nabídka přitom zahrnuje i webové a akademické nástroje, například online nástroj ONDA vyvinutý na Univerzitě v Coimbře (Laranjeiro a Pinto, 2024); ten však do užšího výběru zařazen nebyl, neboť práce se soustředí na plnohodnotné nástroje s lokální instalací.

Na základě uvedených hledisek byly vybrány čtyři nástroje: jeden specializovaný open‑source nástroj zaměřený na PostgreSQL (pgModeler), jeden open‑source nástroj s komerční edicí pokrývající široké spektrum DBMS (DBeaver), jeden freeware specializovaný na MySQL (MySQL Workbench) a jeden freeware vyvíjený komerčním vydavatelem se silnou podporou logického modelování (Oracle SQL Developer Data Modeler). Tři z vybraných nástrojů jsou navíc obsaženy ve zmíněné studii Carvalho et al. (2022), což umožní částečné porovnání výsledků navazující bakalářské práce s existující literaturou. Tři nástroje (Oracle SQL Developer Data Modeler, DBeaver Community Edition a MySQL Workbench Community Edition) jsou v aktuálních verzích připraveny k instalaci přímo z pracovní složky autora; čtvrtý nástroj pgModeler bude stažen z oficiálního webu projektu. Vzhledem k rostoucímu významu a popularitě nerelačních databázových systémů, jak na to poukazuje např. Jedlička (2024), bude při hodnocení nástrojů zohledněna také jejich případná schopnost kooperovat s NoSQL technologiemi (zejména v případě univerzálního nástroje DBeaver).

Základní charakteristiky vybraných nástrojů shrnuje tabulka 1.

| Nástroj | Vydavatel | Licence | Primární DBMS | Klíčové funkce |
|---|---|---|---|---|
| Oracle SQL Developer Data Modeler | Oracle Corporation | Freeware | Oracle Database | Logický, relační, fyzický a multidimenzionální model; forward/reverse engineering |
| DBeaver Community Edition | DBeaver Corp. | Open‑source (Apache 2.0) | Multi‑DBMS | ER diagramy, SQL editor, prohlížeč dat, DDL export |
| MySQL Workbench Community Edition | Oracle Corporation | Freeware | MySQL | EER modelování, forward/reverse engineering, synchronizace s živou databází |
| pgModeler | Raphael Araújo e Silva | Open‑source (GPLv3) | PostgreSQL | Grafický návrh schémat, generování SQL, reverzní inženýrství, validace modelu |

*Tabulka 1 — Základní charakteristiky vybraných nástrojů (zdroje: Oracle, 2026; DBeaver, 2026; MySQL, 2026; pgModeler, 2026)*

## 8.1 Oracle SQL Developer Data Modeler

Oracle SQL Developer Data Modeler je bezplatný grafický nástroj společnosti Oracle pro modelování dat. Podporuje logické, relační, fyzické, multidimenzionální a typové modely, nabízí forward i reverse engineering a integraci se širším portfoliem Oracle SQL Developer. Jako primární databázová platforma je preferován Oracle Database, nástroj však umožňuje pracovat i s dalšími systémy (Oracle, 2026). Pro účely této práce bude testována verze 24.3.

## 8.2 DBeaver Community Edition

DBeaver je open‑source univerzální databázový nástroj s podporou širokého spektra DBMS (PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, SQLite a další). Nabízí editor SQL, prohlížeč dat, vizualizaci databázových struktur pomocí ER diagramů a generování DDL skriptů. Pokročilejší funkce, například datové generátory nebo vizuální dotazování, jsou dostupné v komerční edici (DBeaver, 2026). Pro účely této práce bude testována verze 26.0 Community Edition.

## 8.3 MySQL Workbench Community Edition

MySQL Workbench je oficiální nástroj společnosti Oracle pro práci s databází MySQL. Sjednocuje v jednom prostředí návrh databáze (EER diagramy), správu serveru, modelování, forward i reverse engineering a SQL vývoj. Podporuje synchronizaci modelu s živou databází a export modelu do DDL skriptu (MySQL, 2026). Pro účely této práce bude testována verze 8.0.46 Community Edition.

## 8.4 pgModeler

pgModeler je open‑source nástroj zaměřený přímo na databázi PostgreSQL. Umožňuje grafický návrh schémat, generování SQL skriptů, reverzní inženýrství, validaci modelu a porovnávání modelu s živou databází (pgModeler, 2026). Cílovou databázovou platformou nástroje je PostgreSQL, jehož oficiální dokumentace popisuje podporované datové typy a syntaxi SQL, vůči nimž pgModeler generované skripty validuje (PostgreSQL, 2026). Pro účely této práce bude testována aktuální stabilní verze ke dni testování.

# 9 Návrh hodnoticích kritérií

Při tvorbě hodnoticích kritérií je nutné zohlednit, že nástroje budou srovnávány na úrovni schopností pokrýt návrh a vývoj databáze, nikoli pouze provoz databáze. Vymezení kritérií vychází z obecné struktury hodnoticích kategorií identifikovaných v komparativní studii Carvalho et al. (2022), kteří při hodnocení nástrojů pro datové modelování pracovali s kategoriemi jako funkcionalita, provozní charakteristiky softwaru, dokumentace a komunitní podpora. Tato práce přejímá analogické členění a doplňuje jej o kritéria specifická pro AHP postup a pro kontext návrhu databázových systémů. V navazující bakalářské práci budou kritéria dále upřesněna, případně rozšířena o subkritéria.

Přehled osmi navržených pracovních kritérií uvádí tabulka 2.

| ID | Název kritéria | Typ | Způsob hodnocení |
|---|---|---|---|
| K1 | Funkcionalita | maximalizační | testovací scénář + dokumentace nástroje |
| K2 | Použitelnost | maximalizační | kvalitativní hodnocení v testovacím scénáři |
| K3 | Kompatibilita s DBMS | maximalizační | počet oficiálně podporovaných DBMS |
| K4 | Forward engineering | maximalizační | testovací scénář (generování DDL) |
| K5 | Reverse engineering | maximalizační | testovací scénář (import z existující DB) |
| K6 | Dokumentace a komunitní podpora | maximalizační | kvalitativní hodnocení |
| K7 | Import, export a validace modelu | maximalizační | testovací scénář + formáty |
| K8 | Cena a licence | minimalizační | typ licence, omezení free verze, celková cena |

*Tabulka 2 — Navržená hodnoticí kritéria pro navazující praktickou komparaci*

**K1 — Funkcionalita.** Rozsah podporovaných funkcí: konceptuální, logický a fyzický model, validace modelu, generování SQL, dokumentace modelu, podpora pro práci s různými typy objektů. Maximalizační, kvalitativně‑kvantitativní kritérium.

**K2 — Použitelnost.** Snadnost ovládání, přehlednost rozhraní, kvalita uživatelské zpětné vazby, minimalizace chybovosti při běžných úkonech. Maximalizační, kvalitativní kritérium hodnocené v testovacím scénáři.

**K3 — Kompatibilita s DBMS.** Šíře podporovaných databázových systémů (PostgreSQL, MySQL, Oracle, SQL Server a další). Maximalizační kritérium, kvantifikovatelné počtem oficiálně podporovaných DBMS.

**K4 — Forward engineering.** Schopnost generovat DDL skript nebo přímo vytvořit schéma databáze z modelu, včetně kvality vygenerovaného SQL. Maximalizační, kvalitativně‑kvantitativní kritérium.

**K5 — Reverse engineering.** Schopnost vytvořit model z existující databáze, věrnost převodu a možnosti následných úprav. Maximalizační, kvalitativně‑kvantitativní kritérium.

**K6 — Dokumentace a komunitní podpora.** Rozsah a aktuálnost oficiální dokumentace, dostupnost komunitních zdrojů, frekvence aktualizací. Maximalizační, kvalitativní kritérium.

**K7 — Import, export a validace modelu.** Podporované formáty importu/exportu, schopnost validovat model před nasazením, integrace s verzovacími systémy. Maximalizační, kvalitativně‑kvantitativní kritérium.

**K8 — Cena a licence.** Typ licence (open‑source, freeware, komerční), omezení free verze, celkové náklady na zavedení. Minimalizační kritérium (vyšší cena = nižší skóre).

# 10 Metodický rámec navazující praktické komparace

V navazující bakalářské práci bude postup praktické komparace strukturován do následujících kroků:

1. **Sestavení hierarchie AHP.** Na nejvyšší úrovni cíl „Výběr nejvhodnějšího nástroje pro návrh a vývoj databází", na druhé úrovni kritéria K1–K8, na třetí úrovni alternativy (Oracle SQL Developer Data Modeler, DBeaver, MySQL Workbench, pgModeler).
2. **Párové porovnání kritérií.** Sestavení Saatyho matice 8×8, výpočet vah jednotlivých kritérií metodou geometrického průměru řádků, kontrola konzistence (CR < 0,1).
3. **Testování nástrojů.** Na pracovní stanici autora budou nainstalovány nástroje z instalátorů uložených ve složce `nastroje/`. Na každém z nich bude proveden jednotný testovací scénář: vytvoření konceptuálního modelu malé doménové oblasti (např. evidenci objednávek), převod do relačního schématu, generování SQL skriptu pro PostgreSQL a MySQL, reverzní inženýrství z existujícího schématu.
4. **Párové porovnání alternativ vzhledem ke každému kritériu.** Pro každé kritérium vznikne Saatyho matice 4×4. U kritérií K3, K4 a K8 budou hodnoty opřeny o ověřitelná měřítka (počet podporovaných DBMS, počet kroků pro generování SQL, cena); u kritérií K2 a K6 půjde o kvalitativní hodnocení.
5. **Syntéza lokálních a globálních priorit.** Výsledné pořadí nástrojů vznikne jako vážený součet lokálních priorit přes všechna kritéria.
6. **Analýza citlivosti.** Bude sledováno, jak se mění výsledné pořadí při změně vah klíčových kritérií, zejména K1 (Funkcionalita) a K8 (Cena a licence).
7. **Doporučení pro praxi.** Na základě výsledků budou formulována doporučení pro typové scénáře malé a střední firmy, kde lze očekávat odlišné váhy kritérií než v scénáři čistě technickém.

# 11 Shrnutí a diskuse

V této seminární práci bylo zpracováno teoretické a metodické zázemí pro komparaci nástrojů pro návrh a vývoj databázových systémů metodou AHP. Bylo vymezeno, co se rozumí databázovým systémem, jak jsou strukturovány fáze návrhu databáze a jaké datové modely se používají, s důrazem na ER/EER model a model relační. Dále byla popsána metoda AHP, principy párového porovnávání, Saatyho škála i kontrola konzistence pomocí CR. Byly představeny čtyři nástroje, které se stanou předmětem praktické komparace, a navrženo osm hodnoticích kritérií spolu s metodickým rámcem dalšího postupu.

Z diskuse vyplývá několik bodů, které je vhodné vzít v úvahu při navazující bakalářské práci. Za prvé je nutné mít na paměti, že AHP nese inherentní subjektivitu v rámci párového porovnávání; tu lze zmírnit jasným zdůvodněním každého rozhodnutí a kontrolou konzistence. Za druhé, výběr čtyř nástrojů s odlišným zaměřením (univerzální vs. specializované, open‑source vs. freeware vs. komerční) umožní zajímavé srovnání, ale současně zvyšuje nároky na pečlivé definování hodnoticích kritérií, zejména v oblasti funkcionality a kompatibility. Za třetí, dokumentace zvolených nástrojů, která bude tvořit klíčový zdroj informací pro praktickou část, je u všech čtyř nástrojů průběžně aktualizována; je proto nutné při citacích pečlivě uvádět datum citace.

Omezením této seminární práce je, že čerpá z užšího seznamu zdrojů soustředěného kolem monografie Pokorného a Valenty (2020) pro oblast databází a kolem prací Saatyho (1990, 2008) pro oblast AHP. Tato volba byla vědomá: vedoucí práce v e‑mailové komunikaci doporučil opřít teoretickou část o kvalitní knižní zdroje a o oficiální produktovou dokumentaci. V bakalářské práci bude seznam zdrojů přiměřeně rozšířen o další odborné publikace, mimo jiné s ohledem na pokrytí historického vývoje databázových systémů a alternativních přístupů k vícekriteriálnímu rozhodování.

# 12 Závěry a doporučení

Cíl seminární práce, tedy zpracování teoretických a metodických východisek navazující bakalářské práce, byl naplněn. Odpovědi na výzkumné otázky lze stručně shrnout takto:

- **K VO1:** Byly vymezeny klíčové pojmy databázových systémů (data, DBMS, schéma, instance, metadata), popsány fáze návrhu databáze (konceptuální, logický, fyzický) a vysvětleny datové modely používané v praxi, zejména ER/EER a relační model spolu s normalizací.
- **K VO2:** Metoda AHP byla popsána jak z hlediska principu (hierarchie cíl–kritéria–alternativy), tak z hlediska postupu (párové porovnání s využitím Saatyho škály, výpočet vah, kontrola konzistence pomocí CR). Bylo zdůvodněno, proč je AHP vhodná pro porovnání softwarových nástrojů.
- **K VO3:** Bylo navrženo osm hodnoticích kritérií (K1–K8) a metodický rámec navazující komparace, zahrnující sestavení hierarchie, párové porovnání kritérií, testovací scénář nad nainstalovanými nástroji, syntézu priorit a analýzu citlivosti.

Pro navazující bakalářskou práci je doporučeno: a) provést testovací scénář na všech čtyřech nástrojích v jednom kalendářním týdnu, aby byly minimalizovány rozdíly ve zkušenosti hodnotitele; b) při hodnocení kvalitativních kritérií (K2, K6) doplnit slovní zdůvodnění každého párového porovnání; c) zařadit analýzu citlivosti minimálně pro váhy K1 a K8; d) zvážit modelový scénář dvou typových firem (malé a střední) s odlišnými váhami kritérií a porovnat výsledné pořadí mezi scénáři.


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Seznam zdrojů

POKORNÝ, Jaroslav a Michal VALENTA. *Databázové systémy*. Praha: České vysoké učení technické v Praze, 2020. ISBN 978‑80‑01‑06708‑6.

CHLAPEK, Dušan, Jan KUČERA a Helena PALOVSKÁ. *Datové modelování a návrh relační databáze: Sbírka řešených úloh*. Praha: Vysoká škola ekonomická v Praze, Nakladatelství Oeconomica, 2019. ISBN 978‑80‑245‑2331‑6.

SAATY, Thomas L. How to make a decision: The Analytic Hierarchy Process. *European Journal of Operational Research*. 1990, **48**(1), 9–26. ISSN 0377‑2217.

SAATY, Thomas L. Decision making with the analytic hierarchy process. *International Journal of Services Sciences*. 2008, **1**(1), 83–98. ISSN 1753‑1454.

SIMANAVIČIENĖ, Rūta a Sonata VDOVINSKIENĖ. Selection of Computer-Aided Design Software Systems Using the AHP Method. *Baltic Journal of Modern Computing*. 2023, **11**(2), 272–284. ISSN 2255‑8950. DOI: 10.22364/bjmc.2023.11.2.04.

LARANJEIRO, Nuno a Alexandre Miguel PINTO. *ONDA: ONLine Database Architect* [online]. arXiv:2401.16552, 2024 [cit. 2026‑06‑15]. DOI: 10.48550/arXiv.2401.16552. Dostupné z: <https://doi.org/10.48550/arXiv.2401.16552>

DBEAVER. *DBeaver Documentation* [online]. DBeaver Corp., 2026 [cit. 2026‑06‑09]. Dostupné z: <https://dbeaver.com/docs/dbeaver/>

MYSQL. *MySQL Workbench Manual* [online]. Oracle Corporation, 2026 [cit. 2026‑06‑09]. Dostupné z: <https://dev.mysql.com/doc/workbench/en/>

ORACLE. *Oracle SQL Developer Data Modeler* [online]. Oracle Corporation, 2026 [cit. 2026‑06‑09]. Dostupné z: <https://www.oracle.com/database/sqldeveloper/technologies/sql-data-modeler/>

PGMODELER. *pgModeler — PostgreSQL Database Modeler* [online]. Raphael Araújo e Silva, 2026 [cit. 2026‑06‑09]. Dostupné z: <https://pgmodeler.io/>

POSTGRESQL. *PostgreSQL Documentation* [online]. The PostgreSQL Global Development Group, 2026 [cit. 2026‑06‑09]. Dostupné z: <https://www.postgresql.org/docs/>

CHOTĚNOVSKÝ, Tomáš. *Tvorba datových modelů a generování dat pro předmět Databázové systémy a návrh databází*. Brno, 2023. Bakalářská práce. Mendelova univerzita v Brně. Provozně ekonomická fakulta. Vedoucí práce Pavel Turčínek.

JANDOVÁ, Věra. *AHP - její silné a slabé stránky*. Olomouc, 2012. Diplomová práce. Univerzita Palackého v Olomouci. Přírodovědecká fakulta. Vedoucí práce Jana Talašová.

JEDLIČKA, Jan. *Key-value databázové systémy*. Ostrava, 2024. Diplomová práce. Vysoká škola báňská – Technická univerzita Ostrava. Fakulta elektrotechniky a informatiky. Vedoucí práce Michal Krátký.

KAŠPAR, Zbyněk. *Databázové systémy v praxi*. Olomouc, 2012. Bakalářská práce. Univerzita Palackého v Olomouci. Pedagogická fakulta. Vedoucí práce Jan Kubrický.

SOUKOPOVÁ, Jana. *Vícekriteriální metody hodnocení*. Brno: Masarykova univerzita, 2016. Učební text. Masarykova univerzita. Ekonomicko-správní fakulta. Dostupné z: <https://is.muni.cz/el/1456/jaro2016/BPE_VIMP/um/>

VOHRADSKÝ, Marek. *Použití metod vícekriteriálního rozhodování při řízení podniku*. Plzeň, 2016. Diplomová práce. Západočeská univerzita v Plzni. Fakulta ekonomická. Vedoucí práce Ladislav Lukáš.

CARVALHO, Gonçalo, Sergii MYKOLYSHYN, Bruno CABRAL, Jorge BERNARDINO a Vasco PEREIRA. Comparative Analysis of Data Modeling Design Tools. *IEEE Access*. 2022, **10**, 3351–3365. ISSN 2169‑3536. DOI                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     