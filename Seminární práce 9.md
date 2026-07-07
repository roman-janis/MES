# 9 Návrh hodnoticích kritérií

Při vytváření kritérií pro hodnocení je potřeba zohlednit, že nástroje budou porovnávány podle toho, jak dokážou podpořit návrh a vývoj databáze, nikoliv pouze podle toho, jak zvládají její provoz a správu. Hodnoticí kritéria vycházejí ze studie Carvalho et al. (2022). Tato studie porovnávala nástroje pro datové modelování podle kategorií, jako jsou funkcionalita, provozní vlastnosti softwaru, dokumentace a komunitní podpora. Předkládaná práce toto členění přebírá a rozšiřuje ho o kritéria specifická pro návrh databázových systémů. U kritérií, která nelze vyjádřit číselně, se použije kvalitativní hodnocení podle zkušenosti a každé porovnání se krátce zdůvodní.

Přehled osmi navržených pracovních kritérií uvádí tabulka 2.

| ID | Název kritéria | Typ kritéria | Způsob a zdroj hodnocení |
|---|---|---|---|
| K1 | Funkcionalita | maximalizační | testovací scénář a dokumentace nástroje |
| K2 | Použitelnost | maximalizační | kvalitativní hodnocení v testovacím scénáři |
| K3 | Kompatibilita s DBMS | maximalizační | počet oficiálně podporovaných DBMS |
| K4 | Forward engineering | maximalizační | testovací scénář (generování DDL) |
| K5 | Reverse engineering | maximalizační | testovací scénář (import z existující DB) |
| K6 | Dokumentace a komunitní podpora | maximalizační | kvalitativní hodnocení |
| K7 | Import a export modelu | maximalizační | testovací scénář a podporované formáty |
| K8 | Náklady a licenční omezení | minimalizační | typ licence, omezení bezplatné verze, celková cena |

*Tabulka 2 – Přehled navržených hodnoticích kritérií (vlastní zpracování na základě Carvalho et al., 2022)*

Význam jednotlivých kritérií je blíže popsán níže.

**K1 Funkcionalita.** Hodnotí se, kolik úrovní modelu nástroj podporuje (konceptuální, logický, fyzický), zda umí validovat a jaké databázové objekty podporuje – například tabulky, pohledy, indexy nebo triggery.

**K2 Použitelnost.** Hodnotí se, jak snadno se nástroj používá, jak přehledné je grafické prostředí a jak jednoduše se provádějí běžné úkony, jako je přidání entity, úprava atributu nebo vytvoření vztahu.

**K3 Kompatibilita s DBMS.** Hodnotí se počet databázových systémů, s nimiž nástroj umí oficiálně pracovat.

**K4 Forward engineering.** Hodnotí se, jestli a jak nástroj z navrženého modelu vygeneruje funkční DDL skript nebo schéma databáze. Výsledek se ověřuje vygenerováním a testem výsledného skriptu.

**K5 Reverse engineering.** Hodnotí se schopnost nástroje sestavit model zpětně z existující databáze, tedy naimportovat její strukturu. Ověřuje se to importem z existující databáze.

**K6 Dokumentace a komunitní podpora.** Hodnotí se množství a aktuálnost oficiální dokumentace nástroje a zároveň dostupnost podpory ze strany komunity. Zároveň se zjištujě jak často nástroj dostává aktualizace.

**K7 Import a export modelu.** Hodnotí se, jaké formáty importu a exportu nástroj podporuje a jestli umí pracovat s verzovacím systémem.

**K8 Náklady a licenční omezení.** Hodnotí se druh licence nástroje (open-source, freeware, komerční), případná omezení bezplatné verze a celková cena zavedení nástroje do provozu.
