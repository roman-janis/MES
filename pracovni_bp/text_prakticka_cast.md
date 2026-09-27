# 9 Návrh aplikace pro podporu rozhodování

## 9.1 Vymezení problému a požadavků

Praktická část navazuje na vymezení databázových nástrojů a hodnoticích kritérií. Jejím hlavním výstupem je aplikace, ve které lze sestavit rozhodovací model, zadat párová porovnání a získat přehledný výsledek. Porovnání čtyř nástrojů na případu Cykloservisu představuje způsob demonstrace aplikace. Aplikace sama nerozhoduje, zda určitý nástroj požadovanou funkci skutečně poskytuje. Tuto informaci musí dodat hodnotitel na základě vlastních podkladů. Výpočet slouží k uspořádání jeho preferencí a k posouzení jejich vnitřní soudržnosti.

Při návrhu byly rozlišeny dvě skupiny požadavků. První skupina se týká sestavení rozhodovacího modelu a práce se vstupy. Druhou skupinu tvoří požadavky na výpočet, kontrolu chyb a zobrazení výsledků. Zvláštní pozornost byla věnována tomu, aby nebyla chybějící preference zaměněna za rovnocennost. Pokud uživatel dvojici neposoudí, musí být vyzván k doplnění. Hodnota jedna se použije pouze tehdy, když je rovnocennost skutečně zadána.

| Označení | Funkční požadavek | Ověřitelný výstup |
|---|---|---|
| F1 | Nabídnout předdefinovaná kritéria a alternativy | Seznam K1–K8 a čtyř nástrojů s popisy a odkazy |
| F2 | Umožnit volbu podmnožiny a přidání vlastních položek | Nové hodnocení obsahuje vybrané i vlastní položky |
| F3 | Sestavit párová porovnání | Každá neuspořádaná dvojice je zadána právě jednou |
| F4 | Doplnit opačná porovnání | Dolní trojúhelník je reciproční a diagonála rovna jedné |
| F5 | Vypočítat váhy a konzistenci | Zobrazené váhy, CI, odhad λ a CR v exportu |
| F6 | Sestavit pořadí alternativ | Součet globálních priorit je roven jedné |
| F7 | Umožnit změnu preferencí a nový výpočet | Výsledek reaguje na úpravu vstupů |
| F8 | Zobrazit upozornění na nekonzistenci | Matice s CR nad 0,10 vyvolá varování |
| F9 | Přenést hodnocení mezi spuštěními | Export a opětovný import JSON se shodnými výsledky |
| F10 | Demonstrovat citlivost | Samostatné změny vah K8, K1 a K3 |

Tabulka 3: Funkční požadavky aplikace (vlastní zpracování).

Nefunkční požadavky zahrnují jednoduché spuštění, srozumitelné formuláře, oddělení výpočtu od uživatelského rozhraní a možnost zpětné kontroly vstupů. Aplikace je určena pro menší rozhodovací úlohy. V rozhraní lze použít dvě až deset kritérií a dvě až deset alternativ. Omezení počtu prvků odpovídá rozsahu použité tabulky RI a současně omezuje množství porovnání, které musí uživatel vyplnit. Při osmi kritériích a čtyřech alternativách jde o 28 porovnání kritérií a 48 porovnání alternativ, tedy celkem 76 rozhodnutí.

Do základního rozsahu nebyly zahrnuty uživatelské účty, administrace, skupinové hodnocení ani automatické získávání parametrů produktů z internetu. Takové funkce by vyžadovaly další návrh oprávnění, ukládání dat a metodiky hodnocení. Pro ověření výpočetního postupu nejsou nezbytné. Export hodnocení umožňuje uložit vstupy bez zavedení databázového serveru. Nejde však o centrální evidenci více hodnotitelů.

## 9.2 Datový návrh

Základními objekty návrhu jsou kritérium, alternativa a hodnocení. Kritérium obsahuje identifikátor, název, popis a odkaz na doplňující informace. Stejná struktura je použita u alternativy. Hodnocení spojuje vybraný seznam kritérií, seznam alternativ a odpovídající párové matice. Pořadí prvků v seznamu jednoznačně určuje pořadí řádků a sloupců matic. Identifikátory musí být v rámci příslušného seznamu jedinečné.

| Objekt | Základní údaje | Význam |
|---|---|---|
| Kritérium | id, name, description, link | Hledisko rozhodování a jeho vymezení |
| Alternativa | id, name, description, link | Posuzovaná možnost a informační podklad |
| Hodnocení | title, schema_version, synthetic | Název úlohy, verze formátu a původ dat |
| Matice kritérií | criteria_matrix | Relativní význam kritérií vůči cíli |
| Matice alternativ | alternative_matrices | Preference alternativ vzhledem ke každému kritériu |
| Výsledek | weights, cr, scores, ranks | Odvozené hodnoty, které lze znovu vypočítat |

Tabulka 4: Datová struktura hodnocení (vlastní zpracování).

Příznak `synthetic` odlišuje zkušební data od vlastního hodnocení. U předem připravené demonstrace je nastaven na pravdivou hodnotu. Přenáší se společně se vstupy a zobrazuje se v uživatelském rozhraní. Označení je nutné zachovat také v tabulkách a v textu, protože samotné pojmenování alternativ názvy existujících produktů by jinak mohlo vyvolat dojem skutečné komparace. Příznak není důkazem pravdivosti dat; pouze zachycuje jejich deklarovaný původ.

Výsledky uložené v exportu nejsou při importu považovány za závazný vstup. Z platných matic se vždy provede nový výpočet. Tím se předchází situaci, kdy by byl změněn některý úsudek a v dokumentu zůstaly staré priority. Pro dlouhodobou reprodukovatelnost je vhodné společně uchovávat vstupní dokument, verzi aplikace a specifikaci výpočtu. Výsledkové tabulky samotné k opakování výpočtu nestačí.

