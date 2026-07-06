# 4 Databázové systémy

## 4.1 Základní pojmy

Při práci s databázemi je nutné rozlišovat některé základní pojmy, jako jsou data, informace, databáze a systém řízení báze dat.
Pod pojmem data si lze představit jednotlivá fakta nebo zaznamenané hodnoty (Elmasri a Navathe, 2016). Tyto hodnoty samy o sobě nemusí být nositeli žádného širšího významu (Watt a Eng, 2014). Informace pak vznikají právě přiřazením významu datům v určitém kontextu (Elmasri a Navathe, 2016; Watt a Eng, 2014).
Pojem databáze pak představuje organizovanou sbírku vzájemně souvisejících dat, která jsou uložena tak, aby s nimi bylo možné dále efektivně pracovat (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Watt a Eng, 2014).

Systém řízení báze dat, běžně označovaný jako DBMS, je specializovaný software, který zajišťuje definici, ukládání, manipulaci, zabezpečení a správu dat uložených v databázi (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Spojení databáze s DBMS vytvoří databázový systém (DBS). Tento datábázový systém který usnadňuje procesy definování, konstrukce, manipulace a sdílení databází mezi různými uživateli a aplikacemi (Elmasri a Navathe, 2016). DBMS v rámci tohoto systému zajišťuje transakční zpracování, obnovení dat po pádu, souběžný přístup více uživatelů i řízení ochrany dat (Pokorný a Valenta, 2020).

Původně se používal především jednoduchý souborový přístup, který měl však řadu problémů a omezení, například v podobě nekonzistentnosti dat při aktualizaci, závislosti na aplikačním programu a na fyzické struktuře, často spojené s redundancí dat (Elmasri a Navathe, 2016). Databázový přístup tyto nedostatky odstraňuje, a to tím, že integruje data do jednoho logického celku a odděluje definici dat od samotných aplikací (Pokorný a Valenta, 2020). Oddělením byla získána vyšší bezpečnost, možnost centrálního řízení integritních omezení a sdílenost dat mezi více uživateli (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

## 4.2 Schéma databáze, instance a metadata

V teorii databází je třeba rozlišovat mezi schématem databáze a instancí databáze.
Schéma databáze představuje popis struktury uložených dat a zahrnuje určení entit, atributů, vazeb a integritních omezení, která mají data splňovat (Pokorný a Valenta, 2020).
Pojem instance databáze naopak vyjadřuje konkrétní aktuální obsah databáze v určitém čase (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
Toto rozlišení odděluje relativně stabilní strukturální návrh od proměnlivých datových hodnot (Elmasri a Navathe, 2016).

S databázovým systémem souvisí také pojem metadata.
Metadata jsou data o datech. Tato data tedy popisují strukturu databáze, význam atributů, integritní omezení nebo například přístupová práva (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
Metadata bývají ukládána v systémovém katalogu, který slouží jako centrální zdroj informací o databázových objektech (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

Správa a údržba schématu databáze je klíčovou rolí správce databáze (DBA), přičemž změny schématu v průběhu životního cyklu systému musí být pečlivě kontrolovány (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Metadata uložená v systémovém katalogu jsou využívána nejen samotným DBMS pro optimalizaci dotazů a kontrolu přístupových práv, ale taky externími nástroji (Elmasri a Navathe, 2016). Tyto nástroje dokážou metadata z katalogu načíst a vizualizovat je ve formě diagramů (Elmasri a Navathe, 2016). Tato vizualizace pak usnadňuje pochopení existující struktury databáze a její další rozvoj (Elmasri a Navathe, 2016).

## 4.3 Funkce DBMS a víceúrovňová architektura

DBMS obvykle poskytuje několik základních skupin funkcí: definici dat, manipulaci s daty, řízení souběžného přístupu více uživatelů, ochranu dat a obnovu po chybě (Pokorný a Valenta, 2020). Pro tyto funkce se používají pojmy jako DDL pro jazyk definice dat, DML pro jazyk manipulace s daty a transakce pro logický celek operací, který má být proveden buď celý, nebo vůbec (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).


Další významnou myšlenkou bylo chápat DBMS jako víceúrovňový systém podle modelu ANSI/SPARC (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Tento přístup představuje databázi jako hierarchii abstrakcí, které oddělují externí, konceptuální a interní rovinu (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Ve zprávě výboru ANSI/X3/SPARC z roku 1975 se toto členění upřesňuje takto: externí úroveň odpovídá pohledům jednotlivých skupin uživatelů, konceptuální úroveň představuje globální logický model celé databáze a interní úroveň popisuje fyzické uložení dat (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
Hlavním smyslem tohoto členění je podpora datové nezávislosti, tedy oddělení aplikací a uživatelských pohledů od fyzické implementace databáze (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

Pro následné porovnání nástrojů v této práci je toto rozdělení vhodné proto, že nástroje nepokrývají všechny úrovně databázového systému stejným způsobem (Rosenthal a Reiner, 1994). Některé se zaměřují především na konceptuální nebo logický model, jiné podporují i fyzické prvky konkrétního DBMS, například datové typy, indexy nebo generování SQL skriptů (Carvalho et al., 2022). Při hodnocení nástrojů proto bude vhodné sledovat nejen možnosti vytváření diagramů, ale také podporu přechodu mezi jednotlivými úrovněmi návrhu a implementace (Rosenthal a Reiner, 1994).

## 4.4 Fáze návrhu databáze

Návrh databáze představuje jednu z hlavních etap v rámci životního cyklu vývoje databázového systému a probíhá v několika na sebe navazujících krocích. Přímý přechod k fyzické implementaci tabulek v konkrétním systému může vést k chybám v návrhu, nadbytečné redundanci a omezené rozšiřitelnosti (Carvalho et al., 2022). Z tohoto důvodu se v literatuře standardně rozlišuje konceptuální, logický a fyzický návrh (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Rosenthal a Reiner, 1994).


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
