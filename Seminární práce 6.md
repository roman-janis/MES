# 6 Vícekriteriální rozhodování

Vícekriteriální rozhodování se zabývá situacemi, ve kterých nelze rozhodovat podle jediného hlediska. V reálných rozhodovacích úlohách jsou alternativy obvykle posuzovány podle více kritérií, která mohou být navzájem v konfliktu. Právě proto je vhodné využít metody, které umožňují tato kritéria systematicky zahrnout do rozhodovacího procesu (Saaty, 2008).

Rozhodovací úloha bývá popsána množinou variant, množinou kritérií a vztahem mezi nimi. Varianty představují jednotlivé posuzované možnosti. Kritéria vyjadřují hlediska, podle kterých jsou varianty hodnoceny. Hodnocení variant podle jednotlivých kritérií se často zapisuje do kriteriální matice (Saaty, 2008).

V souvislosti s vícekriteriálním rozhodováním je vhodné vysvětlit pojmy ideální a bazální varianta, dominance a nedominované řešení. Ideální varianta je hypotetická varianta, která dosahuje ve všech kritériích nejlepších možných hodnot. Bazální varianta naopak představuje hypotetickou variantu s nejhoršími hodnotami. Nedominovaná varianta je taková varianta, pro kterou neexistuje jiná varianta lepší alespoň v jednom kritériu a současně ne horší v ostatních (Saaty, 2008).

Pro potřeby této práce je důležité zejména vícekriteriální hodnocení variant, neboť navazující praktická část bude porovnávat konečný seznam databázových nástrojů. Jde tedy o situaci, kdy jsou předem dány alternativy a je nutné z nich určit nejvhodnější řešení (Saaty, 1990).

## 6.1 Alternativa, kritérium a váha kritéria

Alternativa představuje jednu z možných variant rozhodnutí. V kontextu této práce bude alternativou konkrétní software určený pro návrh a vývoj databázových systémů. Kritérium je hledisko, podle kterého se jednotlivé alternativy posuzují. Může jít například o funkcionalitu, použitelnost, kompatibilitu s různými DBMS, podporu reverzního inženýrství nebo cenu.

Kritéria lze členit různými způsoby. Základní dělení odlišuje kritéria maximalizační a minimalizační. U maximalizačních kritérií je žádoucí co nejvyšší hodnota, například rozsah funkcionality. U minimalizačních kritérií je naopak žádoucí co nejnižší hodnota, typicky například cena nebo náročnost implementace. Kritéria mohou být dále kvantitativní nebo kvalitativní.

Váha kritéria vyjadřuje jeho relativní význam v rámci rozhodovacího procesu. Ne všechna kritéria mají stejnou důležitost, a proto je nutné jejich význam určit explicitně. Určení vah kritérií je jedním z klíčových kroků většiny vícekriteriálních metod (Saaty, 1990; Soukopová, 2016).

## 6.2 Přístupy k odhadu vah kritérií a porovnání alternativ

Pro odhad vah kritérií lze použít několik postupů. Jednodušší přístupy zahrnují metodu pořadí nebo bodovací metodu. Tyto metody jsou snadno použitelné, ale méně jemné při vyjadřování intenzity preference. Pokročilejší přístupy pracují s párovým porovnáváním kritérií, kam patří i Saatyho metoda, která je s metodou AHP přímo spojena (Saaty, 2008). Z hlediska porovnání samotných alternativ umožňuje AHP aplikovat stejný princip párového porovnávání i pro alternativy, a to vůči každému z dříve stanovených kritérií. Výhodou je systematičnost a transparentnost, nevýhodou vyšší pracnost při větším počtu prvků (Saaty, 2008).

Z dalších metod vícekriteriálního hodnocení variant jsou v literatuře rozšířeny zejména metoda váženého součtu (WSA), která pracuje s lineárně normalizovanými hodnotami kritérií a výsledné skóre alternativy vypočítá jako vážený součet normalizovaných hodnot, a metoda TOPSIS, jež hodnotí alternativy podle jejich vzdálenosti od ideální a bazální varianty. Komplexnější strukturou se vyznačuje rodina metod ELECTRE, které pracují s koncepty outrangování (Soukopová, 2016). Pro potřeby navazující bakalářské práce bylo zvoleno AHP ze dvou důvodů: za prvé umožňuje přirozeně kombinovat kvantitativní i kvalitativní kritéria bez nutnosti jejich normalizace na společnou škálu, což je při hodnocení softwaru žádoucí; za druhé nabízí prostřednictvím indexu konzistence CR vestavěný mechanismus ověření soudržnosti hodnotitelových úsudků, který je obzvláště přínosný v situaci, kdy párové porovnávání provádí jeden hodnotitel (Saaty, 1990; Saaty, 2008).

