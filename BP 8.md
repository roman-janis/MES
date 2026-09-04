# Návrh hodnoticích kritérií

Při stanovení kritérií pro hodnocení se bude vycházet z toho, že nástroje budou porovnávány především podle toho, jak dokážou podpořit návrh a vývoj databáze. nikoli podle toho, jak zvládají její provoz a správu. Hodnoticí kritéria vycházejí ze studie Carvalho et al. (2022), která byla využita i při výběru nástrojů v předchozí kapitole. Tato studie porovnávala nástroje pro datové modelování podle kategorií, jako jsou funkcionalita, provozní vlastnosti softwaru, dokumentace a komunitní podpora. Předkládaná práce přebírá její kategoriální členění a rozšiřuje je o kritéria specifická pro návrh databázových systémů. U kritérií, která nelze vyjádřit číselně, se použije kvalitativní hodnocení podle zkušenosti a každé porovnání se krátce zdůvodní.

Přehled osmi navržených pracovních kritérií uvádí tabulka 2.

| **Kritérium** | **Název** | **Význam pro hodnocení** |
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
