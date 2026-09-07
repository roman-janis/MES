# 8 Návrh hodnoticích kritérií

Při stanovení kritérií pro hodnocení se bude vycházet z toho, že nástroje budou porovnávány především podle toho, jak dokážou podpořit návrh a vývoj databáze. nikoli podle toho, jak zvládají její provoz a správu. Hodnoticí kritéria vycházejí ze studie Carvalho et al. (2022), která byla využita i při výběru nástrojů v předchozí kapitole. Tato studie porovnávala nástroje pro datové modelování podle kategorií, jako jsou funkcionalita, provozní vlastnosti softwaru, dokumentace a komunitní podpora. Předkládaná práce přebírá její kategoriální členění a rozšiřuje je o kritéria specifická pro návrh databázových systémů. U kritérií, která nelze vyjádřit číselně, se použije kvalitativní hodnocení podle zkušenosti a každé porovnání se krátce zdůvodní.

Přehled osmi navržených pracovních kritérií uvádí tabulka 2.

| Kritérium | Název | Význam pro hodnocení |
|:--:|:---|:---|
| K1 | Funkcionalita | Podpora úrovní modelu, validace a databázových objektů. |
| K2 | Použitelnost | Přehlednost prostředí a jednoduchost běžných modelovacích úkonů. |
| K3 | Kompatibilita s DBMS | Počet databázových systémů, s nimiž nástroj umí pracovat. |
| K4 | Forward engineering | Možnost vygenerovat funkční DDL skript nebo schéma databáze. |
| K5 | Reverse engineering | Schopnost sestavit model z existující databáze. |
| K6 | Dokumentace a komunitní podpora | Množství a aktuálnost dokumentace, komunita a aktualizace. |
| K7 | Import a export modelu | Podporované formáty importu/exportu a práce s verzováním. |
| K8 | Náklady a licenční omezení | Typ licence, omezení bezplatné verze a cena zavedení. |

<span id="_Toc234483572" class="anchor"></span>Tabulka 2: Přehled navržených hodnoticích kritérií (vlastní zpracování na základě Carvalho et al., 2022)

---

# Návrh nového znění kapitoly 8 – pracovní verze k porovnání

> Následující text je návrh. Původní znění kapitoly je ponecháno výše beze změny. Po kontrole se vybrané části ručně sloučí a tato pracovní poznámka se odstraní.

## 8 Návrh hodnoticích kritérií

Při stanovení kritérií pro hodnocení se vychází z toho, že nástroje budou porovnávány především podle toho, jak podporují návrh a vývoj databáze, nikoli podle toho, jak zvládají její běžný provoz a správu. Hodnoticí kritéria vycházejí ze studie Carvalho et al. (2022), která byla využita také při výběru nástrojů v předchozí kapitole. Studie porovnávala nástroje pro datové modelování podle kategorií, jako jsou funkcionalita, provozní vlastnosti softwaru, dokumentace a komunitní podpora. Předkládaná práce přebírá toto kategoriální členění a doplňuje je o kritéria specifická pro návrh databázových systémů.

Pro praktické porovnání bylo stanoveno osm kritérií K1 až K8. Charakter kritéria v tabulce 2 vyjadřuje způsob, jakým budou posuzovány vlastnosti nástroje. Neurčuje jeho váhu v AHP. Význam jednotlivých kritérií pro výsledné rozhodnutí stanoví uživatel párovým porovnáním podle požadavků konkrétního scénáře.

