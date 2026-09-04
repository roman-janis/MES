# Rozhodnutí o podobě praktické části bakalářské práce

Aktualizace: 1. 9. 2026.

Stav: pracovní podklad pro rozhodnutí a konzultaci s vedoucím. Žádná varianta zatím není schválena a podle zvolené varianty bude nutné upravit cíl, osnovu a zadávací list ve STAGu.

## Výchozí otázka vedoucího

Vedoucí navrhl dvě vzájemně odlišné možnosti praktické části:

1. vytvořit univerzální aplikaci, ve které si uživatel zadá vlastní kritéria a alternativy a provede jejich porovnání metodou AHP;
2. neprogramovat univerzální aplikaci, ale zpracovat tři konkrétní případy užití, pro které budou pomocí AHP vyhodnocena kritéria a nástroje.

Současný pracovní plán kombinuje programování aplikace se dvěma scénáři. Před pokračováním je proto potřeba vybrat jeden hlavní směr a nechat jej potvrdit vedoucím.

## Základní porovnání variant

| Oblast | Varianta 1 - univerzální AHP aplikace | Varianta 2 - tři případy užití |
|---|---|---|
| Hlavní praktický výstup | Funkční webová aplikace pro vlastní kritéria, alternativy a párová porovnání. | Tři kompletní AHP modely pro rozdílné uživatele nebo organizace. |
| Těžiště práce | Analýza požadavků, návrh architektury, implementace algoritmu, uživatelské rozhraní a testování. | Návrh scénářů, zdůvodnění preferencí, vyplnění matic, interpretace a porovnání výsledků. |
| Role programování | Hlavní část praktické práce. | Není nutné; výpočty mohou být v kontrolovatelném Excelu. |
| Role scénářů | Jeden věrohodný příklad může sloužit k předvedení a ověření aplikace. Přesný rozsah musí potvrdit vedoucí. | Tři scénáře jsou hlavním předmětem praktické části. |
| Role databázových nástrojů | Nástroje a kritéria představují demonstrační a ověřovací případ aplikace. Jejich hodnocení stále musí být doložené. | Vlastnosti nástrojů a jejich vhodnost pro jednotlivé scénáře jsou hlavním výsledkem práce. |
| AHP výpočty | Musí být správně implementovány v kódu a ověřeny automatickými i kontrolními testy. | Mohou být provedeny v Excelu, ale všechny matice, váhy a CR musí být doloženy. |
| Co se bude hlavně psát | Požadavky, návrh řešení, datový model, architektura, algoritmus, implementace, testování a validace. | Popis scénářů, důvody párových hodnocení, výsledky, citlivost a doporučení pro praxi. |
| Hlavní riziko | Příliš široký rozsah aplikace nebo nedostatečné otestování matematické správnosti. | Velké množství subjektivních porovnání a opakující se interpretace tří scénářů. |
| Využití současných podkladů | Lze využít teorii AHP, kontrolní příklad, kritéria K1-K8, čtyři nástroje a část testu Cykloservisu. Praktické kapitoly se však musí výrazně přepracovat. | Přímo navazuje na současnou strukturu BP, test Cykloservisu a připravené praktické kapitoly. |
| Vhodnost pro autora | Vysoká: autor pracuje jako PHP programátor a ve škole používá Javu a Spring. | Nižší: více práce spočívá ve formulaci a interpretaci scénářů než v programování. |
| Obhajoba | Ukázka funkční aplikace, vysvětlení architektury a důkaz správnosti výpočtů. | Obhajoba voleb v jednotlivých scénářích, matic, konzistence a výsledných doporučení. |

## Varianta 1 - univerzální AHP aplikace

### Co by bylo cílem

Navrhnout a implementovat webovou aplikaci, která umožní uživateli vytvořit vlastní rozhodovací úlohu, zadat kritéria a alternativy, provést párová porovnání metodou AHP a získat kontrolovatelný výsledek včetně upozornění na nekonzistentní vstupy.

Možná formulace cíle práce:

> Cílem práce je navrhnout a implementovat webovou aplikaci pro univerzální porovnávání alternativ metodou AHP a její správnost a použitelnost ověřit na komparaci vybraných nástrojů pro návrh a vývoj databázových systémů.

Možný upravený název:

> Návrh a implementace aplikace pro komparaci nástrojů pro návrh a vývoj databázových systémů s využitím AHP

Anglická varianta:

> Design and Implementation of an Application for Comparing Database Design and Development Tools Using AHP

### Minimální funkční rozsah aplikace

