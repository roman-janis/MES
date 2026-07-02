# 6 Vícekriteriální rozhodování

Vícekriteriální rozhodování se zabývá situacemi, ve kterých nelze rozhodovat podle jediného hlediska. V reálných rozhodovacích úlohách jsou alternativy obvykle posuzovány podle více kritérií, která mohou být navzájem v konfliktu. Z tohoto důvodu se používají metody, které umožňují tato kritéria systematicky zahrnout do rozhodovacího procesu a výsledek rozhodnutí zdůvodnit (Mardani et al., 2015; Soukopová, 2016; Velasquez a Hester, 2013).
****
Vícekriteriální rozhodování se zabývá situacemi, ve kterých nejde rozhodnout podle jednoho hlediska (Mardani et al., 2015). V běžných rozhodovacích úlohách jsou alternativy obvykle hodnoceny podle více kritérií. Tato kritéria však mohou být ve vzájemném konfliktu (Velasquez a Hester, 2013). Z tohoto důvodu se používají metody, které umožňují tato kritéria systematicky zahrnout do rozhodovacího procesu a výsledek rozhodnutí zdůvodnit (Mardani et al., 2015).
****

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
****
Rozhodovací úloha je běžně popsána množinou variant, množinou hodnoticích kritérií a vztahem mezi nimi (Soukopová, 2016). Varianty představují jednotlivé posuzované možnosti, mezi kterými se rozhoduje. Kritéria určují, z jakých hledisek jsou jednotlivé varianty hodnoceny (Velasquez a Hester, 2013). Hodnocení variant podle jednotlivých kritérií se často zapisuje do kriteriální matice. Tato matice umožňuje zachytit přehledně hodnoty alternativ vzhledem k jednotlivým kritériím (Soukopová, 2016).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Rozhodovací úloha bývá popsána množinou variant, množinou kritérií a vztahem mezi nimi."**
>
> - *Soukopová (2016, s. 1)*: „Vícekriteriální rozhodovací problémy jsou popsány množinou variant, množinou hodnoticích kritérií a řadou vazeb mezi kritérii a variantami..."
> - *Fiala, Jablonský a Maňas (1994, cit. dle Soukopová, 2016, s. 1)*: „Rozhodovací problémy, v nichž jsou varianty posuzovány podle více kritérií, jsou v praxi velmi časté."
>
> **„Hodnocení variant podle jednotlivých kritérií se často zapisuje do kriteriální matice."**
>
> - *Saaty (2008, s. 84)*: „Pairwise comparisons are arranged in a matrix form, which provides a structured framework for the comparison."
> - *Soukopová (2016, s. 2)*: „...matematický model úlohy vícekriteriálního hodnocení variant vyjadřují ve tvaru kriteriální matice: $Y = (y_{ij})$... kde $D = \{a_{i1}, a_{i2}, \dots, a_{im}\}$ je pak množina $m$ vybraných variant..."
> - *Velasquez a Hester (2013, s. 56)*: „MCDM methods are used to evaluate alternatives against a set of criteria."

---

