PARAGRAPHS 202 TABLES 3 SECTIONS 1
HEADINGS
0: [Heading 1] Univerzita Hradec Králové
1: [Heading 2] Fakulta informatiky a managementu
2: [Heading 3] Katedra informatiky a kvantitativních metod
6: [Heading 1] Komparace nástrojů pro návrh a vývoj databázových systémů pomocí AHP
7: [Heading 2] Teoretická východiska – práce
15: [Heading 1] Prohlášení
22: [Heading 1] Abstrakt
26: [Heading 1] Abstract
30: [TOC Heading] Obsah
74: [Heading 1] 1 Úvod
78: [Heading 1] 2 Cíl práce a výzkumné otázky
86: [Heading 1] 3 Metodika práce
92: [Heading 1] 4 Databázové systémy
93: [Heading 2] 4.1 Základní pojmy
97: [Heading 2] 4.2 Schéma databáze, instance a metadata
101: [Heading 2] 4.3 Funkce DBMS a víceúrovňová architektura
105: [Heading 2] 4.4 Fáze návrhu databáze
112: [Heading 1] 5 Datové modely
114: [Heading 2] 5.1 Konceptuální modelování a ER/EER model
115: [Heading 3] 5.1.1 Konceptuální modelování a základní pojmy ER modelu
119: [Heading 3] 5.1.2 Atributy, EER model a notace
123: [Heading 2] 5.2 Relační model
127: [Heading 2] 5.3 Transformace ER/EER modelu do relačního modelu
130: [Heading 2] 5.4 Normalizace relačního modelu
134: [Heading 1] 6 Vícekriteriální rozhodování
135: [Heading 2] 6.1 Alternativa, kritérium a váha kritéria
136: [Heading 2] 6.2 Přístupy k odhadu vah kritérií a porovnání alternativ
137: [Heading 1] 7 Metoda AHP
138: [Heading 2] 7.1 Saatyho škála a párové porovnání
139: [Heading 2] 7.2 Kontrola konzistence
140: [Heading 2] 7.3 Výhody a omezení AHP
141: [Heading 1] 8 Nástroje pro návrh a vývoj databází
147: [Heading 2] 8.1 Oracle SQL Developer Data Modeler
149: [Heading 2] 8.2 DBeaver Community Edition
151: [Heading 2] 8.3 MySQL Workbench Community Edition
153: [Heading 2] 8.4 pgModeler
155: [Heading 1] 9 Návrh hodnoticích kritérií
168: [Heading 1] 10 Závěry a doporučení
175: [Heading 1] Seznam zdrojů
176: [Heading 2] Tištěné zdroje
192: [Heading 2] Internetové zdroje
TEXT
[0] Univerzita Hradec Králové
[1] Fakulta informatiky a managementu
[2] Katedra informatiky a kvantitativních metod
[6] Komparace nástrojů pro návrh a vývoj databázových systémů pomocí AHP
[7] Teoretická východiska – práce
[9] Práce v předmětu KRCR-MES Metodologický seminář
[14] Hradec Králové, červen 2026
[15] Prohlášení
[16] Prohlašuji, že jsem tuto práci vypracoval samostatně a uvedl jsem všechny použité prameny a literaturu.
[19] V Hradci Králové dne …………………………           ……………………………………
[20] Roman Janiš
[22] Abstrakt
[23] <doplnit>
[24] Klíčová slova: databázový systém, návrh databází, datové modelování, vícekriteriální rozhodování, Analytic Hierarchy Process.
[26] Abstract
[27] <doplnit>
[28] Keywords: database system, database design, data modelling, multi-criteria decision making, Analytic Hierarchy Process.
[30] Obsah
[31] Univerzita Hradec Králové	1
[32] Fakulta informatiky a managementu	1
[33] Katedra informatiky a kvantitativních metod	1
[34] Komparace nástrojů pro návrh a vývoj databázových systémů pomocí AHP	1
[35] Teoretická východiska – práce	1
[36] Prohlášení	3
[37] Poděkování	4
[38] Abstrakt	5
[39] Abstract	5
[40] 1 Úvod	8
[41] 2 Cíl práce a výzkumné otázky	8
[42] 3 Metodika práce	9
[43] 4 Databázové systémy	10
[44] 4.1 Základní pojmy	10
[45] 4.2 Schéma databáze, instance a metadata	11
[46] 4.3 Funkce DBMS a víceúrovňová architektura	11
[47] 4.4 Fáze návrhu databáze	12
[48] 5 Datové modely	13
[49] 5.1 Konceptuální modelování a ER/EER model	13
[50] 5.1.1 Konceptuální modelování a základní pojmy ER modelu	13
[51] 5.1.2 Atributy, EER model a notace	14
[52] 5.2 Relační model	14
[53] 5.3 Transformace ER/EER modelu do relačního modelu	15
[54] 5.4 Normalizace relačního modelu	15
[55] 6 Vícekriteriální rozhodování	16
[56] 6.1 Alternativa, kritérium a váha kritéria	16
[57] 6.2 Přístupy k odhadu vah kritérií a porovnání alternativ	16
[58] 7 Metoda AHP	16
[59] 7.1 Saatyho škála a párové porovnání	16
[60] 7.2 Kontrola konzistence	16
[61] 7.3 Výhody a omezení AHP	16
[62] 8 Nástroje pro návrh a vývoj databází	16
[63] 8.1 Oracle SQL Developer Data Modeler	18
[64] 8.2 DBeaver Community Edition	18
[65] 8.3 MySQL Workbench Community Edition	18
[66] 8.4 pgModeler	18
[67] 9 Návrh hodnoticích kritérií	19
[68] 10 Závěry a doporučení	20
[69] Seznam zdrojů	22
[70] Tištěné zdroje	22
[71] Internetové zdroje	23
[74] 1 Úvod
[75] Návrh databáze předchází samotnou implementaci informačního systému. Kvalita takového datového návrhu značně ovlivňuje spolehlivost, výkon a možnosti dalšího rozšiřování systému. V případě, že při návrhu vzniknou chyby, jejich odstranění je v dalších etapách složité a nákladné. Při návrhu a vývoji databází se proto využívají různé softwarové nástroje, jako například nástroje pro datové modelování, tvorbu ER diagramů, generování SQL skriptů nebo správu databázových schémat. Jednotlivé nástroje se mezi sebou liší rozsahem nabízených funkcí, podporovanými databázemi, možnostmi modelování nebo licenčními podmínkami.
[76] Vybrat vhodný nástroj není v praxi často jednoduché. Obvykle se nedá rozhodovat jen podle jednoho kritéria, například podle ceny nebo rozšířenosti nástroje. Většinou do výběru vstupují další kritéria, která se navzájem dostávají do konfliktu. Proto je vhodné použít postup, který umožní jednotlivá kritéria porovnat a následně podle nich posoudit, který z nástrojů je nejvhodnější. Díky tomu nedojde k výběru podle subjektivního názoru, ale ke skutečně podloženému vyhodnocení. Tato práce se proto zaměřuje na porovnání nástrojů pro návrh a vývoj databází. Pro toto porovnání je využita metoda vícekriteriálního rozhodování Analytic Hierarchy Process (AHP). Na ní je pak celý postup hodnocení založen.
[77] Práce tak tvoří teoretický a metodický podklad pro navazující praktické porovnání těchto nástrojů. Na začátku se text věnuje definicím a termínům spojenými s databázovými systémy, datovým modelováním a návrhem databáze, poté vysvětluje princip vícekriteriálního rozhodování a metodu AHP. Na tento rámec navazuje výběr nástrojů a návrh hodnoticích kritérií. S těmi se bude dále pokračovat v praktické části. Výsledné porovnání pak pomůže lépe rozhodnout, který nástroj je vhodný pro různé typy použití, a zároveň ukázat, jak se výsledek mění podle změn priorit.
[78] 2 Cíl práce a výzkumné otázky
[79] Cílem práce je připravit teoretická a metodická východiska pro porovnání vybraných nástrojů pro návrh a vývoj databázových systémů. K dosažení hlavního cíle bude potřeba splnit tyto dílčí cíle:
[80] vymezit základní pojmy z oblasti databázových systémů, datového modelování a návrhu databáze,
[81] vysvětlit principy vícekriteriálního rozhodování, metodu AHP a její použitelnost pro porovnání softwarových nástrojů,
[82] vybrat a charakterizovat nástroje, které budou předmětem porovnávání, a navrhnout hodnoticí kritéria.
[83] Výzkumné otázky vycházejí z cíle práce a z potřeby postupně připravit teoretický a metodický rámec pro budoucí porovnání nástrojů: od vymezení databázových systémů a jejich vývoje, přes vysvětlení, jak nástroje hodnotit podle více kritérií, až po volbu kritérií a postupu porovnání. Metoda AHP přitom umožňuje rozdělit rozhodování na menší přehledné části a systematicky porovnat jak jednotlivá kritéria, tak hodnocené nástroje.
[84] Tomuto zaměření odpovídají následující výzkumné otázky: - VO1: Jaké klíčové pojmy, modely a postupy se využívají při návrhu a vývoji databázových systémů? - VO2: Jaké principy a postupy nabízí metoda AHP pro porovnání alternativ podle více kritérií? - VO3: Jaká hodnoticí kritéria a jaký postup zvolit pro praktické porovnání nástrojů a jak jejich volbu zdůvodnit?
[85] Odpovědi na uvedené výzkumné otázky postupně tvoří obsah jednotlivých kapitol.
[86] 3 Metodika práce
[87] Zpracování práce probíhalo v několika navazujících krocích. Nejprve byly vymezeny oblasti, které je nutné vysvětlit tak, aby bylo možné nástroje později porovnat a navrhnout vhodná hodnoticí kritéria. Jednalo se o oblast databázových systémů, datové modelování, návrhu databáze, vícekriteriální rozhodování a metody AHP. K těmto oblastem byly potom dohledány odborné zdroje.
[88] Zdroje byly vybírány tak, aby pokryly jednak celou teoretickou část práce, ale zároveň také výběr konkrétních nástrojů. Pro databázové systémy byla jako hlavní zdroj použita publikace Pokorného a Valenty (2020). Pro datové modelování a návrh relačních databází byla využita publikace Chlapka, Kučery a Palovské (2019). Metoda AHP byla zpracována podle prací Saatyho (1990, 2008) a učebního textu Soukopové (2016).
[89] Dalším krokem byl výběr nástrojů, které budou v práci porovnávány. Pro jejich výběr byla využita studie Carvalho et al. (2022), protože se zabývá podobným tématem a porovnávala nástroje pro datové modelování jinou metodou. Dále byly použity oficiální dokumentace vybraných nástrojů. Z nich byly převzaty informace o funkcích, podporovaných databázových platformách, licenčních podmínkách a další informace. Jako podpůrný zdroj byl použit také článek Simanavičienė a Vdovinskienė (2023), který ukazuje použití metody AHP při výběru softwaru.
[90] Na základě prostudovaných zdrojů byly následně vybrány nástroje a navržena hodnoticí kritéria. V další části práce budou nástroje hodnoceny podle jednotného postupu. Bude sledována například tvorba modelu, převod do logického a fyzického návrhu, generování SQL skriptu, reverzní inženýrství, použitelnost a licenční podmínky. Výsledky budou následně zpracovány metodou AHP.
[91] Samotné porovnání nástrojů proběhne metodou AHP. Volba této metody vychází z přehledových studií vícekriteriálního rozhodování (MCDM), které AHP označují za jeden z nejvhodnějších přístupů pro hodnocení softwarových systémů, a to zejména díky její schopnosti kombinovat kvantitativní i kvalitativní kritéria (Velasquez a Hester, 2013; Ishizaka a Labib, 2011). Metoda AHP rozloží rozhodovací problém do hierarchie složené z cíle, kritérií a hodnocených nástrojů. Kritéria i nástroje se vzájemně porovnávají po dvojicích na Saatyho škále a z výsledků se vypočítají váhy a celkové pořadí nástrojů. Součástí bude také analýza citlivosti sledující, jak se pořadí mění při změně vah kritérií. Pro usnadnění výpočtů může vzniknout jednoduchá podpůrná aplikace.
[92] 4 Databázové systémy
[93] 4.1 Základní pojmy
[94] Při práci s databázemi je nutné rozlišovat některé základní pojmy, jako jsou data, informace, databáze a systém řízení báze dat. Pod pojmem data si lze představit jednotlivá fakta nebo zaznamenané hodnoty (Elmasri a Navathe, 2016; Watt a Eng, 2014). Tyto hodnoty samy o sobě nemusí být nositeli žádného širšího významu. Informace pak vznikají právě přiřazením významu datům v určitém kontextu (Elmasri a Navathe, 2016; Watt a Eng, 2014). Pojem databáze pak představuje organizovanou sbírku vzájemně souvisejících dat, která jsou uložena tak, aby s nimi bylo možné dále efektivně pracovat (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Watt a Eng, 2014).
[95] Systém řízení báze dat, běžně označovaný jako DBMS, je specializovaný software, který zajišťuje definici, ukládání, manipulaci, zabezpečení a správu dat uložených v databázi (Pokorný a Valenta, 2020). Spojení databáze s DBMS vytvoří databázový systém (DBS) (Elmasri a Navathe, 2016). DBMS v rámci tohoto systému zajišťuje transakční zpracování, obnovení dat po pádu, souběžný přístup více uživatelů i řízení ochrany dat (Pokorný a Valenta, 2020).
[96] Původně se používal především jednoduchý souborový přístup, který měl však řadu problémů a omezení, například v podobě nekonzistentnosti dat při aktualizaci, závislosti na aplikačním programu a na fyzické struktuře, často spojené s redundancí dat (Elmasri a Navathe, 2016). Databázový přístup tyto nedostatky odstraňuje, a to tím, že integruje data do jednoho logického celku a odděluje definici dat od samotných aplikací (Pokorný a Valenta, 2020). Oddělením byla získána vyšší bezpečnost, možnost centrálního řízení integritních omezení a sdílenost dat mezi více uživateli (Pokorný a Valenta, 2020).
[97] 4.2 Schéma databáze, instance a metadata
[98] V teorii databází je třeba rozlišovat mezi schématem databáze a instancí databáze. Schéma databáze představuje popis struktury uložených dat, zahrnuje určení entit, atributů, vazeb a integritních omezení, která mají data splňovat (Pokorný a Valenta, 2020). Pojem instance databáze naopak vyjadřuje konkrétní aktuální obsah databáze v určitém čase. Toto rozlišení odděluje relativně stabilní strukturální návrh od proměnlivých datových hodnot (Elmasri a Navathe, 2016).
[99] S databázovým systémem souvisí také pojem metadata. Metadata jsou data o datech. Tato data tedy popisují strukturu databáze, význam atributů, integritní omezení nebo například přístupová práva. Metadata bývají ukládána v systémovém katalogu, který slouží jako centrální zdroj informací o databázových objektech (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
[100] Správa a údržba schématu databáze je klíčovou rolí správce databáze (DBA), přičemž změny schématu v průběhu životního cyklu systému musí být pečlivě kontrolovány. Metadata uložená v systémovém katalogu jsou využívána nejen samotným DBMS pro optimalizaci dotazů a kontrolu přístupových práv, ale také externími návrhovými nástroji. Tyto nástroje dokážou metadata z katalogu načíst a vizualizovat je ve formě diagramů. Tato vizualizace pak usnadňuje pochopení existující struktury databáze a její další rozvoj (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
[101] 4.3 Funkce DBMS a víceúrovňová architektura
[102] DBMS obvykle poskytuje několik základních skupin funkcí: definici dat, manipulaci s daty, řízení souběžného přístupu více uživatelů, ochranu dat a obnovu po chybě (Pokorný a Valenta, 2020). Pro tyto funkce se používají pojmy jako DDL pro jazyk definice dat, DML pro jazyk manipulace s daty a transakce pro logický celek operací, který má být proveden buď celý, nebo vůbec (Elmasri a Navathe, 2016; Watt a Eng, 2014).
[103] Další významnou myšlenkou bylo chápat DBMS jako víceúrovňový systém podle modelu ANSI/SPARC. Tento přístup představuje databázi jako hierarchii abstrakcí, které oddělují externí, konceptuální a interní rovinu. Myšlenkou bylo podívat se na stavbu databáze jako implementaci hierarchie jistých abstrakcí. Ve zprávě výboru ANSI/X3/SPARC z roku 1975 se objevuje rozdělení na externí, konceptuální a interní úroveň pohledu, kde externí úroveň odpovídá pohledům jednotlivých skupin uživatelů, konceptuální úroveň představuje globální logický model celé databáze a interní úroveň popisuje fyzické uložení dat. Hlavním smyslem tohoto členění je podpora datové nezávislosti, tedy oddělení aplikací a uživatelských pohledů od fyzické implementace databáze (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
[104] Pro budoucí porovnání nástrojů v této práci je toto rozdělení důležité proto, že návrhové nástroje nepokrývají všechny úrovně databázového systému stejným způsobem (Rosenthal a Reiner, 1994). Některé se zaměřují především na konceptuální nebo logický model, jiné podporují i fyzické prvky konkrétního DBMS, například datové typy, indexy nebo generování SQL skriptů (Carvalho et al., 2022). Při hodnocení nástrojů proto bude vhodné sledovat nejen možnosti vytváření diagramů, ale také podporu přechodu mezi jednotlivými úrovněmi návrhu a implementace (Rosenthal a Reiner, 1994).
[105] 4.4 Fáze návrhu databáze
[106] Návrh databáze představuje jednu z klíčových etap vývoje databázového systému a probíhá v několika na sebe navazujících fázích. Přímý přechod k fyzické implementaci tabulek v konkrétním systému může vést k chybám v návrhu, nadbytečné redundanci a omezené rozšiřitelnosti. Z tohoto důvodu se v literatuře standardně rozlišuje konceptuální, logický a fyzický návrh (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Rosenthal a Reiner, 1994).
[107] Konceptuální návrh zachycuje strukturu aplikační domény bez vazby na konkrétní databázový systém (Carvalho et al., 2022; Rosenthal a Reiner, 1994). V této fázi jsou identifikovány entity, vztahy mezi nimi, atributy a základní integritní omezení. Výsledkem je konceptuální schéma, které věrně popisuje realitu a je nezávislé na zvoleném DBMS (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
[108] Na konceptuální návrh navazuje logický návrh. V této části se konceptuální model převádí do zvoleného datového modelu, v případě této práce jde zejména o model relační (Rosenthal a Reiner, 1994). Dochází k návrhu relací, atributů, klíčů, cizích klíčů a integritních omezení (Pokorný a Valenta, 2020). Výsledkem je pak logické schéma databáze, které lze implementovat v konkrétním DBMS (Pokorný a Valenta, 2020).
[109] Ve fyzickém návrhu se řeší způsob uložení dat v konkrétním databázovém systému. Řeší se zde organizace datových souborů, indexy, výkonové aspekty, optimalizace přístupu a další technické detaily (Rosenthal a Reiner, 1994). Na rozdíl od konceptuálního a logického návrhu je fyzický návrh silně závislý na konkrétní technologii (Pokorný a Valenta, 2020).
[110] Mezi jednotlivými kroky návrhu existuje zpětná vazba. Pokud se při fyzickém návrhu ukáže, že některé části modelu vedou například k výkonovým problémům, je nutné vrátit se zpět k návrhu logickému. Podobně může změna požadavků uživatelů vyvolat úpravu konceptuálního modelu a následně i všech dalších úrovní. Návrh databáze proto nelze chápat jako striktně lineární proces, nýbrž jako proces iterativní (Rosenthal a Reiner, 1994).
[111] Rozdělení návrhu databáze na konceptuální, logickou a fyzickou úroveň tvoří vhodný výchozí bod pro pozdější definici hodnoticích kritérií. Nástroj určený pro návrh databázového systému by měl umožnit zachytit požadavky, převést je do konzistentního schématu a podle potřeby podpořit technickou implementaci v konkrétním databázovém prostředí (Rosenthal a Reiner, 1994). Právě míra podpory těchto kroků představuje jeden z praktických rozdílů mezi porovnávanými nástroji (Carvalho et al., 2022; Rosenthal a Reiner, 1994).
[112] 5 Datové modely
[113] Datový model poskytuje formalizovaný nástroj, který slouží k popisu dat, jejich struktur a vztahů mezi nimi. Definuje datové objekty a jejich vzájemné vztahy včetně omezení, která se jich týkají (Pokorný a Valenta, 2020). Datový model je zjednodušený popis reality, který je vytvořen tak, aby se podle něj dala navrhnout a implementovat databáze (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
[114] 5.1 Konceptuální modelování a ER/EER model
[115] 5.1.1 Konceptuální modelování a základní pojmy ER modelu
[116] Konceptuální modelování slouží pro zachycení požadavků aplikační domény, kterou má aplikace pokrývat, ale bez ohledu na konkrétní databázovou technologii. Jeho cílem je vytvořit přehledný a věrný model reálného světa (Carvalho et al., 2022). V praxi se pro tuto fázi velmi často používá entitně-relační model (ER model), případně jeho rozšířená varianta EER (Chen, 1976; Elmasri a Navathe, 2016).
[117] Základními pojmy ER modelu jsou entita, entitní množina, vztah a atribut. Za entitu je považován objekt, který je schopen samostatné existence a lze jej jednoznačně odlišit od ostatních objektů (Chen, 1976). Entitní množina je pak množina entit, které jsou stejného typu a mají společné vlastnosti (Chen, 1976). Vztah vyjadřuje vazbu mezi entitami nebo entitními množinami a atribut představuje vlastnost entity nebo vztahu (Chen, 1976).
[118] Vztahy mezi entitami lze popsat například kardinalitou a participací. Kardinalita udává, kolik entit jedné množiny může být ve vztahu k entitě jiné množiny (Elmasri a Navathe, 2016). Typickými případy jsou vazby 1:1, 1:N a M:N. Participace vyjadřuje, zda je účast entity ve vztahu povinná nebo nepovinná. Tyto pojmy jsou důležité nejen na konceptuální úrovni, ale i pro následnou transformaci do relačního modelu (Pokorný a Valenta, 2020).
[119] 5.1.2 Atributy, EER model a notace
[120] Atributy jsou svázány s doménami, tedy s množinami přípustných hodnot (Elmasri a Navathe, 2016). Rozlišujeme jednoduché a složené atributy, případně i další typy (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Pro jednoznačnou identifikaci entit slouží kandidátní a primární klíče (Elmasri a Navathe, 2016).
[121] Rozšířený ER model (EER) doplňuje základní ER model o supertřídy, podtřídy a dědičnost atributů (Pokorný a Valenta, 2020). EER model je vhodný především tam, kde je potřeba přesněji vystihnout specializaci nebo generalizaci objektů (Elmasri a Navathe, 2016). V praxi se ER/EER model vyjadřuje různými grafickými notacemi, přičemž mezi nejčastější patří Chenova notace, Crow’s Foot a UML (Elmasri a Navathe, 2016; Carvalho et al., 2022).
[122] Pro hodnocení databázových nástrojů je podpora konceptuálního modelování významná hlavně z praktického hlediska. Nástroj by měl umožnit vyjádřit entity, vztahy, kardinality a omezení způsobem, který je srozumitelný jak analytikům, tak i vývojářům (Rosenthal a Reiner, 1994). Jednotlivé nástroje se přitom mohou lišit použitou notací, úrovní podpory EER prvků a možností následného převodu modelu do relačního schématu (Carvalho et al., 2022; Rosenthal a Reiner, 1994).
[123] 5.2 Relační model
[124] Relační model je založen na relacích, které jsou v praxi neformálně reprezentovány tabulkami. Každá relace má své schéma, tedy jméno relace, seznam atributů a jejich domén (Pokorný a Valenta, 2020). Konkrétní řádky tabulky odpovídají n-ticím. Relační model pracuje s atomickými hodnotami a s přesně vymezenými atributy (Codd, 1970; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
[125] Klíče jsou v relačním modelu zásadní. Primární klíč slouží k jednoznačné identifikaci řádku tabulky (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Cizí klíč umožňuje vyjádřit vazbu mezi tabulkami a je základem referenční integrity (Watt a Eng, 2014). Mezi obecné vlastnosti relačních tabulek patří nezávislost na pořadí řádků a sloupců a požadavek na neduplicitu řádků (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
[126] Relační model je pro tuto práci důležitý také proto, že většina běžně používaných návrhových nástrojů pro databáze směřuje k tvorbě relačního schématu a k práci s SQL databázemi. Při jejich porovnání proto bude důležité, zda nástroj podporuje definici primárních a cizích klíčů, integritních omezení, datových typů a generování nebo zpětné načítání databázového schématu (Carvalho et al., 2022).
[127] 5.3 Transformace ER/EER modelu do relačního modelu
[128] Při přechodu z konceptuálního modelu k modelu relačnímu se entity obvykle převádějí na tabulky a atributy na sloupce (Chlapek, Kučera a Palovská, 2019). Vztahy typu 1:N se zpravidla reprezentují pomocí cizího klíče na straně N, zatímco pro vztahy M:N je vyžadováno vytvoření samostatné spojovací tabulky. Specifické případy představují vztahy 1:1, atributy vztahů nebo převod supertříd a podtříd (Elmasri a Navathe, 2016). Tato transformace je důležitým přechodem mezi konceptuálním a logickým návrhem. Pokud je tato transformace provedena nekonzistentně, vede k problémům v následné implementaci (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
[129] U nástrojů pro návrh databází je proto důležité, zda převod mezi konceptuálním a relačním modelem pouze vizuálně naznačují, nebo zda tento převod dokážou částečně automatizovat a kontrolovat. Automatické generování relačního schématu může práci urychlit, ale je potřeba ověřit, zda nástroj také správně zachází s kardinalitami, vazbami M:N, povinnými atributy a integritními omezeními (Carvalho et al., 2022; Rosenthal a Reiner, 1994).
[130] 5.4 Normalizace relačního modelu
[131] Normalizace je proces, jehož cílem je odstranit nadbytečnost dat a předcházet anomáliím při vkládání, aktualizaci a mazání údajů. Teoretickým základem normalizace jsou funkční závislosti, které určují vztahy mezi atributy a umožňují identifikovat nadbytečnost a anomálie v databázovém schématu. Pro tuto práci by mělo být dostačující vysvětlit první, druhou a třetí normální formu (Codd, 1970; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
[132] První normální forma vyžaduje atomické hodnoty a nepřipouští skupiny, které se opakují (Codd, 1970; Elmasri a Navathe, 2016). Druhá normální forma řeší závislost neklíčových atributů na celém klíči (Codd, 1970; Elmasri a Navathe, 2016). Třetí normální forma odstraňuje tranzitivní závislosti mezi neklíčovými atributy (Codd, 1970; Elmasri a Navathe, 2016). Tyto formy postačují k zajištění základní konzistence relačního schématu a tvoří standard, který by každý nástroj pro návrh databází měl uživateli umožňovat respektovat (Codd, 1970; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
[133] Normalizace ukazuje mimo jiné, že kvalita návrhového nástroje nespočívá jen v grafické podobě diagramu. Důležité je, zda nástroj podporuje konzistenci modelu, upozorňuje na chybějící klíče nebo problematické vazby a umožňuje vytvořit návrh, který lze převést do udržitelného relačního schématu. Tato hlediska navazují na pozdější výběr hodnoticích kritérií pro komparaci nástrojů (Carvalho et al., 2022).
[134] 6 Vícekriteriální rozhodování
[135] 6.1 Alternativa, kritérium a váha kritéria
[136] 6.2 Přístupy k odhadu vah kritérií a porovnání alternativ
[137] 7 Metoda AHP
[138] 7.1 Saatyho škála a párové porovnání
[139] 7.2 Kontrola konzistence
[140] 7.3 Výhody a omezení AHP
[141] 8 Nástroje pro návrh a vývoj databází
[142] Výběr nástrojů pro porovnání vycházel nejprve z přehledu dostupných nástrojů pro návrh a vývoj databází. Jako jeden z podkladů byla využita studie Carvalho et al. (2022), která hodnotila sedmnáct nástrojů pro datové modelování. V této studii je vidět, že nabídka těchto nástrojů je velmi široká a obsahuje nástroje online i desktopové, bezplatné i komerční a také nástroje zaměřené na různé databázové platformy. Příkladem online nástroje je ONDA vyvinutý na Univerzitě v Coimbře (Laranjeiro a Pinto, 2024); do užšího výběru však zařazen nebyl, protože práce se soustředí na plnohodnotné desktopové nástroje. Dalším podkladem byly oficiální online dokumentace vybraných nástrojů, ze kterých byly ověřeny jejich základní funkce, podporované databázové platformy a licenční podmínky. Pro posouzení významu jednotlivých databázových platforem byl využit také žebříček DB-Engines (2026).
[143] Na základě těchto podkladů byly pro další práci vybrány čtyři nástroje: Oracle SQL Developer Data Modeler, DBeaver Community Edition, MySQL Workbench Community Edition a pgModeler. Při výběru bylo zohledněno, zda nástroj podporuje návrh databáze, zda je dostupný v bezplatné nebo volně testovatelné verzi a zda vhodně doplňuje ostatní vybrané nástroje. Oracle SQL Developer Data Modeler je zaměřený hlavně na Oracle Database, MySQL Workbench na MySQL, pgModeler na PostgreSQL a DBeaver představuje univerzálnější nástroj podporující více DBMS. Tři z těchto nástrojů jsou uvedeny také ve studii Carvalho et al. (2022). Díky tomu bude možné pozdější výsledky alespoň částečně porovnat s již publikovanou studií.
[144] Volba databázových platforem vychází také z jejich rozšířenosti. Oracle Database, MySQL a PostgreSQL patří podle žebříčku DB-Engines (2026) mezi významné relační databázové systémy. Do úvahy byl brán i Microsoft SQL Server, ten však nebyl zařazen, protože pro zvolený postup práce lépe odpovídají nástroje dostupné bezplatně nebo ve volně použitelné komunitní verzi. U univerzálních nástrojů bude při hodnocení sledováno také to, zda umožňují práci s více databázovými platformami, případně i s nerelačními databázemi.
[145] Základní charakteristiky vybraných nástrojů shrnuje tabulka 1.
[146] Tabulka 1 – Základní charakteristiky vybraných nástrojů (zdroje: Oracle, 2026; DBeaver, 2026; MySQL, 2026; pgModeler, 2026)
[147] 8.1 Oracle SQL Developer Data Modeler
[148] Oracle SQL Developer Data Modeler je bezplatný grafický nástroj společnosti Oracle pro modelování dat. Podporuje logické, relační, fyzické, multidimenzionální a typové modely, nabízí forward i reverse engineering a integraci se širším portfoliem Oracle SQL Developer. Jako primární databázová platforma je preferován Oracle Database, nástroj však umožňuje pracovat i s dalšími systémy (Oracle, 2026). Pro účely této práce bude testována verze 24.3.
[149] 8.2 DBeaver Community Edition
[150] DBeaver je open-source univerzální databázový nástroj s podporou širokého spektra DBMS (PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, SQLite a další). Nabízí editor SQL, prohlížeč dat, vizualizaci databázových struktur pomocí ER diagramů a generování DDL skriptů. Pokročilejší funkce, například datové generátory nebo vizuální dotazování, jsou dostupné v komerční edici (DBeaver, 2026). Pro účely této práce bude testována verze 26.0 Community Edition.
[151] 8.3 MySQL Workbench Community Edition
[152] MySQL Workbench je oficiální nástroj společnosti Oracle pro práci s databází MySQL. Sjednocuje v jednom prostředí návrh databáze (EER diagramy), správu serveru, modelování, forward i reverse engineering a SQL vývoj. Podporuje synchronizaci modelu s živou databází a export modelu do DDL skriptu (MySQL, 2026). Pro účely této práce bude testována verze 8.0.
[153] 8.4 pgModeler
[154] pgModeler, jehož název vychází z označení PostgreSQL Database Modeler, je open-source nástroj zaměřený přímo na databázi PostgreSQL. Umožňuje grafický návrh schémat, generování SQL skriptů, reverzní inženýrství, validaci modelu a porovnávání modelu s živou databází (pgModeler, 2026). Cílovou databázovou platformou nástroje je PostgreSQL, jehož oficiální dokumentace popisuje podporované datové typy a syntaxi SQL, vůči nimž pgModeler generované skripty validuje (PostgreSQL, 2026). Pro účely této práce bude testována aktuální stabilní verze ke dni testování.
[155] 9 Návrh hodnoticích kritérií
[156] Při vytváření kritérií pro hodnocení je potřeba zohlednit, že nástroje budou porovnávány podle toho, jak dokážou podpořit návrh a vývoj databáze, nikoliv pouze podle toho, jak zvládají její provoz a správu. Hodnoticí kritéria vycházejí ze studie Carvalho et al. (2022). Tato práce porovnávala nástroje pro datové modelování podle kategorií jako: funkcionalita, provozní vlastnosti softwaru, dokumentace a komunitní podpora. Tato práce toto členění přebírá a rozšiřuje ho o kritéria specifická pro návrh databázových systémů. U kritérií, která nejdou vyjádřit číselně, se použije kvalitativní hodnocení podle zkušenosti a každé porovnání se krátce zdůvodní.
[157] Přehled osmi navržených pracovních kritérií uvádí tabulka 2.
[158] Tabulka 2 – Přehled navržených hodnoticích kritérií (vlastní zpracování na základě Carvalho et al., 2022)
[159] Význam jednotlivých kritérií je blíže popsán níže.
[160] K1 Funkcionalita. Rozsah funkcí nástroje — typy modelů (konceptuální, logický, fyzický), validace, dokumentace a podpora objektů jako tabulky, pohledy, indexy nebo triggery.
[161] K2 Použitelnost. Vyjadřuje, jak snadno se s nástrojem pracuje – jak rychle se v něm uživatel zorientuje, nakolik je prostředí editoru modelu přehledné a jak náročné je provést běžné úkony.
[162] K3 Kompatibilita s DBMS. Udává, kolik databázových systémů nástroj oficiálně podporuje.
[163] K4 Forward engineering. Sleduje, jak nástroj generuje DDL skript nebo schéma databáze z navrženého modelu.
[164] K5 Reverse engineering. Týká se schopnosti nástroje sestavit model z již existující databáze.
[165] K6 Dokumentace a komunitní podpora. Posuzuje rozsah a aktuálnost oficiální dokumentace i dostupnost komunitní podpory a aktualizací.
[166] K7 Import a export modelu. Zaměřuje se na podporované formáty importu a exportu a na propojení s verzovacími systémy.
[167] K8 Cena a licence. Bere v úvahu typ licence (open source, freeware, komerční), omezení bezplatné verze a celkové náklady na zavedení.
[168] 10 Závěry a doporučení
[169] Cíl práce, tedy zpracování teoretických a metodických východisek pro praktickou část, byl naplněn. Odpovědi na výzkumné otázky lze stručně shrnout takto:
[170] K VO1: Byly vymezeny klíčové pojmy databázových systémů (data, DBMS, schéma, instance, metadata), popsány fáze návrhu databáze (konceptuální, logický, fyzický) a vysvětleny datové modely používané v praxi, zejména ER/EER a relační model spolu s normalizací.
[171] K VO2: Metoda AHP byla popsána jak z hlediska principu (hierarchie cíl–kritéria–alternativy), tak z hlediska postupu (párové porovnání s využitím Saatyho škály, výpočet vah, kontrola konzistence pomocí CR). Bylo zdůvodněno, proč je AHP vhodná pro porovnání softwarových nástrojů.
[172] K VO3: Bylo navrženo osm hodnoticích kritérií (K1–K8) a metodický rámec navazující komparace, zahrnující sestavení hierarchie, párové porovnání kritérií, testovací scénář nad nainstalovanými nástroji, syntézu priorit a analýzu citlivosti.
[173] Tento navržený teoretický a metodický rámec tvoří přímý základ pro navazující praktickou komparaci v bakalářské práci. Pro realizaci této praktické části se doporučuje: a) provést testovací scénář na všech čtyřech nástrojích v jednom kalendářním týdnu, aby se minimalizovaly rozdíly ve zkušenostech hodnotitele; b) při hodnocení kvalitativních kritérií (K2, K6) doplnit slovní zdůvodnění každého párového porovnání; c) zařadit analýzu citlivosti minimálně pro váhy K1 a K8; d) zvážit modelový scénář dvou typových firem (malé a střední) s odlišnými váhami kritérií a porovnat výsledné pořadí mezi scénáři. Vedle toho bude v bakalářské práci detailně rozpracován jednotný testovací scénář a případný výpočet vah v excelovém modelu či jednoduché podpůrné aplikaci.
[175] Seznam zdrojů
[176] Tištěné zdroje
[177] CARVALHO, Gonçalo, Sergii MYKOLYSHYN, Bruno CABRAL, Jorge BERNARDINO a Vasco PEREIRA. Comparative Analysis of Data Modeling Design Tools. IEEE Access. 2022, 10, 3351-3365. ISSN 2169-3536. DOI: 10.1109/ACCESS.2021.3139071.
[178] CHEN, Peter Pin-Shan. The entity-relationship model—toward a unified view of data. ACM Transactions on Database Systems. 1976, 1(1), 9–36. ISSN 0362-5915. DOI: 10.1145/320434.320440.
[179] CHLAPEK, Dušan, Jan KUČERA a Helena PALOVSKÁ. Datové modelování a návrh relační databáze: Sbírka řešených úloh. Praha: Vysoká škola ekonomická v Praze, Nakladatelství Oeconomica, 2019. ISBN 978-80-245-2331-6.
[180] CODD, Edgar F. A relational model of data for large shared data banks. Communications of the ACM. 1970, 13(6), 377–387. ISSN 0001-0782. DOI: 10.1145/362384.362685.
[181] ELMASRI, Ramez a Shamkant B. NAVATHE. Fundamentals of Database Systems. 7th ed. Boston: Pearson, 2016. ISBN 978-0-13-397077-7.
[182] HO, William. Integrated analytic hierarchy process and its applications – a literature review. European Journal of Operational Research. 2008, 186(1), 211–228. ISSN 0377-2217. DOI: 10.1016/j.ejor.2007.01.004.
[183] ISHIZAKA, Alessio a Ashraf LABIB. Review of the main developments in the Analytic Hierarchy Process. Expert Systems with Applications. 2011, 38(11), 14336–14345. ISSN 0957-4174. DOI: 10.1016/j.eswa.2011.04.143.
[184] MARDANI, Abbas, Ahmad JUSOH, Khalil MD NOR, Zainab KHALIFAH, Norhayati ZAKWAN a Alireza VALIPOUR. Multiple criteria decision-making techniques and their applications – a review of the literature from 2000 to 2014. Economic Research – Ekonomska Istraživanja. 2015, 28(1), 516–571. ISSN 1331-677X. DOI: 10.1080/1331677X.2015.1075139.
[185] POKORNÝ, Jaroslav a Michal VALENTA. Databázové systémy. Praha: České vysoké učení technické v Praze, 2020. ISBN 978-80-01-06708-6.
[186] ROSENTHAL, Arnon a David REINER. Tools and Transformations — Rigorous and Otherwise — for Practical Database Design. ACM Transactions on Database Systems. 1994, 19(2), 167-211. ISSN 0362-5915. DOI: 10.1145/176567.176568.
[187] SAATY, Thomas L. How to make a decision: The Analytic Hierarchy Process. European Journal of Operational Research. 1990, 48(1), 9-26. ISSN 0377-2217.
[188] SAATY, Thomas L. Decision making with the analytic hierarchy process. International Journal of Services Sciences. 2008, 1(1), 83-98. ISSN 1753-1454.
[189] SIMANAVIČIENĖ, Rūta a Sonata VDOVINSKIENĖ. Selection of Computer-Aided Design Software Systems Using the AHP Method. Baltic Journal of Modern Computing. 2023, 11(2), 272-284. ISSN 2255-8950. DOI: 10.22364/bjmc.2023.11.2.04.
[190] VAIDYA, Omkarprasad S. a Sushil KUMAR. Analytic hierarchy process: An overview of applications. European Journal of Operational Research. 2006, 169(1), 1–29. ISSN 0377-2217. DOI: 10.1016/j.ejor.2004.04.028.
[191] VELASQUEZ, Mark a Patrick T. HESTER. An Analysis of Multi-Criteria Decision Making Methods. International Journal of Operations Research. 2013, 10(2), 56–66. ISSN 1813-713X.
[192] Internetové zdroje
[193] DBEAVER. DBeaver Documentation [online]. DBeaver Corp., 2026 [cit. 2026-06-09]. Dostupné z: https://dbeaver.com/docs/dbeaver/
[194] DB-ENGINES. DB-Engines Ranking [online]. solid IT gmbh, 2026 [cit. 2026-06-14]. Dostupné z: https://db-engines.com/en/ranking
[195] LARANJEIRO, Nuno a Alexandre Miguel PINTO. ONDA: ONLine Database Architect [online]. arXiv:2401.16552, 2024 [cit. 2026-06-15]. DOI: 10.48550/arXiv.2401.16552. Dostupné z: https://doi.org/10.48550/arXiv.2401.16552
[196] MYSQL. MySQL Workbench Manual [online]. Oracle Corporation, 2026 [cit. 2026-06-09]. Dostupné z: https://dev.mysql.com/doc/workbench/en/
[197] ORACLE. Oracle SQL Developer Data Modeler [online]. Oracle Corporation, 2026 [cit. 2026-06-09]. Dostupné z: https://www.oracle.com/database/sqldeveloper/technologies/sql-data-modeler/
[198] PGMODELER. pgModeler – PostgreSQL Database Modeler [online]. Raphael Araújo e Silva, 2026 [cit. 2026-06-09]. Dostupné z: https://pgmodeler.io/
[199] POSTGRESQL. PostgreSQL Documentation [online]. The PostgreSQL Global Development Group, 2026 [cit. 2026-06-09]. Dostupné z: https://www.postgresql.org/docs/
[200] SOUKOPOVÁ, Jana. Vícekriteriální metody hodnocení [online]. Brno: Masarykova univerzita, Ekonomicko-správní fakulta, 2016. Učební text [cit. 2026-06-09]. Dostupné z: https://is.muni.cz/el/1456/jaro2016/BPE_VIMP/um/
[201] WATT, Adrienne a Nelson ENG. Database Design [online]. 2nd ed. Victoria: BCcampus, 2014 [cit. 2026-06-18]. Dostupné z: https://opentextbc.ca/dbdesign01/