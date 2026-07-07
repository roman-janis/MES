# Univerzita Hradec Králové

## Fakulta informatiky a managementu

### Katedra informatiky a kvantitativních metod

&nbsp;

&nbsp;

&nbsp;

# Komparace nástrojů pro návrh a vývoj databázových systémů pomocí AHP

## Teoretická a metodická východiska

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
| **Vedoucí práce:** | Ing. et Ing. Martin Lněnička, Ph.D. |
| **Pracoviště vedoucího:** | Katedra informatiky a kvantitativních metod |

&nbsp;

&nbsp;

Hradec Králové, červen 2026


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Prohlášení

Prohlašuji, že jsem tuto práci vypracoval samostatně a uvedl jsem všechny použité prameny a literaturu. V případě využití nástrojů umělé inteligence jsem plně deklaroval(a) způsob jejich využití při vypracování této práce.

&nbsp;

&nbsp;

V Hradci Králové dne ………………………… &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ……………………………………

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Roman Janiš


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Poděkování

Tímto bych rád poděkoval vedoucímu práce Ing. et Ing. Martinu Lněničkovi, Ph.D., za odborné vedení, věcné připomínky a konzultace, které přispěly ke zpracování této práce.


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Abstrakt

Práce představuje teoretická a metodická východiska porovnání nástrojů pro návrh a vývoj databázových systémů s využitím metody vícekriteriálního rozhodování AHP (Analytic Hierarchy Process). V první části jsou vymezeny základní pojmy z oblasti databázových systémů, popsány fáze návrhu databáze a vysvětleny datové modely používané při návrhu, zejména entitně-relační model a model relační. Druhá část je věnována vícekriteriálnímu rozhodování, vymezení pojmů alternativa, kritérium a váha kritéria a podrobnému výkladu metody AHP, včetně párového porovnávání, Saatyho škály a kontroly konzistence. Třetí část představuje nástroje, které budou předmětem navazující praktické komparace v bakalářské práci, navrhuje hodnoticí kritéria a popisuje metodický rámec dalšího postupu. Výstupem práce je teoretický a metodický základ, na který přímo naváže praktická část práce.

**Klíčová slova:** databázový systém, návrh databází, datové modelování, vícekriteriální rozhodování, Analytic Hierarchy Process.

&nbsp;

# Abstract

This paper presents the theoretical and methodological background of a bachelor thesis focused on the comparison of tools for the design and development of database systems using the Analytic Hierarchy Process, a multi-criteria decision-making method. The first part defines fundamental terms related to database systems, describes the phases of database design and explains the data models used in design, in particular the entity-relationship model and the relational model. The second part addresses multi-criteria decision-making, defines the terms alternative, criterion and criterion weight, and provides a detailed explanation of the AHP method, including pairwise comparison, Saaty's scale and consistency checking. The third part introduces the tools that will be the subject of the follow-up practical comparison in the bachelor thesis, proposes evaluation criteria and describes the methodological framework of further work. The result is a theoretical and methodological foundation on which the practical part of the bachelor thesis will directly build.

**Keywords:** database system, database design, data modelling, multi-criteria decision making, Analytic Hierarchy Process.


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
<w:p><w:pPr><w:pStyle w:val="Nadpisobsahu"/></w:pPr><w:r><w:t>Obsah</w:t></w:r></w:p>
<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/><w:instrText xml:space="preserve"> TOC \o "1-3" \h \z \u </w:instrText><w:fldChar w:fldCharType="separate"/><w:t>Pole obsahu – ve Wordu klikněte do pole pravým tlačítkem a zvolte „Aktualizovat pole", případně stiskněte F9.</w:t><w:fldChar w:fldCharType="end"/></w:r></w:p>
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# 1 Úvod

Návrh databáze obvykle předchází samotné implementaci informačního systému. Kvalita takového datového návrhu značně ovlivňuje spolehlivost, výkon a možnosti dalšího rozšiřování systému. V případě, že při návrhu vzniknou chyby, jejich odstranění je v dalších etapách složité a nákladné. Při návrhu a vývoji databází se proto využívají různé softwarové nástroje, jako například nástroje pro datové modelování, tvorbu ER diagramů, generování SQL skriptů nebo správu databázových schémat. Jednotlivé nástroje se mezi sebou liší rozsahem nabízených funkcí, podporovanými databázemi, možnostmi modelování nebo licenčními podmínkami.

Vybrat vhodný nástroj není v praxi často jednoduché. Obvykle se nedá rozhodovat jen podle jednoho kritéria, například podle ceny nebo rozšířenosti nástroje. Většinou do výběru vstupují další kritéria, která se navzájem dostávají do konfliktu. Proto je vhodné zvolit postup, který umožní jednotlivá kritéria porovnat a následně podle nich rozhodnout, který z nástrojů je nejvhodnější. Díky tomu se do daného hodnocení promítají také osobní názory hodnotitele, ale zároveň to eliminuje riziko čistě intuitivní volby. Tato práce se proto zaměřuje na přípravu teoretických východisek pro porovnání nástrojů pro návrh a vývoj databází. Pro toto hodnocení je použita metoda vícekriteriálního rozhodování Analytic Hierarchy Process (AHP).

Práce tak tvoří teoretický a metodický podklad pro navazující praktické porovnání těchto nástrojů. Na úvod se text práce věnuje definicím a termínům spojeným s databázovými systémy, datovým modelováním a návrhem databáze. Vzápětí vysvětluje princip vícekriteriálního rozhodování a metodu AHP. Na tento přístup navazuje výběr nástrojů a návrh hodnoticích kritérií. Tato kritéria a nástroje budou dále použity v praktické části. Výsledné porovnání pak poskytne podklady pro rozhodnutí, který nástroj je vhodný pro konkrétní scénář nasazení, a zároveň ukáže, jak se výsledek mění při změně priorit.

# 2 Cíl práce a výzkumné otázky

Cílem práce je připravit teoretická a metodická východiska pro porovnání vybraných nástrojů pro návrh a vývoj databázových systémů. K dosažení hlavního cíle je potřeba splnit tyto dílčí cíle:

- vymezit základní pojmy z oblasti databázových systémů, datového modelování a návrhu databáze
- vysvětlit principy vícekriteriálního rozhodování, metodu AHP a její použitelnost pro porovnání softwarových nástrojů
- vybrat a charakterizovat nástroje, které budou předmětem porovnávání, a navrhnout hodnoticí kritéria

Výzkumné otázky navazují na cíl práce a na potřebu postupně připravit teoretický a metodický rámec pro budoucí porovnání nástrojů. Tento rámec zahrnuje vymezení databázových systémů a jejich vývoje, vysvětlení principů vícekriteriálního hodnocení, volbu kritérií a přípravu pro budoucí porovnání. Metoda AHP umožní rozdělit rozhodování na menší přehledné části a přehledně porovnat jak jednotlivá kritéria, tak i jednotlivě hodnocené nástroje.

Tomuto zaměření odpovídají následující výzkumné otázky:
- **VO1:** Jaké klíčové pojmy, modely a postupy se využívají při návrhu a vývoji databázových systémů?
- **VO2:** Jaké principy a postupy nabízí metoda AHP pro porovnání alternativ podle více kritérií?
- **VO3:** Jaká hodnoticí kritéria a jaký postup zvolit pro praktické porovnání nástrojů a jak zdůvodnit jejich výběr?

Odpovědi na uvedené výzkumné otázky postupně tvoří obsah jednotlivých kapitol.

# 3 Metodika práce

Zpracování práce probíhalo v několika navazujících krocích. Nejprve byly vymezeny oblasti, které je třeba popsat tak, aby bylo možné nástroje později porovnat a navrhnout vhodná hodnoticí kritéria. Jednalo se o oblasti databázových systémů, datového modelování, návrhu databáze, vícekriteriálního rozhodování a metody AHP. K těmto oblastem byly následně vyhledány odborné zdroje.