K vícekriteriálnímu rozhodování patří také pojmy ideální a bazální varianta, dominance a nedominované řešení. Ideální varianta je hypotetická varianta, která dosahuje ve všech kritériích nejlepších možných hodnot. Bazální varianta naopak představuje hypotetickou variantu s nejhoršími hodnotami. Nedominovaná varianta je taková varianta, pro kterou neexistuje jiná varianta lepší alespoň v jednom kritériu a současně ne horší v ostatních. Tyto pojmy jsou užitečné zejména u metod, které pracují se vzdáleností od ideálního řešení nebo s porovnáváním dominance mezi variantami (Soukopová, 2016; Velasquez a Hester, 2013).
****
S vícekriteriálním rozhodováním souvisejí i pojmy jako ideální a bazální varianta, dominance a nedominované řešení. Ideální varianta je hypotetická varianta, která ve všech kritériích získává nejlepší možné hodnoty (Soukopová, 2016; Velasquez a Hester, 2013). Bazální varianta naopak představuje hypotetickou variantu s nejhoršími hodnotami (Soukopová, 2016). Nedominovaná varianta je taková varianta, pro kterou neexistuje jiná varianta lepší alespoň v jednom kritériu a současně nehorší v ostatních (Soukopová, 2016). Tyto pojmy se používají především u metod, které pracují se vzdáleností od ideálního řešení nebo s porovnáváním dominance mezi variantami (Velasquez a Hester, 2013).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Ideální varianta je hypotetická varianta, která dosahuje ve všech kritériích nejlepších možných hodnot."**
>
> - *Soukopová (2016, s. 3)*: „První z nich, tedy varianta, která dosahuje ve všech kritériích nejlepší možné hodnoty, se nazývá ideální varianta $I = (I_1, I_1, \dots, I_k)$. Naopak varianta, která má všechny hodnoty kritérií na nejnižším stupni se nazývá bazální varianta $B = (B_1, B_2, \dots, B_k)$."
> - *Velasquez a Hester (2013, s. 60)*: „TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is based on the concept that the chosen alternative should have the shortest Euclidean distance from the positive ideal solution and the farthest distance from the negative ideal solution."
>
> **„Nedominovaná varianta je taková varianta, pro kterou neexistuje jiná varianta lepší alespoň v jednom kritériu a současně ne horší v ostatních."**
>
> - *Soukopová (2016, s. 2)*: „Nedominovanou variantou rozumíme takovou, ke které neexistuje v množině variant jiná varianta, lépe hodnocená alespoň podle jednoho kritéria a ne hůře podle ostatních kritérií. V opačném případě se varianta nazývá dominovaná a říkáme, že ji „lepší" varianta z uvedené definice dominuje."
> - *Ishizaka a Labib (2011, s. 444)*: „The goal is to select the best alternative among all available alternatives."

---

Pro tuto práci je podstatné zejména vícekriteriální hodnocení variant, protože navazující praktická část bude porovnávat konečný seznam databázových nástrojů. Jde tedy o situaci, kdy jsou předem dány alternativy a je nutné z nich určit nejvhodnější řešení. Cílem přitom není označit jeden nástroj za univerzálně nejvhodnější, ale vysvětlit jeho vhodnost vzhledem ke zvoleným kritériím, jejich vahám a uvažovanému použití (Saaty, 1990; Soukopová, 2016).
****
Pro tuto práci je důležité zejména vícekriteriální hodnocení variant. Důvodem je navazující část, kde se bude porovnávat konečný seznam databázových nástrojů. Jde tedy o případ, kdy jsou předem dány alternativy a z těchto alternativ je nutné určit nejvhodnější řešení (Mardani et al., 2015; Saaty, 1990). Cílem přitom není označit jeden nástroj za univerzálně nejvhodnější, ale vysvětlit jeho vhodnost vzhledem ke zvoleným kritériím, jejich vahám a uvažovanému použití (Saaty, 2008; Soukopová, 2016).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Jde tedy o situaci, kdy jsou předem dány alternativy a je nutné z nich určit nejvhodnější řešení."**
>
> - *Saaty (1990, s. 13)*: „The problem of choice consists in selecting the best alternative from a set of available alternatives in view of all the criteria that bear on the problem."
> - *Mardani et al. (2015, s. 517)*: „Multiple criteria decision-making (MCDM) is a branch of a general class of operations research models which deal with decision problems..."
>
> **„Cílem přitom není označit jeden nástroj za univerzálně nejvhodnější, ale vysvětlit jeho vhodnost vzhledem ke zvoleným kritériím, jejich vahám..."**
>
> - *Soukopová (2016, s. 6)*: „Pořadí variant závisí na zvolených vahách kritérií. Změna vah může vést ke změně pořadí variant."
> - *Saaty (2008, s. 83)*: „The AHP structures a problem as a hierarchy consisting of a goal, criteria, and alternatives."

