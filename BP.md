<!-- BP-DOPLNIT: Před odevzdáním nahradit všechny výrazy v závorkách ⟦...⟧ skutečnými údaji a výsledky. -->

Univerzita Hradec Králové

Fakulta informatiky a managementu

Katedra informatiky a kvantitativních metod

**Komparace nástrojů pro návrh a vývoj databázových systémů pomocí AHP**

**Comparison of Database Design and Development Tools Using AHP**

Bakalářská práce

| | |
|---|---|
| **Autor:** | Roman Janiš |
| **Osobní číslo:** | I2400792 |
| **Studijní program:** | B0613A140033 Aplikovaná informatika |
| **Specializace:** | Softwarové inženýrství |
| **Vedoucí práce:** | Ing. et Ing. Martin Lněnička, Ph.D. |
| **Pracoviště vedoucího:** | Katedra informatiky a kvantitativních metod |

Hradec Králové, ⟦ROK ODEVZDÁNÍ⟧

---

**Prohlášení**

Prohlašuji, že jsem tuto práci vypracoval samostatně a uvedl jsem všechny použité prameny a literaturu. V případě využití nástrojů umělé inteligence jsem plně deklaroval způsob jejich využití při vypracování této práce.

V Hradci Králové dne ⟦DATUM⟧

Roman Janiš

> **Před dokončením:** Ověřit přesné znění prohlášení podle aktuální oficiální šablony FIM UHK.

---

**Poděkování**

Tímto bych rád poděkoval vedoucímu práce Ing. et Ing. Martinu Lněničkovi, Ph.D., za odborné vedení, věcné připomínky a konzultace, které přispěly ke zpracování této práce.

---

**Anotace**

Práce se zabývá komparací nástrojů pro návrh a vývoj databázových systémů pomocí metody Analytic Hierarchy Process (AHP). Teoretická část vymezuje databázové systémy, datové modelování, návrh relační databáze a principy vícekriteriálního rozhodování. Porovnávány jsou Oracle SQL Developer Data Modeler, DBeaver Community Edition, MySQL Workbench Community Edition a pgModeler. Praktická část ověřuje nástroje na společném modelovém příkladu databáze cykloservisu a hodnotí je podle osmi kritérií. AHP je použita pro dva modelové scénáře s odlišnými prioritami a výsledky jsou ověřeny analýzou citlivosti. Ve scénáři malé organizace se jako nejvhodnější umístil nástroj ⟦NEVYHODNOCENO⟧, zatímco ve scénáři středně velké organizace dosáhl nejvyššího skóre nástroj ⟦NEVYHODNOCENO⟧. Analýza citlivosti ukázala ⟦NEVYHODNOCENO – HLAVNÍ ZJIŠTĚNÍ⟧.

**Klíčová slova:** databázový systém, návrh databáze, datové modelování, nástroje pro modelování databází, vícekriteriální rozhodování, Analytic Hierarchy Process

**Abstract**

The thesis compares tools for database systems design and development using the Analytic Hierarchy Process (AHP). The theoretical part defines database systems, data modelling, relational database design, and the principles of multiple-criteria decision-making. Oracle SQL Developer Data Modeler, DBeaver Community Edition, MySQL Workbench Community Edition, and pgModeler are compared. The practical part tests the tools on a common bicycle-service database scenario and evaluates them according to eight criteria. AHP is applied to two model scenarios with different priorities, and sensitivity analysis is used to examine the stability of the results. In the small-organisation scenario, ⟦NOT YET EVALUATED⟧ achieved the highest score, whereas ⟦NOT YET EVALUATED⟧ ranked first in the medium-sized-organisation scenario. The sensitivity analysis showed ⟦NOT YET EVALUATED – MAIN FINDING⟧.

**Keywords:** database system, database design, data modelling, database modelling tools, multiple-criteria decision-making, Analytic Hierarchy Process

---

**Obsah**

> Ve finálním dokumentu bude obsah automaticky vygenerován ze stylů nadpisů.

1. Úvod
2. Cíl práce a výzkumné otázky
3. Metodika práce
4. Databázové systémy
5. Datové modely
6. Vícekriteriální rozhodování
7. Nástroje pro návrh a vývoj databází
8. Návrh hodnoticích kritérií
9. Praktická komparace
10. Výsledky praktického testování
11. Vyhodnocení nástrojů metodou AHP
12. Diskuse výsledků a doporučení
13. Závěr
14. Seznam zdrojů
15. Přílohy

**Seznam tabulek**

> Ve finálním dokumentu bude seznam tabulek automaticky vygenerován. Před odevzdáním je nutné zkontrolovat názvy a číslování všech tabulek.

**Seznam obrázků**

> Ve finálním dokumentu bude seznam obrázků automaticky vygenerován. Každý screenshot a diagram musí mít číslo, popisek, zdroj a odkaz v textu.

**Seznam zkratek**

| Zkratka | Význam |
|:--|:--|
| AHP | Analytic Hierarchy Process |
| CI | Consistency Index, index konzistence |
| CR | Consistency Ratio, poměr konzistence |
| DBMS | Database Management System, systém řízení báze dat |
| DDL | Data Definition Language |
| EER | Enhanced Entity–Relationship model |
| ER | Entity–Relationship model |
| MCDM | Multiple-Criteria Decision-Making |
| RI | Random Index, náhodný index |
| SQL | Structured Query Language |

> **Před dokončením:** Doplnit nebo odstranit zkratky podle konečného textu.

# Úvod

Návrh databáze obvykle předchází samotné implementaci databázového systému. Kvalita takového datového návrhu značně ovlivňuje spolehlivost, výkon a možnosti dalšího rozšiřování systému. V případě, že při návrhu vzniknou chyby, jejich odstranění je v dalších etapách složité a nákladné. Při návrhu a vývoji databází se proto využívají různé softwarové nástroje, jako například nástroje pro datové modelování, generování Structured Query Language (SQL) skriptů nebo správu databázových schémat. Jednotlivé nástroje se mezi sebou liší rozsahem nabízených funkcí, podporovanými databázovými systémy, možnostmi modelování nebo licenčními podmínkami.

Vybrat vhodný nástroj není v praxi často jednoduché. Obvykle se nedá rozhodovat jen podle jednoho kritéria, například podle ceny nebo rozšířenosti nástroje. Většinou do výběru vstupují další kritéria, která se navzájem dostávají do konfliktu. Proto je vhodné zvolit postup, který umožní jednotlivá kritéria porovnat a následně podle nich rozhodnout, který z nástrojů je pro danou situaci nejvhodnější. Díky tomu se do hodnocení promítají také zkušenosti a názory hodnotitele, ale zároveň se omezuje riziko čistě intuitivní volby. Tato práce se proto zaměřuje na porovnání nástrojů pro návrh a vývoj databází. Pro hodnocení je použita metoda vícekriteriálního rozhodování s názvem Analytic Hierarchy Process (AHP).

Předmětem porovnání jsou Oracle SQL Developer Data Modeler, DBeaver Community Edition, MySQL Workbench Community Edition a pgModeler. Nástroje jsou ověřeny na jednotném modelovém příkladu databáze cykloservisu a hodnoceny podle osmi předem vymezených kritérií. Pro odlišení potřeb uživatelů jsou vytvořeny dva modelové scénáře: malá organizace s důrazem na použitelnost a náklady a středně velká organizace s vyšším důrazem na funkcionalitu a kompatibilitu. Stabilita výsledků je posouzena analýzou citlivosti.

Práce se nejprve věnuje definicím a termínům spojeným s databázovými systémy, datovým modelováním a návrhem databáze. Následně vysvětluje princip vícekriteriálního rozhodování a metodu AHP. Na tento přístup navazuje výběr nástrojů a návrh hodnoticích kritérií. Praktická část popisuje modelový příklad, testovací prostředí a jednotný postup testování, prezentuje výsledky jednotlivých nástrojů a zpracovává je metodou AHP. Závěrečné kapitoly výsledky diskutují, porovnávají oba modelové scénáře a formulují doporučení pro praxi.

# Cíl práce a výzkumné otázky

Hlavním cílem bakalářské práce je porovnat vybrané nástroje pro návrh a vývoj databázových systémů pomocí metody AHP a na základě výsledků formulovat doporučení pro jejich využití ve dvou modelových situacích. Porovnávány jsou Oracle SQL Developer Data Modeler, DBeaver Community Edition, MySQL Workbench Community Edition a pgModeler.

K dosažení hlavního cíle byly stanoveny následující dílčí cíle:

- vymezit teoretická východiska databázových systémů, datového modelování a návrhu databáze;
- vysvětlit principy vícekriteriálního rozhodování a metody AHP;
- zdůvodnit výběr porovnávaných nástrojů a operacionalizovat hodnoticí kritéria;
- navrhnout jednotný a opakovatelný postup praktického testování;
- prakticky ověřit nástroje na společném modelovém příkladu;
- sestavit AHP hodnocení pro dvě modelové situace a ověřit konzistenci párových porovnání;
- provést analýzu citlivosti a formulovat doporučení pro praxi.

Na hlavní a dílčí cíle navazují tyto výzkumné otázky:

- **VO1:** Jak se vybrané nástroje liší podle stanovených hodnoticích kritérií při provedení stejných modelovacích úloh?
- **VO2:** Který z porovnávaných nástrojů je podle metody AHP nejvhodnější pro modelovou malou organizaci a který pro modelovou středně velkou organizaci?
- **VO3:** Jak stabilní je výsledné pořadí nástrojů při změně vah vybraných kritérií?

Odpověď na VO1 vychází z praktického testování a souhrnného porovnání K1–K8. VO2 je zodpovězena syntézou AHP pro oba scénáře. VO3 je vyhodnocena analýzou citlivosti, při níž se mění váhy kritérií s největším předpokládaným vlivem na rozhodnutí.

> **Před dokončením:** Po výpočtech zkontrolovat, zda formulace VO2 přesně odpovídá skutečně použitým scénářům a zda analýza citlivosti skutečně umožňuje jednoznačně odpovědět na VO3.

# Metodika práce

<!-- BP-DOPLNIT: Minulý čas v popisu praktického postupu je nutné před odevzdáním ověřit podle skutečně provedených testů. -->

Zpracování práce probíhalo v několika navazujících krocích. Nejprve byly vymezeny oblasti, které je třeba popsat tak, aby bylo možné nástroje porovnat a navrhnout vhodná hodnoticí kritéria. Jednalo se o oblasti databázových systémů, datového modelování, návrhu databáze, vícekriteriálního rozhodování a metody AHP. K těmto oblastem byly následně vyhledány odborné zdroje.

## Rešerše a výběr zdrojů

Zdroje byly vybírány tak, aby pokryly nejen celou teoretickou část práce, ale i výběr konkrétních nástrojů. Pro databázové systémy byly jako hlavní zdroje použity publikace Pokorného a Valenty (2020) a Elmasriho a Navatha (2016). Pro datové modelování a návrh relačních databází byla využita publikace Chlapka, Kučery a Palovské (2019). Metoda AHP byla zpracována na základě prací Saatyho (1990, 2008), učebního textu Soukopové (2016) a přehledových studií zaměřených na vícekriteriální rozhodování.

Dalším krokem byl výběr nástrojů, které jsou v práci porovnávány. Při jejich výběru byla využita studie Carvalho et al. (2022), protože se zabývá podobným tématem a porovnává nástroje pro datové modelování jinou metodou. Dále byla použita oficiální dokumentace vybraných nástrojů. Z ní byly převzaty údaje o funkcích, podporovaných databázových platformách, licenčních podmínkách a další podrobnosti. Jako podpůrný zdroj byl použit také článek Simanavičienė a Vdovinskienė (2023), který ukazuje použití metody AHP při výběru softwaru.

## Výběr nástrojů a kritérií

Na základě prostudovaných zdrojů byly vybrány Oracle SQL Developer Data Modeler, DBeaver Community Edition, MySQL Workbench Community Edition a pgModeler. Kritéria zahrnují funkcionalitu, použitelnost, kompatibilitu s databázovými systémy, forward engineering, reverse engineering, dokumentaci a komunitní podporu, import a export modelu a náklady a licenční omezení. Jejich přesná operacionalizace je uvedena v kapitole 8.

## Modelový příklad a praktické testování

Pro praktické porovnání byl vytvořen jednotný modelový příklad informačního systému malého cykloservisu. Jádro modelu tvoří deset entit a zahrnuje vazby 1:N, M:N realizované asociačními entitami, vazbu 1:1, složené primární klíče, nepovinný cizí klíč, unikátní omezení a kontrolu povolených hodnot. Tato skladba umožňuje ověřit běžné modelovací úlohy bez nepřiměřeného zvýhodnění některého nástroje.

Nástroje byly testovány na stejném počítači a za srovnatelných podmínek. Pro ověření vygenerovaných schémat a reverse engineeringu byly použity databáze MySQL, PostgreSQL a Oracle Database spuštěné v kontejnerech Docker. Každý nástroj pracoval se stejným významovým zadáním a stejným cílovým rozsahem modelu. Pokud testovaná edice neumožňovala samostatné modelování od prázdného diagramu, byla použita nejbližší dostupná cesta k vytvoření stejné databázové struktury a tento rozdíl byl výslovně zaznamenán. Funkce nedostupná v testované edici nebyla nahrazena funkcí jiné edice bez uvedení této skutečnosti.

Jednotný protokol zahrnoval vytvoření struktury podle textového zadání, nastavení atributů, klíčů, vztahů a integritních omezení, vygenerování DDL a ověření jeho spustitelnosti, reverse engineering referenční databáze a export diagramu. Pro každý krok byl veden záznam obsahující čas začátku a konce, výsledek, počet nutných ručních zásahů, popis problému a odkaz na screenshot nebo výstupní soubor.

