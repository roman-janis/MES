# 7 Metoda AHP

Metoda *Analytic Hierarchy Process* (AHP) patří mezi nejznámější metody vícekriteriálního rozhodování. Jejím autorem je Thomas L. Saaty. Podstatou této metody je rozklad složitého rozhodovacího problému do hierarchické struktury, která obsahuje cíl, kritéria, případně subkritéria a alternativy. Tento rozklad umožňuje lépe zachytit strukturu rozhodovací úlohy a následně jednotlivé prvky systematicky porovnat (Saaty, 1990; Saaty, 2008; Vaidya a Kumar, 2006).

Na nejvyšší úrovni hierarchie stojí cíl rozhodování, například výběr nejvhodnějšího databázového nástroje. Na nižších úrovních se nacházejí kritéria, případně subkritéria, a na nejnižší úrovni alternativy. Klíčovým principem metody je párové porovnávání prvků na stejné úrovni vzhledem k prvku nadřazenému (Saaty, 2008).

AHP je použitelná zejména pro úlohy, ve kterých rozhodovatel potřebuje kombinovat technická, ekonomická a kvalitativně hodnocená kritéria. To odpovídá i tématu této práce, protože nástroje pro návrh a vývoj databázových systémů nelze hodnotit pouze jednou měřitelnou veličinou. Vedle ceny nebo podpory konkrétního DBMS je třeba zohlednit například rozsah modelovacích funkcí, použitelnost, dokumentaci, podporu reverzního inženýrství nebo možnosti generování SQL skriptů. Přehledové studie ukazují, že AHP se používá v širokém spektru rozhodovacích úloh a lze ji aplikovat i při výběru softwarových systémů (Ho, 2008; Simanavičienė a Vdovinskienė, 2023; Vaidya a Kumar, 2006).

Typický postup AHP lze shrnout do několika kroků. Nejprve je vymezen cíl rozhodování a sestavena hierarchie kritérií a alternativ. Poté se provedou párová porovnání kritérií vzhledem k cíli a párová porovnání alternativ vzhledem ke každému kritériu. Z těchto porovnání se vypočítají lokální priority, ověří se konzistence úsudků a nakonec se lokální váhy agregují do celkového pořadí alternativ (Saaty, 1990; Saaty, 2008; Ishizaka a Labib, 2011).

## 7.1 Saatyho škála a párové porovnání

Při párovém porovnávání se používá Saatyho škála. Základní hodnoty této škály jsou 1, 3, 5, 7 a 9, přičemž vyjadřují stejnou důležitost, mírnou, silnou, velmi silnou až absolutní preferenci. Sudé hodnoty 2, 4, 6, 8 lze chápat jako mezistupně. Pokud je jeden prvek méně významný než druhý, použije se převrácená hodnota. Hodnota 1 tedy znamená rovnocennost dvou prvků, zatímco hodnota 9 vyjadřuje krajní převahu jednoho prvku nad druhým (Saaty, 1990; Saaty, 2008).

Výsledkem párového porovnání je čtvercová reciproční matice, označovaná jako Saatyho matice. Reciproční povaha matice znamená, že pokud je prvek A vůči prvku B hodnocen hodnotou 5, pak opačné porovnání B vůči A má hodnotu 1/5. Hlavní diagonála matice obsahuje hodnoty 1, protože každý prvek je sám se sebou stejně důležitý (Saaty, 1990).

Z této matice se následně vypočítají lokální váhy. V literatuře se používá více postupů výpočtu, například metoda vlastního vektoru nebo výpočet založený na geometrickém průměru řádků. Výsledkem je vektor priorit, jehož hodnoty vyjadřují relativní význam porovnávaných prvků. U kritérií tyto hodnoty představují jejich váhy, u alternativ pak jejich lokální hodnocení vzhledem ke konkrétnímu kritériu (Saaty, 2008; Ishizaka a Labib, 2011).

