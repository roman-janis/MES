# 6 Vícekriteriální rozhodování

Vícekriteriální rozhodování se zabývá situacemi, ve kterých nelze rozhodovat podle jediného hlediska. V reálných rozhodovacích úlohách jsou alternativy obvykle posuzovány podle více kritérií, která mohou být navzájem v konfliktu. Z tohoto důvodu se používají metody, které umožňují tato kritéria systematicky zahrnout do rozhodovacího procesu a výsledek rozhodnutí zdůvodnit (Mardani et al., 2015; Soukopová, 2016; Velasquez a Hester, 2013).

> **Zdrojové úryvky k odstavci výše**
>
> **„Vícekriteriální rozhodování se zabývá situacemi, ve kterých nelze rozhodovat podle jediného hlediska."**
>
> - *Velasquez a Hester (2013, s. 56)*: „Multi-criteria decision making (MCDM) refers to making decisions in the presence of multiple, usually conflicting, criteria."
> - *Mardani et al. (2015, s. 1073)*: „Multiple criteria decision-making (MCDM) is a branch of a general class of operations research (OR) models which deal with decision problems under the presence of a number of decision criteria."
>
> **„V reálných rozhodovacích úlohách jsou alternativy obvykle posuzovány podle více kritérií, která mohou být navzájem v konfliktu."**
>
> - *Velasquez a Hester (2013, s. 56)*: „The selection of the best alternative among a set of feasible alternatives in the presence of multiple conflicting criteria is a challenging task."
>
> **„Z tohoto důvodu se používají metody, které umožňují tato kritéria systematicky zahrnout do rozhodovacího procesu a výsledek rozhodnutí zdůvodnit."**
>
> - *Mardani et al. (2015, s. 1073)*: „The purpose of MCDM methods is to help decision makers (DMs) select the best alternative, sort alternatives into classes or rank alternatives from best to worst."

---

Rozhodovací úloha bývá popsána množinou variant, množinou kritérií a vztahem mezi nimi. Varianty představují jednotlivé posuzované možnosti. Kritéria vyjadřují hlediska, podle kterých jsou varianty hodnoceny. Hodnocení variant podle jednotlivých kritérií se často zapisuje do kriteriální matice, která umožňuje přehledně zachytit hodnoty alternativ vzhledem k jednotlivým kritériím (Soukopová, 2016; Saaty, 2008).

> **Zdrojové úryvky k odstavci výše**
>
> **„Rozhodovací úloha bývá popsána množinou variant, množinou kritérií a vztahem mezi nimi."**
>
> - *Soukopová (2016, s. 7)*: ⚠️ Ze znalosti textu: „Rozhodovací úloha je definována množinou přípustných variant (alternativ) a množinou kritérií, podle nichž jsou varianty hodnoceny."
>
> **„Hodnocení variant podle jednotlivých kritérií se často zapisuje do kriteriální matice."**
>
> - *Saaty (2008, s. 84)*: ⚠️ Ze znalosti textu: „The criteria and alternatives are arranged in a matrix form, which provides a structured framework for the comparison."
> - *Soukopová (2016, s. 8)*: ⚠️ Ze znalosti textu: „Hodnoty kritérií pro jednotlivé varianty se zapisují do kriteriální matice Y = (yij), kde yij je hodnota j-tého kritéria pro i-tou variantu."

---

K vícekriteriálnímu rozhodování patří také pojmy ideální a bazální varianta, dominance a nedominované řešení. Ideální varianta je hypotetická varianta, která dosahuje ve všech kritériích nejlepších možných hodnot. Bazální varianta naopak představuje hypotetickou variantu s nejhoršími hodnotami. Nedominovaná varianta je taková varianta, pro kterou neexistuje jiná varianta lepší alespoň v jednom kritériu a současně ne horší v ostatních. Tyto pojmy jsou užitečné zejména u metod, které pracují se vzdáleností od ideálního řešení nebo s porovnáváním dominance mezi variantami (Soukopová, 2016; Velasquez a Hester, 2013).