Konkrétní konfigurace, pravidla měření času, pořadí testování a opatření proti vlivu předchozí zkušenosti jsou uvedeny v kapitole 9. Údaje, které dosud nebyly zaznamenány, jsou v pracovní verzi označeny výrazem ⟦NEZAZNAMENÁNO⟧.

## Zpracování výsledků metodou AHP

Samotné porovnání nástrojů bylo provedeno pomocí metody AHP. Volba této metody vychází ze studií zabývajících se problematikou vícekriteriálního rozhodování (Multiple-Criteria Decision-Making, MCDM), podle nichž lze AHP využít pro hodnocení softwarových systémů zejména díky schopnosti kombinovat kvantitativní i kvalitativní kritéria (Ishizaka a Labib, 2011; Moreno-Jiménez a Vargas, 2018; Velasquez a Hester, 2013).

Metoda AHP rozkládá rozhodovací problém do hierarchické struktury složené z cíle, hodnoticích kritérií a hodnocených nástrojů. Jednotlivá kritéria i nástroje byly porovnávány po dvojicích za využití Saatyho devítibodové škály. Na základě párových matic byly metodou geometrického průměru řádků vypočteny váhy kritérií a preference alternativ. Současně byla ověřena konzistence rozhodovacích úsudků pomocí Consistency Ratio (CR). Matice s hodnotou CR rovnou nebo vyšší než 0,1 byla znovu posouzena pouze návratem k původním údajům a důvodům hodnocení, nikoli s cílem vytvořit předem očekávané pořadí (Saaty, 1990; Saaty, 2008).

Výsledkem procesu je celkové skóre každého nástroje a jejich pořadí podle vhodnosti pro definovaný účel. Úplné matice, vzorce, hodnoty CI a CR a kontrolní výpočet budou uvedeny v kapitole 11 a v přílohách. Použitý výpočtový soubor nebo aplikace je v pracovní verzi označen jako ⟦NEZAZNAMENÁNO⟧.

## Modelové scénáře a analýza citlivosti

Pro ověření praktické použitelnosti byly připraveny dva modelové scénáře. Scénář A představuje malou organizaci, pro kterou jsou významnější použitelnost a náklady. Scénář B představuje středně velkou organizaci s vyššími požadavky na funkcionalitu a kompatibilitu. Matice alternativ vzhledem ke kritériím zůstávají v obou scénářích stejné; mění se pouze význam kritérií.

Součástí hodnocení je analýza citlivosti, jejímž cílem je posoudit stabilitu dosažených výsledků a identifikovat kritéria, která mají největší vliv na konečné pořadí nástrojů. Ostatní váhy jsou při změně vybraného kritéria poměrně přepočteny tak, aby jejich součet zůstal roven jedné (Saaty, 1990; Saaty, 2008). Rozsah a krok změny budou doplněny podle skutečně provedené analýzy.

## Omezení a důvěryhodnost postupu

Hodnocení prováděl jeden hodnotitel, a proto může být ovlivněno jeho zkušenostmi a preferencemi. Tento vliv je omezen jednotným zadáním, předem stanoveným protokolem, uchováním výstupů a slovním zdůvodněním párových porovnání. Výsledky se vztahují k testovaným verzím a edicím nástrojů a nelze je bez dalšího zobecnit na jiné verze nebo odlišné typy projektů. Modelový příklad pokrývá běžné relační konstrukce, nikoli všechny možnosti rozsáhlých podnikových databází.

Pro usnadnění výpočtů, správu hodnoticích matic a prezentaci výsledků může být v rámci práce vytvořena jednoduchá podpůrná aplikace implementující základní kroky metody AHP. Pokud aplikace nevznikne, nebude v práci prezentována jako realizovaný výstup.

## Použití nástrojů umělé inteligence

<!-- BP-DOPLNIT: Prohlášení v BP 0.md slibuje plnou deklaraci využití AI nástrojů, ale ta dosud v textu chybí. Před odevzdáním doplnit podle skutečně použitých nástrojů: název a verze nástroje, účel použití (např. jazyková kontrola, kontrola konzistence kapitol, podpora při formulaci textu, kontrola citací), konkrétní metoda zadávání (promptů) a rozsah, ve kterém byl výstup nástroje použit nebo upraven. Nevyplňovat obecnou formulací — fakulta požaduje popis nástroje, verze, účelu, metody a rozsahu. -->

⟦DOPLNIT: popis použití nástrojů umělé inteligence⟧

# Databázové systémy

## Základní pojmy

Při práci s databázemi je nutné rozlišovat některé základní pojmy, jako jsou data, informace, databáze a systém řízení báze dat. Pod pojmem data si lze představit jednotlivá fakta nebo zaznamenané hodnoty (Elmasri a Navathe, 2016). Tyto hodnoty samy o sobě nemusí být nositeli žádného širšího významu (Watt a Eng, 2014). Informace pak vznikají právě přiřazením významu datům v určitém kontextu (Elmasri a Navathe, 2016; Watt a Eng, 2014). Pojem databáze pak představuje organizovanou sbírku vzájemně souvisejících dat, která jsou uložena tak, aby s nimi bylo možné dále efektivně pracovat (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Watt a Eng, 2014).