Předdefinovaná data jsou uložena v souborech JSON mimo veřejně dostupný adresář aplikace. Během práce je hodnocení uchováváno v serverové relaci. Po skončení relace lze navázat importem dříve uloženého exportu. Toto řešení je přiměřené rozsahu demonstrace, ale nezajišťuje správu historie ani spolupráci více uživatelů. Pokud by byla aplikace později rozšířena, lze uvedené objekty převést do databázových tabulek bez změny matematického jádra.

## 9.3 Zvolený výpočetní postup

Pro výpočet vah byla zvolena metoda geometrických průměrů řádků. Její použití v AHP je popsáno například v přehledu Ishizaky a Labiba (2011). Jednotný postup je použit pro matici kritérií i pro všechny matice alternativ. Volba jedné metody je důležitá pro kontrolu výsledků, protože různé postupy odhadu priorit nemusí u nekonzistentních matic poskytnout zcela shodné hodnoty.

Pro matici A o rozměru n × n je geometrický průměr i-tého řádku určen vztahem

$$g_i=\left(\prod_{j=1}^{n}a_{ij}\right)^{1/n}.$$

Normalizovaná váha příslušného prvku je poté

$$w_i=\frac{g_i}{\sum_{r=1}^{n}g_r}.$$

Každá váha je kladná a jejich součet je roven jedné. V PHP je součin nahrazen ekvivalentním výpočtem pomocí logaritmů, tedy exponenciálou průměru logaritmů prvků řádku. V kontrolním sešitu je použit vzorec GEOMEAN. V samostatném kontrolním skriptu je použit přímý součin s desetinnou aritmetikou o přesnosti 50 míst. Rozdílný způsob zápisu výpočtu umožňuje lépe odhalit implementační chybu než pouhé opakované spuštění stejné funkce.

Z vah a vstupní matice je dále vytvořen vektor Aw. Pro každý řádek se vypočítá podíl jeho složky a příslušné váhy. Průměr těchto podílů je v implementaci označen jako odhad dominantního vlastního čísla:

$$\hat\lambda=\frac{1}{n}\sum_{i=1}^{n}\frac{(Aw)_i}{w_i}.$$

Je nutné rozlišovat tento odhad a přesné dominantní vlastní číslo matice. U geometrických vah se obecně nemusí jednat o tutéž hodnotu. V pracovní implementaci navazuje na odhad výpočet CI a CR. Při kontrole v jiném nástroji proto musí být ověřeno, zda nástroj používá stejný způsob stanovení priorit a konzistence. Samotná drobná odchylka při jiné metodě vah by nebyla automaticky důkazem chyby programu. Význam vzájemné konzistence a vztahu k vlastnímu vektoru rozebírají také Tomeš a Alcnauer (2014).

Pro n větší než dvě jsou použity vztahy

$$CI=\frac{\hat\lambda-n}{n-1},\qquad CR=\frac{CI}{RI_n}.$$

Záporná hodnota CI vzniklá pouze numerickým zaokrouhlením se nahradí nulou. V algoritmu se ale tímto způsobem neopravují vstupní preference. Tabulka RI obsahuje hodnoty 0,58 pro rozměr tři, 0,90 pro čtyři, 1,12 pro pět, 1,24 pro šest, 1,32 pro sedm, 1,41 pro osm, 1,45 pro devět a 1,49 pro deset. Pro jednu a dvě položky je RI nulový a aplikace neprovádí dělení. Zobrazuje CR rovné nule s vysvětlením, že v těchto rozměrech se kontrola konzistence tímto poměrem nevyhodnocuje. V rozhraní je požadována alespoň dvojice prvků.

Pracovní hranice přijatelné konzistence je stanovena na CR ≤ 0,10. Pokud je překročena, výsledky se nezamlčí, ale je zobrazeno upozornění a možnost návratu k porovnáním. Automatické přepisování preferencí není použito. Uživatel musí sám zhodnotit, zda rozdílná porovnání skutečně odpovídají jeho záměru. Nízké CR přitom potvrzuje pouze vnitřní soudržnost zadaných poměrů; nevypovídá o správnosti informací o produktech.

## 9.4 Syntéza a citlivost

Globální priorita alternativy a vzniká jako součet součinů vah kritérií a lokálních priorit příslušné alternativy:

$$P_a=\sum_{k=1}^{m}w_k l_{ak}.$$

Alternativy se řadí sestupně podle P. Při shodě priorit s tolerancí 10⁻¹² je přiřazeno stejné pořadí. Součet všech priorit je roven jedné. Uživatel nesmí tento výsledek chápat jako absolutní procento kvality nástroje. Vyjadřuje relativní preferenci uvnitř daného modelu, při konkrétním souboru alternativ, kritérií a úsudků.

Analýza citlivosti je provedena třemi samostatnými zásahy do vah. Postupně je zesílena váha K8, K1 a K3. Každý zásah vychází ze základního běhu. Zvolená váha je vynásobena dvěma a všechny váhy jsou následně normalizovány. Pro dotčené kritérium t platí w′t = 2wt/(1 + wt), pro ostatní kritéria w′j = wj/(1 + wt). Lokální váhy alternativ se nemění. Postup odpovídá otázce, jak se změní výsledek při větším významu nákladů, modelování nebo podpory DBMS.

Tato citlivost pracuje přímo s vahami. Faktor dva je předem zvolený scénář relativního zesílení jednoho hlediska, nikoli nový pozorovaný údaj nebo úsudek ze Saatyho škály. Po normalizaci zůstává součet vah jedna a poměry všech nezesílených kritérií mezi sebou se zachovají. Tři samostatné zásahy tak umožňují sledovat vliv konkrétní preference bez současné změny lokálního hodnocení nástrojů. Stejný postup bude použit i po nahrazení syntetických dat skutečnými vstupy. Nevytváří nové Saatyho matice kritérií a nezadává se za uživatele další sada párových úsudků. Proto se k pozměněným vahám nepřipojuje nová hodnota CR. CR původních vstupních matic zůstává údajem o základním hodnocení. Tím je oddělena kontrola zadaných úsudků od zkoumání jejich důsledků. Nezměněné pořadí je přípustným výsledkem; analýza nemá za cíl změnu pořadí vynutit.