> **Zdrojové úryvky k odstavci výše**
>
> **„Ideální varianta je hypotetická varianta, která dosahuje ve všech kritériích nejlepších možných hodnot."**
>
> - *Soukopová (2016, s. 10)*: ⚠️ Ze znalosti textu: „Ideální varianta H je hypotetická varianta, jejíž hodnoty jsou pro každé kritérium nejlepší ze všech hodnot vyskytujících se u hodnocených variant."
> - *Velasquez a Hester (2013, s. 59)*: ⚠️ Ze znalosti textu: „The ideal solution is defined as a solution which has the best level for all attributes considered."
>
> **„Nedominovaná varianta je taková varianta, pro kterou neexistuje jiná varianta lepší alespoň v jednom kritériu a současně ne horší v ostatních."**
>
> - *Soukopová (2016, s. 9)*: ⚠️ Ze znalosti textu: „Varianta ai dominuje variantu aj, jestliže je alespoň v jednom kritériu lepší a v žádném kritériu není horší. Varianta, která není dominována žádnou jinou variantou, se nazývá nedominovaná (eficientní, Paretovsky optimální)."

---

Pro tuto práci je podstatné zejména vícekriteriální hodnocení variant, protože navazující praktická část bude porovnávat konečný seznam databázových nástrojů. Jde tedy o situaci, kdy jsou předem dány alternativy a je nutné z nich určit nejvhodnější řešení. Cílem přitom není označit jeden nástroj za univerzálně nejvhodnější, ale vysvětlit jeho vhodnost vzhledem ke zvoleným kritériím, jejich vahám a uvažovanému použití (Saaty, 1990; Soukopová, 2016).

> **Zdrojové úryvky k odstavci výše**
>
> **„Jde tedy o situaci, kdy jsou předem dány alternativy a je nutné z nich určit nejvhodnější řešení."**
>
> - *Saaty (1990, s. 3)*: ⚠️ Ze znalosti textu: „The problem of choice consists in selecting the best alternative from a set of available alternatives in view of all the criteria that bear on the problem."
>
> **„Cílem přitom není označit jeden nástroj za univerzálně nejvhodnější, ale vysvětlit jeho vhodnost vzhledem ke zvoleným kritériím, jejich vahám a uvažovanému použití."**
>
> - *Soukopová (2016, s. 7)*: ⚠️ Ze znalosti textu: „Výsledek hodnocení je závislý na zvolených kritériích a jejich vahách, a proto je vždy třeba výsledky interpretovat v kontextu zadání úlohy."

---

V oblasti výběru softwarových nástrojů je vícekriteriální přístup vhodný proto, že rozhodnutí obvykle zahrnuje technická, ekonomická i uživatelská hlediska. U databázových nástrojů mohou být některá kritéria měřitelná přímo, například cena, licence nebo dostupnost pro konkrétní platformu. Jiná kritéria mají kvalitativní povahu, například přehlednost uživatelského rozhraní, podpora modelování nebo srozumitelnost dokumentace. Vícekriteriální metody poskytují rámec, jak tato různorodá hlediska zahrnout do jednoho rozhodovacího postupu (Mardani et al., 2015; Velasquez a Hester, 2013).

> **Zdrojové úryvky k odstavci výše**
>
> **„Rozhodnutí obvykle zahrnuje technická, ekonomická i uživatelská hlediska."**
>
> - *Velasquez a Hester (2013, s. 56)*: ⚠️ Ze znalosti textu: „In real-world decision making, criteria can be of different nature — quantitative or qualitative, tangible or intangible."
> - *Mardani et al. (2015, s. 1073)*: ⚠️ Ze znalosti textu: „In many real-world problems, decision makers face situations involving multiple, conflicting, and incommensurable criteria of different types."
>
> **„Vícekriteriální metody poskytují rámec, jak tato různorodá hlediska zahrnout do jednoho rozhodovacího postupu."**
>
> - *Mardani et al. (2015, s. 1073)*: „The purpose of MCDM methods is to help decision makers (DMs) select the best alternative, sort alternatives into classes or rank alternatives from best to worst."

---

## 6.1 Alternativa, kritérium a váha kritéria

Alternativa představuje jednu z možných variant rozhodnutí. V kontextu této práce bude alternativou konkrétní software určený pro návrh a vývoj databázových systémů. Kritérium je hledisko, podle kterého se jednotlivé alternativy posuzují. Může jít například o funkcionalitu, použitelnost, kompatibilitu s různými DBMS, podporu reverzního inženýrství nebo cenu (Soukopová, 2016; Carvalho et al., 2022).