---

V oblasti výběru softwarových nástrojů je vícekriteriální přístup vhodný proto, že rozhodnutí obvykle zahrnuje technická, ekonomická i uživatelská hlediska. U databázových nástrojů mohou být některá kritéria měřitelná přímo, například cena, licence nebo dostupnost pro konkrétní platformu. Jiná kritéria mají kvalitativní povahu, například přehlednost uživatelského rozhraní, podpora modelování nebo srozumitelnost dokumentace. Vícekriteriální metody poskytují rámec, jak tato různorodá hlediska zahrnout do jednoho rozhodovacího postupu (Mardani et al., 2015; Velasquez a Hester, 2013).
****
Při rozhodování o výběru softwarových nástrojů je vícekriteriální přístup vhodný proto, že rozhodnutí obvykle zahrnuje technická, ekonomická a uživatelská hlediska (Mardani et al., 2015; Velasquez a Hester, 2013). U databázových nástrojů jsou obvykle některá kritéria měřitelná přímo, například cena, licence nebo dostupnost pro konkrétní platformu. Jiná kritéria naopak mají popisnou povahu, například přehlednost uživatelského rozhraní, podpora modelování nebo srozumitelnost dokumentace. Vícekriteriální metody pomáhají přehledně spojit všechna důležitá hlediska do jednoho rozhodovacího procesu (Mardani et al., 2015).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Rozhodnutí obvykle zahrnuje technická, ekonomická i uživatelská hlediska."**
>
> - *Velasquez a Hester (2013, s. 56)*: „Multi-criteria decision making (MCDM) refers to making decisions in the presence of multiple, usually conflicting, criteria. MCDM has been used in many fields..."
> - *Mardani et al. (2015, s. 517)*: „In many real-world problems, decision makers face situations involving multiple, conflicting, and incommensurable criteria of different types."
>
> **„Vícekriteriální metody poskytují rámec, jak tato různorodá hlediska zahrnout do jednoho rozhodovacího postupu."**
>
> - *Mardani et al. (2015, s. 1073)*: „The purpose of MCDM methods is to help decision makers (DMs) select the best alternative, sort alternatives into classes or rank alternatives from best to worst."

---

## 6.1 Alternativa, kritérium a váha kritéria

Alternativa představuje jednu z možných variant rozhodnutí. V kontextu této práce bude alternativou konkrétní software určený pro návrh a vývoj databázových systémů. Kritérium je hledisko, podle kterého se jednotlivé alternativy posuzují. Může jít například o funkcionalitu, použitelnost, kompatibilitu s různými DBMS, podporu reverzního inženýrství nebo cenu (Soukopová, 2016; Carvalho et al., 2022).
****
Alternativa představuje jednu z možných variant rozhodnutí (Soukopová, 2016). V rámci této práce bude každá alternativa představovat konkrétní softwarový nástroj určený pro návrh a vývoj databázových systémů. Kritérium je hledisko, podle kterého se jednotlivé alternativy posuzují (Soukopová, 2016). Může jít například o funkcionalitu, použitelnost, kompatibilitu s různými DBMS, podporu reverzního inženýrství nebo cenu (Carvalho et al., 2022).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Alternativa představuje jednu z možných variant rozhodnutí."**
>
> - *Soukopová (2016, s. 1)*: „...posuzovány rozhodovací varianty (v našem případě projekty, resp. alternativy). Úlohy vícekriteriálního rozhodování jsou klasifikovány zpravidla podle charakteru množiny rozhodovacích variant..."
>
> **„Kritérium je hledisko, podle kterého se jednotlivé alternativy posuzují."**
>
> - *Soukopová (2016, s. 2)*: „Cílem metody (funkce) výběru je najít variantu $a_{opt}$ resp. množinu $D$ variant, které by podle všech kritérií dosáhly co nejlepšího ohodnocení..."
> - *Velasquez a Hester (2013, s. 56)*: „Dozens of methods have been developed, with even small variations to existing methods..."
>
> **„Může jít například o funkcionalitu, použitelnost, kompatibilitu s různými DBMS, podporu reverzního inženýrství nebo cenu."**
>
> - *Carvalho et al. (2022, s. 3351–3352)*: „We provide a brief description of the key features, such as the release year; real-time collaboration options; generation of the physical model; the presence of Reverse Engineering (auto-generation of ER from SQL) and Forward Engineering; supported DBMS and data types; different constraints; the incorporation of CM; finally, the pros and cons are analyzed."