# 10 Implementace webové aplikace

## 10.1 Architektura a použité prostředky

Pro implementaci byl použit jazyk PHP a serverově vytvářené stránky HTML. Vzhled je upraven samostatným souborem CSS. Základní ovládání nevyžaduje JavaScript. Tato volba umožňuje sledovat vazbu mezi formulářem, přijatými hodnotami a výpočtem bez další aplikační vrstvy. Funkčnost byla při tomto zpracování ověřena na místním prostředí PHP 8.5.11. Aplikace vyžaduje PHP 8.2 nebo novější; kompatibilita nebyla v tomto běhu prakticky testována na všech podporovaných verzích.

Matematika je soustředěna do třídy AhpCalculator. Třída Evaluation kontroluje strukturu hodnocení, jednotlivé položky a úplnost matic. Vstupní stránka index.php přijímá formuláře, vybírá zobrazení a předává validovaná data výpočtu. Připravené seznamy jsou odděleny od zdrojového kódu. Změna popisu alternativy proto nevyžaduje zásah do matematického algoritmu.

| Součást | Odpovědnost | Důvod oddělení |
|---|---|---|
| AhpCalculator | Váhy, konzistence, syntéza, citlivost a pořadí | Výpočet lze testovat bez prohlížeče |
| Evaluation | Formát dokumentu, odkazy, identifikátory, matice | Chybná data se odmítají před výpočtem |
| index.php | Formuláře, relace, směrování a výstup | Uživatelský postup je soustředěn na jednom místě |
| style.css | Rozložení a vzhled | Úprava vzhledu nemění výpočet |
| JSON data | Připravené položky a ukázkové vstupy | Data lze kontrolovat samostatně |

Tabulka 5: Členění implementace (vlastní zpracování).

Pro nové hodnocení se nejprve vytvoří seznam vybraných prvků. Následně se sestaví formuláře obsahující právě jednu položku pro každou dvojici. Po odeslání se z horního trojúhelníku vytvoří celá reciproční matice. Validace je provedena na serveru i tehdy, když prohlížeč již kontroluje povinná pole. Klientské omezení samo o sobě nestačí, protože požadavek lze odeslat jinou cestou než připraveným formulářem.

Předdefinované hodnoty nejsou připojeny k tabulce údajně naměřených vlastností. Aplikace zobrazuje jejich věcné vymezení a odkaz, ale neposkytuje automatické produktové skóre. Vlastní kritérium nebo alternativa se zadává názvem, popisem a volitelným odkazem. Stejný výpočetní mechanismus následně platí pro připravené i vlastní prvky. Rozšiřitelnost tak vychází ze struktury rozhodovacího modelu, nikoli ze zvláštního výpočetního kódu pro konkrétní produkt.

## 10.2 Uživatelský postup

Úvodní stránka nabízí vlastní hodnocení, syntetickou demonstraci a malý kontrolní příklad. Oddělením ukázky od vlastního hodnocení se snižuje riziko, že uživatel pouze převezme připravené preference. Při vlastní práci je nejprve vyplněn název a zvolen seznam položek. U každého kritéria je dostupný popis. Ten má pomoci zejména při rozlišení funkcionality modelování, generování DDL, zpětného načítání schématu a přenosu modelových souborů.

Na stránce porovnání jsou nejprve zadány preference kritérií. Poté následují alternativy vzhledem k jednotlivým kritériím. U každé dvojice je zobrazen plný název obou prvků a nabídka hodnot škály. Text nabídky odlišuje převahu prvního a druhého prvku. Uživatel tedy nemusí sám vytvářet dolní trojúhelník a nemůže omylem zadat obě směrová porovnání rozdílně. Při novém hodnocení zůstávají dvojice nevyplněné.

Výsledková stránka začíná pořadím a prioritami. Pod výsledkem jsou uvedeny váhy kritérií, CR matice kritérií a CR jednotlivých matic alternativ. Následuje tabulka lokálních priorit. Díky tomu lze rozlišit, zda je dobrý celkový výsledek způsoben převahou v důležitém kritériu, nebo vyrovnaným hodnocením v širší skupině hledisek. Souhrnné pořadí tak není jediným dostupným výstupem.

Při přítomnosti kritérií K8, K1 a K3 se zobrazí také příslušné varianty citlivosti. Každá varianta obsahuje přepočtené priority a pořadí. U jinak pojmenovaných vlastních kritérií není automaticky domýšleno, které z nich představuje cenu nebo modelování. Takový zásah by bez věcného vymezení mohl být zavádějící. Uživatel může změnit vlastní preference návratem do formuláře.

![Úvodní stránka vytvořené aplikace](outputs/bp_20260927/app_home.png)

Obrázek 1: Úvodní stránka místní PHP aplikace (vlastní zpracování; skutečný snímek vytvořené aplikace).

## 10.3 Kontrola vstupů a chybové stavy

Každá matice musí být čtvercová, úplná a kladná. Povolené hodnoty tvoří Saatyho škála a její převrácené hodnoty. Kontrola odmítá nulové hodnoty, záporné hodnoty, nečíselné údaje, nesprávnou diagonálu i porušení reciprocity. Hodnota mimo škálu není automaticky zaokrouhlena. Zaokrouhlením skutečného úsudku by se bez souhlasu hodnotitele změnil vstupní rozhodovací model.