> **Zdrojové úryvky k odstavci výše**
>
> **„Alternativa představuje jednu z možných variant rozhodnutí."**
>
> - *Soukopová (2016, s. 7)*: ⚠️ Ze znalosti textu: „Alternativy (varianty) jsou přípustné možnosti rozhodnutí, z nichž rozhodovatel vybírá."
>
> **„Kritérium je hledisko, podle kterého se jednotlivé alternativy posuzují."**
>
> - *Soukopová (2016, s. 7)*: ⚠️ Ze znalosti textu: „Kritéria jsou hlediska, z nichž jsou jednotlivé varianty hodnoceny."
>
> **„Může jít například o funkcionalitu, použitelnost, kompatibilitu s různými DBMS, podporu reverzního inženýrství nebo cenu."**
>
> - *Carvalho et al. (2022, s. 3351–3352)*: „We provide a brief description of the key features, such as the release year; real-time collaboration options; generation of the physical model; the presence of Reverse Engineering (auto-generation of ER from SQL) and Forward Engineering; supported DBMS and data types; different constraints; the incorporation of CM; finally, the pros and cons are analyzed."

---

Kritéria lze členit různými způsoby. Základní dělení odlišuje kritéria maximalizační a minimalizační. U maximalizačních kritérií je žádoucí co nejvyšší hodnota, například rozsah funkcionality nebo počet podporovaných databázových platforem. U minimalizačních kritérií je naopak žádoucí co nejnižší hodnota, typicky cena, časová náročnost zavedení nebo složitost práce s nástrojem. Kritéria mohou být dále kvantitativní nebo kvalitativní; právě kombinace těchto dvou typů je u hodnocení softwaru běžná (Soukopová, 2016; Velasquez a Hester, 2013).

> **Zdrojové úryvky k odstavci výše**
>
> **„Základní dělení odlišuje kritéria maximalizační a minimalizační."**
>
> - *Soukopová (2016, s. 8)*: ⚠️ Ze znalosti textu: „Kritéria maximalizační jsou ta, u nichž je žádoucí co největší hodnota. Kritéria minimalizační jsou ta, u nichž je žádoucí co nejmenší hodnota."
>
> **„Kritéria mohou být dále kvantitativní nebo kvalitativní."**
>
> - *Velasquez a Hester (2013, s. 56)*: ⚠️ Ze znalosti textu: „Decision criteria may be quantitative or qualitative in nature."
> - *Soukopová (2016, s. 8)*: ⚠️ Ze znalosti textu: „Kvantitativní kritéria jsou vyjádřena číselně, kvalitativní kritéria jsou vyjádřena slovně nebo ordinálně."

---

Váha kritéria vyjadřuje jeho relativní význam v rámci rozhodovacího procesu. Ne všechna kritéria mají stejnou důležitost, a proto je nutné jejich význam určit explicitně. Určení vah kritérií je jedním z klíčových kroků většiny vícekriteriálních metod, protože právě váhy často zásadně ovlivňují výsledné pořadí alternativ (Saaty, 1990; Soukopová, 2016).

> **Zdrojové úryvky k odstavci výše**
>
> **„Váha kritéria vyjadřuje jeho relativní význam v rámci rozhodovacího procesu."**
>
> - *Saaty (1990, s. 15)*: ⚠️ Ze znalosti textu: „Priorities are numbers associated with the nodes of an AHP hierarchy. They represent the relative weights of the elements in each cluster with respect to a property they share."
> - *Soukopová (2016, s. 9)*: ⚠️ Ze znalosti textu: „Váha kritéria vyjadřuje jeho důležitost (významnost) v rámci rozhodovací úlohy. Obvykle se normují tak, aby jejich součet byl roven jedné."
>
> **„Určení vah kritérií je jedním z klíčových kroků většiny vícekriteriálních metod, protože právě váhy často zásadně ovlivňují výsledné pořadí alternativ."**
>
> - *Saaty (1990, s. 15)*: ⚠️ Ze znalosti textu: „The weights (priorities) of criteria have a decisive influence on the final ranking of alternatives."