| Oblast | Požadovaná funkce | Důvod |
|---|---|---|
| Rozhodovací projekt | Vytvořit projekt a pojmenovat jeho cíl. | Uživatel musí vědět, jaké rozhodnutí provádí. |
| Kritéria | Přidat, upravit a odebrat vlastní kritéria. | Aplikace má být univerzální. |
| Alternativy | Přidat, upravit a odebrat vlastní alternativy. | Aplikace nesmí být pevně svázána se čtyřmi databázovými nástroji. |
| Matice kritérií | Automaticky vytvořit párovou matici kritérií. | Z matice vzniknou váhy kritérií. |
| Matice alternativ | Pro každé kritérium vytvořit párovou matici alternativ. | Získají se lokální preference alternativ. |
| Zadávání hodnot | Nabídnout Saatyho škálu 1-9 a převrácené hodnoty. | Omezí se neplatné vstupy a chyby uživatele. |
| Reciprocita | Po zadání hodnoty automaticky doplnit převrácenou hodnotu. | Matice musí být reciproční. |
| Výpočet vah | Vypočítat geometrické průměry a normalizované váhy. | Základní výpočet používaný v připraveném návodu. |
| Konzistence | Vypočítat lambda max, CI, RI a CR. | Uživatel musí poznat, zda jsou jeho úsudky přijatelné. |
| Validace | Upozornit na neúplnou matici, neplatnou hodnotu nebo CR >= 0,1. | Vedoucí výslovně zdůraznil chybové hlášky a správné používání AHP. |
| Syntéza | Vypočítat globální skóre a pořadí alternativ. | Jde o konečný výsledek rozhodování. |
| Výsledky | Zobrazit váhy, CR, pořadí a přehledný graf. | Výsledek musí být srozumitelný i běžnému uživateli. |
| Uložení | Uložit projekt a později jej znovu otevřít. | U většího počtu matic nelze spoléhat na dokončení v jednom kroku. |
| Export | Exportovat výsledky alespoň do přehledného tiskového nebo datového formátu. | Výsledek musí být použitelný jako doklad nebo příloha. |

Univerzální aplikace nemusí znamenat neomezený počet prvků. Lze stanovit a zdůvodnit bezpečný rozsah, například 2-10 kritérií a 2-10 alternativ. Vyšší počet by vedl k velmi velkému množství párových porovnání a vyžadoval by další hodnoty RI.

### Co by bylo vhodné doplnit, pokud zbude prostor

| Rozšíření | Význam | Priorita |
|---|---|---|
| Analýza citlivosti | Uživatel změní váhu kritéria a sleduje změnu pořadí. | Vysoká, pokud zůstane v cíli práce. |
| Více hodnocení jednoho projektu | Umožní porovnat názory více uživatelů nebo scénářů. | Střední. |
| Import a export projektu | Usnadní přenos a kontrolu vstupních dat. | Střední. |
| Uživatelské účty | Oddělí projekty různých uživatelů. | Nízká; pro bakalářskou práci nemusí být nutné. |
| Administrace | Správa uživatelů nebo veřejných šablon. | Nízká; hrozí odklon od hlavního cíle. |

### Doporučené technické varianty

| Technologie | Výhody | Nevýhody | Hodnocení pro tuto práci |
|---|---|---|---|
| Java + Spring Boot + serverově vykreslené webové rozhraní | Navazuje na výuku, dobře se testuje pomocí jednotkových testů, jasné rozdělení vrstev a vhodné téma pro popis architektury. | Více počáteční konfigurace a nutnost upevnit znalosti Springu. | Preferovaná varianta, pokud má práce ukázat také rozvoj znalostí ze školy. |
| PHP + běžný webový framework | Navazuje na profesní zkušenost, rychlejší implementace a menší riziko, že vývoj zablokuje neznalost technologie. | Pokud autor pracuje hlavně s legacy PHP, je nutné uhlídat moderní strukturu, automatické testy a oddělení výpočtové logiky od rozhraní. | Bezpečnější varianta z hlediska rychlosti dokončení. |
| Spring Boot REST API + samostatný JavaScript frontend | Výrazné oddělení backendu a frontendu a moderní architektura. | Dvě aplikace, více integrační práce a vyšší riziko zbytečného rozšíření rozsahu. | Použít jen tehdy, pokud je samostatný frontend součástí záměru, ne pouze kvůli dojmu modernosti. |

Pracovní preference: **Java a Spring Boot**, protože navazují na školní výuku a umožní v práci dobře popsat architekturu a automatické testování. **PHP** zůstává rozumnou záložní volbou díky profesní zkušenosti. Konkrétní technologii není nutné slíbit vedoucímu dříve, než potvrdí rozsah aplikace.

### Co by se muselo otestovat