Při importu se kromě matic kontrolují také počty kritérií a alternativ, identifikátory položek, délky textů a typ příznaku syntetických dat. Odkaz může být prázdný nebo musí používat schéma HTTP či HTTPS. Všechny texty jsou při zobrazení v HTML escapovány. Formuláře měnící stav používají token proti podvrženým požadavkům. Velikost importovaného dokumentu je omezena na jeden megabajt. Tato opatření nepředstavují úplný bezpečnostní audit, ale odstraňují základní rizika vyplývající ze způsobu zpracování vstupů.

Nekonzistence je odlišena od neplatného vstupu. Matice může být technicky platná, ale obsahovat vzájemně rozporné preference. V takovém případě lze váhy matematicky vypočítat, avšak výsledek musí být doprovázen upozorněním. Uživatel se může vrátit k porovnáním a posoudit příčinu. Program nikdy neopravuje vysoké CR nahrazením matice ideálně konzistentními poměry, protože tím by zanikl původní úsudek.

## 10.4 Uložení a reprodukovatelnost

Exportovaný dokument obsahuje vstupní položky, matice, příznak syntetických dat a odvozené výsledky. U připraveného dema je navíc uvedeno inicializační číslo generátoru a způsob tvorby matic. Hodnocení lze uložit do běžného souboru a znovu vložit do aplikace. Při opakovaném načtení se výsledky vypočítají z aktuálních vstupů. Tím je možné kontrolovat, že stejné preference vedou ke stejným výsledkům.

Kontrolní Excel obsahuje vzorce, nikoli jen předem vypsané priority. Horní trojúhelník tvoří upravitelné vstupy, spodní trojúhelník je dopočítán. Geometrické průměry, normalizace, součiny Aw a ukazatele konzistence jsou ponechány viditelné. Při změně vstupu se má přepočítat celý navazující řetězec. Samostatná tabulka etalonů v kontrolním příkladu obsahuje původní hodnoty pro srovnání; při změně matic se záměrně nemění.

Aplikace byla v rámci této verze spuštěna místně. Veřejné nasazení ani ověření na vzdáleném hostingu není tímto textem tvrzeno. Pro případné nasazení je určena veřejná složka public, zatímco data a výpočetní třídy zůstávají mimo ni. Po přenosu na hosting musí být zopakován kontrolní příklad. Lokální úspěch sám o sobě nepotvrzuje správné nastavení produkčního serveru.

# 11 Ověření výpočtů a funkčnosti

## 11.1 Rozsah ověření

Ověření bylo rozděleno na matematické jádro, tabulkový kontrolní výpočet a průchod webovými formuláři. V každé vrstvě byla sledována jiná možná příčina chyby. Kontrola matematického jádra ověřuje vzorce a okrajové případy. Kontrolní sešit umožňuje sledovat jednotlivé mezivýsledky. HTTP zkoušky ověřují, že jsou vstupy z formulářů skutečně zpracovány a že se správné výsledky dostanou k uživateli.

Pro ověření byl zvolen malý model se třemi kritérii F, P a C a třemi abstraktními alternativami A1, A2 a A3. Označení alternativ bylo sjednoceno v textu, aplikaci i sešitu, aby se kritérium C nezaměňovalo s třetí alternativou. Jde pouze o přejmenování; matice a číselné výsledky kontrolního příkladu se nemění. Tento příklad je odlišný od hodnocení databázových nástrojů. Nemá dokazovat vlastnosti produktů, ale správnost zvoleného výpočetního postupu. Jeho rozsah dovoluje nezávisle zkontrolovat každý prvek matice i každý krok syntézy. Podklady příkladu vycházejí z pracovního návodu AHP, ale hodnoty byly znovu vypočteny z původních matic bez převzetí zaokrouhlených součtů.

Za přijatelnou shodu byl pro automatickou kontrolu stanoven absolutní rozdíl nejvýše 10⁻⁹. Tento požadavek je přísnější než pracovní limit 0,001 uvedený v plánu projektu. Kontrolují se váhy, priority a CR, nejen výsledné pořadí. Shodné pořadí by samo o sobě nemuselo odhalit chybu, pokud by se jednotlivé priority změnily jen mírně.

## 11.2 Kontrolní příklad

Matice kritérií je tvořena řádky (1; 3; 5), (1/3; 1; 3) a (1/5; 1/3; 1). Geometrické průměry jsou přibližně 2,4662120743; 1; 0,4054801330. Po normalizaci získáme váhy 0,6369855717; 0,2582849944 a 0,1047294339. Matice není dokonale konzistentní. Odhad λ je 3,0385110906, CI je 0,0192555453 a CR je 0,0331992160. Pro zvolenou hranici je tedy konzistence přijatelná.

Tři lokální matice alternativ jsou zvoleny tak, aby byly dokonale konzistentní. V prvním kritériu mají alternativy váhy 4/7, 2/7 a 1/7. Ve druhém kritériu se prohodí preference A1 a A2. Ve třetím kritériu činí váhy 2/9, 1/9 a 6/9. Tím se ověřuje také správné přiřazení jednotlivých lokálních výsledků ke kritériím. Pokud by došlo k záměně pořadí kritérií nebo alternativ, projeví se chyba až při syntéze, i když by samotné lokální výpočty byly správné.

{{CONTROL_TABLE}}

Tabulka 6: Přepočtený kontrolní příklad; vstupy jsou abstraktní, nikoli měření produktů (vlastní výpočet).

Výsledné pořadí kontrolního příkladu je A1, A2, A3. Příklad potvrzuje shodu konkrétní implementace se specifikovaným postupem, nikoli univerzální správnost jakéhokoli rozhodovacího modelu. K úplnému ověření je potřeba i zkouška chybových vstupů a výpočtů, ve kterých je konzistence záměrně nízká.

## 11.3 Automatické a tabulkové kontroly