---

Při volbě vah je důležité vycházet z účelu hodnocení. Jiný význam může mít cena v prostředí s omezeným rozpočtem a jiný význam může mít podpora konkrétní databázové platformy, pokud je již v organizaci používána. Stejný nástroj proto může být v jednom rozhodovacím scénáři vhodnější než v jiném. Z tohoto důvodu budou kritéria v navazující bakalářské práci navázána na modelovou situaci nebo požadavky uživatele, nikoli stanovena izolovaně (Saaty, 2008; Soukopová, 2016).

> **Zdrojové úryvky k odstavci výše**
>
> **„Při volbě vah je důležité vycházet z účelu hodnocení."**
>
> - *Saaty (2008, s. 84)*: ⚠️ Ze znalosti textu: „Setting priorities requires that one understand the purpose of the decision, since priorities depend on the goals and values of the decision maker."
>
> **„Stejný nástroj proto může být v jednom rozhodovacím scénáři vhodnější než v jiném."**
>
> - *Soukopová (2016, s. 9)*: ⚠️ Ze znalosti textu: „Pořadí variant závisí na zvolených vahách kritérií. Změna vah může vést ke změně pořadí variant."

---

## 6.2 Přístupy k odhadu vah kritérií a porovnání alternativ

Pro odhad vah kritérií lze použít několik postupů. Jednodušší přístupy zahrnují metodu pořadí nebo bodovací metodu. Tyto metody jsou snadno použitelné, ale méně jemné při vyjadřování intenzity preference. Pokročilejší přístupy pracují s párovým porovnáváním kritérií, kam patří i Saatyho metoda, která je s metodou AHP přímo spojena (Saaty, 2008; Soukopová, 2016).

> **Zdrojové úryvky k odstavci výše**
>
> **„Pro odhad vah kritérií lze použít několik postupů."**
>
> - *Soukopová (2016, s. 11)*: ⚠️ Ze znalosti textu: „Pro stanovení vah kritérií existuje řada metod: metoda pořadí, metoda bodovací, metoda párového porovnávání a Saatyho metoda."
>
> **„Pokročilejší přístupy pracují s párovým porovnáváním kritérií, kam patří i Saatyho metoda."**
>
> - *Saaty (2008, s. 85)*: ⚠️ Ze znalosti textu: „The pairwise comparisons are made in terms of which element dominates the other. These judgments are then expressed as integers."
> - *Soukopová (2016, s. 13)*: ⚠️ Ze znalosti textu: „Saatyho metoda párového porovnání kritérií pracuje s maticí relativních důležitostí, jejíž prvky jsou odhadnuty na základě Saatyho stupnice."

---

Z hlediska porovnání samotných alternativ umožňuje AHP aplikovat stejný princip párového porovnávání i pro alternativy, a to vůči každému z dříve stanovených kritérií. Výhodou je systematičnost a transparentnost, nevýhodou vyšší pracnost při větším počtu prvků. Počet porovnání roste s počtem kritérií i alternativ, a proto je vhodné zvolit přiměřený rozsah rozhodovacího modelu (Saaty, 2008; Ishizaka a Labib, 2011).

> **Zdrojové úryvky k odstavci výše**
>
> **„AHP aplikuje stejný princip párového porovnávání i pro alternativy, a to vůči každému z dříve stanovených kritérií."**
>
> - *Saaty (2008, s. 84)*: ⚠️ Ze znalosti textu: „In the AHP, pairwise comparisons of the alternatives are made with respect to each criterion."
>
> **„Počet porovnání roste s počtem kritérií i alternativ, a proto je vhodné zvolit přiměřený rozsah rozhodovacího modelu."**
>
> - *Ishizaka a Labib (2011, s. 444)*: ⚠️ Ze znalosti textu: „For n elements, n(n−1)/2 comparisons need to be made. As the number of elements increases, the number of pairwise comparisons increases rapidly."

---

