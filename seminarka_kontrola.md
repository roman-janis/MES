# 1 Úvod

Návrh databáze předchází samotnou implementaci informačního systému. Kvalita takového datového návrhu značně ovlivňuje spolehlivost, výkon a možnosti dalšího rozšiřování systému. V případě, že při návrhu vzniknou chyby, jejich odstranění je v dalších etapách složité a nákladné. Při návrhu a vývoji databází se proto využívají různé softwarové nástroje, jako například nástroje pro datové modelování, tvorbu ER diagramů, generování SQL skriptů nebo správu databázových schémat. Jednotlivé nástroje se mezi sebou liší rozsahem nabízených funkcí, podporovanými databázemi, možnostmi modelování nebo licenčními podmínkami.
 
Vybrat vhodný nástroj není v praxi často jednoduché. Obvykle se nedá rozhodovat jen podle jednoho kritéria, například podle ceny nebo rozšířenosti nástroje. Většinou do výběru vstupují další kritéria, která se navzájem dostávají do konfliktu. Proto je vhodné použít postup, který umožní jednotlivá kritéria porovnat a následně podle nich posoudit, který z nástrojů je nejvhodnější. Díky tomu nedojde k výběru podle subjektivního názoru, ale ke skutečně podloženému vyhodnocení. Tato práce se proto zaměřuje na porovnání nástrojů pro návrh a vývoj databází. Pro toto porovnání je využita metoda vícekriteriálního rozhodování Analytic Hierarchy Process (AHP). Na ní je pak celý postup hodnocení založen.

Práce tak tvoří teoretický a metodický podklad pro navazující praktické porovnání těchto nástrojů. Na začátku se text věnuje definicím a termínům spojenými s databázovými systémy, datovým modelováním a návrhem databáze, poté vysvětluje princip vícekriteriálního rozhodování a metodu AHP. Na tento rámec navazuje výběr nástrojů a návrh hodnoticích kritérií. S těmi se bude dále pokračovat v praktické části. Výsledné porovnání pak bude pomoci lépe rozhodnout, který nástroj je vhodný pro různé typy použití, a zároveň ukázat, jak se výsledek mění podle změn priorit.

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

Při práci s databázemi je potřeba rozlišovat některé základní pojmy jako jsou data, informace, databáze a systém řízení báze dat.
Za data lze považovat jednotlivá fakta nebo zaznamenané hodnoty (Elmasri a Navathe, 2016; Watt a Eng, 2014). Tyto hodnoty samy o sobě nemusí být nositelem žádného širšího významu.
Informace pak vznikají právě přiřazením významu datům v určitém kontextu. (Elmasri a Navathe, 2016; Watt a Eng, 2014)
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

## 5.2 Relační model

## 5.3 Transformace ER/EER modelu do relačního modelu

## 5.4 Normalizace relačního modelu

# 6 Vícekriteriální rozhodování

## 6.1 Alternativa, kritérium a váha kritéria

## 6.2 Přístupy k odhadu vah kritérií a porovnání alternativ

# 7 Metoda AHP

## 7.1 Saatyho škála a párové porovnání

## 7.2 Kontrola konzistence

## 7.3 Výhody a omezení AHP

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