| Typ testu | Příklad |
|---|---|
| Jednotkové testy výpočtů | Geometrický průměr, normalizace vah, lambda max, CI, CR a syntéza. |
| Kontrolní matematický příklad | Výsledky aplikace musí odpovídat ručně spočítanému příkladu v `AHP_NAVOD_SAATY.md`. |
| Test nekonzistentní matice | Aplikace musí správně rozpoznat CR >= 0,1 a srozumitelně upozornit uživatele. |
| Test validačních pravidel | Neúplná matice, neplatná hodnota, příliš málo kritérií nebo alternativ. |
| Integrační test | Uložení projektu, jeho opětovné načtení a zachování výsledků. |
| Uživatelský průchod | Vytvoření celého rozhodnutí od založení projektu po výsledné pořadí. |
| Ověřovací případ z tématu BP | Jedno doložené porovnání čtyř databázových nástrojů podle finalizovaných kritérií. |

### Co by se změnilo v psaní práce

Programátorská varianta neznamená méně psaní, ale jiné kapitoly. Místo podrobného rozboru tří scénářů by bylo nutné popsat zejména:

1. analýzu existujících AHP aplikací a jejich nedostatků;
2. funkční a nefunkční požadavky;
3. případy užití aplikace;
4. návrh architektury, databáze a doménového modelu;
5. implementaci výpočetního modulu AHP;
6. řešení validací, chybových stavů a uživatelského rozhraní;
7. automatické a uživatelské testování;
8. ověření aplikace na porovnání databázových nástrojů;
9. omezení řešení a možné další rozšíření.

### Výhody varianty 1

| Výhoda | Konkrétní přínos |
|---|---|
| Odpovídá zkušenostem autora | Programování je bližší než rozsáhlá interpretace tří subjektivních scénářů. |
| Jasný praktický výstup | U obhajoby lze předvést fungující aplikaci. |
| Dobře prokazatelná vlastní práce | Zdrojový kód, návrhová rozhodnutí a testy jsou dohledatelné. |
| Opakovaná použitelnost | Aplikace může řešit jiné rozhodovací problémy než pouze databázové nástroje. |
| Lepší prostor pro softwarové inženýrství | Lze popsat architekturu, datový model, testovatelnost, validace a uživatelské rozhraní. |
| Navazuje na podklady vedoucího | Starý návrh rozhraní ukazuje směr, ale ponechává prostor pro vlastní dokončenou implementaci. |

### Nevýhody a rizika varianty 1

| Riziko | Jak je omezit |
|---|---|
| Aplikace přeroste do příliš velkého systému. | Předem stanovit minimální funkční rozsah a nepřidávat administraci nebo složitá oprávnění bez důvodu. |
| Výpočty budou fungovat jen na jednom příkladu. | Oddělit výpočetní modul od UI a otestovat různé velikosti matic. |
| Matematická chyba znehodnotí výsledek. | Použít kontrolní příklady, automatické testy a nezávislou kontrolu výsledků. |
| Práce se odchýlí od komparace databázových nástrojů. | Zachovat jedno věrohodné a doložené porovnání nástrojů jako případovou studii. |
| Přepis současné praktické struktury. | Nejdříve získat potvrzení vedoucího, teprve potom upravovat BP a plán. |
| Příliš mnoho času na vzhled aplikace. | Upřednostnit správnost, použitelnost a chybové hlášky před složitým frontendem. |

## Varianta 2 - tři případy užití

### Co by bylo cílem

Finalizovat kritéria a alternativy a na základě jednoho společného praktického testu sestavit tři AHP modely pro rozdílné uživatele nebo organizace. Každý případ užití by měl vlastní priority a mohl by vést k jinému pořadí databázových nástrojů.

### Možné případy užití

| Případ užití | Typické priority |
|---|---|
| Student nebo samostatný vývojář | Nízké náklady, snadné použití, dokumentace a dostatek funkcí. |
| Střední firma | Automatizace, forward a reverse engineering, exporty a začlenění do vývojového procesu. |
| Velká organizace | Široká kompatibilita, funkcionalita, dokumentace, dodavatelská podpora a licenční podmínky. |

### Co by tato varianta obnášela

1. dokončit stejný praktický test všech čtyř databázových nástrojů;
2. opravit a sjednotit záznamy K1-K8 včetně důkazů a skóre;
3. přesně popsat tři modelové uživatele a jejich požadavky;
4. sestavit tři matice významu kritérií;
5. sestavit a zdůvodnit matice alternativ vzhledem ke kritériím;
6. vypočítat váhy, lambda max, CI, CR a výsledná pořadí;
7. provést analýzu citlivosti;
8. porovnat výsledky scénářů a formulovat doporučení.