V PHP testu bylo provedeno 146 kontrol. Porovnány byly kontrolní i syntetické matice s nezávislým referenčním výpočtem v Pythonu. Největší zaznamenaný absolutní rozdíl činil přibližně 1,78 × 10⁻¹⁵. Rozdíl odpovídá úrovni numerické přesnosti a je výrazně nižší než stanovená tolerance. Byly zahrnuty i součty vah, citlivost, shodná pořadí, rozměry jedna a dvě a odmítnutí neplatných vstupů.

Oba sešity byly vytvořeny s výpočetními vzorci a následně přepočteny v LibreOffice Calc. Při kontrole přepočtených buněk nebyly zjištěny chybové hodnoty vzorců. Výsledky kontrolního i demonstračního běhu odpovídaly nezávislým etalonům v toleranci 10⁻⁹. Kontrola změny vstupu dále ověřila, že změna párové preference vyvolá změnu váhy. Nejde tedy pouze o zobrazení uloženého výsledku bez funkční návaznosti vzorců.

| Skupina zkoušek | Očekávané chování | Zjištěný stav |
|---|---|---|
| Kontrolní příklad | Shoda vah, CR a priorit s referencí | Splněno v automatické kontrole |
| Syntetický model 8 × 4 | Shoda základního běhu i tří citlivostí | Splněno v automatické kontrole |
| Platná konzistentní matice | CR numericky rovné nule | Splněno |
| Záměrně nekonzistentní matice | Výpočet a současně varování | Splněno přes HTTP |
| Neúplná či neplatná matice | Odmítnutí s chybovým hlášením | Splněno |
| Vlastní kritérium a alternativa | Zařazení do modelu a přepočet | Splněno přes formulář |
| Export a import | Obnovení vstupů a shodný výsledek | Splněno |
| Osobní ruční přepočet autora | Nezávislá kontrola podle vzorců | Dosud neproveden v této verzi |
| Odborná kontrola vedoucím | Vlastní kontrola vedoucího | Není zde doložena |
| Jiná specializovaná AHP aplikace | Porovnání při shodné metodě | Zůstává k provedení |

Tabulka 7: Rozsah ověření aplikace (vlastní zpracování podle skutečně spuštěných zkoušek).

## 11.4 Ověření rozhraní a omezení důkazu

Přes HTTP bylo provedeno 14 zkoušek. Zahrnují načtení dema a kontrolního příkladu, získání výsledků exportem, import, vlastní položky a odpovědi na chybné vstupy. V prohlížeči Chrome byl dále ověřen počet 76 dvojic modelového případu, změna preference a následný přepočet. Snímky rozhraní zachycují skutečně spuštěnou aplikaci. Na úvodní stránce byla ověřena také mobilní šířka 390 pixelů bez vodorovného přetečení.

Tyto zkoušky neznamenají, že bylo provedeno uživatelské šetření použitelnosti. Prohlížečová automatizace ověřuje průchod a zobrazení, nikoli to, zda běžný uživatel správně porozumí všem rozhodovacím krokům. K takovému závěru by bylo potřeba pozorovat uživatele, zaznamenat jeho postup a vyhodnotit konkrétní obtíže. Stejně tak nebylo provedeno měření výkonu při souběhu mnoha relací ani bezpečnostní audit veřejně nasazeného systému.

Automatické kontroly připravené s pomocí AI jsou užitečným vývojovým důkazem, ale nenahrazují osobní nezávislý přepočet. Proto zůstává v pracovním postupu samostatný krok, ve kterém budou matice znovu zadány do kontrolního sešitu a zkontrolovány autorem. Výsledek kontroly jinou specializovanou aplikací musí být doplněn včetně jejího názvu, verze, zvolené metody a případných rozdílů. Bez těchto údajů by samotné tvrzení o externím ověření nebylo reprodukovatelné.

# 12 Demonstrace na modelovém případu Cykloservis

## 12.1 Rozhodovací situace

Modelovým případem je návrh databáze menšího cykloservisu. Rozhodovatel vystupuje v roli vývojáře, který vybírá nástroj pro návrh a vývoj databázového systému ještě před definitivním výběrem DBMS. Výběr se týká modelovacího a vývojového nástroje, nikoli provozního databázového serveru. Požadavky na zálohování, správu uživatelů serveru nebo výkonnost SQL dotazů proto nejsou samostatnými kritérii hodnocení.

Cykloservis eviduje zákazníky, jejich kola, servisní zakázky, zaměstnance, použité služby, spotřebované díly, dodavatele a faktury. U položek zakázky se uchovává cena platná při opravě. Nestačí odkazovat pouze na současnou ceníkovou cenu, která se může později změnit. Pracovní sešit rozšiřuje původní desetientitní zadání o elektrokolo. Pro tuto pracovní verzi se používá právě tento podrobnější model s jedenácti tabulkami, aby odpovídal současným 51 testovacím blokům.

| Tabulka | Účel v modelu | Významná vlastnost pro test |
|---|---|---|
| zakaznik | Evidence zákazníků | Samostatný PK, unikátní e-mail |
| kolo | Kola zákazníka | FK na zákazníka, unikátní sériové číslo |
| elektrokolo | Rozšíření vybraného kola | Jeden sloupec současně PK a FK |
| zamestnanec | Mechanici | Vazba na zakázky |
| zakazka | Servisní případ | Nepovinný mechanik, stav a časové údaje |
| sluzba | Katalog servisních úkonů | Cena a omezení číselných hodnot |
| dil | Skladovaný materiál | Množství a vazba na dodavatele |
| dodavatel | Dodavatelé dílů | Samostatná evidence |
| zakazka_sluzba | Služby konkrétní zakázky | Složený PK a historická cena |
| zakazka_dil | Spotřebované díly zakázky | Složený PK, množství a historická cena |
| faktura | Faktura k zakázce | Vlastní PK a unikátní FK |