Pro tuto práci je důležité, že párové porovnávání umožňuje hodnotiteli vyjadřovat preference postupně a přehledně. Místo přímého přiřazení přesných vah všem kritériím hodnotitel vždy posuzuje pouze dvojici prvků. To je užitečné zejména u kritérií, která nejsou přímo měřitelná, například přehlednost prostředí nebo kvalita podpory modelování (Saaty, 2008; Simanavičienė a Vdovinskienė, 2023).

## 7.2 Kontrola konzistence

Protože párové porovnávání vychází z lidského úsudku, není vždy dokonale konzistentní. Součástí metody AHP je proto kontrola konzistence. K tomu slouží *Consistency Index* (CI), *Random Consistency Index* (RI) a *Consistency Ratio* (CR). V praxi se uvádí, že hodnota CR menší než 0,1 značí přijatelnou úroveň konzistence; vyšší hodnoty obvykle vedou k přehodnocení porovnání (Saaty, 1990; Saaty, 2008).

Konzistence znamená, že jednotlivé úsudky by si neměly navzájem odporovat. Pokud je například kritérium A výrazně důležitější než kritérium B a kritérium B je důležitější než kritérium C, potom by mělo být kritérium A zároveň důležitější než kritérium C. Menší odchylky jsou při rozhodování přirozené, příliš vysoká nekonzistence však snižuje důvěryhodnost výsledků (Ishizaka a Labib, 2011; Saaty, 2008).

Možnost kontroly konzistence je jedním z důvodů, proč je AHP pro tuto práci vhodnější než jednodušší bodovací postup. Při hodnocení databázových nástrojů bude část úsudků založena na kvalitativním posouzení, například u použitelnosti nebo přehlednosti práce s modelem. Ukazatel CR umožňuje ověřit, zda jsou tato porovnání vnitřně soudržná, a případně se k problematickým porovnáním vrátit (Saaty, 1990; Ishizaka a Labib, 2011).

## 7.3 Výhody a omezení AHP

Výhodou AHP je možnost kombinovat kvantitativní i kvalitativní kritéria a transparentně zdůvodnit, jak bylo dosaženo výsledného pořadí alternativ. Metoda současně umožňuje analýzu citlivosti, tedy sledování dopadu změny vah kritérií na výsledné pořadí. To je důležité zejména tehdy, když jsou výsledky citlivé na malé změny preferencí a kdy je třeba ověřit stabilitu doporučení (Saaty, 2008; Ishizaka a Labib, 2011; Ho, 2008).

Nevýhodou je vyšší pracnost při větším počtu kritérií a alternativ a určitá míra subjektivity, která je s párovým porovnáváním spjata. Pokud je v modelu mnoho prvků, počet potřebných porovnání rychle roste a hodnotitel může být zatížen opakováním podobných rozhodnutí. Proto je vhodné udržet počet kritérií i alternativ v přiměřeném rozsahu a jasně vymezit význam jednotlivých kritérií (Saaty, 2008; Ishizaka a Labib, 2011).

V literatuře se v souvislosti s AHP diskutuje také jev tzv. rank reversal, tedy možná změna pořadí alternativ při přidání nebo odebrání varianty z modelu. Tento problém neznamená, že AHP nelze použít, ale ukazuje, že výsledky je třeba interpretovat s ohledem na zvolený soubor alternativ a nastavení modelu. U navazující praktické části proto bude důležité jasně zdůvodnit, proč byly vybrány právě dané nástroje a jaké požadavky reprezentují (Saaty, 2008; Vaidya a Kumar, 2006).

V kontextu výběru databázového nástroje je AHP přínosná také tím, že umožňuje oddělit váhy kritérií od hodnocení alternativ. Nejprve lze stanovit, jak důležitá je například funkcionalita, použitelnost, kompatibilita, cena nebo podpora vývojového procesu, a teprve poté hodnotit jednotlivé nástroje vůči těmto kritériím. Díky tomu je výsledek lépe kontrolovatelný než prosté celkové dojmové hodnocení softwaru (Saaty, 1990; Simanavičienė a Vdovinskienė, 2023).
