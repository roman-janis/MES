# 5 Datové modely

## 5.1 Konceptuální modelování a ER/EER model

Datový model představuje formalizovaný prostředek pro popis dat, jejich struktury a vztahů mezi nimi. Datové modely umožňují zachytit realitu tak, aby s ní bylo možné systematicky pracovat při návrhu databází i při jejich následné implementaci (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

Konceptuální modelování slouží k zachycení požadavků aplikační domény bez ohledu na konkrétní databázovou technologii. Jeho cílem je vytvořit srozumitelný a logicky konzistentní model reality. V praxi se pro tuto fázi velmi často používá entitně-relační model (ER model), případně jeho rozšířená varianta EER (Chen, 1976; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

Základními pojmy ER modelu jsou entita, entitní množina, vztah a atribut. Entita je objekt reálného světa, který je schopen samostatné existence a lze jej jednoznačně odlišit od ostatních objektů. Entitní množina je množina entit stejného typu, které mají společné vlastnosti. Vztah vyjadřuje vazbu mezi entitami nebo entitními množinami a atribut představuje vlastnost entity nebo vztahu (Chen, 1976).

Vztahy mezi entitami se popisují mimo jiné pomocí kardinality a participace. Kardinalita určuje, kolik entit jedné množiny může být ve vztahu k entitě jiné množiny. Typickými případy jsou vazby 1:1, 1:N a M:N. Participace vyjadřuje, zda je účast entity ve vztahu povinná nebo nepovinná. Tyto pojmy jsou důležité nejen na konceptuální úrovni, ale i pro následnou transformaci do relačního modelu (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

Atributy jsou svázány s doménami, tedy s množinami přípustných hodnot. Rozlišují se jednoduché a složené atributy, případně další typy atributů. Pro jednoznačnou identifikaci entit slouží kandidátní a primární klíče. Rozšířený ER model (EER) doplňuje základní ER model o supertřídy, podtřídy a dědičnost atributů. EER model je vhodný tam, kde je třeba přesněji vystihnout specializaci nebo generalizaci objektů (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020). V praxi se ER/EER model vyjadřuje různými grafickými notacemi; mezi nejčastější patří Chenova notace, Crow's Foot a UML.

Pro hodnocení databázových návrhových nástrojů je podpora konceptuálního modelování významná z praktického hlediska. Nástroj by měl umožnit vyjádřit entity, vztahy, kardinality a omezení způsobem, který je srozumitelný analytikům i vývojářům. Jednotlivé nástroje se přitom mohou lišit použitou notací, úrovní podpory EER prvků a možností následného převodu modelu do relačního schématu (Carvalho et al., 2022; Rosenthal a Reiner, 1994).

## 5.2 Relační model

Relační model je založen na relacích, které jsou v praxi reprezentovány tabulkami. Každá relace má své schéma, tedy jméno relace, seznam atributů a jejich domén. Konkrétní řádky tabulky odpovídají n-ticím. Relační model pracuje s atomickými hodnotami a s přesně vymezenými atributy (Codd, 1970; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

Klíče jsou v relačním modelu zásadní. Primární klíč slouží k jednoznačné identifikaci řádku tabulky. Cizí klíč umožňuje vyjádřit vazbu mezi tabulkami a je základem referenční integrity. Mezi obecné vlastnosti relačních tabulek patří nezávislost na pořadí řádků a sloupců a požadavek na neduplicitu řádků (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Watt a Eng, 2014).

Relační model je pro tuto práci důležitý také proto, že většina běžně používaných návrhových nástrojů pro databáze směřuje k tvorbě relačního schématu a k práci s SQL databázemi. Při jejich porovnání proto bude podstatné, zda nástroj podporuje definici primárních a cizích klíčů, integritních omezení, datových typů a generování nebo zpětné načítání databázového schématu (Carvalho et al., 2022).

## 5.3 Transformace ER/EER modelu do relačního modelu

Při přechodu od konceptuálního modelu k modelu relačnímu se entity obvykle převádějí na tabulky a atributy na sloupce. Vztahy typu 1:N se zpravidla reprezentují pomocí cizího klíče na straně N, zatímco vztahy M:N vyžadují vytvoření samostatné spojovací tabulky. Specifické případy představují vztahy 1:1, atributy vztahů nebo převod supertříd a podtříd. Tato transformace je důležitým mostem mezi konceptuálním a logickým návrhem; pokud je provedena nekonzistentně, vede k problémům v navazující implementaci (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Chlapek, Kučera a Palovská, 2019).

U nástrojů pro návrh databází je proto prakticky významné, zda převod mezi konceptuálním a relačním modelem pouze vizuálně naznačují, nebo zda jej dokážou částečně automatizovat a kontrolovat. Automatické generování relačního schématu může práci urychlit, současně je však nutné ověřit, zda nástroj správně zachází s kardinalitami, vazbami M:N, povinnými atributy a integritními omezeními (Carvalho et al., 2022; Rosenthal a Reiner, 1994).

## 5.4 Normalizace relačního modelu

Normalizace je proces, jehož cílem je odstranit nadbytečnost dat a předcházet anomáliím při vkládání, aktualizaci a mazání údajů. Teoretickým základem normalizace jsou funkční závislosti. Pro potřeby této práce je dostačující vysvětlit první až třetí normální formu (Elmasri a Navathe, 2016; Pokorný a Valenta, 2020).

První normální forma vyžaduje atomické hodnoty a nepřipouští opakující se skupiny. Druhá normální forma řeší závislost neklíčových atributů na celém klíči. Třetí normální forma odstraňuje tranzitivní závislosti mezi neklíčovými atributy. Tyto formy postačují k zajištění základní konzistence relačního schématu a tvoří standard, který by každý nástroj pro návrh databází měl uživateli umožňovat respektovat (Codd, 1970; Elmasri a Navathe, 2016; Pokorný a Valenta, 2020; Chlapek, Kučera a Palovská, 2019).

Normalizace zároveň ukazuje, že kvalita návrhového nástroje nespočívá pouze v grafické podobě diagramu. Důležité je, zda nástroj podporuje konzistenci modelu, upozorňuje na chybějící klíče nebo problematické vazby a umožňuje vytvořit návrh, který lze převést do udržitelného relačního schématu. Tato hlediska navazují na pozdější výběr hodnoticích kritérií pro komparaci nástrojů.