Tabulka 8: Rozsah modelového případu podle listu Model a pravidla (vlastní zpracování).

Vztah zakázky a faktury je z pohledu zakázky 1 ku 0..1: zakázka může existovat před vystavením faktury, ale nemá mít více faktur. Podobně může kolo existovat bez záznamu elektrokola. Tyto konstrukce jsou v relačním schématu vyjádřeny odlišně. Faktura má vlastní identifikátor a unikátní cizí klíč na zakázku. Elektrokolo používá identifikátor kola současně jako primární i cizí klíč. Testování proto nemá skončit zjištěním, že nástroj umí nakreslit čáru označenou 1:1; musí být ověřeno skutečné omezení v modelu a v DDL.

## 12.2 Jednotný postup praktických testů

Pro každý ze čtyř nástrojů je určeno stejné zadání. Nejprve má být vytvořen model od začátku, bez importu připraveného výsledku. Následuje generování DDL z vlastního modelu, jeho spuštění a kontrola omezení. Poté se z referenční databáze provede reverse engineering. Poslední skupinou úloh je přenos modelu nebo diagramu a ověření doplňujících podkladů pro kompatibilitu, dokumentaci a licenci.

Jednotnost postupu neznamená, že musí všechny produkty používat totožné názvy nabídek nebo zcela stejnou posloupnost kliknutí. Srovnává se splnění stejného věcného požadavku. Pokud edice samostatný model nepodporuje a vyžaduje živou databázi, musí být tato okolnost zaznamenána. Postup založený na úpravě existujícího schématu nesmí být označen za úspěšné offline modelování. Stejně tak nelze zaměnit tisk diagramu do PDF za nativní export jeho datové struktury.

Pomocné známky používají škálu od jedné do pěti. Jednička představuje bezproblémové splnění, pětka nepodporovanou nebo nefunkční možnost. Známka však nezachycuje vše, co je pro rozhodnutí podstatné. Musí být doplněna popisem postupu, omezení a důkazem. Stejné číslo může vzniknout kvůli chybějící funkci, licenčnímu omezení nebo obtížnému ovládání; význam těchto situací pro jednotlivá kritéria se liší.

Při převodu podkladů do AHP se nebude používat prostý průměr všech 51 známek. Kritéria nejsou zastoupena stejným počtem úloh a některé podbody pouze rozepisují vytvoření jednotlivých tabulek. Průměr by tak přidělil větší význam kritériu jen proto, že bylo podrobněji rozděleno. Úlohy mají sloužit jako důkazy pro věcné shrnutí K1–K8 a následné zdůvodnění jednotlivých párových preferencí.

## 12.3 Původ a vytvoření syntetických vstupů

**Výsledky v této kapitole jsou založeny výhradně na syntetických datech. Testy databázových nástrojů nebyly pro tento běh provedeny.** Byly připraveny dvě samostatné sady vstupů. První sada obsahuje náhodné pomocné známky pro 51 testovacích bloků a čtyři nástroje, tedy 204 známek. Druhá sada obsahuje párovou matici osmi kritérií a osm párových matic čtyř alternativ. Pomocné známky nebyly automaticky převedeny na Saatyho škálu.

Generátor používá inicializační číslo 20260927. Nejprve jsou náhodně vytvořeny pomocné latentní preference. Jejich poměry jsou mírně změněny náhodnou odchylkou a následně přiblíženy k nejbližší hodnotě Saatyho škály podle logaritmické vzdálenosti. Přijaty jsou pouze matice s CR nejvýše 0,10. Účelem je získat přehledný demonstrační příklad s přijatelnou konzistencí. Nejde o simulaci skutečného chování produktů ani o odhad úsudku budoucího hodnotitele.

Omezení generátoru na nízké CR se nesmí použít k manipulaci reálných výsledků. Skutečná nekonzistentní preference se musí znovu věcně posoudit, nikoli zahodit a nahradit náhodnou hodnotou, která projde kontrolou. Obdobně se při pozdějších testech nesmějí dodatečně vymýšlet důkazy odpovídající již hotové matici. Pořadí skutečné práce je opačné: nejprve pozorování, poté jejich interpretace a až následně párové preference.

K náhodným známkám nebyly přiřazeny údajné naměřené časy, smyšlené verze nástrojů, ceny nebo výpisy chyb. Všechny záznamy nesou označení, že test nebyl proveden. Díky tomu lze zkušební tabulky využít pro přípravu zpracování a současně zachovat hranici mezi návrhem experimentu a jeho skutečným provedením.

## 12.4 Váhy kritérií a lokální priority

{{CRITERIA_TABLE}}

Tabulka 9: Váhy kritérií a konzistence v syntetickém běhu (vlastní výpočet ze syntetických vstupů).

{{CRITERIA_COMMENT}}

{{LOCAL_TABLE}}

Tabulka 10: Lokální priority alternativ v syntetickém běhu (vlastní výpočet ze syntetických vstupů).

Lokální priority umožňují vysvětlit následnou syntézu. Každý sloupec tvoří samostatné porovnání čtyř alternativ vzhledem k jednomu kritériu. Součet v každém sloupci je roven jedné. Údaje v tabulce nepředstavují skutečnou funkcionalitu nástrojů; jsou matematickým důsledkem náhodných preferencí. Nesmí z nich být vyvozováno například tvrzení, že konkrétní produkt prokazatelně nabízí nejlepší dokumentaci nebo nejnižší náklady.

## 12.5 Výsledná syntéza

{{RANKING_TABLE}}

Tabulka 11: Výsledné pořadí syntetické demonstrace (vlastní výpočet; nejde o doporučení produktů).

{{RANKING_COMMENT}}