Zdroje byly vybírány tak, aby pokryly nejen celou teoretickou část práce, ale i výběr konkrétních nástrojů. Pro databázové systémy byla jako hlavní zdroj použita publikace Pokorného a Valenty (2020). Pro datové modelování a návrh relačních databází byla využita publikace Chlapka, Kučery a Palovské (2019). Metoda AHP byla zpracována na základě práce Saatyho (1990, 2008) a učebního textu Soukopové (2016).

Dalším krokem byl výběr nástrojů, které budou v práci porovnávány. Při jejich výběru byla využita studie Carvalho et al. (2022), protože se zabývá podobným tématem a porovnává nástroje pro datové modelování jinou metodou. Dále byla použita oficiální dokumentace vybraných nástrojů. Z ní byly převzaty údaje o funkcích, podporovaných databázových platformách, licenčních podmínkách a další podrobnosti. Jako podpůrný zdroj byl použit také článek Simanavičienė a Vdovinskienė (2023), který ukazuje použití metody AHP při výběru softwaru.

Na základě prostudovaných zdrojů byly následně vybrány nástroje a navržena hodnoticí kritéria. V navazující praktické části budou nástroje hodnoceny podle jednotného postupu. Mezi hodnocená kritéria patří například tvorba modelu, převod do logického a fyzického modelu, generování SQL skriptu, reverzní inženýrství, použitelnost a také licenční podmínky. Výsledky budou následně zpracovány metodou AHP.

Samotné porovnání nástrojů proběhne v navazující praktické části pomocí metody AHP. Volba této metody vychází z přehledových studií vícekriteriálního rozhodování (MCDM), které AHP označují za jeden z nejvhodnějších přístupů pro hodnocení softwarových systémů, a to zejména díky její schopnosti kombinovat kvantitativní i kvalitativní kritéria (Velasquez a Hester, 2013; Ishizaka a Labib, 2011). Metoda AHP rozloží rozhodovací problém do hierarchie složené z cíle, kritérií a hodnocených nástrojů. Kritéria i nástroje se vzájemně porovnávají po dvojicích na Saatyho škále a z výsledků se vypočítají váhy a celkové pořadí nástrojů. Součástí bude také analýza citlivosti, sledující, jak se pořadí mění při změně vah kritérií. Pro usnadnění výpočtů může vzniknout jednoduchá podpůrná aplikace.

# 4 Databázové systémy

## 4.1 Základní pojmy

Při práci s databázemi je nutné rozlišovat některé základní pojmy, jako jsou data, informace, databáze a systém řízení báze dat.
Pod pojmem data si lze představit jednotlivá fakta nebo zaznamenané hodnoty (Elmasri a Navathe, 2016). Tyto hodnoty samy o sobě nemusí být nositeli žádného širšího významu (Watt a Eng, 2014). Informace pak vznikají právě přiřazením významu datům v určitém kontextu (Elmasri a Navathe, 2016; Watt a Eng, 2014).
Pojem databáze pak představuje organizovanou sbírku vzájemně souvisejících dat, která jsou uložena tak, aby s nimi bylo možné dále efektivně pracovat (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Watt a Eng, 2014).