### Výhody varianty 2

| Výhoda | Konkrétní přínos |
|---|---|
| Menší technické riziko | Není nutné vyvíjet a ladit samostatnou aplikaci. |
| Přímá návaznost na současnou BP | Velká část praktické struktury, Cykloservis a kritéria jsou připravené. |
| Jasná vazba na název práce | Hlavním výsledkem zůstává komparace databázových nástrojů. |
| Snadnější kontrola rozsahu | Výstupy jsou předem známé: matice, váhy, CR, pořadí a interpretace. |
| Vhodné pro AHP | Varianta dobře ukazuje subjektivitu vah a změnu výsledků podle požadavků uživatele. |

### Nevýhody a rizika varianty 2

| Riziko | Jak je omezit |
|---|---|
| Velké množství subjektivních úsudků. | U každého porovnání uchovat slovní důvod a vazbu na praktický test. |
| Scénáře mohou působit uměle. | Přesně popsat jejich potřeby a nevymýšlet vlastnosti bez podkladu. |
| Opakující se text a tabulky. | Úplné matice dát do příloh a v hlavním textu vysvětlit pouze rozhodující rozdíly. |
| Menší využití programátorských zkušeností. | Automatizovat kontrolu výpočtů nebo vytvořit jen interní pomocný nástroj, pokud to vedoucí dovolí. |
| Sporné pořadí může být obtížné obhájit. | Zdůraznit subjektivitu AHP, konzistenci a podmíněnost výsledku konkrétním scénářem. |

## Předběžné rozhodnutí autora

Autor se **přiklání k variantě 1**, protože:

- pracuje jako PHP programátor;
- ve škole používá Javu a Spring;
- programování, návrh aplikace a automatické testování jsou mu bližší než formulace a rozbor tří rozsáhlých scénářů;
- funkční aplikace představuje jasný a obhajitelný praktický výstup.

Rozhodnutí však závisí na potvrzení těchto bodů vedoucím:

1. Může být návrh, implementace a testování univerzální AHP aplikace hlavním praktickým výstupem práce?
2. Stačí v aplikaci zpracovat jedno věrohodné porovnání databázových nástrojů místo tří samostatných scénářů?
3. Jak podrobné musí být praktické testování vlastností čtyř databázových nástrojů, pokud budou sloužit především jako ověřovací případ aplikace?
4. Má aplikace povinně obsahovat analýzu citlivosti, ukládání projektů a export výsledků, nebo jde o doporučená rozšíření?

Do potvrzení těchto otázek není vhodné zásadně přepisovat existující kapitoly BP ani zadávací list.

## Návrh e-mailu vedoucímu

**Předmět:** Volba praktické části bakalářské práce

Dobrý den,

děkuji za zaslané podklady a vysvětlení obou možností praktické části. Po jejich projití se předběžně přikláním k první variantě, tedy k vytvoření univerzální aplikace pro porovnávání kritérií a alternativ metodou AHP.

Pracuji jako PHP programátor a ve škole se věnujeme Javě a Springu, proto je mi návrh a programování aplikace bližší než zpracování tří rozsáhlých modelových scénářů. Praktickou část bych chtěl postavit především na analýze požadavků, návrhu architektury, implementaci výpočtů AHP, uživatelském rozhraní a testování správnosti aplikace. Předběžně uvažuji o webové aplikaci v Javě a Springu; případně bych mohl využít PHP, se kterým mám profesní zkušenost. Konkrétní technologii bych zvolil až podle potvrzeného rozsahu.

Aplikace by umožňovala zadat vlastní kritéria a alternativy, vytvořit párové matice, vypočítat váhy a konzistenční poměr, upozornit na neúplné nebo nekonzistentní vstupy a zobrazit výsledné pořadí. Správnost výpočtů bych ověřil pomocí kontrolních příkladů a automatických testů. Vybrané nástroje pro návrh a vývoj databázových systémů a již navržená kritéria bych použil jako konkrétní demonstrační a ověřovací případ aplikace.

Nejsem si však jistý, jak rozsáhlá má v této variantě zůstat samotná praktická komparace databázových nástrojů. Chápu správně, že by hlavním výstupem byla implementovaná a otestovaná aplikace a že by místo tří samostatných scénářů stačilo v aplikaci zpracovat jedno věrohodné porovnání vybraných databázových nástrojů? Zároveň bych se chtěl zeptat, zda má být součástí minimálního rozsahu také ukládání projektů, export výsledků a analýza citlivosti.

Pokud je tento směr vhodný, upravím podle něj cíl, osnovu a zadávací list ve STAGu.

Děkuji.

S pozdravem

Roman Janiš