---

Kritéria lze členit různými způsoby. Základní dělení odlišuje kritéria maximalizační a minimalizační. U maximalizačních kritérií je žádoucí co nejvyšší hodnota, například rozsah funkcionality nebo počet podporovaných databázových platforem. U minimalizačních kritérií je naopak žádoucí co nejnižší hodnota, typicky cena, časová náročnost zavedení nebo složitost práce s nástrojem. Kritéria mohou být dále kvantitativní nebo kvalitativní; právě kombinace těchto dvou typů je u hodnocení softwaru běžná (Soukopová, 2016; Velasquez a Hester, 2013).
****
Samotná kritéria lze uspořádat různými způsoby podle potřeb konkrétní rozhodovací úlohy. Základní dělení odlišuje kritéria maximalizační a minimalizační (Soukopová, 2016). U maximalizačních kritérií je požadována co nejvyšší hodnota, například rozsah funkcí nebo počet podporovaných databázových platforem. U minimalizačních kritérií je naopak požadována co nejnižší hodnota, například cena, časová náročnost zavedení nebo složitost práce. Kritéria mohou být kvantitativní nebo kvalitativní, a jejich kombinace je u hodnocení softwaru zcela běžná (Soukopová, 2016; Velasquez a Hester, 2013).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Základní dělení odlišuje kritéria maximalizační a minimalizační."**
>
> - *Soukopová (2016, s. 2)*: „Cílem metody (funkce) výběru je najít variantu... které by podle všech kritérií dosáhly co nejlepšího ohodnocení (tedy nejvyšších hodnot kritérií)..."
> - *Soukopová (2016, s. 3)*: „V kriteriální matici jsou [některá] kritéria stanovena jako minimalizační. Proto zavedeme nové stupnice..."
>
> **„Kritéria mohou být dále kvantitativní nebo kvalitativní."**
>
> - *Velasquez a Hester (2013, s. 56)*: „In real-world decision making, criteria can be of different nature — quantitative or qualitative, tangible or intangible."
> - *Soukopová (2016, s. 5)*: „1. stupnice intervalová, kdy jsou pro posuzování projektů zvolena kvantitativní kritéria... 2. stupnice poměrová, kde je počátek měřené vlastnosti dán přirozeným počátkem měřené veličiny... V případě, že kritéria nelze kvantifikovat, je možné použít... kvalitativní hodnocení."

---

Váha kritéria vyjadřuje jeho relativní význam v rámci rozhodovacího procesu. Ne všechna kritéria mají stejnou důležitost, a proto je nutné jejich význam určit explicitně. Určení vah kritérií je jedním z důležitých kroků většiny vícekriteriálních metod, protože právě váhy často zásadně ovlivňují výsledné pořadí alternativ (Saaty, 1990; Soukopová, 2016).
****
Váha kritéria vyjadřuje jeho relativní význam v rámci rozhodovacího procesu (Saaty, 1990; Soukopová, 2016). Ne všechna kritéria mají stejnou důležitost, a proto je nutné jejich význam určit explicitně. Určení vah kritérií je jedním z klíčových kroků většiny vícekriteriálních metod. Právě váhy často zásadně ovlivňují výsledné pořadí alternativ (Saaty, 1990).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Váha kritéria vyjadřuje jeho relativní význam v rámci rozhodovacího procesu."**
>
> - *Saaty (1990, s. 15)*: „Priorities are numbers associated with the nodes of an AHP hierarchy. They represent the relative weights of the elements in each cluster with respect to a property they share."
> - *Soukopová (2016, s. 6)*: „...váhy vyjadřují důležitost jednotlivých kritérií... tyto váhy se normalizují tak, aby jejich součet byl roven jedné. Získat váhy kritérií přímo v numerické formě bývá velmi obtížné."
>
> **„Určení vah kritérií je jedním z klíčových kroků většiny vícekriteriálních metod, protože právě váhy často zásadně ovlivňují výsledné pořadí alternativ."**
>
> - *Saaty (1990, s. 15)*: „The weights (priorities) of criteria have a decisive influence on the final ranking of alternatives."
> - *Ishizaka a Labib (2011, s. 444)*: „One of the advantages of AHP is that it can handle both tangible and intangible criteria... and compute local priorities."