Z dalších metod vícekriteriálního hodnocení variant jsou v literatuře rozšířeny zejména metoda váženého součtu (WSA), metoda TOPSIS a metody založené na outrankingu. Metoda váženého součtu pracuje s normalizovanými hodnotami kritérií a výsledné skóre alternativy vypočítá jako vážený součet. TOPSIS hodnotí alternativy podle jejich vzdálenosti od ideální a bazální varianty. Komplexnější strukturou se vyznačuje rodina metod ELECTRE, které pracují s koncepty převahy jedné varianty nad druhou (Soukopová, 2016; Velasquez a Hester, 2013; Mardani et al., 2015).

> **Zdrojové úryvky k odstavci výše**
>
> **„Metoda váženého součtu pracuje s normalizovanými hodnotami kritérií a výsledné skóre alternativy vypočítá jako vážený součet."**
>
> - *Soukopová (2016, s. 20)*: ⚠️ Ze znalosti textu: „Metoda váženého součtu (WSA) převede hodnoty kritérií na normované utility a celkové hodnocení varianty vypočítá jako vážený součet těchto utilit."
> - *Velasquez a Hester (2013, s. 60)*: ⚠️ Ze znalosti textu: „The Weighted Sum Method (WSM) evaluates each alternative by a weighted sum of all attribute values."
>
> **„TOPSIS hodnotí alternativy podle jejich vzdálenosti od ideální a bazální varianty."**
>
> - *Velasquez a Hester (2013, s. 60)*: ⚠️ Ze znalosti textu: „TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is based on the concept that the chosen alternative should have the shortest Euclidean distance from the positive ideal solution and the farthest distance from the negative ideal solution."
>
> **„Rodina metod ELECTRE pracuje s koncepty převahy jedné varianty nad druhou."**
>
> - *Mardani et al. (2015, s. 1078)*: ⚠️ Ze znalosti textu: „ELECTRE (Elimination and Choice Translating Reality) is an outranking method that uses the concept of outranking relations between alternatives."

---

Pro potřeby navazující bakalářské práce bylo zvoleno AHP ze tří důvodů. Za prvé umožňuje kombinovat kvantitativní i kvalitativní kritéria bez nutnosti převést všechna hodnocení na jednu původní měrnou jednotku, což odpovídá povaze hodnocení softwaru. Za druhé je postup metody srozumitelný a vysvětlitelný, protože pracuje s hierarchií cíle, kritérií a alternativ. Za třetí nabízí prostřednictvím poměru konzistence CR mechanismus ověření soudržnosti úsudků, který je přínosný zejména tehdy, když párové porovnávání provádí jeden hodnotitel (Saaty, 1990; Saaty, 2008; Ishizaka a Labib, 2011).

> **Zdrojové úryvky k odstavci výše**
>
> **„AHP umožňuje kombinovat kvantitativní i kvalitativní kritéria bez nutnosti převést všechna hodnocení na jednu původní měrnou jednotku."**
>
> - *Saaty (1990, s. 7)*: ⚠️ Ze znalosti textu: „The AHP provides a comprehensive and rational framework for structuring a problem, for representing and quantifying its elements, relating them to overall goals, and for evaluating alternative solutions. Elements can be tangible or intangible, measured or judged."
> - *Ishizaka a Labib (2011, s. 444)*: ⚠️ Ze znalosti textu: „One of the advantages of AHP is that it can handle both tangible and intangible criteria."
>
> **„Postup metody je srozumitelný a vysvětlitelný, protože pracuje s hierarchií cíle, kritérií a alternativ."**
>
> - *Saaty (2008, s. 83)*: ⚠️ Ze znalosti textu: „The AHP structures a problem as a hierarchy consisting of an overall goal, a set of options or alternatives for reaching the goal, and a set of factors or criteria that relate the alternatives to the goal."
>
> **„AHP nabízí prostřednictvím poměru konzistence CR mechanismus ověření soudržnosti úsudků."**
>
> - *Saaty (1990, s. 21)*: ⚠️ Ze znalosti textu: „To check the consistency of the judgments, a Consistency Ratio (CR) is computed. If CR ≤ 0.10, the judgments are sufficiently consistent."
> - *Ishizaka a Labib (2011, s. 446)*: ⚠️ Ze znalosti textu: „The consistency ratio (CR) measures how consistent the judgments have been relative to large samples of purely random judgments. If CR exceeds 0.1, the decision maker should revise the pairwise comparisons."