Systém řízení báze dat, běžně označovaný jako DBMS, je specializovaný software, který zajišťuje definici, ukládání, manipulaci, zabezpečení a správu dat uložených v databázi (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Spojení databáze s DBMS vytvoří databázový systém, který usnadňuje definování, vytváření, manipulaci a sdílení databáze mezi různými uživateli a aplikacemi (Elmasri a Navathe, 2016). DBMS v rámci tohoto systému zajišťuje transakční zpracování, obnovení dat po pádu, souběžný přístup více uživatelů i řízení ochrany dat (Pokorný a Valenta, 2020).

Původně se používal především jednoduchý souborový přístup, který měl však řadu problémů a omezení, například v podobě nekonzistentnosti dat při aktualizaci, závislosti na aplikačním programu a na fyzické struktuře, často spojené s redundancí dat (Elmasri a Navathe, 2016). Databázový přístup tyto nedostatky odstraňuje, a to tím, že integruje data do jednoho logického celku a odděluje definici dat od samotných aplikací (Pokorný a Valenta, 2020). Tímto oddělením se získává vyšší bezpečnost, možnost centrálního řízení integritních omezení a možnost sdílení dat mezi více uživateli (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

## Schéma databáze, instance a metadata

V teorii databází je třeba rozlišovat mezi schématem databáze a instancí databáze. Schéma databáze představuje popis struktury uložených dat a zahrnuje určení entit, atributů, vazeb a integritních omezení, která mají data splňovat (Pokorný a Valenta, 2020). Pojem instance databáze naopak vyjadřuje konkrétní aktuální obsah databáze v určitém čase (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Toto rozlišení odděluje relativně stabilní strukturální návrh od proměnlivých datových hodnot (Elmasri a Navathe, 2016).

S databázovým systémem souvisí také pojem metadata. Metadata jsou data o datech. Tato data tedy popisují strukturu databáze, význam atributů, integritní omezení nebo například přístupová práva (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Metadata bývají ukládána v systémovém katalogu, který slouží jako centrální zdroj informací o databázových objektech (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

Správa a údržba schématu databáze je klíčovou rolí správce databáze (DBA), přičemž změny schématu v průběhu životního cyklu systému musí být pečlivě kontrolovány (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Metadata uložená v systémovém katalogu jsou využívána nejen samotným DBMS pro optimalizaci dotazů a kontrolu přístupových práv, ale také externími nástroji (Elmasri a Navathe, 2016). Tyto nástroje dokážou metadata z katalogu načíst a vizualizovat je ve formě diagramů. Tato vizualizace pak usnadňuje pochopení existující struktury databáze a její další rozvoj (Pokorný a Valenta, 2020).

## Funkce DBMS a víceúrovňová architektura

DBMS obvykle poskytuje několik základních skupin funkcí: definici dat, manipulaci s daty, řízení souběžného přístupu více uživatelů, ochranu dat a obnovu po chybě (Pokorný a Valenta, 2020). Pro tyto funkce se používá jazyk DDL (Data Definition Language), který slouží k definici dat, a pak jazyk DML (Data Manipulation Language) určený pro manipulaci s daty. Vedle toho se používá pojem transakce, což je logický celek operací, který má být proveden buď celý, nebo vůbec (Elmasri a Navathe, 2016).

Další významnou myšlenkou bylo chápat DBMS jako víceúrovňový systém podle modelu ANSI/SPARC. Tento přístup představuje databázi jako hierarchii abstrakcí, které oddělují externí, konceptuální a interní úroveň (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Ve zprávě výboru ANSI/X3/SPARC z roku 1975 se toto členění upřesňuje takto: externí úroveň odpovídá pohledům jednotlivých skupin uživatelů, konceptuální úroveň představuje globální logický model celé databáze a interní úroveň popisuje fyzické uložení dat. Hlavním smyslem tohoto členění je podpora datové nezávislosti, tedy oddělení aplikací a uživatelských pohledů od fyzické implementace databáze (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Watt a Eng, 2014).

Pro následné porovnání nástrojů v této práci je toto rozdělení vhodné proto, že nástroje nepokrývají všechny úrovně databázového systému stejným způsobem (Rosenthal a Reiner, 1994). Některé se zaměřují především na konceptuální nebo logický model, jiné podporují i fyzické prvky konkrétního DBMS, například datové typy, indexy nebo generování SQL skriptů (Carvalho et al., 2022). Při hodnocení nástrojů je proto vhodné sledovat nejen možnosti vytváření diagramů, ale také podporu přechodu mezi jednotlivými úrovněmi návrhu a implementace (Rosenthal a Reiner, 1994).

## Fáze návrhu databáze

Návrh databáze představuje jednu z hlavních fází v rámci životního cyklu vývoje databázového systému a probíhá v několika na sebe navazujících krocích. Přímý přechod k fyzické implementaci tabulek v konkrétním systému může vést k chybám v návrhu, redundanci a omezené rozšiřitelnosti (Carvalho et al., 2022). Z tohoto důvodu se v literatuře standardně rozlišuje konceptuální, logický a fyzický návrh (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Rosenthal a Reiner, 1994).

Konceptuální návrh zachycuje strukturu aplikační domény bez vazby na konkrétní databázový systém (Carvalho et al., 2022; Rosenthal a Reiner, 1994). V této fázi jsou identifikovány entity, vztahy mezi nimi, atributy a základní integritní omezení. Výsledkem je konceptuální schéma, které věrně popisuje realitu a je nezávislé na zvoleném DBMS (Carvalho et al., 2022; Pokorný a Valenta, 2020).

Na konceptuální návrh navazuje logický návrh. V této části se konceptuální model převádí do zvoleného datového modelu, v případě této práce jde zejména o model relační (Rosenthal a Reiner, 1994). Dochází k návrhu relací, atributů, klíčů, cizích klíčů a integritních omezení. Výsledkem je logické schéma databáze, které lze implementovat v konkrétním DBMS (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

Ve fyzickém návrhu se řeší způsob uložení dat v konkrétním databázovém systému (Pokorný a Valenta, 2020; Rosenthal a Reiner, 1994). Řeší se zde organizace datových souborů, indexy, výkonové aspekty, optimalizace přístupu a další technické detaily (Rosenthal a Reiner, 1994). Na rozdíl od konceptuálního a logického návrhu je fyzický návrh silně závislý na konkrétní technologii (Pokorný a Valenta, 2020).

Mezi jednotlivými kroky návrhu existuje zpětná vazba. Pokud se při fyzickém návrhu ukáže, že některé části modelu vedou například k výkonovým problémům, je nutné vrátit se zpět k logickému návrhu (Rosenthal a Reiner, 1994). Podobně může změna požadavků uživatelů vyvolat úpravu konceptuálního modelu a následně i všech dalších úrovní (Carvalho et al., 2022; Rosenthal a Reiner, 1994). Návrh databáze proto nelze chápat jako striktně lineární proces, ale jako iterativní postup, v němž se schéma průběžně zpřesňuje, opravuje a reorganizuje (Carvalho et al., 2022; Rosenthal a Reiner, 1994).

Rozdělení návrhu databáze na konceptuální, logickou a fyzickou úroveň tvoří vhodný výchozí bod pro pozdější definici hodnoticích kritérií. Nástroj určený pro návrh databázového systému by měl umožnit zachytit požadavky, převést je do konzistentního schématu a podle potřeby podpořit technickou implementaci v konkrétním databázovém prostředí (Rosenthal a Reiner, 1994). Úroveň podpory těchto kroků představuje důležitý ukazatel kvality daného nástroje (Carvalho et al., 2022; Rosenthal a Reiner, 1994).

# Datové modely

Datový model poskytuje formalizovaný nástroj, který slouží k popisu dat, jejich struktur a vztahů mezi nimi (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Definuje datové objekty a jejich vzájemné vztahy včetně omezení, která se jich týkají. Datový model je zjednodušený popis reality, který je vytvořen tak, aby se podle něj dala navrhnout a implementovat databáze (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

## Konceptuální modelování a ER/EER model

### Konceptuální modelování a základní pojmy ER modelu

Konceptuální modelování slouží k zachycení požadavků aplikační domény, kterou má navrhovaný systém pokrývat, ale bez ohledu na konkrétní databázovou technologii (Carvalho et al., 2022; Chlapek, Kučera a Palovská, 2019). Jeho cílem je vytvořit přehledný a věrný model reálného světa (Carvalho et al., 2022). V praxi se pro tuto fázi velmi často používá entitně-relační model (ER model) (Chen, 1976), případně jeho rozšířená varianta Enhanced Entity-Relationship (EER) model (Elmasri a Navathe, 2016).

Základními pojmy ER modelu jsou entita, entitní množina, vztah a atribut. Za entitu je považován objekt, který je schopen samostatné existence a lze jej jednoznačně odlišit od ostatních objektů (Chen, 1976). Entitní množina je pak množina entit, které jsou stejného typu a mají společné vlastnosti (Chen, 1976). Vztah vyjadřuje vazbu mezi entitami nebo entitními množinami a atribut představuje vlastnost entity nebo vztahu (Chen, 1976).

Vztahy mezi entitami lze popsat například kardinalitou a participací. Kardinalita udává, kolik entit jedné množiny může být ve vztahu k entitě jiné množiny (Elmasri a Navathe, 2016). Typickými případy jsou vazby 1:1, 1:N a M:N. Participace vyjadřuje, zda je účast entity ve vztahu povinná nebo nepovinná (Elmasri a Navathe, 2016). Tyto pojmy jsou důležité nejen na konceptuální úrovni, ale i pro následnou transformaci do relačního modelu (Pokorný a Valenta, 2020).

### Atributy, EER model a notace

Atributy jsou svázány s doménami, tedy s množinami přípustných hodnot (Elmasri a Navathe, 2016). Rozlišujeme jednoduché a složené atributy, případně i další typy (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Pro jednoznačnou identifikaci entit slouží kandidátní a primární klíče (Elmasri a Navathe, 2016).

Rozšířený ER model (EER) doplňuje základní ER model o supertřídy, podtřídy a dědičnost atributů (Elmasri a Navathe, 2016). EER model je vhodný především tam, kde je potřeba přesněji vystihnout specializaci nebo generalizaci objektů (Elmasri a Navathe, 2016). V praxi se ER/EER model vyjadřuje různými grafickými notacemi, přičemž mezi nejčastější patří Chenova notace a Crow’s Foot. Alternativně lze pro modelování datových struktur využít také UML diagram tříd (Carvalho et al., 2022; Chlapek, Kučera a Palovská, 2019).

Pro hodnocení databázových nástrojů je podpora konceptuálního modelování významná hlavně z praktického hlediska. Nástroj by měl umožnit vyjádřit entity, vztahy, kardinality a omezení způsobem, který je srozumitelný jak analytikům, tak i vývojářům (Carvalho et al., 2022). Jednotlivé nástroje se přitom mohou lišit použitou notací, úrovní podpory EER prvků a možností následného převodu modelu do relačního schématu (Carvalho et al., 2022; Rosenthal a Reiner, 1994).

## Relační model

Relační model je založen na relacích, které se v praxi obvykle zobrazují jako tabulky (Elmasri a Navathe, 2016). Každá relace má své schéma, tedy jméno relace, seznam atributů a jejich domén (Pokorný a Valenta, 2020). Konkrétní řádky tabulky odpovídají n-ticím (Codd, 1970; Elmasri a Navathe, 2016). Relační model pracuje s atomickými hodnotami a s přesně vymezenými atributy (Codd, 1970; Elmasri a Navathe, 2016).

Klíče jsou v relačním modelu zásadní. Primární klíč slouží k jednoznačné identifikaci řádku tabulky (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Cizí klíč umožňuje vyjádřit vazbu mezi tabulkami a je základem referenční integrity (Watt a Eng, 2014). Mezi obecné vlastnosti relačních tabulek patří nezávislost na pořadí řádků a sloupců a požadavek na neduplicitu řádků (Codd, 1970; Elmasri a Navathe, 2016).

Relační model je pro tuto práci důležitý také proto, že většina běžně používaných návrhových nástrojů pro databáze směřuje k tvorbě relačního schématu a k práci s SQL databázemi. Při jejich porovnání je proto důležité, zda nástroj podporuje definici primárních a cizích klíčů, integritních omezení, datových typů a generování nebo zpětné načítání databázového schématu (Carvalho et al., 2022).

## Transformace ER/EER modelu do relačního modelu

Při přechodu z konceptuálního modelu k modelu relačnímu se entity obvykle převádějí na tabulky a atributy na sloupce (Chlapek, Kučera a Palovská, 2019). Vztahy typu 1:N se zpravidla reprezentují pomocí cizího klíče na straně N, zatímco pro vztahy M:N je vyžadováno vytvoření samostatné spojovací tabulky. Specifické případy představují vztahy 1:1, atributy vztahů nebo převod supertříd a podtříd (Elmasri a Navathe, 2016). Tato transformace je důležitým přechodem mezi konceptuálním a logickým návrhem (Rosenthal a Reiner, 1994). Pokud je tato transformace provedena nekonzistentně, vede k problémům v následné implementaci (Carvalho et al., 2022; Rosenthal a Reiner, 1994).

U nástrojů pro návrh databází je proto důležité, zda převod mezi konceptuálním a relačním modelem pouze vizuálně naznačují, nebo zda tento převod dokážou částečně automatizovat a kontrolovat (Carvalho et al., 2022; Rosenthal a Reiner, 1994). Automatické generování relačního schématu může práci urychlit, ale je potřeba ověřit, zda nástroj také správně zachází s kardinalitami, vazbami M:N, povinnými atributy a integritními omezeními (Carvalho et al., 2022).

## Normalizace relačního modelu

Normalizace je proces, jehož cílem je odstranit nadbytečnost dat a předcházet anomáliím při vkládání, aktualizaci a mazání údajů (Codd, 1970; Elmasri a Navathe, 2016). Teoretickým základem normalizace jsou funkční závislosti, které určují vztahy mezi atributy a umožňují identifikovat nadbytečnost a anomálie v databázovém schématu (Codd, 1970; Elmasri a Navathe, 2016).

Normální formy představují soubor pravidel pro návrh relační databáze, jejichž cílem je omezit redundanci dat a snížit riziko nekonzistence. První normální forma vyžaduje, aby atributy obsahovaly pouze atomické hodnoty a aby se v tabulkách nevyskytovaly skupiny, které se opakují (Codd, 1970; Elmasri a Navathe, 2016). Druhá normální forma se zaměřuje na tabulky se složeným klíčem a požaduje, aby každý neklíčový atribut závisel na celém klíči, nikoli pouze na jeho části (Codd, 1970; Elmasri a Navathe, 2016). Třetí normální forma dále odstraňuje tranzitivní závislosti, u nichž jeden neklíčový atribut závisí na jiném neklíčovém atributu (Codd, 1970; Elmasri a Navathe, 2016). Dodržování těchto forem podle Codda (1970) a Elmasriho s Navathem (2016) vede k zajištění základní konzistence relačního schématu. Z toho důvodu by tato pravidla měla respektovat většina nástrojů pro návrh databází.

Normalizace ukazuje mimo jiné, že kvalita návrhového nástroje nespočívá jen v grafické podobě diagramu. Důležité je, zda nástroj podporuje konzistenci modelu, upozorňuje na chybějící klíče nebo problematické vazby a umožňuje vytvořit návrh, který lze převést do udržitelného relačního schématu. Tato hlediska navazují na pozdější výběr hodnoticích kritérií pro komparaci nástrojů (Carvalho et al., 2022).

# Vícekriteriální rozhodování

Vícekriteriální rozhodování se zabývá situacemi, ve kterých nelze rozhodnout podle jednoho hlediska (Mardani et al., 2015). V běžných rozhodovacích úlohách jsou alternativy obvykle hodnoceny podle více kritérií. Tato kritéria však mohou být ve vzájemném konfliktu (Velasquez a Hester, 2013). Z tohoto důvodu se používají metody, které umožňují tato kritéria systematicky zahrnout do rozhodovacího procesu a výsledek rozhodnutí zdůvodnit (Mardani et al., 2015).

Rozhodovací úloha je běžně popsána množinou variant, množinou hodnoticích kritérií a vztahem mezi nimi (Soukopová, 2016). Varianty představují jednotlivé posuzované možnosti, mezi kterými se rozhoduje. Kritéria určují, z jakých hledisek jsou jednotlivé varianty hodnoceny (Velasquez a Hester, 2013). Hodnocení variant podle jednotlivých kritérií se často zapisuje do kriteriální matice. Tato matice umožňuje zachytit přehledně hodnoty alternativ vzhledem k jednotlivým kritériím (Soukopová, 2016).

S vícekriteriálním rozhodováním souvisejí i pojmy jako ideální a bazální varianta, dominance a nedominované řešení. Ideální varianta je hypotetická varianta, která ve všech kritériích získává nejlepší možné hodnoty (Soukopová, 2016; Velasquez a Hester, 2013). Bazální varianta naopak představuje hypotetickou variantu s nejhoršími hodnotami. Dominance vyjadřuje vztah mezi dvěma variantami, kdy jedna varianta je alespoň v jednom kritériu lepší a v ostatních není horší než druhá varianta. Nedominovaná varianta je taková varianta, pro kterou neexistuje jiná varianta lepší alespoň v jednom kritériu a současně ne horší v ostatních (Soukopová, 2016). Tyto pojmy se používají především u metod, které pracují se vzdáleností od ideálního řešení nebo s porovnáváním dominance mezi variantami (Velasquez a Hester, 2013).

Pro tuto práci je důležité zejména vícekriteriální hodnocení variant. V praktické části je porovnáván konečný seznam nástrojů pro návrh a vývoj databázových systémů. Jde tedy o případ, kdy jsou předem dány alternativy a z těchto alternativ je nutné určit nejvhodnější řešení (Mardani et al., 2015; Saaty, 1990). Cílem přitom není označit jeden nástroj za univerzálně nejvhodnější, ale vysvětlit jeho vhodnost vzhledem ke zvoleným kritériím, jejich vahám a uvažovanému použití (Saaty, 2008; Soukopová, 2016).

Při rozhodování o výběru softwarových nástrojů je vícekriteriální přístup vhodný proto, že rozhodnutí obvykle zahrnuje technická, ekonomická a uživatelská hlediska (Mardani et al., 2015; Velasquez a Hester, 2013). U databázových nástrojů jsou obvykle některá kritéria měřitelná přímo, například cena, licence nebo dostupnost pro konkrétní platformu. Jiná kritéria naopak mají popisnou povahu, například přehlednost uživatelského rozhraní, podpora modelování nebo srozumitelnost dokumentace. Vícekriteriální metody pomáhají přehledně spojit všechna důležitá hlediska do jednoho rozhodovacího procesu (Mardani et al., 2015).

## Alternativa, kritérium a váha kritéria

Alternativa představuje jednu z možných variant rozhodnutí (Soukopová, 2016). V rámci této práce každá alternativa představuje konkrétní softwarový nástroj určený pro návrh a vývoj databázových systémů. Kritérium je hledisko, podle kterého se jednotlivé alternativy posuzují (Soukopová, 2016). Může jít například o funkcionalitu, použitelnost, kompatibilitu s různými DBMS, podporu reverzního inženýrství nebo cenu (Carvalho et al., 2022).

Samotná kritéria lze uspořádat různými způsoby podle potřeb konkrétní rozhodovací úlohy. Základní dělení odlišuje kritéria maximalizační a minimalizační (Soukopová, 2016). U maximalizačních kritérií je požadována co nejvyšší hodnota, například rozsah funkcí nebo počet podporovaných databázových platforem. U minimalizačních kritérií je naopak požadována co nejnižší hodnota, například cena, časová náročnost zavedení nebo složitost práce. Kritéria mohou být kvantitativní nebo kvalitativní, a jejich kombinace je u hodnocení softwaru zcela běžná (Soukopová, 2016; Velasquez a Hester, 2013).

Váha kritéria vyjadřuje jeho relativní význam v rámci rozhodovacího procesu (Saaty, 1990; Soukopová, 2016). Ne všechna kritéria mají stejnou důležitost, a proto je nutné jejich význam určit explicitně. Určení vah kritérií je jedním z klíčových kroků většiny vícekriteriálních metod. Právě váhy často zásadně ovlivňují výsledné pořadí alternativ (Saaty, 1990).

Při volbě vah je důležité vycházet z účelu hodnocení (Saaty, 2008; Soukopová, 2016). V prostředí s omezeným rozpočtem může být cena klíčová, zatímco ve firmě, která už používá určitou databázovou platformu, může mít větší váhu právě její podpora. Stejný nástroj proto může být v jednom rozhodovacím scénáři vhodnější než v jiném. Kritéria jsou proto v praktické části navázána na modelovou situaci a požadavky uživatele (Saaty, 2008).

## Přístupy k odhadu vah kritérií a porovnání alternativ

Pro odhadnutí vah jednotlivých kritérií lze použít několik postupů (Saaty, 2008; Soukopová, 2016). Mezi nejznámější jednoduché přístupy patří metoda pořadí nebo bodovací metoda. Tyto metody lze použít jednoduše, ale nejsou dostatečně přesné při popisu toho, jak výrazně je jedna z možností důležitější než druhá. Pokročilejší postupy pracují s párovým porovnáváním kritérií a do této skupiny patří právě i Saatyho metoda, která je s metodou AHP přímo spojena (Saaty, 1990; Soukopová, 2016).

Při hodnocení samotných alternativ umožňuje AHP použít stejný princip párového porovnávání i pro alternativy, a to vzhledem ke každému z dříve stanovených kritérií (Saaty, 2008; Vaidya a Kumar, 2006). Výhodou pak je systematičnost a transparentnost, naopak nevýhodou je vyšší pracnost při větším počtu prvků. Počet porovnání roste s počtem kritérií a alternativ. Proto je vhodné zvolit přiměřený rozsah rozhodovacího modelu (Ishizaka a Labib, 2011).

Z dalších metod vícekriteriálního hodnocení variant jsou rozšířeny především metoda váženého součtu (WSA), metoda TOPSIS a metody založené na outrankingu. Metoda váženého součtu pracuje s normalizovanými hodnotami kritérií a výsledné skóre alternativy vypočítá jako vážený součet (Soukopová, 2016; Velasquez a Hester, 2013). TOPSIS hodnotí alternativy podle jejich vzdálenosti od ideální a bazální varianty (Velasquez a Hester, 2013). Komplexnější strukturou se vyznačuje rodina metod ELECTRE, které pracují s koncepty převahy jedné varianty nad druhou (Mardani et al., 2015; Velasquez a Hester, 2013).

Pro potřeby práce je metoda AHP vhodná ze tří důvodů. Za prvé, AHP umožňuje pracovat současně s kvantitativními i kvalitativními kritérii, a to dokonce bez nutnosti převádět jednotlivá hodnocení na jednotnou měrnou škálu (Ishizaka a Labib, 2011; Saaty, 1990). Za druhé, je postup metody srozumitelný a vysvětlitelný, protože pracuje s hierarchií cíle, kritérií a alternativ (Saaty, 2008). Za třetí, AHP pomocí poměru konzistence umožňuje zkontrolovat, zda na sebe jednotlivá hodnocení logicky navazují. To je zvlášť užitečné v situacích, kdy párové porovnávání provádí jen jedna osoba (Ishizaka a Labib, 2011; Saaty, 1990).

## Metoda AHP

Metoda AHP patří mezi nejznámější metody vícekriteriálního rozhodování (Ishizaka a Labib, 2011; Moreno-Jiménez a Vargas, 2018; Vaidya a Kumar, 2006). Jejím autorem je Thomas L. Saaty. Podstata této metody spočívá v rozdělení složitého rozhodovacího problému do přehledné hierarchie, která obsahuje hlavní cíl, kritéria, případně subkritéria a jednotlivé alternativy (Saaty, 1990; Saaty, 2008). Díky tomuto rozkladu lze lépe porozumět struktuře rozhodovací úlohy a následně jednotlivé prvky systematicky porovnat (Vaidya a Kumar, 2006).

Na nejvyšší úrovni hierarchie se nachází hlavní cíl rozhodování, například výběr nejvhodnějšího databázového nástroje (Saaty, 2008). Pod ním se nacházejí kritéria, případně subkritéria, a na nejnižší úrovni stojí jednotlivé alternativy. Hlavní myšlenkou metody je porovnat dva prvky na stejné úrovni a určit jejich relativní důležitost vzhledem k nadřazenému prvku (Saaty, 1990; Saaty, 2008).

AHP se využívá hlavně v případech, kdy je potřeba při rozhodování spojit různé typy kritérií, například technické parametry, ekonomické ukazatele a kritéria, která se hodnotí spíše subjektivně nebo kvalitativně (Ishizaka a Labib, 2011; Saaty, 1990). Pro tuto práci je tato metoda vhodná, protože jednotlivé nástroje pro návrh a vývoj databázových systémů nelze hodnotit jen kvantitativně jednou měřitelnou veličinou. Kromě ceny nebo podpory konkrétního DBMS je třeba zohlednit i další vlastnosti – například jaké modelovací funkce nabízí, jak se s ním pracuje, jak kvalitní je dokumentace, zda podporuje reverzní inženýrství a jaké možnosti poskytuje pro generování SQL skriptů. Přehledové studie ukazují, že AHP se využívá v mnoha různých typech rozhodovacích úloh a je vhodná i pro situace, kdy je potřeba vybírat mezi softwarovými systémy (Ho, 2008; Moreno-Jiménez a Vargas, 2018; Simanavičienė a Vdovinskienė, 2023; Vaidya a Kumar, 2006).

Typický postup AHP lze shrnout do několika kroků. Nejprve je vymezen cíl rozhodování a sestavena hierarchie kritérií a alternativ (Saaty, 2008). Poté se provedou párová porovnání kritérií vzhledem k cíli a párová porovnání alternativ vzhledem ke každému kritériu (Saaty, 1990). Z těchto porovnání se vypočítají lokální priority a ověří se konzistence úsudků. Nakonec se lokální váhy agregují do celkového pořadí alternativ (Ishizaka a Labib, 2011; Saaty, 2008).

### Saatyho škála a párové porovnání

Při párovém porovnávání se používá Saatyho škála. Základní hodnoty této škály jsou 1, 3, 5, 7 a 9, které vyjadřují stejnou důležitost, mírnou, silnou, velmi silnou až absolutní preferenci (Saaty, 1990; Saaty, 2008). Sudé hodnoty 2, 4, 6, 8 jsou chápány jako mezistupně. Pokud je jeden prvek méně významný než druhý, použije se převrácená hodnota (Ishizaka a Labib, 2011; Saaty, 1990). Hodnota 1 tedy znamená rovnocennost dvou prvků, zatímco hodnota 9 vyjadřuje krajní převahu jednoho prvku nad druhým.

Výsledkem párového porovnání je čtvercová reciproční matice, označovaná jako Saatyho matice (Saaty, 1990). Reciproční povaha matice znamená, že pokud je prvek A vůči prvku B hodnocen hodnotou 5, pak opačné porovnání B vůči A má hodnotu 1/5 (Ishizaka a Labib, 2011; Saaty, 2008). Hlavní diagonála matice obsahuje hodnoty 1, protože každý prvek je sám se sebou stejně důležitý.

Z této matice se následně vypočítají lokální váhy. V odborné literatuře se objevují různé způsoby výpočtu vah v metodě AHP, například postup založený na vlastním vektoru nebo metoda využívající geometrický průměr řádků (Ishizaka a Labib, 2011; Saaty, 1990). Výsledkem výpočtu je vektor priorit. Hodnoty vektoru priorit vyjadřují relativní význam porovnávaných prvků (Saaty, 1990; Saaty, 2008). U kritérií tyto hodnoty představují jejich váhy, u alternativ pak jejich lokální hodnocení vzhledem ke konkrétnímu kritériu.

Pro tuto práci je důležité, že párové porovnávání umožňuje hodnotiteli vyjadřovat preference postupně a přehledně. Místo toho, aby musel přímo přiřazovat přesné váhy všem kritériím, posuzuje vždy jen dvojici prvků a rozhoduje, který z nich je vzhledem k danému cíli nebo kritériu důležitější (Saaty, 2008). To je užitečné zejména u kritérií, která nejsou přímo měřitelná, například přehlednost prostředí nebo kvalita podpory modelování (Saaty, 1990).

### Kontrola konzistence

Protože párové porovnávání vychází z lidského úsudku, není vždy dokonale konzistentní. Součástí metody AHP je proto kontrola konzistence. K tomu slouží Consistency Index (CI), Random Consistency Index (RI) a Consistency Ratio (CR) (Ishizaka a Labib, 2011; Saaty, 1990). V praxi se uvažuje, že hodnota CR menší než 0,1 značí přijatelnou úroveň konzistence. Vyšší hodnoty poměru konzistence (CR) obvykle vedou k přehodnocení porovnání (Saaty, 1990; Saaty, 2008).

Konzistence ověřuje, zda jsou jednotlivé úsudky hodnotící osoby vzájemně logické a v souladu a zda si navzájem neodporují (Ishizaka a Labib, 2011; Saaty, 2008). Pokud je například kritérium A výrazně důležitější než kritérium B a kritérium B je důležitější než kritérium C, potom by mělo být kritérium A zároveň důležitější než kritérium C. Menší odchylky jsou při rozhodování přirozené, příliš vysoká nekonzistence však snižuje důvěryhodnost výsledků (Saaty, 1990; Saaty, 2008).

Možnost ověřit konzistenci je jedním z důvodů, proč je AHP pro tuto práci vhodnější než jednodušší bodovací postup. Při hodnocení databázových nástrojů je část úsudků založena na kvalitativním posouzení, například u použitelnosti nebo přehlednosti práce s modelem. Ukazatel CR umožňuje ověřit, zda jsou tato porovnání vnitřně soudržná, a případně se k problematickým porovnáním vrátit (Ishizaka a Labib, 2011; Saaty, 1990; Saaty, 2008).

### Výhody a omezení AHP

Výhody metody AHP byly stručně naznačeny již v kapitole 6.2, a to možnost kombinovat kvantitativní i kvalitativní kritéria, srozumitelnost postupu a kontrola konzistence úsudků. Následující text pak tyto výhody rozvádí a doplňuje je o další přínosy metody a uvádí i její hlavní omezení. Metoda současně umožňuje analýzu citlivosti, tedy sledování dopadu změny vah kritérií na výsledné pořadí (Ho, 2008; Saaty, 2008). To je důležité zejména tehdy, když jsou výsledky citlivé na malé změny preferencí a kdy je třeba ověřit stabilitu doporučení.

Nevýhodou metody je pracnost při větším počtu kritérií a alternativ a jistá míra subjektivity, která je s párovým porovnáváním spojena (Ishizaka a Labib, 2011; Saaty, 2008). Pokud je v modelu mnoho prvků, počet potřebných porovnání rychle roste. Hodnotitel pak může být zatížen opakováním podobných rozhodnutí (Ishizaka a Labib, 2011). Proto je vhodné udržet počet kritérií i alternativ v přiměřeném rozsahu a jasně vymezit význam jednotlivých kritérií.

V odborné literatuře se diskutuje jev rank reversal, tedy možná změna pořadí alternativ při přidání nebo odebrání varianty z modelu (Ishizaka a Labib, 2011; Saaty, 2008; Vaidya a Kumar, 2006). Tento problém neznamená, že AHP nelze použít, ale ukazuje, že výsledky je třeba interpretovat s ohledem na zvolený soubor alternativ a nastavení modelu. V praktické části je proto zdůvodněno, proč byly vybrány právě dané nástroje a jaké požadavky reprezentují.

V souvislosti s výběrem databázového nástroje je AHP užitečná tím, že umožňuje oddělit stanovení vah kritérií od samotného hodnocení alternativ (Catak et al., 2012; Ebrahimi a Taheri, 2015; Simanavičienė a Vdovinskienė, 2023). Nejprve je možné určit, jak významná je například funkcionalita, použitelnost, kompatibilita, cena nebo podpora vývojového procesu, a teprve poté hodnotit jednotlivé nástroje vůči těmto kritériím (Saaty, 1990). Díky tomu je výsledné pořadí zdůvodněno explicitně, nikoli pouze celkovým dojmem.

# Nástroje pro návrh a vývoj databází

<!-- BP-DOPLNIT: Před odevzdáním nahradit údaje ⟦NEOVĚŘENO⟧ přesnými verzemi a edicemi skutečně použitými při testu. -->

Výběr nástrojů pro porovnání vycházel nejprve z přehledu dostupných nástrojů pro návrh a vývoj databází. Jako jeden z podkladů byla využita studie Carvalho et al. (2022), která hodnotila sedmnáct nástrojů pro datové modelování. Ze studie vyplývá, že nabídka těchto nástrojů je velmi široká a obsahuje nástroje online i desktopové, bezplatné i komerční a také nástroje zaměřené na různé databázové platformy. Příkladem online nástroje je ONDA vyvinutý na Univerzitě v Coimbře (Laranjeiro a Pinto, 2024), který však do výběru zařazen nebyl, protože práce se soustředí na plnohodnotné desktopové nástroje. Dalším podkladem byla oficiální online dokumentace vybraných nástrojů, ze které byly ověřeny jejich základní funkce, podporované databázové platformy a licenční podmínky. Pro posouzení významu jednotlivých databázových platforem byl využit také žebříček DB-Engines (2026).

Na základě těchto podkladů byly pro další práci vybrány čtyři nástroje: Oracle SQL Developer Data Modeler, DBeaver Community Edition, MySQL Workbench Community Edition a pgModeler. Při výběru bylo zohledněno, zda vybraný nástroj podporuje návrh databáze, zda je dostupný v bezplatné nebo volně testovatelné verzi a zda vhodně doplňuje ostatní vybrané nástroje. Oracle SQL Developer Data Modeler je zaměřený hlavně na Oracle Database, MySQL Workbench na MySQL, pgModeler na PostgreSQL a DBeaver představuje univerzálnější nástroj podporující více DBMS. Tři z těchto nástrojů (Oracle SQL Developer Data Modeler, MySQL Workbench a pgModeler) jsou uvedeny také ve studii Carvalho et al. (2022), přičemž pgModeler v jejich hodnocení dosáhl ze všech sedmnácti posuzovaných nástrojů nejlepšího výsledku. DBeaver byl do výběru zařazen navíc jako univerzální nástroj podporující více DBMS, který v původní studii chybí. Díky tomu je možné výsledky alespoň částečně porovnat s již publikovanou studií. Volba databázových platforem vychází také z jejich rozšířenosti. Oracle Database, MySQL a PostgreSQL patří podle žebříčku DB-Engines (2026) mezi významné relační databázové systémy. Do úvahy byl brán také Microsoft SQL Server, avšak nakonec nebyl zařazen, protože práce se zaměřuje na nástroje s velkou podporou databázového modelování a zároveň chce zachovat přiměřený počet alternativ pro AHP. U univerzálních nástrojů se při hodnocení sleduje také to, zda umožňují práci s více databázovými platformami, případně i s nerelačními databázemi.

Základní charakteristiky vybraných nástrojů shrnuje tabulka 1.

| **Nástroj** | **Zaměření** | **Licence** | **Vybrané funkce** |
|:---|:---|:---|:---|
| Oracle SQL Developer Data Modeler | Oracle Database | bezplatný nástroj | logické, relační a fyzické modely, forward a reverse engineering |
| DBeaver Community Edition | více databázových systémů | open-source komunitní edice | SQL vývoj, správa dat, ER diagramy, generování DDL |
| MySQL Workbench Community Edition | MySQL | komunitní edice | EER diagramy, správa serveru, forward a reverse engineering |
| pgModeler | PostgreSQL | Community / placená edice Plus | návrh schémat, SQL export a validace; dostupnost reverse engineeringu se ověřuje podle přesné verze a edice |

<span id="_Toc234483571" class="anchor"></span>Tabulka 1: Základní charakteristiky vybraných nástrojů (vlastní zpracování podle Oracle, 2026; DBeaver, 2026; MySQL, 2026; pgModeler, 2026)

## Oracle SQL Developer Data Modeler

Oracle SQL Developer Data Modeler je bezplatný grafický nástroj společnosti Oracle pro modelování dat. Podporuje logické, relační, fyzické, multidimenzionální a typové modely, nabízí forward i reverse engineering a integraci se širším portfoliem Oracle SQL Developer. Jako primární databázová platforma je preferována Oracle Database, nástroj však umožňuje pracovat i s dalšími systémy (Oracle, 2026).

V praktické části byla použita verze **⟦NEOVĚŘENO – Oracle SQL Developer Data Modeler⟧**.

## DBeaver Community Edition

DBeaver je open-source univerzální databázový nástroj s podporou širokého spektra DBMS (PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, SQLite a další). Nabízí editor SQL, prohlížeč dat, vizualizaci databázových struktur pomocí ER diagramů a generování DDL skriptů. Pokročilejší funkce, například datové generátory nebo vizuální dotazování, jsou dostupné v komerční edici. Editace databázových objektů přímo v ER diagramu je podle aktuální dokumentace dostupná v edicích Enterprise a Ultimate, nikoli v Community Edition; Community Edition však umožňuje vytvářet databázové objekty prostřednictvím jejich editoru a zobrazovat diagram existujícího schématu (DBeaver, 2026).

V praktické části byla použita verze **⟦NEOVĚŘENO – DBeaver Community Edition⟧**.

## MySQL Workbench Community Edition

MySQL Workbench je oficiální nástroj společnosti Oracle pro práci s databází MySQL. Sjednocuje v jednom prostředí návrh databáze (EER diagramy), správu serveru, modelování, forward i reverse engineering a SQL vývoj. Podporuje synchronizaci modelu s živou databází a export modelu do DDL skriptu (MySQL, 2026).

V praktické části byla použita verze **⟦NEOVĚŘENO – MySQL Workbench Community Edition⟧**.

## pgModeler

pgModeler, jehož název vychází z označení PostgreSQL Database Modeler, je nástroj zaměřený přímo na databázi PostgreSQL. Umožňuje grafický návrh schémat, generování SQL skriptů a validaci modelu. Projekt nabízí komunitní variantu a placenou edici Plus. Aktuální produktové členění uvádí reverse engineering a synchronizaci mezi funkcemi edice Plus; dostupnost těchto funkcí se však musí vztáhnout k přesné testované verzi a sestavení (pgModeler, 2026). Cílovou databázovou platformou je PostgreSQL, jehož dokumentace vymezuje podporované datové typy a syntaxi SQL (PostgreSQL, 2026).

V praktické části byla použita verze a edice **⟦NEOVĚŘENO – pgModeler⟧**. Nedostupné funkce byly hodnoceny podle skutečných možností této edice, nikoli podle možností uvedených pouze pro jinou variantu.

# Návrh hodnoticích kritérií

<!-- BP-DOPLNIT: Před odevzdáním doplnit ověřené licenční údaje a konečná převodní pravidla pro Saatyho škálu. -->

Při stanovení kritérií pro hodnocení se vychází z toho, že nástroje jsou porovnávány především podle toho, jak dokážou podpořit návrh a vývoj databáze, nikoli podle toho, jak zvládají její provoz a správu. Hodnoticí kritéria vycházejí ze studie Carvalho et al. (2022), která byla využita i při výběru nástrojů v předchozí kapitole. Tato studie porovnávala nástroje pro datové modelování podle kategorií, jako jsou funkcionalita, provozní vlastnosti softwaru, dokumentace a komunitní podpora. Předkládaná práce přebírá její kategoriální členění a rozšiřuje je o kritéria specifická pro návrh databázových systémů a o vlastnosti, které lze ověřit jednotným praktickým testem. U kritérií, která nelze vyjádřit přímo číselně, se používá kvalitativní hodnocení a každé párové porovnání je stručně zdůvodněno.

## Přehled kritérií

Přehled osmi kritérií uvádí tabulka 2. Kritéria jsou stanovena před vyhodnocením výsledků, aby se omezilo jejich dodatečné přizpůsobení očekávanému pořadí nástrojů.

| **Kritérium** | **Název** | **Pozorované vlastnosti** | **Doklad** |
|:--:|:---|:---|:---|
| K1 | Funkcionalita | úrovně modelu, objekty, vztahy, integritní omezení, validace | checklist funkcí, model, screenshoty |
| K2 | Použitelnost | orientace v rozhraní, počet kroků, čas, chyby a potřeba dohledání postupu | časový záznam a protokol úloh |
| K3 | Kompatibilita s DBMS | podporované platformy a prakticky ověřená připojení | dokumentace a záznam připojení |
| K4 | Forward engineering | úplnost DDL, možnost spuštění a počet ručních oprav | vygenerovaný skript a protokol spuštění |
| K5 | Reverse engineering | dostupnost funkce a úplnost obnoveného modelu | model vytvořený z referenční databáze |
| K6 | Dokumentace a komunitní podpora | dostupnost, aktuálnost a použitelnost návodů a řešení problémů | odkazy a záznam vyhledávání |
| K7 | Import a export modelu | podporované formáty a kvalita použitelných výstupů | exportované soubory |
| K8 | Náklady a licenční omezení | pořizovací náklady a omezení testované edice | licenční podmínky a ceník |

<span id="_Toc234483572" class="anchor"></span>Tabulka 2: Přehled navržených hodnoticích kritérií (vlastní zpracování na základě Carvalho et al., 2022)

## Operacionalizace kritérií

### K1 Funkcionalita

Funkcionalita vyjadřuje rozsah modelovacích možností relevantních pro společné zadání. Sleduje se podpora logického nebo konceptuálního a fyzického modelu, definice tabulek a atributů, primárních a cizích klíčů, vazeb 1:N a 1:1, asociačních tabulek, složených klíčů, unikátních a kontrolních omezení a automatické validace modelu. Samostatně se zaznamenává, zda lze strukturu navrhovat v modelu nezávislém na živé databázi, nebo zda nástroj vytváří diagram až nad existujícími databázovými objekty. Funkce je započtena pouze tehdy, pokud byla v testované edici skutečně dostupná nebo ověřená.

### K2 Použitelnost

Použitelnost je posuzována při shodném cílovém zadání. Vedle celkového času se zaznamenává počet situací, kdy bylo nutné hledat postup v dokumentaci, počet chybných nebo opakovaných kroků, srozumitelnost chybových hlášení a subjektivní přehlednost prostředí. Samotný čas nesmí být interpretován bez kontextu, protože jej ovlivňuje předchozí zkušenost hodnotitele i rozdíl mezi modelově orientovaným a databázově orientovaným pracovním postupem.

### K3 Kompatibilita s DBMS

Kompatibilita rozlišuje deklarovanou a skutečně ověřenou podporu databázových platforem. Za silnější výsledek je považována podpora více relevantních DBMS bez nutnosti měnit edici nebo kupovat samostatný modul. U specializovaných nástrojů se jejich užší zaměření popisuje jako vlastnost, nikoli automaticky jako chyba; význam kompatibility se projeví zejména ve scénáři středně velké organizace.

### K4 Forward engineering

Forward engineering je hodnocen podle toho, zda nástroj vytvořil DDL odpovídající navrženému modelu, zda byl skript bez úprav spustitelný na cílové databázi a kolik ručních zásahů bylo nutné provést. Zaznamenávají se také chybějící objekty, změny datových typů a ztráta integritních omezení.

### K5 Reverse engineering

Reverse engineering je ověřen nad referenční databází vytvořenou ze stejného schématu. Sleduje se dostupnost funkce v testované edici, zachování tabulek, atributů, klíčů, vztahů a omezení a čitelnost výsledného diagramu. Pokud je funkce dostupná pouze v jiné placené edici, je tato skutečnost hodnocena současně v K5 a z hlediska nákladů také v K8, přičemž je v diskusi upozorněno na možné překrytí obou kritérií.

### K6 Dokumentace a komunitní podpora

Hodnocení vychází z oficiální dokumentace a z praktického dohledání postupů potřebných během testu. Zaznamenává se, zda dokumentace odpovídá použité verzi, obsahuje konkrétní postupy a umožnila vyřešit vzniklé problémy. Velikost komunity není zaměňována za kvalitu dokumentace a je používána pouze jako doplňující údaj.

### K7 Import a export modelu

Sleduje se export diagramu do PDF a PNG, export DDL a další formáty relevantní pro přenos nebo verzování modelu. Hodnocena je nejen existence položky v nabídce, ale také čitelnost a praktická použitelnost vytvořeného souboru.

### K8 Náklady a licenční omezení

Kritérium zahrnuje pořizovací cenu testované varianty a omezení, která ovlivňují splnění společných úloh. Bezplatnost není posuzována izolovaně; pokud bezplatná edice neobsahuje důležitou funkci, je omezení popsáno a zohledněno. Ceny a licenční podmínky jsou vztaženy ke konkrétnímu datu.

Datum zjištění cen, měna, typy licencí a přesné podmínky použité pro K8: **⟦NEOVĚŘENO⟧**.

## Převod pozorování do párových porovnání

Párové hodnoty nejsou určovány pouze intuitivně. Pro každé porovnání je uchován stručný důvod odkazující na testovací protokol, checklist nebo licenční údaj. Hodnota 1 vyjadřuje srovnatelný výsledek, hodnoty 3, 5, 7 a 9 postupně mírnou, silnou, velmi silnou a extrémní převahu jedné alternativy; sudé hodnoty slouží jako mezistupně. Opačný směr je vyjádřen převrácenou hodnotou.

Konkrétní rozhodovací pravidla pro převod rozdílu času, počtu splněných funkcí, počtu oprav a licenčních nákladů na Saatyho škálu: **⟦NEVYHODNOCENO⟧**. Pravidla nesmějí být stanovena zpětně podle požadovaného vítěze.

U každé matice je kontrolován poměr konzistence. Pokud CR dosáhne nebo překročí hodnotu 0,1, jsou znovu posouzeny původní argumenty a vstupní data. Úprava hodnot nesmí sloužit pouze k matematickému snížení CR nebo ke změně pořadí alternativ.

# Praktická komparace

<!-- BP-DOPLNIT: Před odevzdáním nahradit všechny výrazy ⟦NEZAZNAMENÁNO⟧ skutečným průběhem testování a připojit uvedené doklady. -->

Praktická komparace ověřuje čtyři vybrané nástroje na stejném zadání, za srovnatelných podmínek a podle předem stanoveného protokolu. Cílem není pouze sestavit výsledné pořadí, ale také vytvořit dohledatelný podklad pro párová porovnání v AHP. Proto jsou vedle výsledku jednotlivých úloh zaznamenávány časy, nutné ruční zásahy, chybové stavy, nedostupné funkce a výstupní soubory.

## Modelová situace

Modelová situace představuje malý cykloservis, který eviduje zákazníky a jejich kola, přijímá servisní zakázky, přiřazuje mechaniky, zaznamenává provedené služby a spotřebované díly a vystavuje faktury. Systém uchovává historii oprav konkrétního kola a cenu služby nebo dílu platnou v okamžiku zakázky.

Zadání bylo zvoleno proto, že je srozumitelné bez znalosti specializované podnikové domény a současně obsahuje konstrukce potřebné pro ověření databázového modelovacího nástroje. Jádro modelu tvoří deset entit:

- Zákazník;
- Kolo;
- Zaměstnanec;
- Zakázka;
- Služba;
- Díl;
- Dodavatel;
- Zakázka_Služba;
- Zakázka_Díl;
- Faktura.

Model zahrnuje vazby 1:N, dvě vazby M:N řešené asociačními entitami, vazbu 1:1, složené primární klíče, nepovinný cizí klíč, unikátní omezení a kontrolní omezení povolených hodnot. Rozsah byl omezen na deset entit, aby bylo možné strukturu vytvořit v každém nástroji a současně zachovat dostatečnou rozmanitost modelovacích konstrukcí.

## Referenční model a databázové platformy

Pro ověření forward engineeringu byly použity databázové platformy odpovídající hlavnímu zaměření nástrojů. Oracle SQL Developer Data Modeler pracoval s Oracle Database, MySQL Workbench s MySQL a pgModeler s PostgreSQL. DBeaver Community Edition byl podle testovacího protokolu primárně ověřen s platformou PostgreSQL, protože umožňuje nezávisle zkontrolovat referenční schéma i výstup vygenerovaný pgModelerem; připojení k dalším DBMS (MySQL, Oracle Database) bylo posouzeno v rámci K3, pokud na něj zbyl čas.

Pro reverse engineering byla předem vytvořena referenční schémata se stejným významem a strukturou, ale s datovými typy a syntaxí přizpůsobenými Oracle Database, MySQL a PostgreSQL. Referenční skripty nebyly použity při ručním modelování ani při generování DDL, aby neovlivnily výsledek těchto úloh.

Referenční ER model: **⟦NEZAZNAMENÁNO – VLOŽIT OBRÁZEK, ČÍSLO, POPISEK A ODKAZ NA PŘÍLOHU⟧**.

## Testovací prostředí

Testování probíhalo na jednom pracovním počítači, čímž se omezil vliv rozdílného výkonu a konfigurace. Databázové servery byly provozovány v kontejnerech Docker. Každý nástroj byl spuštěn v testované edici uvedené v kapitole 7.

| Položka | Použitá konfigurace |
|:---|:---|
| Počítač | **⟦NEZAZNAMENÁNO – procesor a RAM⟧** |
| Operační systém | **⟦NEZAZNAMENÁNO⟧** |
| Rozlišení obrazovky | **⟦NEZAZNAMENÁNO⟧** |
| Docker | **⟦NEZAZNAMENÁNO – přesná verze⟧** |
| Oracle Database | image `gvenzl/oracle-free:23-slim`; přesná verze instance **⟦NEZAZNAMENÁNO⟧** |
| MySQL | image `mysql:8.0`; přesná verze instance **⟦NEZAZNAMENÁNO⟧** |
| PostgreSQL | image `postgres:16`; přesná verze instance **⟦NEZAZNAMENÁNO⟧** |
| Období testování | **⟦NEZAZNAMENÁNO – datum od–do⟧** |

## Jednotný testovací protokol

Jednotný byl cílový rozsah modelu a požadované výstupy. Konkrétní pracovní cesta se mohla lišit podle možností testované edice. Tento rozdíl nebyl zakryt, protože schopnost vytvořit samostatný model bez živé databáze je sama o sobě relevantním výsledkem pro K1, K2 a K4.

### Vytvoření struktury podle zadání

Hodnotitel obdržel textové zadání a seznam požadovaných entit, atributů a vazeb. V nástrojích, které podporují samostatný návrhový model, vytvořil nový projekt a celý model bez použití připraveného SQL skriptu. Pokud testovaná edice umožňovala diagram pouze nad existujícími databázovými objekty, byla struktura vytvořena nejbližším dostupným grafickým nebo metadatovým postupem na prázdném schématu a následně zobrazena v diagramu. Takový postup nebyl označen za plnohodnotné modelování od prázdného diagramu.

Měřený čas začínal **⟦NEZAZNAMENÁNO – přesný okamžik⟧** a končil **⟦NEZAZNAMENÁNO – přesný okamžik⟧**. Během práce byly zaznamenány kroky vyžadující dohledání dokumentace, chyby, opakované operace a omezení modelovacího rozhraní.

### Forward engineering

Z modelu vytvořeného v předchozím kroku byl vygenerován DDL skript pro příslušnou databázi. Skript byl spuštěn na prázdném schématu. Zaznamenalo se, zda proběhl bez chyby, které objekty vznikly, jaké ruční opravy byly nutné a zda výsledné schéma odpovídalo modelu. U nástroje s databázově orientovaným postupem byl vyexportován DDL výsledného schématu a ověřeno, zda umožní znovu vytvořit stejnou strukturu na prázdném schématu; rozdíl oproti modelově orientovanému forward engineeringu byl uveden ve výsledcích.

### Reverse engineering

Na cílový server bylo nejprve nahráno referenční schéma. Nástroj se připojil k databázi a pomocí dostupné funkce vytvořil model nebo diagram. Výsledek byl porovnán s referenčním modelem podle počtu a vlastností tabulek, atributů, primárních a cizích klíčů, vztahů a omezení. Pokud testovaná verze nebo edice tuto funkci neobsahovala, byla nedostupnost zaznamenána a nebyla nahrazena funkcí jiné edice bez uvedení změny.

### Export výsledků

Poslední úloha ověřila export diagramu do dostupných obrazových nebo dokumentových formátů a export databázového schématu do SQL. U výstupů byla posouzena jejich existence, úplnost, čitelnost a případná potřeba dodatečných úprav rozložení. Pokud požadovaný formát nebyl podporován přímo, bylo to zaznamenáno jako výsledek; tisk do PDF nebyl vydáván za nativní export bez příslušné poznámky.

## Záznam výsledků

Pro každý nástroj byl veden samostatný protokol. Jeho strukturu shrnuje tabulka 3.

| Úloha | Začátek | Konec | Čas | Výsledek | Ruční zásahy | Chyby a poznámky | Doklad |
|:---|:---:|:---:|---:|:---|:---|:---|:---|
| Vytvoření struktury | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ |
| Forward engineering | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ |
| Reverse engineering | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ |
| Export | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ |

Tabulka 3: Struktura protokolu praktického testování (vlastní zpracování)

## Zajištění srovnatelnosti

Srovnatelnost je založena na stejném rozsahu modelu, shodných očekávaných výstupech, jednom hodnotiteli, jednotném způsobu měření a uchování důkazů. Rozdíly vyplývající ze zaměření nástroje nejsou odstraňovány, protože právě ony jsou předmětem hodnocení. Současně je odlišeno, zda horší výsledek vznikl omezením produktu, konkrétní edice, chybou hodnotitele nebo nekompatibilitou zvoleného postupu.

Pořadí testování může ovlivnit rychlost práce, protože hodnotitel postupně získává zkušenost s modelovým zadáním. Tento vliv byl omezen **⟦NEZAZNAMENÁNO – popsat skutečné opatření, například zkušební úlohu, opakování nebo střídání pořadí⟧**.

# Výsledky praktického testování

<!-- BP-DOPLNIT: Kapitola obsahuje pouze strukturu výsledků. Všechny výrazy ⟦NEVYHODNOCENO⟧ musí být před odevzdáním nahrazeny skutečnými údaji a doklady. -->

Kapitola uvádí výsledky jednotného praktického testu popsaného v kapitole 9. Nejprve jsou zaznamenány výsledky jednotlivých nástrojů a následně jejich souhrnné porovnání podle kritérií K1–K8. Popis odděluje pozorovaný výsledek od jeho pozdější interpretace v AHP.

## Oracle SQL Developer Data Modeler

Testována byla verze **⟦NEVYHODNOCENO⟧**. Vytvoření modelu nebo cílové struktury trvalo **⟦NEVYHODNOCENO⟧** a výsledný model obsahoval **⟦NEVYHODNOCENO⟧**. Při modelování byly zaznamenány tyto významné skutečnosti: **⟦NEVYHODNOCENO – stručný věcný popis doložený protokolem⟧**.

| Oblast | Výsledek | Doklad |
|:---|:---|:---|
| Vytvoření struktury | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Forward engineering | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Reverse engineering | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Export PDF/PNG/SQL | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Hlavní omezení | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |

Výsledný model: **⟦NEVYHODNOCENO – vložit obrázek, popisek a odkaz na protokol⟧**.

## DBeaver Community Edition

Testována byla verze **⟦NEVYHODNOCENO⟧** s databázovou platformou **⟦NEVYHODNOCENO⟧**. Struktura byla vytvořena nebo zobrazena postupem **⟦NEVYHODNOCENO – přesně odlišit samostatné modelování, úpravu živého schématu a diagram vytvořený z databáze⟧**. Funkce komerčních edic nebyly vykázány jako prakticky ověřené v Community Edition.

| Oblast | Výsledek | Doklad |
|:---|:---|:---|
| Vytvoření struktury | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Forward engineering | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Reverse engineering | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Export PDF/PNG/SQL | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Hlavní omezení | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |

Výsledný diagram: **⟦NEVYHODNOCENO – vložit obrázek, popisek a odkaz na protokol⟧**.

## MySQL Workbench Community Edition

Testována byla verze **⟦NEVYHODNOCENO⟧**. Model byl vytvořen pro databázi MySQL **⟦NEVYHODNOCENO – přesná verze⟧**. Celkový čas a hlavní pozorování byly **⟦NEVYHODNOCENO⟧**.

| Oblast | Výsledek | Doklad |
|:---|:---|:---|
| Vytvoření struktury | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Forward engineering | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Reverse engineering | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Export PDF/PNG/SQL | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Hlavní omezení | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |

Výsledný EER diagram a údaj o případných úpravách DDL: **⟦NEVYHODNOCENO⟧**.

## pgModeler

Testována byla verze a edice **⟦NEVYHODNOCENO⟧** pro PostgreSQL **⟦NEVYHODNOCENO – přesná verze⟧**. Výsledky jsou vztaženy pouze k této verzi a edici. Funkce dostupné výhradně v jiné variantě nejsou vykazovány jako prakticky ověřené.

| Oblast | Výsledek | Doklad |
|:---|:---|:---|
| Vytvoření struktury | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Forward engineering | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Reverse engineering | ⟦NEVYHODNOCENO – dostupnost v použité verzi a edici⟧ | ⟦NEVYHODNOCENO⟧ |
| Export PDF/PNG/SQL | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Hlavní omezení | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |

Výsledný model: **⟦NEVYHODNOCENO – vložit obrázek, popisek a odkaz na protokol⟧**.

## Souhrnné porovnání úloh

Tabulka 4 soustřeďuje pozorované výsledky bez AHP vah. Každá hodnota musí být dohledatelná v podrobných protokolech.

| Ukazatel | Oracle Data Modeler | DBeaver CE | MySQL Workbench CE | pgModeler |
|:---|:---:|:---:|:---:|:---:|
| Typ pracovního postupu | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Čas vytvoření struktury | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Splněné položky K1 | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Počet ručních oprav DDL | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Úplnost reverse engineeringu | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Export PDF | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Export PNG | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |
| Cena testované varianty | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ | ⟦NEVYHODNOCENO⟧ |

Tabulka 4: Souhrn výsledků praktického testování (vlastní zpracování)

## Podklady pro K1–K8

Pro následné párové porovnání byl ke každému kritériu vytvořen souhrnný podklad:

| Kritérium | Hlavní pozorované rozdíly | Zdroj údajů |
|:--:|:---|:---|
| K1 | ⟦NEVYHODNOCENO⟧ | checklist funkcí |
| K2 | ⟦NEVYHODNOCENO⟧ | časy, chyby a poznámky |
| K3 | ⟦NEVYHODNOCENO⟧ | dokumentace a ověřená připojení |
| K4 | ⟦NEVYHODNOCENO⟧ | DDL a protokol spuštění |
| K5 | ⟦NEVYHODNOCENO⟧ | modely nebo diagramy z reverse engineeringu |
| K6 | ⟦NEVYHODNOCENO⟧ | záznam práce s dokumentací |
| K7 | ⟦NEVYHODNOCENO⟧ | exportované soubory |
| K8 | ⟦NEVYHODNOCENO⟧ | licence a ceny ke konkrétnímu datu |

Tabulka 5: Podklady pro párové porovnání alternativ (vlastní zpracování)

Praktické testování ukázalo nejvýznamnější rozdíly v oblastech **⟦NEVYHODNOCENO⟧**. Tyto výsledky tvoří podklad pro párové porovnání v následující kapitole; samotné výsledné pořadí zde ještě není interpretováno.

# Vyhodnocení nástrojů metodou AHP

<!-- BP-DOPLNIT: Značka ⟦NV⟧ znamená „nevypočteno“. Nejde o výsledek ani o číselnou hodnotu a před odevzdáním musí být všude nahrazena skutečným výpočtem. -->

Výsledky praktického testování byly zpracovány metodou AHP. Rozhodovací hierarchii tvoří cíl výběru nejvhodnějšího nástroje, osm kritérií K1–K8 a čtyři alternativy. Pro každé párové porovnání byl uchován slovní důvod a odkaz na podklad z kapitoly 10. Číselné hodnoty v této kapitole musí odpovídat konečné verzi výpočtového souboru **⟦NV – název a verze souboru nebo aplikace⟧**, který bude připojen jako příloha.

## Struktura rozhodovací hierarchie

```text
Cíl: Výběr nejvhodnějšího nástroje
├── K1 Funkcionalita
├── K2 Použitelnost
├── K3 Kompatibilita s DBMS
├── K4 Forward engineering
├── K5 Reverse engineering
├── K6 Dokumentace a komunitní podpora
├── K7 Import a export modelu
└── K8 Náklady a licenční omezení
    ├── Oracle SQL Developer Data Modeler
    ├── DBeaver Community Edition
    ├── MySQL Workbench Community Edition
    └── pgModeler
```

Pro každý řádek párové matice byl vypočten geometrický průměr. Jeho normalizací vznikla lokální váha prvku. Konzistence byla ověřena výpočtem maximálního vlastního čísla λmax, indexu konzistence CI a poměru konzistence CR. Pro matici osmi kritérií je použit náhodný index RI = 1,41, pro matice čtyř alternativ RI = 0,90. Za přijatelnou je považována hodnota CR < 0,1.

## Scénář A – malá organizace

Scénář A představuje malou organizaci s omezeným rozpočtem a menším specializovaným týmem. Vyšší význam proto mají K2 Použitelnost a K8 Náklady a licenční omezení. Ostatní kritéria zůstávají součástí rozhodnutí, ale jejich relativní váha odpovídá potřebám scénáře.

### Matice kritérií

|  | K1 | K2 | K3 | K4 | K5 | K6 | K7 | K8 | Váha |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| K1 | 1 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| K2 | ⟦NV⟧ | 1 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| K3 | ⟦NV⟧ | ⟦NV⟧ | 1 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| K4 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | 1 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| K5 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | 1 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| K6 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | 1 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| K7 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | 1 | ⟦NV⟧ | ⟦NV⟧ |
| K8 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | 1 | ⟦NV⟧ |

Výsledek kontroly konzistence: λmax = **⟦NV⟧**, CI = **⟦NV⟧**, RI = 1,41 a CR = **⟦NV⟧**. Nejdůležitější párové úsudky byly zdůvodněny takto: **⟦NV⟧**.

## Scénář B – středně velká organizace

Scénář B představuje organizaci s více databázovými platformami a vyššími požadavky na funkční rozsah a integraci. Vyšší význam proto mají K1 Funkcionalita a K3 Kompatibilita s DBMS.

### Matice kritérií

|  | K1 | K2 | K3 | K4 | K5 | K6 | K7 | K8 | Váha |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| K1 | 1 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| K2 | ⟦NV⟧ | 1 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| K3 | ⟦NV⟧ | ⟦NV⟧ | 1 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| K4 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | 1 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| K5 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | 1 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| K6 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | 1 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| K7 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | 1 | ⟦NV⟧ | ⟦NV⟧ |
| K8 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | 1 | ⟦NV⟧ |

Výsledek kontroly konzistence: λmax = **⟦NV⟧**, CI = **⟦NV⟧**, RI = 1,41 a CR = **⟦NV⟧**. Rozdíl oproti scénáři A spočívá v **⟦NV⟧**.

## Párové porovnání alternativ

Pro každé kritérium byla sestavena matice čtyř nástrojů. Protože pozorované vlastnosti nástrojů zůstávají stejné, používají oba scénáře stejné lokální váhy alternativ. Mění se pouze význam kritérií. Úplné matice K1–K8 budou uvedeny v příloze; v hlavním textu bude jedna reprezentativní matice doplněna výpočtem a slovním zdůvodněním hodnot.

| Kritérium | Oracle Data Modeler | DBeaver CE | MySQL Workbench CE | pgModeler | CR |
|:--:|:--:|:--:|:--:|:--:|:--:|
| K1 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| K2 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| K3 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| K4 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| K5 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| K6 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| K7 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| K8 | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |

Tabulka 6: Lokální váhy alternativ a konzistence matic (vlastní zpracování)

## Syntéza výsledků

Globální skóre každého nástroje bylo vypočteno jako součet součinů váhy kritéria a lokální váhy nástroje vzhledem k danému kritériu. Součet globálních skóre v každém scénáři musí být po zohlednění zaokrouhlení roven jedné.

| Nástroj | Scénář A – skóre | Scénář A – pořadí | Scénář B – skóre | Scénář B – pořadí |
|:---|---:|:--:|---:|:--:|
| Oracle SQL Developer Data Modeler | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| DBeaver Community Edition | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| MySQL Workbench Community Edition | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |
| pgModeler | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |

Tabulka 7: Výsledné skóre a pořadí nástrojů (vlastní zpracování)

Graf výsledků obou scénářů a popis hlavních rozdílů: **⟦NV⟧**.

## Kontrola konzistence

| Matice | Scénář | CR | Stav |
|:---|:---:|---:|:---|
| Kritéria | A | ⟦NV⟧ | ⟦NV – CR < 0,1?⟧ |
| Kritéria | B | ⟦NV⟧ | ⟦NV – CR < 0,1?⟧ |
| Alternativy K1–K8 | společné | ⟦NV – jednotlivé hodnoty nebo rozsah⟧ | ⟦NV⟧ |

Pokud některá matice podmínku CR < 0,1 nesplnila v první verzi, bude uvedeno, která hodnocení byla znovu posouzena a z jakého věcného důvodu.

## Analýza citlivosti

Analýza citlivosti mění váhu **⟦NV – K1, K8 nebo jiné kritérium⟧** v rozsahu **⟦NV⟧** s krokem **⟦NV⟧**. Ostatní váhy jsou poměrně přepočteny tak, aby jejich součet zůstal roven jedné.

| Změněné kritérium | Rozsah váhy | Bod změny vítěze | Nový vítěz | Interpretace |
|:---|:---:|:---:|:---|:---|
| ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ | ⟦NV⟧ |

Graf citlivosti a přesný rozsah stability pořadí: **⟦NV⟧**. Pokud se vítěz v testovaném rozsahu nezměnil, bude uveden nejmenší rozdíl skóre a celý testovaný rozsah, nikoli pouze obecné tvrzení o stabilitě.

# Diskuse výsledků a doporučení

<!-- BP-DOPLNIT: Všechny výrazy ⟦NEVYHODNOCENO⟧ musí být nahrazeny interpretací skutečných výsledků z kapitol 10 a 11. -->

Diskuse interpretuje výsledky praktického testování a AHP ve vztahu k výzkumným otázkám, modelovým scénářům, použité metodě a dřívějším studiím. Neopakuje pouze pořadí nástrojů, ale vysvětluje, proč se pořadí vytvořilo a za jakých podmínek by se mohlo změnit.

## Rozdíly mezi nástroji

Praktické testování ukázalo rozdíly zejména v oblastech **⟦NEVYHODNOCENO – uvést podle K1–K8⟧**. Nástroj **⟦NEVYHODNOCENO⟧** dosáhl silného výsledku v **⟦NEVYHODNOCENO⟧**, zatímco jeho hlavní omezení spočívalo v **⟦NEVYHODNOCENO⟧**. U nástroje **⟦NEVYHODNOCENO⟧** se projevila výhoda specializace nebo univerzálnosti tím, že **⟦NEVYHODNOCENO⟧**.

Zvláštní pozornost vyžaduje rozdíl mezi nástroji orientovanými na samostatný návrhový model a nástroji, které diagram vytvářejí především nad existujícím databázovým schématem. Tento rozdíl se projevil v **⟦NEVYHODNOCENO⟧** a ovlivnil zejména kritéria **⟦NEVYHODNOCENO⟧**. Interpretace vychází pouze z vlastností skutečně ověřených v testované verzi a edici.

## Porovnání modelových scénářů

Ve scénáři malé organizace byla vyšší váha přidělena použitelnosti a nákladům. Výsledné pořadí bylo **⟦NEVYHODNOCENO⟧**. Ve scénáři středně velké organizace získaly vyšší význam funkcionalita a kompatibilita a pořadí bylo **⟦NEVYHODNOCENO⟧**. Rozdíl mezi scénáři ukazuje **⟦NEVYHODNOCENO – vysvětlit konkrétní změnu nebo stabilitu pořadí⟧**.

Pokud se vítěz mezi scénáři nezměnil, neznamená to automaticky, že váhy nemají význam. Rozdíl skóre se změnil o **⟦NEVYHODNOCENO⟧** a výsledek analýzy citlivosti ukázal **⟦NEVYHODNOCENO⟧**. Pokud se vítěz změnil, rozhodující vliv měla kritéria **⟦NEVYHODNOCENO⟧**, jejichž váhy byly stanoveny z důvodu **⟦NEVYHODNOCENO⟧**.

## Vztah ke studii Carvalho et al.

Studie Carvalho et al. (2022) porovnávala širší soubor nástrojů a používala odlišný hodnoticí rámec. Shoda nebo rozdíl oproti jejím výsledkům proto nemůže být interpretován bez zohlednění verzí nástrojů, vybraných kritérií, modelového zadání a použití AHP.

Vlastní hodnocení Oracle SQL Developer Data Modeleru, MySQL Workbench a pgModeleru se se studií Carvalho et al. (2022) shoduje v **⟦NEVYHODNOCENO⟧** a liší v **⟦NEVYHODNOCENO⟧**. DBeaver nebyl ve studii zahrnut, a proto u něj přímé srovnání provedeno není. Zjištěné rozdíly lze vysvětlit zejména **⟦NEVYHODNOCENO – verze, edice, kritéria nebo rozsah testu⟧**.

## Stabilita výsledků

Analýza citlivosti prokázala, že pořadí **⟦NEVYHODNOCENO – zůstalo stabilní nebo se změnilo⟧** při **⟦NEVYHODNOCENO – přesná změna vah⟧**. Kritériem s největším vlivem bylo **⟦NEVYHODNOCENO⟧**. Praktický význam tohoto zjištění spočívá v **⟦NEVYHODNOCENO⟧**. Výsledek lze označit za stabilní pouze v rozsahu **⟦NEVYHODNOCENO⟧**.

## Omezení práce

Výsledky ovlivňují zejména tato omezení:

- hodnocení prováděl jeden hodnotitel;
- časové měření ovlivňuje jeho předchozí zkušenost a pořadí testů;
- porovnání se vztahuje ke konkrétním verzím a edicím;
- model cykloservisu nepokrývá všechny konstrukce rozsáhlých podnikových databází;
- některá kritéria obsahují kvalitativní úsudek;
- nástroje nepoužívají vždy stejný pracovní postup, takže samotný čas nelze interpretovat bez kontextu;
- licenční podmínky, ceny a funkce se mohou v čase změnit;
- užší zaměření specializovaného nástroje může být výhodou v jednom scénáři a nevýhodou v jiném;
- částečně se mohou překrývat K1, K5 a K8, pokud je funkce dostupná pouze v některé edici.

Tato omezení nesnižují použitelnost výsledků pro definované scénáře, ale vymezují podmínky, za nichž lze doporučení zobecnit.

## Doporučení pro praxi

Pro modelovou malou organizaci lze doporučit **⟦NEVYHODNOCENO – nástroj⟧**, pokud její priority odpovídají vahám scénáře A a pokud **⟦NEVYHODNOCENO – podmínky doporučení⟧**. Pro středně velkou organizaci lze doporučit **⟦NEVYHODNOCENO – nástroj⟧** za předpokladu **⟦NEVYHODNOCENO⟧**.

Doporučení není formulováno jako obecně platný vítěz pro všechny uživatele. Organizace by měla před výběrem upravit váhy kritérií podle vlastních požadavků, ověřit aktuální licenční podmínky a pilotně vyzkoušet nejvýše hodnocené varianty na vlastním schématu.

## Odpovědi na výzkumné otázky

- **VO1:** Vybrané nástroje se podle K1–K8 lišily zejména v **⟦NEVYHODNOCENO – souhrnná odpověď založená na testu⟧**.
- **VO2:** Pro modelovou malou organizaci dosáhl nejvyššího skóre **⟦NEVYHODNOCENO⟧**, zatímco pro středně velkou organizaci **⟦NEVYHODNOCENO⟧**; doporučení platí za podmínek **⟦NEVYHODNOCENO⟧**.
- **VO3:** Pořadí bylo při změně vah **⟦NEVYHODNOCENO – přesný výsledek analýzy citlivosti⟧**.

# Závěr

<!-- BP-DOPLNIT: Závěr je připraven jako souvislý text, ale všechny výrazy ⟦NEVYHODNOCENO⟧ musí být nahrazeny skutečnými výsledky. -->

Bakalářská práce se zabývala porovnáním čtyř nástrojů pro návrh a vývoj databázových systémů: Oracle SQL Developer Data Modeler, DBeaver Community Edition, MySQL Workbench Community Edition a pgModeler. Hlavním cílem bylo nástroje prakticky porovnat pomocí metody AHP a formulovat doporučení pro jejich využití ve dvou modelových situacích.

Teoretická část vymezila databázové systémy, datové modelování, návrh relační databáze, vícekriteriální rozhodování a metodu AHP. Na základě odborných zdrojů byly zvoleny porovnávané nástroje a osm hodnoticích kritérií. Praktická část použila společný model databáze cykloservisu a jednotný protokol zahrnující vytvoření struktury podle zadání, forward engineering, reverse engineering a export výstupů. Získaná pozorování byla převedena do párových porovnání a vyhodnocena ve dvou scénářích s odlišnými vahami kritérií.

Hlavní cíl práce byl naplněn vytvořením **⟦NEVYHODNOCENO – uvést konkrétní výstupy, nikoli pouze tvrzení o splnění cíle⟧**. Ve scénáři malé organizace dosáhl nejvyššího globálního skóre nástroj **⟦NEVYHODNOCENO⟧** s hodnotou **⟦NEVYHODNOCENO⟧**. Ve scénáři středně velké organizace se na prvním místě umístil nástroj **⟦NEVYHODNOCENO⟧** se skóre **⟦NEVYHODNOCENO⟧**. Nejvýznamnější rozdíly mezi nástroji se projevily v **⟦NEVYHODNOCENO⟧**. Hodnoty CR se pohybovaly **⟦NEVYHODNOCENO⟧**, takže **⟦NEVYHODNOCENO – uvést závěr o konzistenci⟧**.

Analýza citlivosti ukázala, že výsledné pořadí **⟦NEVYHODNOCENO – zůstalo stabilní nebo se změnilo⟧** při změně vah **⟦NEVYHODNOCENO⟧**. Ke změně vítěze došlo při **⟦NEVYHODNOCENO⟧**, případně se vítěz v testovaném rozsahu nezměnil a nejmenší rozdíl skóre činil **⟦NEVYHODNOCENO⟧**. Výsledek proto lze považovat za stabilní pouze za podmínek **⟦NEVYHODNOCENO⟧**.

Pro malou organizaci lze doporučit **⟦NEVYHODNOCENO⟧**, pokud **⟦NEVYHODNOCENO – podmínky doporučení⟧**. Pro středně velkou organizaci je vhodnější **⟦NEVYHODNOCENO⟧** za předpokladu **⟦NEVYHODNOCENO⟧**. Výsledky současně potvrzují, že žádný nástroj nelze označit za univerzálně nejlepší bez znalosti konkrétních požadavků, podporovaných databázových platforem, rozpočtu a požadovaného pracovního postupu.

Výsledky jsou omezeny rozsahem modelového příkladu, konkrétními verzemi a edicemi nástrojů a hodnocením jednoho autora. Další práce by mohla ověřit postup na rozsáhlejším schématu, zahrnout více hodnotitelů nebo porovnat další komerční a webové nástroje. Pokud vznikla podpůrná aplikace, její přínos spočívá v **⟦NEVYHODNOCENO⟧**; pokud realizována nebyla, bude tato věta z konečné verze odstraněna.

# Seznam zdrojů

<!-- BP-DOPLNIT: Aktuálně je převzato 27 ověřených položek ze seminární práce (abecední řazení zkontrolováno a je správné). Z toho jsou jednoznačně knihy nebo odborné články jen CARVALHO, CATAK, CHEN, CHLAPEK, CODD, EBRAHIMI, ELMASRI, HO, ISHIZAKA, MARDANI, MORENO-JIMÉNEZ, POKORNÝ, ROSENTHAL, SAATY (1990), SAATY (2008), SIMANAVIČIENĖ, VAIDYA, VELASQUEZ = 18 položek; DBEAVER, DB-ENGINES, MYSQL, ORACLE, PGMODELER a POSTGRESQL jsou dokumentace/weby nástrojů a do kvóty knih a článků se nepočítají; LARANJEIRO (arXiv preprint), SOUKOPOVÁ (učební text) a WATT (otevřená učebnice bez ISBN) jsou hraniční případy, které vedoucí nemusí uznat jako knihu nebo odborný článek. Požadavek vedoucího je nejméně 30 zdrojů celkem a alespoň 20 knih a odborných článků — i při nejpříznivějším zařazení hraničních položek (21) práci chybí minimálně 3 zdroje do celkového počtu a je těsně na hraně u kvóty knih/článků, proto by nové doplněné položky (viz `ZDROJE.md`, sekce 5) měly být přednostně knihy nebo recenzované články, ne další dokumentace nástrojů. Všechny nové položky musí být skutečně použity v textu. U CATAK a EBRAHIMI chybí ISSN časopisu (ostatní články ISSN uvádějí) — před odevzdáním dohledat a doplnit, nebo sjednotit formát bez ISSN, pokud jej časopis nemá přiděleno. -->

CARVALHO, Gonçalo, Sergii MYKOLYSHYN, Bruno CABRAL, Jorge BERNARDINO a Vasco PEREIRA. Comparative Analysis of Data Modeling Design Tools. *IEEE Access*. 2022, 10, 3351-3365. ISSN 2169-3536. DOI: 10.1109/ACCESS.2021.3139071.

CATAK, F. Ozgur, Servet KARABAS a Serkan YILDIRIM. Fuzzy Analytic Hierarchy Based DBMS Selection in Turkish National Identity Card Management Project. *International Journal of Information Sciences and Techniques*. 2012, 2(4), 29–38. DOI: 10.5121/ijist.2012.2403.

CHEN, Peter Pin-Shan. The entity-relationship model—toward a unified view of data. *ACM Transactions on Database Systems*. 1976, 1(1), 9–36. ISSN 0362-5915. DOI: 10.1145/320434.320440.

CHLAPEK, Dušan, Jan KUČERA a Helena PALOVSKÁ. *Datové modelování a návrh relační databáze: Sbírka řešených úloh*. Praha: Vysoká škola ekonomická v Praze, Nakladatelství Oeconomica, 2019. ISBN 978-80-245-2331-6.

CODD, Edgar F. A relational model of data for large shared data banks. *Communications of the ACM*. 1970, 13(6), 377–387. ISSN 0001-0782. DOI: 10.1145/362384.362685.

DBEAVER. *DBeaver Documentation* \[online\]. DBeaver Corp., 2026 \[cit. 2026-06-09\]. Dostupné z: https://dbeaver.com/docs/dbeaver/

DB-ENGINES. *DB-Engines Ranking* \[online\]. solid IT gmbh, 2026 \[cit. 2026-06-14\]. Dostupné z: https://db-engines.com/en/ranking

EBRAHIMI, Seyed Babak a Maryam TAHERI. Selection of Database Management System with Fuzzy-AHP for Electronic Medical Record. *Information Engineering and Electronic Business*. 2015, 7(5), 1–9. DOI: 10.5815/ijieeb.2015.05.01.

ELMASRI, Ramez a Shamkant B. NAVATHE. *Fundamentals of Database Systems*. 7th ed. Boston: Pearson, 2016. ISBN 978-0-13-397077-7.

HO, William. Integrated analytic hierarchy process and its applications – a literature review. *European Journal of Operational Research*. 2008, 186(1), 211–228. ISSN 0377-2217. DOI: 10.1016/j.ejor.2007.01.004.

ISHIZAKA, Alessio a Ashraf LABIB. Review of the main developments in the Analytic Hierarchy Process. *Expert Systems with Applications*. 2011, 38(11), 14336–14345. ISSN 0957-4174. DOI: 10.1016/j.eswa.2011.04.143.

LARANJEIRO, Nuno a Alexandre Miguel PINTO. *ONDA: ONLine Database Architect* \[online\]. arXiv:2401.16552, 2024 \[cit. 2026-06-15\]. DOI: 10.48550/arXiv.2401.16552. Dostupné z: https://doi.org/10.48550/arXiv.2401.16552

MARDANI, Abbas, Ahmad JUSOH, Khalil MD NOR, Zainab KHALIFAH, Norhayati ZAKWAN a Alireza VALIPOUR. Multiple criteria decision-making techniques and their applications – a review of the literature from 2000 to 2014. *Economic Research – Ekonomska Istraživanja*. 2015, 28(1), 516–571. ISSN 1331-677X. DOI: 10.1080/1331677X.2015.1075139.

MORENO-JIMÉNEZ, José María a Luis G. VARGAS. Cognitive multiple criteria decision making and the legacy of the analytic hierarchy process. *Studies of Applied Economics*. 2018, 36(1), 67–80. ISSN 1133-3197. DOI: 10.25115/eea.v36i1.2516.

MYSQL. *MySQL Workbench Manual* \[online\]. Oracle Corporation, 2026 \[cit. 2026-06-09\]. Dostupné z: https://dev.mysql.com/doc/workbench/en/

ORACLE. *Oracle SQL Developer Data Modeler* \[online\]. Oracle Corporation, 2026 \[cit. 2026-06-09\]. Dostupné z: https://www.oracle.com/database/sqldeveloper/technologies/sql-data-modeler/

PGMODELER. *pgModeler – PostgreSQL Database Modeler* \[online\]. Raphael Araújo e Silva, 2026 \[cit. 2026-06-09\]. Dostupné z: https://pgmodeler.io/

POKORNÝ, Jaroslav a Michal VALENTA. *Databázové systémy*. Praha: České vysoké učení technické v Praze, 2020. ISBN 978-80-01-06708-6.

POSTGRESQL. *PostgreSQL Documentation* \[online\]. The PostgreSQL Global Development Group, 2026 \[cit. 2026-06-09\]. Dostupné z: https://www.postgresql.org/docs/

ROSENTHAL, Arnon a David REINER. Tools and Transformations — Rigorous and Otherwise — for Practical Database Design. *ACM Transactions on Database Systems*. 1994, 19(2), 167–211. ISSN 0362-5915. DOI: 10.1145/176567.176568.

SAATY, Thomas L. How to make a decision: The Analytic Hierarchy Process. *European Journal of Operational Research*. 1990, 48(1), 9–26. ISSN 0377-2217.

SAATY, Thomas L. Decision making with the analytic hierarchy process. *International Journal of Services Sciences*. 2008, 1(1), 83–98. ISSN 1753-1454.

SIMANAVIČIENĖ, Rūta a Sonata VDOVINSKIENĖ. Selection of Computer-Aided Design Software Systems Using the AHP Method. *Baltic Journal of Modern Computing*. 2023, 11(2), 272–284. ISSN 2255-8950. DOI: 10.22364/bjmc.2023.11.2.04.

SOUKOPOVÁ, Jana. *Vícekriteriální metody hodnocení* \[online\]. Brno: Masarykova univerzita, Ekonomicko-správní fakulta, 2016. Učební text \[cit. 2026-06-09\]. Dostupné z: https://is.muni.cz/el/1456/jaro2016/BPE_VIMP/um/

VAIDYA, Omkarprasad S. a Sushil KUMAR. Analytic hierarchy process: An overview of applications. *European Journal of Operational Research*. 2006, 169(1), 1–29. ISSN 0377-2217. DOI: 10.1016/j.ejor.2004.04.028.

VELASQUEZ, Mark a Patrick T. HESTER. An Analysis of Multi-Criteria Decision Making Methods. *International Journal of Operations Research*. 2013, 10(2), 56–66. ISSN 1813-713X.

WATT, Adrienne a Nelson ENG. *Database Design* \[online\]. 2nd ed. Victoria: BCcampus, 2014 \[cit. 2026-06-18\]. Dostupné z: https://opentextbc.ca/dbdesign01/

> **Před dokončením:** Spárovat všechny citace v textu se seznamem, odstranit nepoužité položky, doplnit pouze skutečně prostudované zdroje praktické části a aktualizovat data citování webů podle ISO 690:2022.

# Přílohy

<!-- BP-DOPLNIT: Před odevzdáním vložit skutečné diagramy, protokoly, výstupy a výpočty. Níže uvedené tabulky jsou připravenou strukturou příloh, nikoli výsledkem testování. -->

## Příloha A – Zadání modelové databáze

Modelový příklad představuje informační systém malého cykloservisu:

> Malý cykloservis eviduje zákazníky a jejich kola, přijímá zakázky na opravy a servis, k zakázkám přiřazuje mechaniky, účtuje provedené služby a spotřebovaný materiál a k dokončeným zakázkám vystavuje faktury. Náhradní díly odebírá od několika dodavatelů a sleduje jejich skladové množství. Systém má evidovat historii oprav konkrétního kola a umožnit dohledat služby a díly použité v jedné zakázce včetně jejich ceny v okamžiku zakázky.

Jádro zadání obsahuje deset entit:

| Entita | Klíčové atributy a omezení |
|:---|:---|
| Zákazník | id_zakaznik (PK), jmeno, prijmeni, telefon, email (UNIQUE), adresa, datum_registrace |
| Kolo | id_kolo (PK), id_zakaznik (FK), znacka, model, typ, rok_vyroby, seriove_cislo (UNIQUE) |
| Zaměstnanec | id_zamestnanec (PK), jmeno, prijmeni, pozice, telefon, datum_nastupu |
| Zakázka | id_zakazka (PK), id_kolo (FK), id_zamestnanec (FK, NULL), datum_prijeti, datum_dokonceni, stav, poznamka |
| Služba | id_sluzba (PK), nazev, popis, cena_zakladni, odhad_doby_min |
| Díl | id_dil (PK), nazev, cena_prodejni, mnozstvi_sklad, id_dodavatel (FK) |
| Dodavatel | id_dodavatel (PK), nazev, kontaktni_osoba, telefon, email |
| Zakázka_Služba | id_zakazka (FK), id_sluzba (FK), mnozstvi, cena_za_jednotku; složený PK |
| Zakázka_Díl | id_zakazka (FK), id_dil (FK), mnozstvi, cena_za_jednotku; složený PK |
| Faktura | id_faktura (PK), id_zakazka (FK, UNIQUE), datum_vystaveni, castka_celkem, zpusob_platby, stav_platby |

Model obsahuje vazby 1:N, dvě vazby M:N řešené asociačními entitami, vazbu 1:1, složené primární klíče, nepovinný cizí klíč, unikátní omezení a kontrolní omezení povolených hodnot.

## Příloha B – Referenční ER model

**⟦NEZAZNAMENÁNO – vložit čitelný referenční diagram, číslo obrázku, popisek a legendu použité notace⟧**

## Příloha C – Referenční DDL skripty

Referenční schéma je připraveno ve třech dialektech:

- PostgreSQL pro kontejner `mes-postgres`;
- MySQL pro kontejner `mes-mysql`;
- Oracle SQL pro kontejner `mes-oracle`.

**⟦NEZAZNAMENÁNO – vložit konečné skripty nebo uvést přesné názvy elektronických příloh a kontrolu jejich spuštění⟧**

## Příloha D – Protokoly testování

Pro každý nástroj bude přiložen samostatný protokol v této struktuře:

| Úloha | Začátek | Konec | Čas | Výsledek | Ruční zásahy | Chyby a poznámky | Doklad |
|:---|:---:|:---:|---:|:---|:---|:---|:---|
| Vytvoření struktury | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ |
| Forward engineering | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ |
| Reverse engineering | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ |
| Export | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ | ⟦NEZAZNAMENÁNO⟧ |

## Příloha E – Výstupy nástrojů

Pro každý nástroj budou přiloženy diagramy, exportované DDL, dostupné obrazové nebo dokumentové exporty a záznam přesné verze a edice. **⟦NEZAZNAMENÁNO⟧**

## Příloha F – AHP matice a výpočty

Příloha bude obsahovat:

- matici kritérií scénáře A;
- matici kritérií scénáře B;
- matice čtyř alternativ pro K1–K8;
- geometrické průměry, normalizované váhy, λmax, CI a CR;
- syntézu globálních skóre a kontrolu jejich součtu.

**⟦NEVYHODNOCENO – vložit skutečné matice a výpočty⟧**

## Příloha G – Analýza citlivosti

**⟦NEVYHODNOCENO – vložit úplnou tabulku změn vah, výsledných skóre, pořadí a odpovídající graf⟧**

## Příloha H – Podpůrná aplikace

Pokud podpůrná aplikace vznikne, příloha uvede zdrojový kód nebo odkaz na elektronickou přílohu, návod ke spuštění, použité technologie a kontrolní vstupy. Pokud aplikace realizována nebude, bude tato příloha z konečné verze odstraněna.
