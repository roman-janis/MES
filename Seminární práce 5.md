# 5 Datové modely

## 5.1 Konceptuální modelování a ER/EER model

Datový model představuje formalizovaný prostředek pro popis dat, jejich struktury a vztahů mezi nimi. Datové modely umožňují zachytit realitu tak, aby s ní bylo možné systematicky pracovat při návrhu databází i při jejich následné implementaci (Pokorný a Valenta, 2020).

Konceptuální modelování slouží k zachycení požadavků aplikační domény bez ohledu na konkrétní databázovou technologii. Jeho cílem je vytvořit srozumitelný a logicky konzistentní model reality. V praxi se pro tuto fázi velmi často používá entitně-relační model (ER model), případně jeho rozšířená varianta EER (Pokorný a Valenta, 2020).

Základními pojmy ER modelu jsou entita, entitní množina, vztah a atribut. Entita je objekt reálného světa, který je schopen samostatné existence a lze jej jednoznačně odlišit od ostatních objektů. Entitní množina je množina entit stejného typu, které mají společné vlastnosti. Vztah vyjadřuje vazbu mezi entitami nebo entitními množinami a atribut představuje vlastnost entity nebo vztahu.

Vztahy mezi entitami se popisují mimo jiné pomocí kardinality a participace. Kardinalita určuje, kolik entit jedné množiny může být ve vztahu k entitě jiné množiny. Typickými případy jsou vazby 1:1, 1:N a M:N. Participace vyjadřuje, zda je účast entity ve vztahu povinná nebo nepovinná. Tyto pojmy jsou důležité nejen na konceptuální úrovni, ale i pro následnou transformaci do relačního modelu (Pokorný a Valenta, 2020).

Atributy jsou svázány s doménami, tedy s množinami přípustných hodnot. Rozlišují se jednoduché a složené atributy, případně další typy atributů. Pro jednoznačnou identifikaci entit slouží kandidátní a primární klíče. Rozšířený ER model (EER) doplňuje základní ER model o supertřídy, podtřídy a dědičnost atributů. EER model je vhodný tam, kde je třeba přesněji vystihnout specializaci nebo generalizaci objektů (Pokorný a Valenta, 2020). V praxi se ER/EER model vyjadřuje různými grafickými notacemi; mezi nejčastější patří Chenova notace, Crow's Foot a UML.

## 5.2 Relační model

Relační model je založen na relacích, které jsou v praxi reprezentovány tabulkami. Každá relace má své schéma, tedy jméno relace, seznam atributů a jejich domén. Konkrétní řádky tabulky odpovídají n-ticím. Relační model pracuje s atomickými hodnotami a s přesně vymezenými atributy (Pokorný a Valenta, 2020).

Klíče jsou v relačním modelu zásadní. Primární klíč slouží k jednoznačné identifikaci řádku tabulky. Cizí klíč umožňuje vyjádřit vazbu mezi tabulkami a je základem referenční integrity. Mezi obecné vlastnosti relačních tabulek patří nezávislost na pořadí řádků a sloupců a požadavek na neduplicitu řádků (Pokorný a Valenta, 2020).

## 5.3 Transformace ER/EER modelu do relačního modelu

Při přechodu od konceptuálního modelu k modelu relačnímu se entity obvykle převádějí na tabulky a atributy na sloupce. Vztahy typu 1:N se zpravidla reprezentují pomocí cizího klíče na straně N, zatímco vztahy M:N vyžadují vytvoření samostatné spojovací tabulky. Specifické případy představují vztahy 1:1, atributy vztahů nebo převod supertříd a podtříd. Tato transformace je důležitým mostem mezi konceptuálním a logickým návrhem; pokud je provedena nekonzistentně, vede k problémům v navazující implementaci (Pokorný a Valenta, 2020; Chlapek, Kučera a Palovská, 2019).

## 5.4 Normalizace relačního modelu

Normalizace je proces, jehož cílem je odstranit nadbytečnost dat a předcházet anomáliím při vkládání, aktualizaci a mazání údajů. Teoretickým základem normalizace jsou funkční závislosti. Pro potřeby této práce je dostačující vysvětlit první až třetí normální formu.

První normální forma vyžaduje atomické hodnoty a nepřipouští opakující se skupiny. Druhá normální forma řeší závislost neklíčových atributů na celém klíči. Třetí normální forma odstraňuje tranzitivní závislosti mezi neklíčovými atributy. Tyto formy postačují k zajištění základní konzistence relačního schématu a tvoří standard, který by každý nástroj pro návrh databází měl uživateli umožňovat respektovat (Pokorný a Valenta, 2020; Chlapek, Kučera a Palovská, 2019).

