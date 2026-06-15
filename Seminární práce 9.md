# 9 Návrh hodnoticích kritérií

Při vytváření kritérií pro hodnocení je třeba zohlednit, že nástroje budou porovnávány podle toho, jak dokážou podpořit návrh a vývoj databáze, nikoliv pouze podle toho, jak zvládají její provoz. Hodnoticí kritéria vycházejí ze studie Carvalho et al. (2022): Tato práce porovnávala nástroje pro datové modelování podle kategorií jako funkcionalita, provozní vlastnosti softwaru, dokumentace a komunitní podpora. Tato práce toto členění přebírá a rozšiřuje ho o kritéria specifická pro návrh databázových systémů. V navazující práci budou kritéria dále upřesněna, případně rozšířena.

Přehled osmi navržených pracovních kritérií uvádí tabulka 2.

| ID | Název kritéria | Typ kritéria | Způsob a zdroj hodnocení |
|---|---|---|---|
| K1 | Funkcionalita | maximalizační | testovací scénář + dokumentace nástroje |
| K2 | Použitelnost | maximalizační | kvalitativní hodnocení v testovacím scénáři |
| K3 | Kompatibilita s DBMS | maximalizační | počet oficiálně podporovaných DBMS |
| K4 | Forward engineering | maximalizační | testovací scénář (generování DDL) |
| K5 | Reverse engineering | maximalizační | testovací scénář (import z existující DB) |
| K6 | Dokumentace a komunitní podpora | maximalizační | kvalitativní hodnocení |
| K7 | Import, export a validace modelu | maximalizační | testovací scénář + formáty |
| K8 | Cena a licence | minimalizační | typ licence, omezení free verze, celková cena |

*Tabulka 2 — Navržená hodnoticí kritéria pro navazující praktickou komparaci*

Následující odstavce blíže popisují, co každé kritérium zahrnuje.

**K1 — Funkcionalita.** Hodnotí, jak dobře nástroj pokrývá potřeby návrhu databáze: konceptuální, logický a fyzický model, validaci modelu, generování SQL, dokumentaci modelu a práci s různými typy objektů.

**K2 — Použitelnost.** Posuzuje, jak snadno se nástroj ovládá: přehlednost rozhraní, kvalitu uživatelské zpětné vazby a chybovost při běžných úkonech.

**K3 — Kompatibilita s DBMS.** Zkoumá, kolik databázových systémů nástroj oficiálně podporuje (PostgreSQL, MySQL, Oracle, SQL Server a další).

**K4 — Forward engineering.** Hodnotí, jak nástroj generuje DDL skript nebo schéma databáze z modelu, včetně kvality vygenerovaného SQL.

**K5 — Reverse engineering.** Hodnotí, jak nástroj vytvoří model z existující databáze: věrnost převodu a možnosti následných úprav.

**K6 — Dokumentace a komunitní podpora.** Posuzuje rozsah a aktuálnost oficiální dokumentace a dostupnost komunitní podpory a aktualizací.

**K7 — Import, export a validace modelu.** Zkoumá, jaké formáty importu a exportu nástroj podporuje, zda umí model validovat a jak se integruje s verzovacími systémy.

**K8 — Cena a licence.** Hodnotí typ licence (open‑source, freeware, komerční), omezení bezplatné verze a celkové náklady na zavedení.