Systém řízení báze dat, běžně označovaný jako DBMS, je specializovaný software, který zajišťuje definici, ukládání, manipulaci, zabezpečení a správu dat uložených v databázi (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Spojení databáze s DBMS vytvoří databázový systém (DBS), který usnadňuje definování, vytváření, manipulaci a sdílení databáze mezi různými uživateli a aplikacemi (Elmasri a Navathe, 2016). DBMS v rámci tohoto systému zajišťuje transakční zpracování, obnovení dat po pádu, souběžný přístup více uživatelů i řízení ochrany dat (Pokorný a Valenta, 2020).

Původně se používal především jednoduchý souborový přístup, který měl však řadu problémů a omezení, například v podobě nekonzistentnosti dat při aktualizaci, závislosti na aplikačním programu a na fyzické struktuře, často spojené s redundancí dat (Elmasri a Navathe, 2016). Databázový přístup tyto nedostatky odstraňuje, a to tím, že integruje data do jednoho logického celku a odděluje definici dat od samotných aplikací (Pokorný a Valenta, 2020). Tímto oddělením se získává vyšší bezpečnost, možnost centrálního řízení integritních omezení a možnost sdílení dat mezi více uživateli (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

## 4.2 Schéma databáze, instance a metadata

V teorii databází je třeba rozlišovat mezi schématem databáze a instancí databáze.
Schéma databáze představuje popis struktury uložených dat a zahrnuje určení entit, atributů, vazeb a integritních omezení, která mají data splňovat (Pokorný a Valenta, 2020).
Pojem instance databáze naopak vyjadřuje konkrétní aktuální obsah databáze v určitém čase (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
Toto rozlišení odděluje relativně stabilní strukturální návrh od proměnlivých datových hodnot (Elmasri a Navathe, 2016).

S databázovým systémem souvisí také pojem metadata.
Metadata jsou data o datech. Tato data tedy popisují strukturu databáze, význam atributů, integritní omezení nebo například přístupová práva (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
Metadata bývají ukládána v systémovém katalogu, který slouží jako centrální zdroj informací o databázových objektech (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

Správa a údržba schématu databáze je klíčovou rolí správce databáze (DBA), přičemž změny schématu v průběhu životního cyklu systému musí být pečlivě kontrolovány (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Metadata uložená v systémovém katalogu jsou využívána nejen samotným DBMS pro optimalizaci dotazů a kontrolu přístupových práv, ale také externími nástroji (Elmasri a Navathe, 2016). Tyto nástroje dokážou metadata z katalogu načíst a vizualizovat je ve formě diagramů (Elmasri a Navathe, 2016). Tato vizualizace pak usnadňuje pochopení existující struktury databáze a její další rozvoj (Elmasri a Navathe, 2016).

## 4.3 Funkce DBMS a víceúrovňová architektura

DBMS obvykle poskytuje několik základních skupin funkcí: definici dat, manipulaci s daty, řízení souběžného přístupu více uživatelů, ochranu dat a obnovu po chybě (Pokorný a Valenta, 2020). Pro tyto funkce se používá jazyk DDL (Data Definition Language), který slouží k definici dat, a pak jazyk DML (Data Manipulation Language) určený pro manipulaci s daty. Vedle toho se používá pojem transakce, což je logický celek operací, který má být proveden buď celý, nebo vůbec (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

Další významnou myšlenkou bylo chápat DBMS jako víceúrovňový systém podle modelu ANSI/SPARC (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Tento přístup představuje databázi jako hierarchii abstrakcí, které oddělují externí, konceptuální a interní úroveň (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Ve zprávě výboru ANSI/X3/SPARC z roku 1975 se toto členění upřesňuje takto: externí úroveň odpovídá pohledům jednotlivých skupin uživatelů, konceptuální úroveň představuje globální logický model celé databáze a interní úroveň popisuje fyzické uložení dat (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
Hlavním smyslem tohoto členění je podpora datové nezávislosti, tedy oddělení aplikací a uživatelských pohledů od fyzické implementace databáze (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

Pro následné porovnání nástrojů v této práci je toto rozdělení vhodné proto, že nástroje nepokrývají všechny úrovně databázového systému stejným způsobem (Rosenthal a Reiner, 1994). Některé se zaměřují především na konceptuální nebo logický model, jiné podporují i fyzické prvky konkrétního DBMS, například datové typy, indexy nebo generování SQL skriptů (Carvalho et al., 2022). Při hodnocení nástrojů proto bude vhodné sledovat nejen možnosti vytváření diagramů, ale také podporu přechodu mezi jednotlivými úrovněmi návrhu a implementace (Rosenthal a Reiner, 1994).

## 4.4 Fáze návrhu databáze

Návrh databáze představuje jednu z hlavních fází v rámci životního cyklu vývoje databázového systému a probíhá v několika na sebe navazujících krocích. Přímý přechod k fyzické implementaci tabulek v konkrétním systému může vést k chybám v návrhu, redundanci a omezené rozšiřitelnosti (Carvalho et al., 2022). Z tohoto důvodu se v literatuře standardně rozlišuje konceptuální, logický a fyzický návrh (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Rosenthal a Reiner, 1994).

Konceptuální návrh zachycuje strukturu aplikační domény bez vazby na konkrétní databázový systém (Carvalho et al., 2022; Rosenthal a Reiner, 1994).
V této fázi jsou identifikovány entity, vztahy mezi nimi, atributy a základní integritní omezení (Rosenthal a Reiner, 1994). Výsledkem je konceptuální schéma, které věrně popisuje realitu a je nezávislé na zvoleném DBMS (Carvalho et al., 2022; Pokorný a Valenta, 2020).

Na konceptuální návrh navazuje logický návrh.
V této části se konceptuální model převádí do zvoleného datového modelu, v případě této práce jde zejména o model relační (Rosenthal a Reiner, 1994).
Dochází k návrhu relací, atributů, klíčů, cizích klíčů a integritních omezení (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
Výsledkem je pak logické schéma databáze, které lze implementovat v konkrétním DBMS (Pokorný a Valenta, 2020).

Ve fyzickém návrhu se řeší způsob uložení dat v konkrétním databázovém systému (Pokorný a Valenta, 2020; Rosenthal a Reiner, 1994).
Řeší se zde organizace datových souborů, indexy, výkonové aspekty, optimalizace přístupu a další technické detaily (Rosenthal a Reiner, 1994).
Na rozdíl od konceptuálního a logického návrhu je fyzický návrh silně závislý na konkrétní technologii (Pokorný a Valenta, 2020).

Mezi jednotlivými kroky návrhu existuje zpětná vazba. Pokud se při fyzickém návrhu ukáže, že některé části modelu vedou například k výkonovým problémům, je nutné vrátit se zpět k logickému návrhu (Rosenthal a Reiner, 1994).
Podobně může změna požadavků uživatelů vyvolat úpravu konceptuálního modelu a následně i všech dalších úrovní (Carvalho et al., 2022; Rosenthal a Reiner, 1994).
Návrh databáze proto nelze chápat jako striktně lineární proces, ale jako iterativní postup, v němž se schéma průběžně zpřesňuje, opravuje a reorganizuje (Carvalho et al., 2022; Rosenthal a Reiner, 1994).

Rozdělení návrhu databáze na konceptuální, logickou a fyzickou úroveň tvoří vhodný výchozí bod pro pozdější definici hodnoticích kritérií. Nástroj určený pro návrh databázového systému by měl umožnit zachytit požadavky, převést je do konzistentního schématu a podle potřeby podpořit technickou implementaci v konkrétním databázovém prostředí (Rosenthal a Reiner, 1994). Úroveň podpory těchto kroků představuje důležitý ukazatel kvality daného nástroje (Carvalho et al., 2022; Rosenthal a Reiner, 1994).

# 5 Datové modely

Datový model poskytuje formalizovaný nástroj, který slouží k popisu dat, jejich struktur a vztahů mezi nimi (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Definuje datové objekty a jejich vzájemné vztahy včetně omezení, která se jich týkají (Pokorný a Valenta, 2020). Datový model je zjednodušený popis reality, který je vytvořen tak, aby se podle něj dala navrhnout a implementovat databáze (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

## 5.1 Konceptuální modelování a ER/EER model

### 5.1.1 Konceptuální modelování a základní pojmy ER modelu

Konceptuální modelování slouží k zachycení požadavků aplikační domény, kterou má navrhovaný systém pokrývat, ale bez ohledu na konkrétní databázovou technologii (Carvalho et al., 2022; Elmasri a Navathe, 2016). Jeho cílem je vytvořit přehledný a věrný model reálného světa (Carvalho et al., 2022). V praxi se pro tuto fázi velmi často používá entitně-relační model (ER model) (Chen, 1976), případně jeho rozšířená varianta EER (Elmasri a Navathe, 2016).

Základními pojmy ER modelu jsou entita, entitní množina, vztah a atribut. Za entitu je považován objekt, který je schopen samostatné existence a lze jej jednoznačně odlišit od ostatních objektů (Chen, 1976). Entitní množina je pak množina entit, které jsou stejného typu a mají společné vlastnosti (Chen, 1976). Vztah vyjadřuje vazbu mezi entitami nebo entitními množinami a atribut představuje vlastnost entity nebo vztahu (Chen, 1976).

Vztahy mezi entitami lze popsat například kardinalitou a participací. Kardinalita udává, kolik entit jedné množiny může být ve vztahu k entitě jiné množiny (Elmasri a Navathe, 2016). Typickými případy jsou vazby 1:1, 1:N a M:N. Participace vyjadřuje, zda je účast entity ve vztahu povinná nebo nepovinná (Elmasri a Navathe, 2016). Tyto pojmy jsou důležité nejen na konceptuální úrovni, ale i pro následnou transformaci do relačního modelu (Pokorný a Valenta, 2020).

### 5.1.2 Atributy, EER model a notace

Atributy jsou svázány s doménami, tedy s množinami přípustných hodnot (Elmasri a Navathe, 2016). Rozlišujeme jednoduché a složené atributy, případně i další typy (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Pro jednoznačnou identifikaci entit slouží kandidátní a primární klíče (Elmasri a Navathe, 2016).

Rozšířený ER model (EER) doplňuje základní ER model o supertřídy, podtřídy a dědičnost atributů (Elmasri a Navathe, 2016). EER model je vhodný především tam, kde je potřeba přesněji vystihnout specializaci nebo generalizaci objektů (Elmasri a Navathe, 2016). V praxi se ER/EER model vyjadřuje různými grafickými notacemi, přičemž mezi nejčastější patří Chenova notace, Crow’s Foot a UML (Elmasri a Navathe, 2016; Carvalho et al., 2022).

Pro hodnocení databázových nástrojů je podpora konceptuálního modelování významná hlavně z praktického hlediska. Nástroj by měl umožnit vyjádřit entity, vztahy, kardinality a omezení způsobem, který je srozumitelný jak analytikům, tak i vývojářům (Carvalho et al., 2022).
Jednotlivé nástroje se přitom mohou lišit použitou notací, úrovní podpory EER prvků a možností následného převodu modelu do relačního schématu (Carvalho et al., 2022; Rosenthal a Reiner, 1994).

## 5.2 Relační model

Relační model je založen na relacích, které se v praxi obvykle zobrazují jako tabulky (Elmasri a Navathe, 2016).
Každá relace má své schéma, tedy jméno relace, seznam atributů a jejich domén (Pokorný a Valenta, 2020).
Konkrétní řádky tabulky odpovídají n-ticím (Codd, 1970; Elmasri a Navathe, 2016).
Relační model pracuje s atomickými hodnotami a s přesně vymezenými atributy (Codd, 1970; Elmasri a Navathe, 2016).

Klíče jsou v relačním modelu zásadní.
Primární klíč slouží k jednoznačné identifikaci řádku tabulky (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
Cizí klíč umožňuje vyjádřit vazbu mezi tabulkami a je základem referenční integrity (Watt a Eng, 2014).
Mezi obecné vlastnosti relačních tabulek patří nezávislost na pořadí řádků a sloupců a požadavek na neduplicitu řádků (Codd, 1970; Elmasri a Navathe, 2016).

Relační model je pro tuto práci důležitý také proto, že většina běžně používaných návrhových nástrojů pro databáze směřuje k tvorbě relačního schématu a k práci s SQL databázemi. Při jejich porovnání proto bude důležité, zda nástroj podporuje definici primárních a cizích klíčů, integritních omezení, datových typů a generování nebo zpětné načítání databázového schématu (Carvalho et al., 2022).

## 5.3 Transformace ER/EER modelu do relačního modelu

Při přechodu z konceptuálního modelu k modelu relačnímu se entity obvykle převádějí na tabulky a atributy na sloupce (Chlapek, Kučera a Palovská, 2019).
Vztahy typu 1:N se zpravidla reprezentují pomocí cizího klíče na straně N, zatímco pro vztahy M:N je vyžadováno vytvoření samostatné spojovací tabulky. Specifické případy představují vztahy 1:1, atributy vztahů nebo převod supertříd a podtříd (Elmasri a Navathe, 2016).
Tato transformace je důležitým přechodem mezi konceptuálním a logickým návrhem (Rosenthal a Reiner, 1994). Pokud je tato transformace provedena nekonzistentně, vede k problémům v následné implementaci (Carvalho et al., 2022; Rosenthal a Reiner, 1994).

U nástrojů pro návrh databází je proto důležité, zda převod mezi konceptuálním a relačním modelem pouze vizuálně naznačují, nebo zda tento převod dokážou částečně automatizovat a kontrolovat (Carvalho et al., 2022; Rosenthal a Reiner, 1994).
Automatické generování relačního schématu může práci urychlit, ale je potřeba ověřit, zda nástroj také správně zachází s kardinalitami, vazbami M:N, povinnými atributy a integritními omezeními (Carvalho et al., 2022; Rosenthal a Reiner, 1994).

## 5.4 Normalizace relačního modelu

Normalizace je proces, jehož cílem je odstranit nadbytečnost dat a předcházet anomáliím při vkládání, aktualizaci a mazání údajů (Codd, 1970; Elmasri a Navathe, 2016). Teoretickým základem normalizace jsou funkční závislosti, které určují vztahy mezi atributy a umožňují identifikovat nadbytečnost a anomálie v databázovém schématu (Codd, 1970; Elmasri a Navathe, 2016). Pro tuto práci by mělo být dostačující vysvětlit první, druhou a třetí normální formu.

Normální formy představují soubor pravidel pro návrh relační databáze, jejichž cílem je omezit redundanci dat a snížit riziko nekonzistence. První normální forma vyžaduje, aby atributy obsahovaly pouze atomické hodnoty a aby se v tabulkách nevyskytovaly skupiny, které se opakují (Codd, 1970; Elmasri a Navathe, 2016). Druhá normální forma se zaměřuje na tabulky se složeným klíčem a požaduje, aby každý neklíčový atribut závisel na celém klíči, nikoli pouze na jeho části (Codd, 1970; Elmasri a Navathe, 2016). Třetí normální forma dále odstraňuje tranzitivní závislosti, u nichž jeden neklíčový atribut závisí na jiném neklíčovém atributu (Codd, 1970; Elmasri a Navathe, 2016). Dodržování těchto forem podle Codda (1970) a Elmasriho s Navathem (2016) vede k zajištění základní konzistence relačního schématu. Z toho důvodu by tato pravidla měla respektovat většina nástrojů pro návrh databází.

Normalizace ukazuje mimo jiné, že kvalita návrhového nástroje nespočívá jen v grafické podobě diagramu.
Důležité je, zda nástroj podporuje konzistenci modelu, upozorňuje na chybějící klíče nebo problematické vazby a umožňuje vytvořit návrh, který lze převést do udržitelného relačního schématu. Tato hlediska navazují na pozdější výběr hodnoticích kritérií pro komparaci nástrojů (Carvalho et al., 2022).

# 6 Vícekriteriální rozhodování

Vícekriteriální rozhodování se zabývá situacemi, ve kterých nelze rozhodnout podle jednoho hlediska (Mardani et al., 2015). V běžných rozhodovacích úlohách jsou alternativy obvykle hodnoceny podle více kritérií. Tato kritéria však mohou být ve vzájemném konfliktu (Velasquez a Hester, 2013). Z tohoto důvodu se používají metody, které umožňují tato kritéria systematicky zahrnout do rozhodovacího procesu a výsledek rozhodnutí zdůvodnit (Mardani et al., 2015).

Rozhodovací úloha je běžně popsána množinou variant, množinou hodnoticích kritérií a vztahem mezi nimi (Soukopová, 2016). Varianty představují jednotlivé posuzované možnosti, mezi kterými se rozhoduje. Kritéria určují, z jakých hledisek jsou jednotlivé varianty hodnoceny (Velasquez a Hester, 2013). Hodnocení variant podle jednotlivých kritérií se často zapisuje do kriteriální matice. Tato matice umožňuje zachytit přehledně hodnoty alternativ vzhledem k jednotlivým kritériím (Soukopová, 2016).

S vícekriteriálním rozhodováním souvisejí i pojmy jako ideální a bazální varianta, dominance a nedominované řešení. Ideální varianta je hypotetická varianta, která ve všech kritériích získává nejlepší možné hodnoty (Soukopová, 2016; Velasquez a Hester, 2013). Bazální varianta naopak představuje hypotetickou variantu s nejhoršími hodnotami (Soukopová, 2016). Dominance vyjadřuje vztah mezi dvěma variantami, kdy jedna varianta je alespoň v jednom kritériu lepší a v ostatních není horší než druhá varianta (Soukopová, 2016). Nedominovaná varianta je taková varianta, pro kterou neexistuje jiná varianta lepší alespoň v jednom kritériu a současně ne horší v ostatních (Soukopová, 2016). Tyto pojmy se používají především u metod, které pracují se vzdáleností od ideálního řešení nebo s porovnáváním dominance mezi variantami (Velasquez a Hester, 2013).

Pro tuto práci je důležité zejména vícekriteriální hodnocení variant. Důvodem je navazující část, kde se bude porovnávat konečný seznam databázových nástrojů. Jde tedy o případ, kdy jsou předem dány alternativy a z těchto alternativ je nutné určit nejvhodnější řešení (Mardani et al., 2015; Saaty, 1990). Cílem přitom není označit jeden nástroj za univerzálně nejvhodnější, ale vysvětlit jeho vhodnost vzhledem ke zvoleným kritériím, jejich vahám a uvažovanému použití (Saaty, 2008; Soukopová, 2016).

Při rozhodování o výběru softwarových nástrojů je vícekriteriální přístup vhodný proto, že rozhodnutí obvykle zahrnuje technická, ekonomická a uživatelská hlediska (Mardani et al., 2015; Velasquez a Hester, 2013). U databázových nástrojů jsou obvykle některá kritéria měřitelná přímo, například cena, licence nebo dostupnost pro konkrétní platformu. Jiná kritéria naopak mají popisnou povahu, například přehlednost uživatelského rozhraní, podpora modelování nebo srozumitelnost dokumentace. Vícekriteriální metody pomáhají přehledně spojit všechna důležitá hlediska do jednoho rozhodovacího procesu (Mardani et al., 2015).

## 6.1 Alternativa, kritérium a váha kritéria

Alternativa představuje jednu z možných variant rozhodnutí (Soukopová, 2016). V rámci této práce bude každá alternativa představovat konkrétní softwarový nástroj určený pro návrh a vývoj databázových systémů. Kritérium je hledisko, podle kterého se jednotlivé alternativy posuzují (Soukopová, 2016). Může jít například o funkcionalitu, použitelnost, kompatibilitu s různými DBMS, podporu reverzního inženýrství nebo cenu (Carvalho et al., 2022).

Samotná kritéria lze uspořádat různými způsoby podle potřeb konkrétní rozhodovací úlohy. Základní dělení odlišuje kritéria maximalizační a minimalizační (Soukopová, 2016). U maximalizačních kritérií je požadována co nejvyšší hodnota, například rozsah funkcí nebo počet podporovaných databázových platforem. U minimalizačních kritérií je naopak požadována co nejnižší hodnota, například cena, časová náročnost zavedení nebo složitost práce. Kritéria mohou být kvantitativní nebo kvalitativní, a jejich kombinace je u hodnocení softwaru zcela běžná (Soukopová, 2016; Velasquez a Hester, 2013).

Váha kritéria vyjadřuje jeho relativní význam v rámci rozhodovacího procesu (Saaty, 1990; Soukopová, 2016). Ne všechna kritéria mají stejnou důležitost, a proto je nutné jejich význam určit explicitně. Určení vah kritérií je jedním z klíčových kroků většiny vícekriteriálních metod. Právě váhy často zásadně ovlivňují výsledné pořadí alternativ (Saaty, 1990).

Při volbě vah je důležité vycházet z účelu hodnocení (Saaty, 2008; Soukopová, 2016). V prostředí s omezeným rozpočtem může být cena klíčová, zatímco ve firmě, která už používá určitou databázovou platformu, může mít větší váhu právě její podpora. Stejný nástroj proto může být v jednom rozhodovacím scénáři vhodnější než v jiném. Z tohoto důvodu budou kritéria v navazující práci navázána na modelovou situaci nebo požadavky uživatele (Saaty, 2008).

## 6.2 Přístupy k odhadu vah kritérií a porovnání alternativ

Pro odhadnutí vah jednotlivých kritérií lze použít několik postupů (Saaty, 2008; Soukopová, 2016). Mezi nejznámější jednoduché přístupy patří metoda pořadí nebo bodovací metoda. Tyto metody lze použít jednoduše, ale nejsou dostatečně přesné při popisu toho, jak výrazně je jedna z možností důležitější než druhá. Pokročilejší postupy pracují s párovým porovnáváním kritérií a do této skupiny patří právě i Saatyho metoda, která je s metodou AHP přímo spojena (Saaty, 1990; Soukopová, 2016).

Při hodnocení samotných alternativ umožňuje AHP použít stejný princip párového porovnávání i pro alternativy, a to vzhledem ke každému z dříve stanovených kritérií (Saaty, 2008; Vaidya a Kumar, 2006). Výhodou pak je systematičnost a transparentnost, naopak nevýhodou je vyšší pracnost při větším počtu prvků. Počet porovnání roste s počtem kritérií a alternativ. Proto je vhodné zvolit přiměřený rozsah rozhodovacího modelu (Ishizaka a Labib, 2011).

Z dalších metod vícekriteriálního hodnocení variant jsou rozšířeny především metoda váženého součtu (WSA), metoda TOPSIS a metody založené na outrankingu. Metoda váženého součtu pracuje s normalizovanými hodnotami kritérií a výsledné skóre alternativy vypočítá jako vážený součet (Soukopová, 2016; Velasquez a Hester, 2013). TOPSIS hodnotí alternativy podle jejich vzdálenosti od ideální a bazální varianty (Velasquez a Hester, 2013). Komplexnější strukturou se vyznačuje rodina metod ELECTRE, které pracují s koncepty převahy jedné varianty nad druhou (Mardani et al., 2015; Velasquez a Hester, 2013).

Pro potřeby práce je metoda AHP vhodná ze tří důvodů. Za prvé, AHP umožňuje pracovat současně s kvantitativními i kvalitativními kritérii, a to dokonce bez nutnosti převádět jednotlivá hodnocení na jednotnou měrnou škálu (Ishizaka a Labib, 2011; Saaty, 1990). Za druhé, je postup metody srozumitelný a vysvětlitelný, protože pracuje s hierarchií cíle, kritérií a alternativ (Saaty, 2008). Za třetí, AHP pomocí poměru konzistence (CR) umožňuje zkontrolovat, zda na sebe jednotlivá hodnocení logicky navazují. To je zvlášť užitečné v situacích, kdy párové porovnávání provádí jen jedna osoba (Ishizaka a Labib, 2011; Saaty, 1990).

# 7 Metoda AHP

Metoda *Analytic Hierarchy Process* (AHP) patří mezi nejznámější metody vícekriteriálního rozhodování (Ishizaka a Labib, 2011; Vaidya a Kumar, 2006). Jejím autorem je Thomas L. Saaty. Podstata této metody spočívá v rozdělení složitého rozhodovacího problému do přehledné hierarchie, která obsahuje hlavní cíl, kritéria, případně subkritéria a jednotlivé alternativy (Saaty, 1990; Saaty, 2008). Díky tomuto rozkladu lze lépe porozumět struktuře rozhodovací úlohy a následně jednotlivé prvky systematicky porovnat (Vaidya a Kumar, 2006).

Na nejvyšší úrovni hierarchie se nachází hlavní cíl rozhodování, například výběr nejvhodnějšího databázového nástroje (Saaty, 2008). Pod ním se nacházejí kritéria, případně subkritéria, a na nejnižší úrovni stojí jednotlivé alternativy. Hlavní myšlenkou metody je porovnat dva prvky na stejné úrovni a určit jejich relativní důležitost vzhledem k nadřazenému prvku (Saaty, 1990; Saaty, 2008).

AHP se využívá hlavně v případech, kdy je potřeba při rozhodování spojit různé typy kritérií, například technické parametry, ekonomické ukazatele a kritéria, která se hodnotí spíše subjektivně nebo kvalitativně (Ishizaka a Labib, 2011; Saaty, 1990). Pro tuto práci je tato metoda vhodná, protože jednotlivé nástroje pro návrh a vývoj databázových systémů nelze hodnotit jen kvantitativně jednou měřitelnou veličinou. Kromě ceny nebo podpory konkrétního DBMS je třeba zohlednit i další vlastnosti – například jaké modelovací funkce nabízí, jak se s ním pracuje, jak kvalitní je dokumentace, zda podporuje reverzní inženýrství a jaké možnosti poskytuje pro generování SQL skriptů. Přehledové studie ukazují, že AHP se využívá v mnoha různých typech rozhodovacích úloh a je vhodná i pro situace, kdy je potřeba vybírat mezi softwarovými systémy (Ho, 2008; Simanavičienė a Vdovinskienė, 2023; Vaidya a Kumar, 2006).

Typický postup AHP lze shrnout do několika kroků. Nejprve je vymezen cíl rozhodování a sestavena hierarchie kritérií a alternativ (Saaty, 2008). Poté se provedou párová porovnání kritérií vzhledem k cíli a párová porovnání alternativ vzhledem ke každému kritériu (Saaty, 1990). Z těchto porovnání se vypočítají lokální priority a ověří se konzistence úsudků. Nakonec se lokální váhy agregují do celkového pořadí alternativ (Ishizaka a Labib, 2011; Saaty, 2008).

## 7.1 Saatyho škála a párové porovnání

Při párovém porovnávání se používá Saatyho škála. Základní hodnoty této škály jsou 1, 3, 5, 7 a 9, které vyjadřují stejnou důležitost, mírnou, silnou, velmi silnou až absolutní preferenci (Saaty, 1990; Saaty, 2008). Sudé hodnoty 2, 4, 6, 8 jsou chápány jako mezistupně. Pokud je jeden prvek méně významný než druhý, použije se převrácená hodnota (Ishizaka a Labib, 2011; Saaty, 1990). Hodnota 1 tedy znamená rovnocennost dvou prvků, zatímco hodnota 9 vyjadřuje krajní převahu jednoho prvku nad druhým.

Výsledkem párového porovnání je čtvercová reciproční matice, označovaná jako Saatyho matice (Saaty, 1990). Reciproční povaha matice znamená, že pokud je prvek A vůči prvku B hodnocen hodnotou 5, pak opačné porovnání B vůči A má hodnotu 1/5 (Ishizaka a Labib, 2011; Saaty, 2008). Hlavní diagonála matice obsahuje hodnoty 1, protože každý prvek je sám se sebou stejně důležitý.

Z této matice se následně vypočítají lokální váhy. V odborné literatuře se objevují různé způsoby výpočtu vah v metodě AHP, například postup založený na vlastním vektoru nebo metoda využívající geometrický průměr řádků (Ishizaka a Labib, 2011; Saaty, 1990). Výsledkem výpočtu je vektor priorit. Hodnoty vektoru priorit vyjadřují relativní význam porovnávaných prvků (Saaty, 1990; Saaty, 2008). U kritérií tyto hodnoty představují jejich váhy, u alternativ pak jejich lokální hodnocení vzhledem ke konkrétnímu kritériu.

Pro tuto práci je důležité, že párové porovnávání umožňuje hodnotiteli vyjadřovat preference postupně a přehledně. Místo toho, aby musel přímo přiřazovat přesné váhy všem kritériím, posuzuje vždy jen dvojici prvků a rozhoduje, který z nich je vzhledem k danému cíli nebo kritériu důležitější (Saaty, 2008). To je užitečné zejména u kritérií, která nejsou přímo měřitelná, například přehlednost prostředí nebo kvalita podpory modelování (Saaty, 1990).

## 7.2 Kontrola konzistence

Protože párové porovnávání vychází z lidského úsudku, není vždy dokonale konzistentní. Součástí metody AHP je proto kontrola konzistence. K tomu slouží *Consistency Index* (CI), *Random Consistency Index* (RI) a *Consistency Ratio* (CR) (Ishizaka a Labib, 2011; Saaty, 1990). V praxi se uvažuje, že hodnota CR menší než 0,1 značí přijatelnou úroveň konzistence. Vyšší hodnoty poměru konzistence (CR) obvykle vedou k přehodnocení porovnání (Saaty, 1990; Saaty, 2008).

Konzistence ověřuje, zda jsou jednotlivé úsudky hodnotící osoby vzájemně logické a v souladu a zda si navzájem neodporují (Ishizaka a Labib, 2011; Saaty, 2008). Pokud je například kritérium A výrazně důležitější než kritérium B a kritérium B je důležitější než kritérium C, potom by mělo být kritérium A zároveň důležitější než kritérium C. Menší odchylky jsou při rozhodování přirozené, příliš vysoká nekonzistence však snižuje důvěryhodnost výsledků (Saaty, 1990; Saaty, 2008).

Možnost ověřit konzistenci je jedním z důvodů, proč je AHP pro tuto práci vhodnější než jednodušší bodovací postup. Při hodnocení databázových nástrojů bude část úsudků založena na kvalitativním posouzení, například u použitelnosti nebo přehlednosti práce s modelem. Ukazatel CR umožňuje ověřit, zda jsou tato porovnání vnitřně soudržná, a případně se k problematickým porovnáním vrátit (Ishizaka a Labib, 2011; Saaty, 1990; Saaty, 2008).

## 7.3 Výhody a omezení AHP

Výhody metody AHP byly stručně naznačeny již v kapitole 6.2, a to možnost kombinovat kvantitativní i kvalitativní kritéria, srozumitelnost postupu a kontrola konzistence úsudků. Následující text pak tyto výhody rozvádí a doplňuje je o další přínosy metody a uvádí i její hlavní omezení. Metoda současně umožňuje analýzu citlivosti, tedy sledování dopadu změny vah kritérií na výsledné pořadí (Ho, 2008; Saaty, 2008). To je důležité zejména tehdy, když jsou výsledky citlivé na malé změny preferencí a kdy je třeba ověřit stabilitu doporučení.

Nevýhodou metody je pracnost při větším počtu kritérií a alternativ a jistá míra subjektivity, která je s párovým porovnáváním spojena (Ishizaka a Labib, 2011; Saaty, 2008). Pokud je v modelu mnoho prvků, počet potřebných porovnání rychle roste. Hodnotitel pak může být zatížen opakováním podobných rozhodnutí (Ishizaka a Labib, 2011). Proto je vhodné udržet počet kritérií i alternativ v přiměřeném rozsahu a jasně vymezit význam jednotlivých kritérií.

V odborné literatuře se diskutuje jev *rank reversal*, tedy možná změna pořadí alternativ při přidání nebo odebrání varianty z modelu (Ishizaka a Labib, 2011; Saaty, 2008; Vaidya a Kumar, 2006). Tento problém neznamená, že AHP nelze použít, ale ukazuje, že výsledky je třeba interpretovat s ohledem na zvolený soubor alternativ a nastavení modelu. V navazující praktické části proto bude důležité jasně zdůvodnit, proč byly vybrány právě dané nástroje a jaké požadavky reprezentují.

V souvislosti s výběrem databázového nástroje je AHP užitečná tím, že umožňuje oddělit stanovení vah kritérií od samotného hodnocení alternativ (Catak et al., 2012; Ebrahimi a Taheri, 2015; Simanavičienė a Vdovinskienė, 2023). Nejprve je možné určit, jak významná je například funkcionalita, použitelnost, kompatibilita, cena nebo podpora vývojového procesu, a teprve poté hodnotit jednotlivé nástroje vůči těmto kritériím (Saaty, 1990). Díky tomu je výsledné pořadí zdůvodněno explicitně, nikoli pouze celkovým dojmem.

# 8 Nástroje pro návrh a vývoj databází

Výběr nástrojů pro porovnání vycházel nejprve z přehledu dostupných nástrojů pro návrh a vývoj databází. Jako jeden z podkladů byla využita studie Carvalho et al. (2022), která hodnotila sedmnáct nástrojů pro datové modelování. Ze studie vyplývá, že nabídka těchto nástrojů je velmi široká a obsahuje nástroje online i desktopové, bezplatné i komerční a také nástroje zaměřené na různé databázové platformy. Příkladem online nástroje je ONDA vyvinutý na Univerzitě v Coimbře (Laranjeiro a Pinto, 2024), který však do výběru zařazen nebyl, protože práce se soustředí na plnohodnotné desktopové nástroje. Dalším podkladem byla oficiální online dokumentace vybraných nástrojů, ze které byly ověřeny jejich základní funkce, podporované databázové platformy a licenční podmínky. Pro posouzení významu jednotlivých databázových platforem byl využit také žebříček DB-Engines (2026).

Na základě těchto podkladů byly pro další práci vybrány čtyři nástroje: Oracle SQL Developer Data Modeler, DBeaver Community Edition, MySQL Workbench Community Edition a pgModeler. Při výběru bylo zohledněno, zda nástroj podporuje návrh databáze, zda je dostupný v bezplatné nebo volně testovatelné verzi a zda vhodně doplňuje ostatní vybrané nástroje. Oracle SQL Developer Data Modeler je zaměřený hlavně na Oracle Database, MySQL Workbench na MySQL, pgModeler na PostgreSQL a DBeaver představuje univerzálnější nástroj podporující více DBMS. Tři z těchto nástrojů (Oracle SQL Developer Data Modeler, MySQL Workbench a pgModeler) jsou uvedeny také ve studii Carvalho et al. (2022), přičemž pgModeler v jejich hodnocení dosáhl ze všech sedmnácti posuzovaných nástrojů nejlepšího výsledku. DBeaver byl do výběru zařazen navíc jako univerzální nástroj podporující více DBMS, který v původní studii chybí. Díky tomu bude možné pozdější výsledky alespoň částečně porovnat s již publikovanou studií. Volba databázových platforem vychází také z jejich rozšířenosti. Oracle Database, MySQL a PostgreSQL patří podle žebříčku DB-Engines (2026) mezi významné relační databázové systémy. Do úvahy byl brán také Microsoft SQL Server, avšak nakonec nebyl zařazen, protože práce se zaměřuje na nástroje s velkou podporou databázového modelování a zároveň chce zachovat přiměřený počet alternativ pro AHP. U univerzálních nástrojů bude při hodnocení sledováno také to, zda umožňují práci s více databázovými platformami, případně i s nerelačními databázemi.

Základní charakteristiky vybraných nástrojů shrnuje tabulka 1.

| Nástroj | Vydavatel | Licence | Primární DBMS | Klíčové funkce |
|---|---|---|---|---|
| Oracle SQL Developer Data Modeler | Oracle Corporation | Freeware | Oracle Database | Logický, relační, fyzický a multidimenzionální model; forward/reverse engineering |
| DBeaver Community Edition | DBeaver Corp. | Open-source (Apache 2.0) | Multi-DBMS | ER diagramy, SQL editor, prohlížeč dat, DDL export |
| MySQL Workbench Community Edition | Oracle Corporation | Open-source (GPLv2) | MySQL | EER modelování, forward/reverse engineering, synchronizace s živou databází |
| pgModeler | Raphael Araújo e Silva | Open-source (GPLv3) | PostgreSQL | Grafický návrh schémat, generování SQL, reverzní inženýrství, validace modelu |

*Tabulka 1 – Základní charakteristiky vybraných nástrojů (vlastní zpracování podle Oracle, 2026; DBeaver, 2026; MySQL, 2026; pgModeler, 2026)*

## 8.1 Oracle SQL Developer Data Modeler

Oracle SQL Developer Data Modeler je bezplatný grafický nástroj společnosti Oracle pro modelování dat. Podporuje logické, relační, fyzické, multidimenzionální a typové modely, nabízí forward i reverse engineering a integraci se širším portfoliem Oracle SQL Developer. Jako primární databázová platforma je preferována Oracle Database, nástroj však umožňuje pracovat i s dalšími systémy (Oracle, 2026). Pro účely navazující bakalářské práce bude testována verze 24.3.

## 8.2 DBeaver Community Edition

DBeaver je open-source univerzální databázový nástroj s podporou širokého spektra DBMS (PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, SQLite a další). Nabízí editor SQL, prohlížeč dat, vizualizaci databázových struktur pomocí ER diagramů a generování DDL skriptů. Pokročilejší funkce, například datové generátory nebo vizuální dotazování, jsou dostupné v komerční edici (DBeaver, 2026). Pro účely navazující bakalářské práce bude testována verze 26.0 Community Edition.

## 8.3 MySQL Workbench Community Edition

MySQL Workbench je oficiální nástroj společnosti Oracle pro práci s databází MySQL. Sjednocuje v jednom prostředí návrh databáze (EER diagramy), správu serveru, modelování, forward i reverse engineering a SQL vývoj. Podporuje synchronizaci modelu s živou databází a export modelu do DDL skriptu (MySQL, 2026). Pro účely navazující bakalářské práce bude testována verze 8.0.

## 8.4 pgModeler

pgModeler, jehož název vychází z označení PostgreSQL Database Modeler, je open-source nástroj zaměřený přímo na databázi PostgreSQL. Umožňuje grafický návrh schémat, generování SQL skriptů, reverzní inženýrství, validaci modelu a porovnávání modelu s živou databází (pgModeler, 2026). Cílovou databázovou platformou nástroje je PostgreSQL, jehož oficiální dokumentace popisuje podporované datové typy a syntaxi SQL, vůči nimž pgModeler validuje generované skripty (PostgreSQL, 2026). Pro účely navazující bakalářské práce bude testována stabilní verze 1.1.

# 9 Návrh hodnoticích kritérií

Při vytváření kritérií pro hodnocení je potřeba zohlednit, že nástroje budou porovnávány podle toho, jak dokážou podpořit návrh a vývoj databáze, nikoliv pouze podle toho, jak zvládají její provoz a správu. Hodnoticí kritéria vycházejí ze studie Carvalho et al. (2022) jak už bylo dříve uvedeno. Tato studie porovnávala nástroje pro datové modelování podle kategorií, jako jsou funkcionalita, provozní vlastnosti softwaru, dokumentace a komunitní podpora. Předkládaná práce toto členění přebírá a rozšiřuje ho o kritéria specifická pro návrh databázových systémů. U kritérií, která nelze vyjádřit číselně, se použije kvalitativní hodnocení podle zkušenosti a každé porovnání se krátce zdůvodní.

Přehled osmi navržených pracovních kritérií uvádí tabulka 2.

| ID | Název kritéria | Typ kritéria | Způsob a zdroj hodnocení |
|---|---|---|---|
| K1 | Funkcionalita | maximalizační | dokumentace nástroje |
| K2 | Použitelnost | maximalizační | kvalitativní hodnocení |
| K3 | Kompatibilita s DBMS | maximalizační | počet oficiálně podporovaných DBMS |
| K4 | Forward engineering | maximalizační | generování DDL |
| K5 | Reverse engineering | maximalizační | import z existující DB |
| K6 | Dokumentace a komunitní podpora | maximalizační | kvalitativní hodnocení |
| K7 | Import a export modelu | maximalizační | dokumentace a podporované formáty |
| K8 | Náklady a licenční omezení | minimalizační | typ licence, omezení bezplatné verze, celková cena |

*Tabulka 2 – Přehled navržených hodnoticích kritérií (vlastní zpracování na základě Carvalho et al., 2022)*

Význam jednotlivých kritérií je blíže popsán níže.

**K1 Funkcionalita.** Hodnotí se, kolik úrovní modelu nástroj podporuje (konceptuální, logický, fyzický), zda umí validovat a jaké databázové objekty podporuje – například tabulky, pohledy, indexy nebo triggery.

**K2 Použitelnost.** Hodnotí se, jak snadno se nástroj používá, jak přehledné je grafické prostředí a jak jednoduše se provádějí běžné úkony, jako je přidání entity, úprava atributu nebo vytvoření vztahu.

**K3 Kompatibilita s DBMS.** Hodnotí se počet databázových systémů, s nimiž nástroj umí oficiálně pracovat.

**K4 Forward engineering.** Hodnotí se, jestli a jak nástroj z navrženého modelu vygeneruje funkční DDL skript nebo schéma databáze. Výsledek se ověřuje vygenerováním a testem výsledného skriptu.

**K5 Reverse engineering.** Hodnotí se schopnost nástroje sestavit model zpětně z existující databáze, tedy naimportovat její strukturu. Ověřuje se to importem z existující databáze.

**K6 Dokumentace a komunitní podpora.** Hodnotí se množství a aktuálnost oficiální dokumentace nástroje a zároveň dostupnost podpory ze strany komunity. Zároveň se zjišťuje, jak často nástroj dostává aktualizace.

**K7 Import a export modelu.** Hodnotí se, jaké formáty importu a exportu nástroj podporuje a jestli umí pracovat s verzovacím systémem.

**K8 Náklady a licenční omezení.** Hodnotí se druh licence nástroje (open-source, freeware, komerční), případná omezení bezplatné verze a celková cena zavedení nástroje do provozu.

# 10 Závěry a doporučení

Cíl práce, tedy zpracování teoretických a metodických východisek pro praktickou část, byl naplněn. Odpovědi na výzkumné otázky lze stručně shrnout takto:

- **K VO1:** Byly vymezeny klíčové pojmy databázových systémů (data, DBMS, schéma, instance, metadata), popsány fáze návrhu databáze (konceptuální, logický, fyzický) a vysvětleny datové modely používané v praxi, zejména ER/EER a relační model spolu s normalizací.
- **K VO2:** Metoda AHP byla popsána jak z hlediska principu (hierarchie cíl–kritéria–alternativy), tak z hlediska postupu (párové porovnání s využitím Saatyho škály, výpočet vah, kontrola konzistence pomocí CR). Bylo zdůvodněno, proč je AHP vhodná pro porovnání softwarových nástrojů.
- **K VO3:** Nakonec byly vybrány čtyři nástroje (Oracle SQL Developer Data Modeler, DBeaver CE, MySQL Workbench CE a pgModeler) a navrženo celkem osm hodnoticích kritérií (K1–K8). Výběr nástrojů a kritérií byl zdůvodněn s oporou o studii Carvalho et al. (2022) a kritéria byla rozšířena o specifika databázového modelování. Samotné porovnání bude realizováno metodou AHP, která umožňuje párové hodnocení jak kritérií, tak i nástrojů. Součástí postupu bude také syntéza výsledných priorit a následná analýza citlivosti.

Na tento postup naváže praktické porovnání v následující práci. Každý nástroj bude prakticky ověřen a hodnocen dle kritérií K1–K8. U kvalitativních kritérií K2 a K6 bude párové porovnání doplněno o slovní zdůvodnění, proto, aby bylo hodnocení pochopitelné. Výsledky budou ověřeny analýzou citlivosti pro váhy K1 a K8. Případně bude navržena jednoduchá podpůrná aplikace pro výpočet vah.


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Seznam zdrojů

CARVALHO, Gonçalo, Sergii MYKOLYSHYN, Bruno CABRAL, Jorge BERNARDINO a Vasco PEREIRA. Comparative Analysis of Data Modeling Design Tools. *IEEE Access*. 2022, **10**, 3351-3365. ISSN 2169-3536. DOI: 10.1109/ACCESS.2021.3139071.

CATAK, F. Ozgur, Servet KARABAS a Serkan YILDIRIM. Fuzzy Analytic Hierarchy Based DBMS Selection in Turkish National Identity Card Management Project. *International Journal of Information Sciences and Techniques*. 2012, **2**(4), 29–38. DOI: 10.5121/ijist.2012.2403.

CHEN, Peter Pin-Shan. The entity-relationship model—toward a unified view of data. *ACM Transactions on Database Systems*. 1976, **1**(1), 9–36. ISSN 0362-5915. DOI: 10.1145/320434.320440.

CHLAPEK, Dušan, Jan KUČERA a Helena PALOVSKÁ. *Datové modelování a návrh relační databáze: Sbírka řešených úloh*. Praha: Vysoká škola ekonomická v Praze, Nakladatelství Oeconomica, 2019. ISBN 978-80-245-2331-6.

CODD, Edgar F. A relational model of data for large shared data banks. *Communications of the ACM*. 1970, **13**(6), 377–387. ISSN 0001-0782. DOI: 10.1145/362384.362685.

DBEAVER. *DBeaver Documentation* [online]. DBeaver Corp., 2026 [cit. 2026-06-09]. Dostupné z: <https://dbeaver.com/docs/dbeaver/>

DB-ENGINES. *DB-Engines Ranking* [online]. solid IT gmbh, 2026 [cit. 2026-06-14]. Dostupné z: <https://db-engines.com/en/ranking>

EBRAHIMI, Seyed Babak a Maryam TAHERI. Selection of Database Management System with Fuzzy-AHP for Electronic Medical Record. *I.J. Information Engineering and Electronic Business*. 2015, **7**(5), 1–9. DOI: 10.5815/ijieeb.2015.05.01.

ELMASRI, Ramez a Shamkant B. NAVATHE. *Fundamentals of Database Systems*. 7th ed. Boston: Pearson, 2016. ISBN 978-0-13-397077-7.

HO, William. Integrated analytic hierarchy process and its applications – a literature review. *European Journal of Operational Research*. 2008, **186**(1), 211–228. ISSN 0377-2217. DOI: 10.1016/j.ejor.2007.01.004.

ISHIZAKA, Alessio a Ashraf LABIB. Review of the main developments in the Analytic Hierarchy Process. *Expert Systems with Applications*. 2011, **38**(11), 14336–14345. ISSN 0957-4174. DOI: 10.1016/j.eswa.2011.04.143.

LARANJEIRO, Nuno a Alexandre Miguel PINTO. *ONDA: ONLine Database Architect* [online]. arXiv:2401.16552, 2024 [cit. 2026-06-15]. DOI: 10.48550/arXiv.2401.16552. Dostupné z: <https://doi.org/10.48550/arXiv.2401.16552>

MARDANI, Abbas, Ahmad JUSOH, Khalil MD NOR, Zainab KHALIFAH, Norhayati ZAKWAN a Alireza VALIPOUR. Multiple criteria decision-making techniques and their applications – a review of the literature from 2000 to 2014. *Economic Research – Ekonomska Istraživanja*. 2015, **28**(1), 516–571. ISSN 1331-677X. DOI: 10.1080/1331677X.2015.1075139.

MYSQL. *MySQL Workbench Manual* [online]. Oracle Corporation, 2026 [cit. 2026-06-09]. Dostupné z: <https://dev.mysql.com/doc/workbench/en/>

ORACLE. *Oracle SQL Developer Data Modeler* [online]. Oracle Corporation, 2026 [cit. 2026-06-09]. Dostupné z: <https://www.oracle.com/database/sqldeveloper/technologies/sql-data-modeler/>

PGMODELER. *pgModeler – PostgreSQL Database Modeler* [online]. Raphael Araújo e Silva, 2026 [cit. 2026-06-09]. Dostupné z: <https://pgmodeler.io/>

POKORNÝ, Jaroslav a Michal VALENTA. *Databázové systémy*. Praha: České vysoké učení technické v Praze, 2020. ISBN 978-80-01-06708-6.

POSTGRESQL. *PostgreSQL Documentation* [online]. The PostgreSQL Global Development Group, 2026 [cit. 2026-06-09]. Dostupné z: <https://www.postgresql.org/docs/>

ROSENTHAL, Arnon a David REINER. Tools and Transformations — Rigorous and Otherwise — for Practical Database Design. *ACM Transactions on Database Systems*. 1994, **19**(2), 167-211. ISSN 0362-5915. DOI: 10.1145/176567.176568.

SAATY, Thomas L. How to make a decision: The Analytic Hierarchy Process. *European Journal of Operational Research*. 1990, **48**(1), 9-26. ISSN 0377-2217.

SAATY, Thomas L. Decision making with the analytic hierarchy process. *International Journal of Services Sciences*. 2008, **1**(1), 83-98. ISSN 1753-1454.

SIMANAVIČIENĖ, Rūta a Sonata VDOVINSKIENĖ. Selection of Computer-Aided Design Software Systems Using the AHP Method. *Baltic Journal of Modern Computing*. 2023, **11**(2), 272-284. ISSN 2255-8950. DOI: 10.22364/bjmc.2023.11.2.04.

SOUKOPOVÁ, Jana. *Vícekriteriální metody hodnocení* [online]. Brno: Masarykova univerzita, Ekonomicko-správní fakulta, 2016. Učební text [cit. 2026-06-09]. Dostupné z: <https://is.muni.cz/el/1456/jaro2016/BPE_VIMP/um/>

VAIDYA, Omkarprasad S. a Sushil KUMAR. Analytic hierarchy process: An overview of applications. *European Journal of Operational Research*. 2006, **169**(1), 1–29. ISSN 0377-2217. DOI: 10.1016/j.ejor.2004.04.028.

VELASQUEZ, Mark a Patrick T. HESTER. An Analysis of Multi-Criteria Decision Making Methods. *International Journal of Operations Research*. 2013, **10**(2), 56–66. ISSN 1813-713X.

WATT, Adrienne a Nelson ENG. *Database Design* [online]. 2nd ed. Victoria: BCcampus, 2014 [cit. 2026-06-18]. Dostupné z: <https://opentextbc.ca/dbdesign01/>
