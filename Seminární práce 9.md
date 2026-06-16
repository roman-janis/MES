# 9 Návrh hodnoticích kritérií

Při vytváření kritérií pro hodnocení je třeba zohlednit, že nástroje budou porovnávány podle toho, jak dokážou podpořit návrh a vývoj databáze, nikoliv pouze podle toho, jak zvládají její provoz. Hodnoticí kritéria vycházejí ze studie Carvalho et al. (2022). Tato práce porovnávala nástroje pro datové modelování podle kategorií jako: funkcionalita, provozní vlastnosti softwaru, dokumentace a komunitní podpora. Tato práce toto členění přebírá a rozšiřuje ho o kritéria specifická pro návrh databázových systémů. U kritérií, která nejdou vyjádřit číselně, se použije kvalitativní hodnocení podle zkušenosti a každé porovnání se krátce zdůvodní.

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
| K8 | Cena a licence | minimalizační | typ licence, omezení bezplatné verze, celková cena |

*Tabulka 2 – Přehled navržených hodnoticích kritérií (vlastní zpracování na základě Carvalho et al., 2022)*

Význam jednotlivých kritérií je blíže popsán níže.

**K1 Funkcionalita.** Rozsah funkcí nástroje — typy modelů (konceptuální, logický, fyzický), validace, dokumentace a podpora objektů jako tabulky, pohledy, indexy nebo triggery.

**K2 Použitelnost.** Vyjadřuje, jak snadno se s nástrojem pracuje – jak rychle se v něm uživatel zorientuje, nakolik je prostředí editoru modelu přehledné a jak náročné je provést běžné úkony.

**K3 Kompatibilita s DBMS.** Udává, kolik databázových systémů nástroj oficiálně podporuje.

**K4 Forward engineering.** Sleduje, jak nástroj generuje DDL skript nebo schéma databáze z navrženého modelu.

**K5 Reverse engineering.** Týká se schopnosti nástroje sestavit model z již existující databáze.

**K6 Dokumentace a komunitní podpora.** Posuzuje rozsah a aktuálnost oficiální dokumentace i dostupnost komunitní podpory a aktualizací.

**K7 Import a export modelu.** Zaměřuje se na podporované formáty importu a exportu a na propojení s verzovacími systémy.

**K8 Cena a licence.** Bere v úvahu typ licence (open source, freeware, komerční), omezení bezplatné verze a celkové náklady na zavedení.