| Kritérium | Název | Vymezení kritéria | Charakter posouzení |
|:--:|:---|:---|:---|
| K1 | Funkcionalita modelování | Podpora samostatného modelu, databázových objektů, datových typů, primárních a cizích klíčů, kardinalit a integritních omezení. Nezahrnuje forward engineering, reverse engineering ani export, které mají samostatná kritéria. | Převážně objektivní, doplněné popisem omezení. |
| K2 | Použitelnost | Přehlednost prostředí, dohledatelnost funkcí, srozumitelnost chybových hlášení, počet nutných kroků, časová náročnost a potřeba obcházet omezení při běžných modelovacích úkonech. | Převážně subjektivní, podložené zaznamenaným postupem a časem. |
| K3 | Kompatibilita s DBMS | Rozsah databázových systémů, pro které nástroj skutečně podporuje modelování, generování DDL nebo reverse engineering. Samotná možnost připojení k DBMS se nepovažuje za plnou podporu modelování. | Převážně objektivní. |
| K4 | Forward engineering | Schopnost vytvořit z vlastního modelu spustitelné DDL nebo databázové schéma při zachování tabulek, datových typů, klíčů a omezení a bez nepřiměřených ručních zásahů. | Převážně objektivní. |
| K5 | Reverse engineering | Schopnost načíst existující databázové schéma do modelu nebo diagramu a správně rozpoznat tabulky, klíče, vztahy, kardinality a integritní omezení. | Převážně objektivní. |
| K6 | Dokumentace a komunitní podpora | Dostupnost, aktuálnost a použitelnost oficiální dokumentace a dostupnost relevantní komunitní pomoci pro modelování, forward a reverse engineering a export. | Kombinované objektivní a kvalitativní posouzení. |
| K7 | Import a export modelu | Dostupnost a použitelnost nativních formátů pro export diagramu a import modelu nebo SQL. Tisk do PDF se odlišuje od nativního exportu. Export DDL hodnocený v K4 se zde znovu nezapočítává. | Převážně objektivní. |
| K8 | Náklady a licenční omezení | Cena a typ licence testované edice a omezení bezplatné varianty, která jsou relevantní pro návrh databáze. Funkční nedostatek se hodnotí v příslušném funkčním kritériu; v K8 se posuzuje jeho licenční nebo ekonomická příčina. | Převážně objektivní, časově závislé. |

Tabulka 2: Přehled hodnoticích kritérií (vlastní zpracování na základě Carvalho et al., 2022)

### 8.1 Vazba kritérií na praktické testování

Pro praktické porovnání bude použit jednotný protokol obsahující 51 testovacích bloků. Všechny bloky budou provedeny u všech čtyř nástrojů. Pokud testovaná edice určitou funkci neposkytuje, zaznamená se její nedostupnost jako výsledek testu. Podrobné testy nepředstavují 51 samostatných kritérií AHP. Slouží jako dílčí pozorování a důkazy, které budou následně shrnuty do osmi kritérií K1 až K8.

| Kritérium | Podklady z testovacího protokolu | Způsob souhrnného posouzení |
|:--:|:---|:---|
| K1 | Testy 1.1–1.12, 1.14 a 1.15; body 1.3a–1.3k jako kontrola vytvoření jednotlivých tabulek. | Posoudí se rozsah správně podporovaných modelovacích prvků a závažnost zjištěných omezení. Dílčí tabulky 1.3a–1.3k se nebudou považovat za samostatná kritéria. |
| K2 | Souhrnný test 1.13, zaznamenané časy, chyby, hledání funkcí, počet kroků a nutné obchvaty z celého protokolu. | Posoudí se celková náročnost práce a srozumitelnost ovládání. Samotný čas nebude jediným měřítkem. |
| K3 | Testy K3.1 a K3.2. | Oddělí se deklarovaná podpora z oficiální dokumentace od prakticky ověřené podpory dalšího DBMS. |
| K4 | Testy 2.1–2.6 a kontrola DDL v bodu 4.3. | Posoudí se správnost a spustitelnost generovaného DDL, zachování omezení a rozsah ručních oprav. Export téhož DDL v bodech 2.5 a 4.3 se započítá pouze jednou. |
| K5 | Testy 3.1–3.9. | Posoudí se úplnost a správnost načteného schématu včetně složitějších konstrukcí. |
| K6 | Testy K6.1 a K6.2. | Spojí se ověření oficiální dokumentace a relevantní aktivity komunity k testovaným funkcím. |
| K7 | Testy 4.1, 4.2 a 4.4. | Posoudí se nativní export diagramu, rozdíl mezi exportem a tiskem a možnost importu cizího formátu. DDL z bodu 4.3 zůstává součástí K4. |
| K8 | Testy K8.1 a K8.2. | Posoudí se cena, licence a konkrétní omezení použité bezplatné nebo komunitní edice. |

### 8.2 Zpracování výsledků pro AHP

U každého testu bude zaznamenán skutečný postup, výsledek, případné chybové hlášení nebo obchvat a odpovídající důkaz. Pomocná známka 1 až 5 v testovacím protokolu usnadní jednotný zápis výsledků, nebude však automaticky převedena na hodnotu Saatyho škály ani zprůměrována přes všech 51 bloků. Prostý průměr by zvýhodnil nebo znevýhodnil kritéria pouze podle počtu jejich dílčích testů.

Po dokončení praktických testů vznikne pro každý nástroj věcný souhrn podle K1 až K8. Z těchto podkladů budou zdůvodněna párová porovnání nástrojů vzhledem ke každému kritériu. Váhy kritérií budou stanoveny samostatně podle požadavků zvoleného scénáře. Tím zůstane odděleno ověřené chování nástrojů od subjektivního významu jednotlivých kritérií pro uživatele.