---

Při volbě vah je důležité vycházet z účelu hodnocení. Jiný význam může mít cena v prostředí s omezeným rozpočtem a jiný význam může mít podpora konkrétní databázové platformy, pokud je již v organizaci používána. Stejný nástroj proto může být v jednom rozhodovacím scénáři vhodnější než v jiném. Z tohoto důvodu budou kritéria v navazující bakalářské práci navázána na modelovou situaci nebo požadavky uživatele, nikoli stanovena izolovaně (Saaty, 2008; Soukopová, 2016).
****
Při volbě vah je důležité vycházet z účelu hodnocení (Saaty, 2008; Soukopová, 2016). V prostředí s omezeným rozpočtem může být cena klíčová, zatímco ve firmě, která už používá určitou databázovou platformu, může mít větší váhu právě její podpora. Stejný nástroj proto může být v jednom rozhodovacím scénáři vhodnější než v jiném. Z tohoto důvodu budou kritéria v navazující práci navázána na modelovou situaci nebo požadavky uživatele (Saaty, 2008).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Při volbě vah je důležité vycházet z účelu hodnocení."**
>
> - *Saaty (2008, s. 84)*: „Setting priorities requires that one understand the purpose of the decision, since priorities depend on the goals and values of the decision maker."
> - *Soukopová (2016, s. 6)*: „Uvedený nedostatek spočívající v tom, že stupnice nerozlišují mezi důležitostí kritérií je pak možné řešit vyjádřením preferencí mezi kritérii."
> - *Vaidya a Kumar (2006, s. 1)*: „The Analytic Hierarchy Process (AHP)... is an effective tool for dealing with complex decision making..."

---

## 6.2 Přístupy k odhadu vah kritérií a porovnání alternativ

Pro odhad vah kritérií lze použít několik postupů. Jednodušší přístupy zahrnují metodu pořadí nebo bodovací metodu. Tyto metody jsou snadno použitelné, ale méně jemné při vyjadřování intenzity preference. Pokročilejší přístupy pracují s párovým porovnáváním kritérií, kam patří i Saatyho metoda, která je s metodou AHP přímo spojena (Saaty, 2008; Soukopová, 2016).
****
Pro odhadnutí vah jednotlivých kritérií lze použít několik postupů (Saaty, 2008; Soukopová, 2016). Mezi nejznámější jednoduché přístupy patří metoda pořadí nebo bodovací metoda. Tyto metody jsou jednoduše použitelné, ale nejsou tak přesné při popisu toho, jak výrazně je jedna možnost důležitější než druhá. Pokročilejší přístupy pracují s párovým porovnáváním kritérií a do této skupiny patří i Saatyho metoda, která je s metodou AHP přímo spojena (Saaty, 1990; Soukopová, 2016).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Pro odhad vah kritérií lze použít několik postupů."**
>
> - *Soukopová (2016, s. 6)*: „Mezi nejznámější metody odhadu vah patří: 1. Metoda pořadí Tato metoda vyžaduje od hodnotitele pouze uspořádání kritérií podle důležitosti. [...] Další metody jako metoda bodovací nebo párového porovnání."
> - *Saaty (2008, s. 85)*: „The pairwise comparisons are made in terms of which element dominates the other. These judgements are then expressed as absolute numbers."
>
> **„Pokročilejší přístupy pracují s párovým porovnáváním kritérií, kam patří i Saatyho metoda..."**
>
> - *Soukopová (2016, s. 6)*: „Získat váhy kritérií přímo v numerické formě bývá velmi obtížné... k odhadu vah slouží např. Saatyho metoda párového porovnání kritérií, která je založena na matici relativních důležitostí."
> - *Saaty (1990, s. 13)*: „We construct the pairwise comparison matrix $A = (a_{ij})$ such that $a_{ij} > 0$ and $a_{ji} = 1/a_{ij}$..."

