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