Součet globálních priorit činí jednu. Zaokrouhlené hodnoty zobrazené v tabulkách se mohou při součtu nepatrně lišit, protože jsou uvedeny pouze čtyři desetinná místa. V samotném výpočtu se zaokrouhlené údaje nepoužívají. Všechna čísla této kapitoly jsou odvozena ze stejného vstupního dokumentu jako připravené demo v aplikaci a sešit syntetického hodnocení.

![Výsledek syntetického příkladu v aplikaci](outputs/bp_20260927/app_results.png)

Obrázek 2: Výsledky syntetických vstupů v místně spuštěné aplikaci (vlastní zpracování).

## 12.6 Tři samostatné změny důležitosti kritérií

{{SENSITIVITY_TABLE}}

Tabulka 12: Priority při odděleném zesílení K8, K1 a K3 (vlastní výpočet ze syntetických vstupů).

{{SENSITIVITY_COMMENT}}

Zkoušky citlivosti neprokazují odolnost výsledku vůči všem možným změnám. Sledují pouze tři předem vymezené zásahy. Při změně více vah současně, přidání alternativy nebo odlišném lokálním hodnocení by mohl být výsledek jiný. Pro danou práci je však zvolený rozsah přehledný a přímo navazuje na otázku rozpočtu, kvality modelování a flexibility vůči DBMS. Po získání skutečných výsledků se mají provést stejné zásahy, nikoli vybrat pouze ty, které povedou k zajímavé změně vítěze.

## 12.7 Nahrazení zkušebních údajů skutečnými výsledky

Nahrazení syntetických dat musí proběhnout v několika navazujících vrstvách. Nejprve budou doplněny přesné edice, verze a podmínky testování. Následně budou vykonány úlohy podle společného zadání a uložen odpovídající důkaz. Až z těchto záznamů budou vytvořena věcná shrnutí jednotlivých kritérií. Význam kritérií se stanoví podle rozhodovací situace a preference alternativ podle doložených vlastností.

Samotná výměna čísel v tabulce výsledného pořadí není dostačující. Musí být nahrazeny vstupní párové matice, znovu ověřena jejich konzistence a přepočteny všechny navazující tabulky. Změní se také slovní komentář k vahám, lokálním prioritám, pořadí a citlivosti. Pokud reálné údaje nepodpoří některé předběžné vysvětlení, musí být změněno vysvětlení, nikoli data.

Nakonec bude proveden osobní kontrolní přepočet a bude doplněno srovnání s dalším AHP nástrojem. V textu musí být zachováno rozlišení mezi vývojovým testem programu a odborným hodnocením databázových produktů. První úloha je v této verzi podložena skutečnými automatickými zkouškami. Druhá úloha zůstává připravena k provedení, i když již existují pracovní tabulky, výpočty a interpretační struktura.

# 13 Diskuse výsledků a omezení

## 13.1 Přínos vytvořeného řešení

Hlavním dosavadním přínosem je propojení rozhodovacího modelu, výpočetního postupu a uživatelského rozhraní. Připravené seznamy usnadňují založení úlohy, vlastní položky dovolují přizpůsobit její rozsah a automatické reciproční hodnoty snižují riziko technické chyby při zadávání. Výsledková stránka zobrazuje nejen pořadí, ale také váhy a ukazatele konzistence. Uživatel tak získává podklady pro kontrolu toho, jak výsledek vznikl.

Propojení teorie s implementací se projevuje zejména v nutnosti výslovně stanovit způsob výpočtu vah, použitou tabulku RI, numerickou toleranci a chování při nekonzistenci. Obecný popis AHP pro implementaci sám o sobě nestačí. Nejednoznačnost v jednom z těchto bodů by mohla vést k odlišným výstupům aplikace a kontrolního sešitu, přestože by oba nástroje byly označeny jako AHP.

Využití párového porovnávání mimo oblast databázových nástrojů dokládá například práce Vlčkové a Friebela (2015), která používá AHP ke stanovení vah kritérií kvality účetních dat. Z takového příkladu lze převzít princip explicitního vymezení kritérií a jejich významu. Nelze však převzít konkrétní váhy do jiného rozhodovacího problému. Pro tuto práci musí význam kritérií vycházet z požadavků vývojáře na nástroj, nikoli z výsledků jiné aplikační oblasti.

## 13.2 Vztah k odborné literatuře

Studie Carvalho et al. (2022) tvoří podklad výběru nástrojů a členění sledovaných vlastností. Její výsledky však nelze mechanicky ztotožnit s výsledkem vytvořeného modelu. Liší se soubor alternativ, vymezení kritérií, případně edice produktů i postup při stanovení vah. Shodné první místo by samo o sobě nebylo důkazem správnosti nové komparace a odlišné pořadí by nebylo automaticky rozporem. Nejprve by bylo nutné porovnat metodické podmínky.

V syntetické verzi nelze ani takové věcné srovnání výsledků provést. Názvy produktů jsou zde spojeny s náhodnými preferencemi. Jediné oprávněné srovnání s literaturou se týká způsobu sestavení hierarchie, významu párového porovnávání a transparentnosti výpočtu. Empirická diskuse o tom, proč se jednotlivé produkty umístily na určitém místě, musí vycházet až ze skutečných testovacích protokolů.

Feinberg (2017) nahlíží na vytváření dat jako na soubor návrhových činností závislých na kontextu. V této práci je tato souvislost patrná při volbě toho, co se vůbec zaznamenává do protokolu. Počet kroků, dostupnost funkce nebo potřeba obchvatu nevznikají jako vzájemně zaměnitelné údaje. Jejich význam závisí na zadání úlohy a na způsobu pozorování. Proto musí být popsána pravidla zápisu i hranice mezi pozorováním a následným úsudkem hodnotitele.

## 13.3 Metodická omezení