---

Z hlediska porovnání samotných alternativ umožňuje AHP aplikovat stejný princip párového porovnávání i pro alternativy, a to vůči každému z dříve stanovených kritérií. Výhodou je systematičnost a transparentnost, nevýhodou vyšší pracnost při větším počtu prvků. Počet porovnání roste s počtem kritérií i alternativ, a proto je vhodné zvolit přiměřený rozsah rozhodovacího modelu (Saaty, 2008; Ishizaka a Labib, 2011).
****
Při hodnocení samotných alternativ umožňuje AHP použít stejný princip párového porovnávání i pro alternativy, a to vzhledem ke každému z dříve stanovených kritérií (Saaty, 2008; Vaidya a Kumar, 2006). Výhodou pak je systematičnost a transparentnost, naopak nevýhodou je vyšší pracnost při větším počtu prvků. Počet porovnání roste s počtem kritérií a alternativ. Proto je vhodné zvolit přiměřený rozsah rozhodovacího modelu (Ishizaka a Labib, 2011).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„AHP aplikuje stejný princip párového porovnávání i pro alternativy, a to vůči každému z dříve stanovených kritérií."**
>
> - *Saaty (2008, s. 84)*: „In the AHP, pairwise comparisons of the alternatives are made with respect to each criterion."
> - *Ishizaka a Labib (2011, s. 444)*: „For n elements, n(n−1)/2 comparisons need to be made. As the number of elements increases, the number of pairwise comparisons increases rapidly."
> - *Vaidya a Kumar (2006, s. 1)*: „AHP reduces complex decisions to a series of pairwise comparisons..."

---

Z dalších metod vícekriteriálního hodnocení variant jsou v literatuře rozšířeny zejména metoda váženého součtu (WSA), metoda TOPSIS a metody založené na outrankingu. Metoda váženého součtu pracuje s normalizovanými hodnotami kritérií a výsledné skóre alternativy vypočítá jako vážený součet. TOPSIS hodnotí alternativy podle jejich vzdálenosti od ideální a bazální varianty. Komplexnější strukturou se vyznačuje rodina metod ELECTRE, které pracují s koncepty převahy jedné varianty nad druhou (Soukopová, 2016; Velasquez a Hester, 2013; Mardani et al., 2015).
****
Z dalších metod vícekriteriálního hodnocení variant jsou rozšířeny především metoda váženého součtu (WSA), metoda TOPSIS a metody založené na outrankingu. Metoda váženého součtu pracuje s normalizovanými hodnotami kritérií a výsledné skóre alternativy vypočítá jako vážený součet (Soukopová, 2016; Velasquez a Hester, 2013). TOPSIS hodnotí alternativy podle jejich vzdálenosti od ideální a bazální varianty (Velasquez a Hester, 2013). Komplexnější strukturou se vyznačuje rodina metod ELECTRE, které pracují s koncepty převahy jedné varianty nad druhou (Mardani et al., 2015; Velasquez a Hester, 2013).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„Metoda váženého součtu pracuje s normalizovanými hodnotami kritérií a výsledné skóre alternativy vypočítá jako vážený součet."**
>
> - *Soukopová (2016, s. 8)*: „Metoda váženého součtu (angl. Weight Sum Approach - WSA), známá též pod názvem metoda vážených dílčích pořadí, vychází rovněž z principu maximalizace... celkové hodnocení varianty vypočítá jako vážený součet..."
> - *Velasquez a Hester (2013, s. 57)*: „The preferences of the decision makers also need to be precise, giving specific weights to each of the consequences... WSM evaluates each alternative..."
>
> **„TOPSIS hodnotí alternativy podle jejich vzdálenosti od ideální a bazální varianty."**
>
> - *Velasquez a Hester (2013, s. 60)*: „TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is based on the concept that the chosen alternative should have the shortest Euclidean distance from the positive ideal solution and the farthest distance from the negative ideal solution."
>
> **„Rodina metod ELECTRE pracuje s koncepty převahy jedné varianty nad druhou."**
>
> - *Mardani et al. (2015, s. 520)*: „...TOPSIS, elimination and choice expressing reality (ELECTRE)..."
> - *Velasquez a Hester (2013, s. 62)*: „ELECTRE, along with its many iterations, is an outranking method based on concordance analysis."

