# 9 Návrh hodnoticích kritérií

Při tvorbě hodnoticích kritérií je nutné zohlednit, že nástroje budou srovnávány na úrovni schopností pokrýt návrh a vývoj databáze, nikoli pouze provoz databáze. Vymezení kritérií vychází z obecné struktury hodnoticích kategorií identifikovaných v komparativní studii Carvalho et al. (2022), kteří při hodnocení nástrojů pro datové modelování pracovali s kategoriemi jako funkcionalita, provozní charakteristiky softwaru, dokumentace a komunitní podpora. Tato práce přejímá analogické členění a doplňuje jej o kritéria specifická pro AHP postup a pro kontext návrhu databázových systémů. V navazující bakalářské práci budou kritéria dále upřesněna, případně rozšířena o subkritéria.

Přehled osmi navržených pracovních kritérií uvádí tabulka 2.

| ID | Název kritéria | Typ | Způsob hodnocení |
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

**K1 — Funkcionalita.** Rozsah podporovaných funkcí: konceptuální, logický a fyzický model, validace modelu, generování SQL, dokumentace modelu, podpora pro práci s různými typy objektů. Maximalizační, kvalitativně‑kvantitativní kritérium.

**K2 — Použitelnost.** Snadnost ovládání, přehlednost rozhraní, kvalita uživatelské zpětné vazby, minimalizace chybovosti při běžných úkonech. Maximalizační, kvalitativní kritérium hodnocené v testovacím scénáři.

**K3 — Kompatibilita s DBMS.** Šíře podporovaných databázových systémů (PostgreSQL, MySQL, Oracle, SQL Server a další). Maximalizační kritérium, kvantifikovatelné počtem oficiálně podporovaných DBMS.

**K4 — Forward engineering.** Schopnost generovat DDL skript nebo přímo vytvořit schéma databáze z modelu, včetně kvality vygenerovaného SQL. Maximalizační, kvalitativně‑kvantitativní kritérium.

**K5 — Reverse engineering.** Schopnost vytvořit model z existující databáze, věrnost převodu a možnosti následných úprav. Maximalizační, kvalitativně‑kvantitativní kritérium.

**K6 — Dokumentace a komunitní podpora.** Rozsah a aktuálnost oficiální dokumentace, dostupnost komunitních zdrojů, frekvence aktualizací. Maximalizační, kvalitativní kritérium.

**K7 — Import, export a validace modelu.** Podporované formáty importu/exportu, schopnost validovat model před nasazením, integrace s verzovacími systémy. Maximalizační, kvalitativně‑kvantitativní kritérium.

**K8 — Cena a licence.** Typ licence (open‑source, freeware, komerční), omezení free verze, celkové náklady na zavedení. Minimalizační kritérium (vyšší cena = nižší skóre).