Zásadním omezením pracovních výsledků je syntetický původ produktových hodnocení. Připravené pořadí nelze použít jako doporučení nástroje pro praxi. Má význam pouze jako demonstrace funkčního zpracování vstupů. Nízká hodnota CR na tom nic nemění. Náhodné poměry mohou být vnitřně soudržné, a přesto nemají žádný vztah ke skutečným vlastnostem alternativ.

Při budoucím skutečném hodnocení zůstane omezením jeden hodnotitel. Jeho předchozí zkušenosti s jednotlivými nástroji mohou ovlivnit rychlost práce, četnost chyb i vnímanou srozumitelnost prostředí. Jednotné zadání a podrobný protokol toto omezení zpřehledňují, ale neodstraňují. Výsledek bude nutné vztahovat ke konkrétnímu rozhodovateli a modelovému případu. Nelze jej vydávat za reprezentativní průzkum všech uživatelů.

Dalším omezením je časová proměnlivost produktů. Funkce, licence a dostupnost sestavení se mohou měnit. Z tohoto důvodu musí být každé reálné tvrzení svázáno s edicí, verzí a datem zjištění. Zvláště u K8 je nutné rozlišit licenci zdrojového kódu, cenu připraveného sestavení a omezení zkušební varianty. V jedné tabulce se nesmějí bez vysvětlení kombinovat vlastnosti různých edic.

Výběr DBMS také ovlivňuje interpretaci kompatibility. Nástroj specializovaný na jednu platformu může podrobně podporovat její specifické vlastnosti, zatímco univerzální produkt může poskytovat širší připojitelnost. V K3 se proto nesleduje pouze počet ovladačů, ale podpora skutečně zkoumaných návrhových úkonů. Hodnocení musí oddělit šíři podpory od hloubky práce s jednou platformou a nesmí stejnou výhodu opakovaně započítat do více kritérií bez věcného zdůvodnění.

Matematickým omezením je použití geometrických vah a odhadu λ pro kontrolu konzistence. Tento postup je přesně popsán a reprodukován ve všech vytvořených výstupech. Při jiném algoritmu může dojít k drobným rozdílům. Výsledky jsou navíc závislé na souboru alternativ a na definici kritérií. AHP neposkytuje náhradu za odborné posouzení toho, zda byl rozhodovací problém správně vymezen.

## 13.4 Možnosti dalšího rozvoje

Prvním krokem dalšího rozvoje je dokončení skutečného modelového ověření a osobní kontroly výpočtů. Teprve poté lze posoudit, zda uživatelské rozhraní dostatečně podporuje zamýšlený pracovní postup. Praktické připomínky mohou vést například k doplnění orientace v již vyplněných dvojicích, k lepšímu uchování rozepsaného formuláře nebo k přehlednějšímu vysvětlení problematických preferencí.

Pro dlouhodobější používání by bylo možné doplnit ukládání historie hodnocení, porovnání více uložených verzí a evidenci podkladů přímo u jednotlivých párů. Takové rozšíření by zvýšilo dohledatelnost úsudků. Muselo by však mít jasně navrženou správu dat a nemělo by vést k automatickému vytváření produktových tvrzení bez důkazů. Možnost přidávat jiné sady kritérií a alternativ již vychází z datové struktury, samostatný katalog více rozhodovacích oblastí ale nebyl implementován.

Uživatelské testování lze provést s několika osobami, které dostanou stejný kontrolní příklad a konkrétní úkol. Sledovat by se mělo zejména porozumění směru preference, rozlišení vah a lokálních priorit a reakce na vysoké CR. Cílem takové zkoušky by bylo ověřit srozumitelnost aplikace, nikoli získat skupinové hodnocení databázových nástrojů. Skupinová AHP není součástí vymezeného rozsahu této práce.

# 14 Závěr – pracovní znění pro syntetickou verzi

Cílem práce je návrh a vytvoření webové aplikace pro podporu výběru nástrojů určených pro návrh a vývoj databázových systémů pomocí metody AHP. Na základě teoretických východisek byly vymezeny čtyři alternativy a osm kritérií. Byl navržen datový model hodnocení, specifikován jednotný výpočetní postup a vytvořena PHP aplikace umožňující volbu připravených i vlastních položek, zadávání párových preferencí, výpočet priorit a kontrolu konzistence.

Výpočetní část byla ověřena automatickým srovnáním s nezávislým referenčním výpočtem a s kontrolními tabulkovými vzorci. Provedené zkoušky zahrnuly také chybná zadání, nekonzistentní matice a průchod webovými formuláři. Výsledky podporují závěr, že vytvořená implementace na ověřených případech odpovídá popsanému algoritmu. Nedokládají však správnost dosud neprovedených testů databázových produktů ani použitelnost aplikace pro všechny skupiny uživatelů.

Demonstrace na Cykloservisu ukázala zpracování rozhodovacího modelu s osmi kritérii, čtyřmi alternativami a třemi samostatnými změnami vah. Pro tuto pracovní verzi byla použita syntetická data. Vypočtené pořadí proto slouží k demonstraci postupu a nebude použito jako závěrečné doporučení konkrétního nástroje. Skutečná komparace bude vyžadovat provedení sjednocených testů, doložení preferencí a novou interpretaci výsledků.

Před konečným uzavřením práce zbývá osobní nezávislý přepočet, srovnání s další specializovanou aplikací a ověření modelového případu skutečnými údaji. Na těchto podkladech bude upraven také závěr, abstrakt a diskuse. Připravené řešení již poskytuje výpočetní i textovou strukturu pro dokončení těchto kroků. Za dokončený empirický výsledek ani za finální odevzdávanou verzi však tuto syntetickou demonstraci nelze považovat.

[Pracovní poznámka pro autora: tuto závěrečnou kapitolu po reálných testech dopište podle skutečného naplnění cíle, výsledků, omezení a přínosu. Náhodné pořadí samo o sobě není závěr o kvalitě produktů.]
