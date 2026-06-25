# 5 Datové modely

Datový model představuje formalizovaný prostředek pro popis dat, jejich struktury a vztahů mezi nimi. Datové modely umožňují zachytit realitu tak, aby s ní bylo možné systematicky pracovat při návrhu databází i při jejich následné implementaci (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
***
Datový model poskytuje formalizovaný nástroj, který slouží k popisu dat, jejich struktur a vztahů mezi nimi. Definuje datové objekty a jejich vzájemné vztahy včetně omezení, která se jich týkají (Pokorný a Valenta, 2020). Datový model je zjednodušený popis reality, který je vytvořen tak, aby se podle něj dala navrhnout databáze a později také implementovat. (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
***

> **Zdrojové úryvky k odstavci výše**
>
> **„Datový model představuje formalizovaný prostředek pro popis dat, jejich struktury a vztahů mezi nimi.”**
>
> - *Elmasri a Navathe (2016, s. 29)*: „A *data model*—a collection of concepts that can be used to describe the structure of a database—provides the necessary means to achieve this abstraction. By *structure of a database* we mean the data types, relationships, and constraints that apply to the data.”
> - *Pokorný a Valenta (2020, s. 22)*: „Datový model je prostředek k definici struktury databáze, tedy k definování, které datové objekty jsou v databázi a jaké jsou mezi nimi vztahy a omezení.”

---

## 5.1 Konceptuální modelování a ER/EER model

### 5.1.1 Konceptuální modelování a základní pojmy ER modelu

Konceptuální modelování slouží k zachycení požadavků aplikační domény bez ohledu na konkrétní databázovou technologii.
Jeho cílem je vytvořit srozumitelný a logicky konzistentní model reality.
V praxi se pro tuto fázi velmi často používá entitně-relační model (ER model), případně jeho rozšířená
varianta EER (Chen, 1976; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
***
Konceptuální modelování slouží pro zachycení požadavků aplikační domény, kterou mná aplikace pokrývat, ale bez ohledu na konkrétní databázovou technologii.
Jeho cílem je vytvořit přehledný a věrný model reálného světa (Carvalho et al., 2022).
V praxi se pro tuto fázi velmi často používá entitně-relační model (ER model), případně jeho rozšířená varianta EER (Chen, 1976; Elmasri a Navathe, 2016).
***

> **Zdrojové úryvky k odstavci výše**
>
> **„Konceptuální modelování slouží k zachycení požadavků aplikační domény bez ohledu na konkrétní databázovou technologii.”**
>
> - *Carvalho et al. (2022, s. 3351)*: „CM [Conceptual Model] describes the physical or social aspects of the world abstractly. [...] It will be easier to follow and adapt to user requirements and explore existing relationships between the concepts.”
> - *Elmasri a Navathe (2016, s. 30)*: „*High-level* or *conceptual data models* provide concepts that are close to the way many users perceive data...”
>
> **„V praxi se pro tuto fázi velmi často používá entitně-relační model (ER model), případně jeho rozšířená varianta EER.”**
>
> - *Chen (1976, s. 9)*: „The entity-relationship model can be used as a basis for unification of different views of data: the network model, the relational model, and the entity set model.”
> - *Elmasri a Navathe (2016, s. 59)*: „The *Entity-Relationship (ER) model* is a popular high-level conceptual data model. This model and its variations are frequently used for the conceptual design of database applications...”

---

Základními pojmy ER modelu jsou entita, entitní množina, vztah a atribut. Entita je objekt reálného světa, který je schopen samostatné existence a lze jej jednoznačně odlišit od ostatních objektů. Entitní množina je množina entit stejného typu, které mají společné vlastnosti. Vztah vyjadřuje vazbu mezi entitami nebo entitními množinami a atribut představuje vlastnost entity nebo vztahu (Chen, 1976).
***
Základními pojmy ER modelu jsou entita, entitní množina, vztah a atribut.
Za entitu je považován objekt, který je schopen samostatné existence a lze jej jednoznačně odlišit od ostatních objektů (Chen, 1976).
Entitní množina je pak množina entit, které jsou stejného typu a mají společné vlastnosti (Chen, 1976).
Vztah vyjadřuje vazbu mezi entitami nebo entitními množinami a atribut představuje vlastnost entity nebo vztahu (Chen, 1976).
***

> **Zdrojové úryvky k odstavci výše**
>
> **„Entita je objekt reálného světa, který je schopen samostatné existence a lze jej jednoznačně odlišit od ostatních objektů.”**
>
> - *Chen (1976, s. 9)*: „An *entity* is a 'thing' which can be distinctly identified.”
>
> **„Entitní množina je množina entit stejného typu, které mají společné vlastnosti.”**
>
> - *Chen (1976, s. 9)*: „An *entity set* is a set of entities of the same type that share the same properties, or attributes.”
>
> **„Vztah vyjadřuje vazbu mezi entitami nebo entitními množinami.”**
>
> - *Chen (1976, s. 9–10)*: „A *relationship* is an association among several entities.”
>
> **„Atribut představuje vlastnost entity nebo vztahu.”**
>
> - *Chen (1976, s. 10)*: „The information about an entity is obtained by observation or measurement, and is expressed by a set of *attribute-value* pairs.”

---

Vztahy mezi entitami se popisují mimo jiné pomocí kardinality a participace. Kardinalita určuje, kolik entit jedné množiny může být ve vztahu k entitě jiné množiny. Typickými případy jsou vazby 1:1, 1:N a M:N. Participace vyjadřuje, zda je účast entity ve vztahu povinná nebo nepovinná. Tyto pojmy jsou důležité nejen na konceptuální úrovni, ale i pro následnou transformaci do relačního modelu (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
***
Vztahy mezi entitami lze popsat například kardinalitou a participací. Kardinalita udává, kolik entit jedné množiny může být ve vztahu k entitě jiné množiny (Elmasri a Navathe, 2016). Typickými případy jsou vazby 1:1, 1:N a M:N. Participace vyjadřuje, zda je účast entity ve vztahu povinná nebo nepovinná. Tyto pojmy jsou důležité nejen na konceptuální úrovni, ale i pro následnou transformaci do relačního modelu (Pokorný a Valenta, 2020).
***

> **Zdrojové úryvky k odstavci výše**
>
> **„Kardinalita určuje, kolik entit jedné množiny může být ve vztahu k entitě jiné množiny.”**
>
> - *Elmasri a Navathe (2016, s. 73)*: „The *cardinality ratio* for a binary relationship specifies the maximum number of relationship instances that an entity can participate in.”
> - *Pokorný a Valenta (2020, s. 33)*: „Mohutnost (cardinality) binárního vztahu nám říká, kolik entit jednoho typu může být asociováno s jednou entitou druhého (druhé) entitní množiny.”
>
> **„Participace vyjadřuje, zda je účast entity ve vztahu povinná nebo nepovinná.”**
>
> - *Elmasri a Navathe (2016, s. 74)*: „The *participation constraint* specifies whether the existence of an entity depends on its being related to another entity via the relationship type. This constraint specifies the minimum number of relationship instances that each entity can participate in, and is sometimes called the *minimum cardinality constraint*... There are two types of participation constraints—*total* and *partial*.”

---

### 5.1.2 Atributy, EER model a notace

Atributy jsou svázány s doménami, tedy s množinami přípustných hodnot. Rozlišují se jednoduché a složené atributy, případně další typy atributů. Pro jednoznačnou identifikaci entit slouží kandidátní a primární klíče. Rozšířený ER model (EER) doplňuje základní ER model o supertřídy, podtřídy a dědičnost atributů. EER model je vhodný tam, kde je třeba přesněji vystihnout specializaci nebo generalizaci objektů (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). V praxi se ER/EER model vyjadřuje různými grafickými notacemi; mezi nejčastější patří Chenova notace, Crow's Foot a UML (Elmasri a Navathe, 2016; Carvalho et al., 2022).
***
Atributy jsou svázány s doménami, tedy s množinami přípustných hodnot (Elmasri a Navathe, 2016). Rozlišujeme jednoduché a složené atributy, případně i další typy (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
Pro jednoznačnou identifikaci entit slouží kandidátní a primární klíče (Elmasri a Navathe, 2016).

Rozšířený ER model (EER) doplňuje základní ER model o supertřídy, podtřídy a dědičnost atributů (Pokorný a Valenta, 2020). EER model je vhodný především tam, kde je potřeba přesněji vystihnout specializaci nebo generalizaci objektů (Elmasri a Navathe, 2016). V praxi se ER/EER model vyjadřuje různými grafickými notacemi, a mezi nejčastější patří Chenova notace, Crow's Foot a UML (Elmasri a Navathe, 2016; Carvalho et al., 2022).
***

> **Zdrojové úryvky k odstavci výše**
>
> **„Atributy jsou svázány s doménami, tedy s množinami přípustných hodnot.”**
>
> - *Elmasri a Navathe (2016, s. 65)*: „Each simple attribute of an entity type is associated with a *value set* (or *domain*) of values. The value set specifies the set of values that may be assigned to that attribute for each individual entity.”
>
> **„Rozlišují se jednoduché a složené atributy, případně další typy atributů.”**
>
> - *Elmasri a Navathe (2016, s. 66)*: „*Composite* attributes can be divided into smaller subparts, which represent more basic attributes with independent meanings. [...] *Simple* (or *atomic*) attributes are not divisible into smaller components.”
> - *Pokorný a Valenta (2020, s. 31)*: „Atribut může být jednoduchý nebo složený.”
>
> **„Rozšířený ER model (EER) doplňuje základní ER model o supertřídy, podtřídy a dědičnost atributů.”**
>
> - *Elmasri a Navathe (2016, s. 107)*: „The *enhanced* (or *extended*) *entity-relationship* (*EER*) *model* includes all of the original ER model concepts, plus the concepts of subclass/superclass, specialization/generalization, and union types (categories).”

---

Pro hodnocení databázových návrhových nástrojů je podpora konceptuálního modelování významná z praktického hlediska. Nástroj by měl umožnit vyjádřit entity, vztahy, kardinality a omezení způsobem, který je srozumitelný analytikům i vývojářům. Jednotlivé nástroje se přitom mohou lišit použitou notací, úrovní podpory EER prvků a možností následného převodu modelu do relačního schématu (Carvalho et al., 2022; Rosenthal a Reiner, 1994).
***
Pro hodnocení databázových nástrojů je podpora konceptuálního modelování významná hlavně z praktického hlediska.
Nástroj by měl umožnit vyjádřit entity, vztahy, kardinality a omezení způsobem, který je srozumitelný jak analytikům, tak i vývojářům (Rosenthal a Reiner, 1994).
Jednotlivé nástroje se přitom mohou lišit použitou notací, úrovní podpory EER prvků a možností následného převodu modelu do relačního schématu (Carvalho et al., 2022; Rosenthal a Reiner, 1994).
***

> **Zdrojové úryvky k odstavci výše**
>
> **„Nástroj by měl umožnit vyjádřit entity, vztahy, kardinality a omezení způsobem, který je srozumitelný analytikům i vývojářům.”**
>
> - *Rosenthal a Reiner (1994, s. 168)*: „Conceptual design is done in the Entity-Relationship (ER) model.”
>
> **„Jednotlivé nástroje se přitom mohou lišit použitou notací, úrovní podpory EER prvků a možností následného převodu modelu do relačního schématu.”**
>
> - *Carvalho et al. (2022, s. 3358)*: „Another relevant characteristic is that some tools have a visual representation of the conceptual data model, but others only show the physical data model. However, some have both types of visualization.”
> - *Carvalho et al. (2022, s. 3351–3352)*: „We provide a brief description of the key features, such as [...] the presence of Reverse Engineering (auto-generation of ER from SQL) and Forward Engineering [...] finally, the pros and cons are analyzed.”

---

## 5.2 Relační model

Relační model je založen na relacích, které jsou v praxi reprezentovány tabulkami. Každá relace má své schéma, tedy jméno relace, seznam atributů a jejich domén. Konkrétní řádky tabulky odpovídají n-ticím. Relační model pracuje s atomickými hodnotami a s přesně vymezenými atributy (Codd, 1970; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
***
Relační model je založen na relacích, které jsou v praxi neformálně reprezentovány tabulkami.
Každá relace má své schéma, tedy jméno relace, seznam atributů a jejich domén (Pokorný a Valenta, 2020).
Konkrétní řádky tabulky odpovídají n-ticím.
Relační model pracuje s atomickými hodnotami a s přesně vymezenými atributy (Codd, 1970; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

***

> **Zdrojové úryvky k odstavci výše**
>
> **„Relační model je založen na relacích, které jsou v praxi reprezentovány tabulkami."**
>
> - *Codd (1970, s. 377)*: „The term *relation* is used here in its accepted mathematical sense. Given sets S1, S2, ..., Sn (not necessarily distinct), R is a relation on these n sets if it is a set of n-tuples each of which has its first element from S1, its second element from S2, and so on."
> - *Elmasri a Navathe (2016, s. 141)*: „The *relational model* represents the database as a collection of *relations*. Informally, each relation resembles a *table* of values.“
>
> **„Každá relace má své schéma, tedy jméno relace, seznam atributů a jejich domén."**
>
> - *Elmasri a Navathe (2016, s. 142)*: „A *relation schema* $R$, denoted by $R(A_1, A_2, \dots, A_n)$, is made up of a relation name $R$ and a list of attributes, $A_1, A_2, \dots, A_n$. Each attribute $A_i$ is the name of a role played by some domain $D$ in the relation schema $R$.“
> - *Pokorný a Valenta (2020, s. 48)*: „Schéma relace obsahuje jméno relace a seznam jmen atributů spolu s jejich doménami."
>
> **„Relační model pracuje s atomickými hodnotami."**
>
> - *Codd (1970, s. 381)*: „Each column in a relation contains values from a single domain. [...] the values in the columns are atomic (nondecomposable)."

---

Klíče jsou v relačním modelu zásadní. Primární klíč slouží k jednoznačné identifikaci řádku tabulky (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). Cizí klíč umožňuje vyjádřit vazbu mezi tabulkami a je základem referenční integrity. Mezi obecné vlastnosti relačních tabulek patří nezávislost na pořadí řádků a sloupců a požadavek na neduplicitu řádků (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Watt a Eng, 2014).
***
Klíče jsou v relačním modelu zásadní.
Primární klíč slouží k jednoznačné identifikaci řádku tabulky (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
Cizí klíč umožňuje vyjádřit vazbu mezi tabulkami a je základem referenční integrity (Watt a Eng, 2014).
Mezi obecné vlastnosti relačních tabulek patří nezávislost na pořadí řádků a sloupců a požadavek na neduplicitu řádků (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

***

> **Zdrojové úryvky k odstavci výše**
>
> **„Primární klíč slouží k jednoznačné identifikaci řádku tabulky."**
>
> - *Elmasri a Navathe (2016, s. 146)*: „Usually, one of the candidate keys is designated to be the *primary key* of the relation. This is the candidate key whose values are used to identify tuples in the relation.“
> - *Pokorný a Valenta (2020, s. 49)*: „Primárním klíčem relace R rozumíme takový kandidátní klíč relace R, který byl vybrán jako identifikátor n-tic."
>
> **„Cizí klíč umožňuje vyjádřit vazbu mezi tabulkami a je základem referenční integrity."**
>
> - *Elmasri a Navathe (2016, s. 149)*: „A set of attributes *FK* in relation schema *R1* is a *foreign key* of *R1* that references relation *R2* if [...] the values of *FK* in each tuple *t1* in the current state *r1(R1)* either occur as values of *PK* for some tuple *t2* in the current state *r2(R2)* or are *NULL*.“
> - *Watt a Eng (2014)* — online, kap. 8: „A *foreign key* is an attribute that references the primary key of another table. It creates a link between two tables and enforces *referential integrity*."
>
> **„Mezi obecné vlastnosti relačních tabulek patří nezávislost na pořadí řádků a sloupců a požadavek na neduplicitu řádků."**
>
> - *Elmasri a Navathe (2016, s. 143)*: „The tuples in a relation [...] are not considered to be ordered. [...] All values in a column are of the same data type. [...] Each tuple should be distinct; there should be no duplicate tuples.“
> - *Codd (1970, s. 377)*: „A relation of degree 1 is commonly called a unary relation [...]. Relations of arbitrary degree are permitted [...]. Unlike a mathematical relation, a relation stored in a computer is often considered to be ordered; that is, there is a first tuple, a second tuple, and so on."

---

Relační model je pro tuto práci důležitý také proto, že většina běžně používaných návrhových nástrojů pro databáze směřuje k tvorbě relačního schématu a k práci s SQL databázemi. Při jejich porovnání proto bude podstatné, zda nástroj podporuje definici primárních a cizích klíčů, integritních omezení, datových typů a generování nebo zpětné načítání databázového schématu (Carvalho et al., 2022).
***
Relační model je pro tuto práci důležitý také proto, že většina běžně používaných návrhových nástrojů pro databáze směřuje k tvorbě relačního schématu a k práci s SQL databázemi. Při jejich porovnání proto bude důležité, zda nástroj podporuje definici primárních a cizích klíčů, integritních omezení, datových typů a generování nebo zpětné načítání databázového schématu (Carvalho et al., 2022).
***

> **Zdrojové úryvky k odstavci výše**
>
> **„Při jejich porovnání bude podstatné, zda nástroj podporuje definici primárních a cizích klíčů, integritních omezení, datových typů a generování nebo zpětné načítání databázového schématu."**
>
> - *Carvalho et al. (2022, s. 3351–3352)*: „We provide a brief description of the key features, such as the release year; real-time collaboration options; generation of the physical model; the presence of Reverse Engineering (auto-generation of ER from SQL) and Forward Engineering; supported DBMS and data types; different constraints; the incorporation of CM; finally, the pros and cons are analyzed."

---

## 5.3 Transformace ER/EER modelu do relačního modelu

Při přechodu od konceptuálního modelu k modelu relačnímu se entity obvykle převádějí na tabulky a atributy na sloupce. Vztahy typu 1:N se zpravidla reprezentují pomocí cizího klíče na straně N, zatímco vztahy M:N vyžadují vytvoření samostatné spojovací tabulky. Specifické případy představují vztahy 1:1, atributy vztahů nebo převod supertříd a podtříd. Tato transformace je důležitým mostem mezi konceptuálním a logickým návrhem; pokud je provedena nekonzistentně, vede k problémům v navazující implementaci (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Chlapek, Kučera a Palovská, 2019).
***
Při přechodu z konceptuálního modelu k modelu relačnímu se entity obvykle převádějí na tabulky a atributy na sloupce (Chlapek, Kučera a Palovská, 2019).
Vztahy typu 1:N se zpravidla reprezentují pomocí cizího klíče na straně N, zatímco pro vztahy M:N je vyžadováno vytvoření samostatné spojovací tabulky. Specifické případy představují vztahy 1:1, atributy vztahů nebo převod supertříd a podtříd (Elmasri a Navathe, 2016).
Tato transformace je důležitým přechodem mezi konceptuálním a logickým návrhem. Pokud je tato transformace provedena nekonzistentně, vede k problémům v následné implementaci (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
***

> **Zdrojové úryvky k odstavci výše**
>
> **„Při přechodu od konceptuálního modelu k modelu relačnímu se entity obvykle převádějí na tabulky a atributy na sloupce."**
>
> - *Elmasri a Navathe (2016, s. 290)*: „Step 1: Mapping of Regular Entity Types. For each regular (strong) entity type *E* in the ER schema, create a relation *R* that includes all the simple attributes of *E*.“
> - *Chlapek, Kučera a Palovská (2019, s. 92)*: „Každá entitní množina ER diagramu se transformuje na jednu nebo více relací (tabulek). Atributy entity se stávají sloupci tabulky."
>
> **„Vztahy typu 1:N se zpravidla reprezentují pomocí cizího klíče na straně N, zatímco vztahy M:N vyžadují vytvoření samostatné spojovací tabulky."**
>
> - *Elmasri a Navathe (2016, s. 292)*: „Step 4: Mapping of Binary 1:N Relationship Types. For each regular binary 1:N relationship type *R*, identify the relation *S* that represents the participating entity type at the N-side of *R*. Include as foreign key in *S* the primary key of the relation *T* that represents the other participating entity type.“
> - *Elmasri a Navathe (2016, s. 293)*: „Step 5: Mapping of Binary M:N Relationship Types. For each binary M:N relationship type *R*, create a new relation *S* to represent *R*.“
> - *Pokorný a Valenta (2020, s. 59)*: „Vztah M:N se realizuje novou tabulkou, jejímiž klíčovými atributy jsou primární klíče obou participujících entitních množin."
>
> **„Tato transformace je důležitým mostem mezi konceptuálním a logickým návrhem; pokud je provedena nekonzistentně, vede k problémům v navazující implementaci."**
>
> - *Carvalho et al. (2022, s. 3351)*: „The result of a proper and rigorous CM design is a functionally richer, less error-prone, adequately attuned, able to adapt to varying user requirements, and less expensive system."
> - *Rosenthal a Reiner (1994, s. 172)*: „logical schemas (suited to a particular data model or DBMS interface)"

---

U nástrojů pro návrh databází je proto prakticky významné, zda převod mezi konceptuálním a relačním modelem pouze vizuálně naznačují, nebo zda jej dokážou částečně automatizovat a kontrolovat. Automatické generování relačního schématu může práci urychlit, současně je však nutné ověřit, zda nástroj správně zachází s kardinalitami, vazbami M:N, povinnými atributy a integritními omezeními (Carvalho et al., 2022; Rosenthal a Reiner, 1994).
***
U nástrojů pro návrh databází je proto důležité, zda převod mezi konceptuálním a relačním modelem pouze vizuálně naznačují, nebo zda tento převod dokážou částečně automatizovat a kontrolovat.
Automatické generování relačního schématu může práci urychlit, ale je potřeba ověřit, zda nástroj také správně zachází s kardinalitami, vazbami M:N, povinnými atributy a integritními omezeními (Carvalho et al., 2022; Rosenthal a Reiner, 1994).
***

> **Zdrojové úryvky k odstavci výše**
>
> **„Zda převod mezi konceptuálním a relačním modelem pouze vizuálně naznačují, nebo zda jej dokážou částečně automatizovat a kontrolovat."**
>
> - *Rosenthal a Reiner (1994, s. 170)*: „Logical Design: ER→Relational Schema Translator; ER→Network Schema Translator."
> - *Carvalho et al. (2022, s. 3351–3352)*: „the presence of Reverse Engineering (auto-generation of ER from SQL) and Forward Engineering"

---

## 5.4 Normalizace relačního modelu

Normalizace je proces, jehož cílem je odstranit nadbytečnost dat a předcházet anomáliím při vkládání, aktualizaci a mazání údajů. Teoretickým základem normalizace jsou funkční závislosti. Pro potřeby této práce je dostačující vysvětlit první až třetí normální formu (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
***
Normalizace je proces, jehož cílem je odstranit nadbytečnost dat a předcházet anomáliím při vkládání, aktualizaci a mazání údajů.
Teoretickým základem normalizace jsou funkční závislosti.
Pro potřeby této práce je dostačující vysvětlit první až třetí normální formu (Codd, 1970; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).
***

> **Zdrojové úryvky k odstavci výše**
>
> **„Normalizace je proces, jehož cílem je odstranit nadbytečnost dat a předcházet anomáliím při vkládání, aktualizaci a mazání údajů."**
>
> - *Codd (1970, s. 380)*: „Normalization of the data base consists of the elimination of non-simple domains and the elimination of any relation whose information content can be obtained from other relations in a more elementary way."
> - *Elmasri a Navathe (2016, s. 525)*: „The goals of normalization are to design a good set of relation schemas by *eliminating data redundancy* and the *update anomalies* (insertion, deletion, and modification anomalies) that accompany it.“
>
> **„Teoretickým základem normalizace jsou funkční závislosti."**
>
> - *Elmasri a Navathe (2016, s. 528)*: „The concept of *functional dependency* [...] is a generalization of the concept of a *key*.“
> - *Codd (1970, s. 381–382)*: „A nonkey attribute A of R is *functionally dependent* on the primary key of R if and only if [...] there is at most one value of A associated with each value of the primary key."

---

První normální forma vyžaduje atomické hodnoty a nepřipouští opakující se skupiny. Druhá normální forma řeší závislost neklíčových atributů na celém klíči. Třetí normální forma odstraňuje tranzitivní závislosti mezi neklíčovými atributy. Tyto formy postačují k zajištění základní konzistence relačního schématu a tvoří standard, který by každý nástroj pro návrh databází měl uživateli umožňovat respektovat (Codd, 1970; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Chlapek, Kučera a Palovská, 2019).
***
První normální forma vyžaduje atomické hodnoty a nepřipouští skupiny, které se opakují (Codd, 1970; Elmasri a Navathe, 2016).
Druhá normální forma řeší závislost neklíčových atributů na celém klíči (Codd, 1970; Elmasri a Navathe, 2016).
Třetí normální forma odstraňuje tranzitivní závislosti mezi neklíčovými atributy (Codd, 1970; Elmasri a Navathe, 2016).
Tyto formy postačují k zajištění základní konzistence relačního schématu a tvoří standard, který by každý nástroj pro návrh databází měl uživateli umožňovat respektovat (Codd, 1970; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

***

> **Zdrojové úryvky k odstavci výše**
>
> **„První normální forma vyžaduje atomické hodnoty a nepřipouští opakující se skupiny."**
>
> - *Codd (1970, s. 381)*: „A relation is in first normal form (1NF) if and only if none of its domains has elements which are themselves sets."
> - *Elmasri a Navathe (2016, s. 532)*: „The *first normal form* (1NF) is now considered to be part of the formal definition of a relation in the basic (flat) relational model [...] It states that the domain of an attribute must include only *atomic* (simple, indivisible) values.“
>
> **„Druhá normální forma řeší závislost neklíčových atributů na celém klíči."**
>
> - *Codd (1970, s. 382)*: „A relation schema R is in second normal form (2NF) if every non-prime attribute of R is fully functionally dependent on the primary key."
> - *Elmasri a Navathe (2016, s. 534)*: „A relation schema *R* is in *second normal form* (2NF) if every nonprime attribute *A* in *R* is fully functionally dependent on the primary key of *R*.“
>
> **„Třetí normální forma odstraňuje tranzitivní závislosti mezi neklíčovými atributy."**
>
> - *Codd (1970, s. 382)*: „A relation is in third normal form (3NF) if it is in second normal form and every non-prime attribute of R is non-transitively dependent on every candidate key of R."
> - *Elmasri a Navathe (2016, s. 535)*: „A relation schema *R* is in *third normal form* (3NF) if, whenever a nontrivial functional dependency *X* → *A* holds in *R*, either (a) *X* is a superkey of *R*, or (b) *A* is a prime attribute of *R*.“

---

Normalizace zároveň ukazuje, že kvalita návrhového nástroje nespočívá pouze v grafické podobě diagramu. Důležité je, zda nástroj podporuje konzistenci modelu, upozorňuje na chybějící klíče nebo problematické vazby a umožňuje vytvořit návrh, který lze převést do udržitelného relačního schématu. Tato hlediska navazují na pozdější výběr hodnoticích kritérií pro komparaci nástrojů.
***
Normalizace zároveň ukazuje, že kvalita návrhového nástroje nespočívá jen v grafické podobě diagramu.
Důležité je, zda nástroj podporuje konzistenci modelu, upozorňuje na chybějící klíče nebo problematické vazby a umožňuje vytvořit návrh,
který lze převést do udržitelného relačního schématu.
Tato hlediska navazují na pozdější výběr hodnoticích kritérií pro komparaci nástrojů (Carvalho et al., 2022).

***