---

Pro potřeby navazující bakalářské práce bylo zvoleno AHP ze tří důvodů. Za prvé umožňuje kombinovat kvantitativní i kvalitativní kritéria bez nutnosti převést všechna hodnocení na jednu původní měrnou jednotku, což odpovídá povaze hodnocení softwaru. Za druhé je postup metody srozumitelný a vysvětlitelný, protože pracuje s hierarchií cíle, kritérií a alternativ. Za třetí nabízí prostřednictvím poměru konzistence CR mechanismus ověření soudržnosti úsudků, který je přínosný zejména tehdy, když párové porovnávání provádí jeden hodnotitel (Saaty, 1990; Saaty, 2008; Ishizaka a Labib, 2011).
****
Pro potřeby práce je metoda AHP vhodná ze tří důvodů. AHP totiž umožňuje pracovat současně s kvantitativními i kvalitativními kritérii, a to dokonce bez nutnosti převádět jednotlivá hodnocení na jednotnou měrnou škálu (Ishizaka a Labib, 2011; Saaty, 1990). Za druhé je postup metody srozumitelný a vysvětlitelný, protože pracuje s hierarchií cíle, kritérií a alternativ (Saaty, 2008). Za třetí AHP pomocí poměru konzistence (CR) umožňuje zkontrolovat, zda na sebe jednotlivá hodnocení logicky navazují. To je zvlášť užitečné v situacích, kdy párové porovnávání provádí jen jedna osoba (Ishizaka a Labib, 2011; Saaty, 1990).
****

> **Zdrojové úryvky k odstavci výše**
>
> **„AHP umožňuje kombinovat kvantitativní i kvalitativní kritéria bez nutnosti převést všechna hodnocení na jednu původní měrnou jednotku."**
>
> - *Saaty (1990, s. 10)*: „The AHP is a method for structuring, representing, and solving decision problems... It can handle tangible and intangible criteria."
> - *Ishizaka a Labib (2011, s. 444)*: „One of the advantages of AHP is that it can handle both tangible and intangible criteria."
>
> **„Postup metody je srozumitelný a vysvětlitelný, protože pracuje s hierarchií cíle, kritérií a alternativ."**
>
> - *Saaty (2008, s. 83)*: „The AHP structures a problem as a hierarchy consisting of a goal, criteria, subcriteria, and alternatives."
>
> **„AHP nabízí prostřednictvím poměru konzistence CR mechanismus ověření soudržnosti úsudků."**
>
> - *Saaty (1990, s. 13)*: „To check the consistency of the judgments, a Consistency Ratio (CR) is computed. If CR <= 0.10, the judgments are sufficiently consistent."
> - *Ishizaka a Labib (2011, s. 446)*: „The consistency ratio (CR) measures how consistent the judgements have been relative to large samples of purely random judgements... If CR is less than 0.1, the judgments are acceptable."
