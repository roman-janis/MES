# Zdroje a literatura

Aktualizace: 19. 6. 2026.

V práci je nyní **24 citovaných zdrojů**; v seznamu jsou seřazené abecedně a rozdělené na tištěné (Carvalho et al.; Chen 1976; Chlapek, Kučera a Palovská; Codd 1970; Elmasri a Navathe; Ho 2008; Ishizaka a Labib; Mardani et al. 2015; Pokorný a Valenta; Rosenthal a Reiner; Saaty 1990; Saaty 2008; Simanavičienė a Vdovinskienė; Vaidya a Kumar; Velasquez a Hester) a internetové (DBeaver; DB-Engines; Laranjeiro a Pinto; MySQL; Oracle; pgModeler; PostgreSQL; Soukopová; Watt a Eng). Všechny in-text citace párují se seznamem.

Tento soubor popisuje, jak jsou v projektu rozdělené zdroje. Nerozlišuji zde zvlášť seminární práci a bakalářskou práci; beru to jako jeden pracovní základ pro budoucí BP.

## Princip třídění

- `literatura/` - zdroje, které je možné uvést v dokumentu v seznamu literatury.
- `literatura/inspirace/` - vzory, kvalifikační práce, ukázky a návody, ze kterých je možné se podívat na postup, strukturu nebo způsob zpracování, ale nemají se uvádět jako použité zdroje.
- `smazat/` - rozbité soubory, duplicity, neověřené odkazy nebo materiály mimo téma.

## 1. Zdroje k databázím, datovému modelování a nástrojům

Tyto soubory zůstávají v `literatura/DB`, protože se mohou použít jako zdroje v práci nebo později v BP.

- **POKORNÝ, Jaroslav a Michal VALENTA.** *Databázové systémy*. Praha: České vysoké učení technické v Praze, 2020. ISBN 978-80-01-06708-6.  
  Umístění: `literatura/DB/Pokorny_Valenta_Databazove_systemy_2020.pdf`

- **CHLAPEK, Dušan, Jan KUČERA a Helena PALOVSKÁ.** *Datové modelování a návrh relační databáze: Sbírka řešených úloh*. Praha: VŠE, Nakladatelství Oeconomica, 2019. ISBN 978-80-245-2331-6.  
  Umístění: `literatura/DB/Chlapek_Kucera_Palovska_2019_Datove_modelovani_relacni_databaze.pdf`

- **JEDLIČKA, Jan.** *Key-value databázové systémy*. Ostrava, 2024. Diplomová práce. VŠB-TUO.  
  Umístění: `literatura/DB/JED0050_FEI_N2647_2612T025_2024.pdf`  
  Poznámka: ponecháno jako možný zdroj k širšímu přehledu databázových systémů. Pokud se v textu nebude řešit key-value / NoSQL oblast, není nutné ho citovat.

- **ROSENTHAL, Arnon a David S. REINER.** *Tools and Transformations - Rigorous and Otherwise - for Practical Database Design*. ACM Transactions on Database Systems, 1994.  
  Umístění: `literatura/DB/Rosenthal_Reiner_1994_Tools_Transformations_DB_Design.pdf`  
  Poznámka: vhodné spíše pro BP, pokud se bude řešit návrh databáze, transformace modelů a nástroje podporující návrh.

- **CARVALHO, Gonçalo, Sergii MYKOLYSHYN, Bruno CABRAL, Jorge BERNARDINO a Vasco PEREIRA.** Comparative Analysis of Data Modeling Design Tools. *IEEE Access*. 2022, 10, 3351-3365. DOI: 10.1109/ACCESS.2021.3139071.  
  Umístění: `literatura/DB/Comparative_Analysis_of_Data_Modeling_Design_Tools.pdf`

- **CHEN, Peter Pin-Shan.** The entity-relationship model—toward a unified view of data. *ACM Transactions on Database Systems*. 1976, 1(1), 9–36. DOI: 10.1145/320434.320440.  
  Citováno v §5.1 (ER model — původní článek). Volně dostupné: <http://bit.csc.lsu.edu/~chen/pdf/erd-5-pages.pdf> a ACM DL. Nalezeno přes reference Carvalho et al. (2022), ref [25].

- **ELMASRI, Ramez a Sham NAVATHE.** *Fundamentals of Database Systems*. 7th ed. Boston: Pearson, 2016. ISBN 978-0133970777.  
  Umístění: `literatura/DB/Elmasri_Navathe_2016_Fundamentals_of_Database_Systems.pdf`  
  Citováno v §4.1 (základní pojmy, funkce DBMS), §4.2 (schéma, instance, metadata), §4.3 (víceúrovňová architektura ANSI/SPARC) a §4.4 (fáze návrhu databáze). Čtvrtý zdroj kapitoly 4, doplněn 19. 6. 2026 podle doporučení vedoucího.

### Dokumentace nástrojů

- **DBeaver Documentation** - `literatura/DB/DBeaver_Documentation.url`
- **MySQL Workbench Manual** - `literatura/DB/MySQL_Workbench_Manual.url`
- **Oracle SQL Developer Data Modeler** - `literatura/DB/Oracle_SQL_Developer_Data_Modeler.url`
- **pgModeler - PostgreSQL Database Modeler** - `literatura/DB/pgModeler.url`
- **PostgreSQL Documentation** - `literatura/DB/PostgreSQL_Documentation.url`
- **DB-Engines Ranking** [online]. solid IT gmbh, 2026 - citováno v §8 (rozšířenost DBMS). <https://db-engines.com/en/ranking>

## 2. Zdroje k vícekriteriálnímu rozhodování a AHP

Tady je schválně ponechaný menší počet zdrojů. Pro AHP není potřeba mít velké množství bakalářských a diplomových prací. Stačí jeden český učební text, původní zdroje metody a jeden článek, který ukazuje použití AHP při výběru softwaru.

- **SOUKOPOVÁ, Jana.** *Vícekriteriální metody hodnocení*. Brno: Masarykova univerzita, 2016. Učební text.  
  Umístění: `literatura/AHP/Soukopova_2016_Vicekriterialni_metody_hodnoceni.pdf`

- **SAATY, Thomas L.** How to make a decision: The Analytic Hierarchy Process. *European Journal of Operational Research*. 1990, 48(1), 9-26.  
  Umístění: `literatura/AHP/Saaty_1990_How_to_make_a_decision_AHP.pdf`

- **SAATY, Thomas L.** Decision making with the analytic hierarchy process. *International Journal of Services Sciences*. 2008, 1(1), 83-98.  
  Umístění: `literatura/AHP/Saaty_2008_Decision_making_with_AHP.pdf`

- **SIMANAVIČIENĖ, Rūta a Sonata VDOVINSKIENĖ.** Selection of Computer-Aided Design Software Systems Using the AHP Method. *Baltic Journal of Modern Computing*. 2023, 11(2), 272-284. DOI: 10.22364/bjmc.2023.11.2.04.  
  Umístění: `literatura/AHP/Simanaviciene_Vdovinskiene_2023_CAD_software_AHP_selection.pdf`

- **VELASQUEZ, Mark a Patrick T. HESTER.** An Analysis of Multi-Criteria Decision Making Methods. *International Journal of Operations Research*. 2013, 10(2), 56–66. ISSN 1813-713X.  
  Umístění: `literatura/AHP/Velasquez_Hester_2013_Analysis_MCDM_Methods.pdf`  
  Citováno v §6.2 (přehled metod WSA, TOPSIS, ELECTRE). Přesunuto ze sekce 5C, přidáno do bibliografie 18. 6.

- **ISHIZAKA, Alessio a Ashraf LABIB.** Review of the main developments in the Analytic Hierarchy Process. *Expert Systems with Applications*. 2011, 38(11), 14336–14345. DOI: 10.1016/j.eswa.2011.04.143.  
  Umístění: `literatura/AHP/Ishizaka_Labib_2011_Review_AHP_Developments.pdf`  
  Citováno v §6.2 (index konzistence CR, zdůvodnění volby AHP) a §7.3 (omezení AHP — pracnost a subjektivita). Přesunuto ze sekce 5C, přidáno do bibliografie 18. 6.

- **MARDANI, Abbas, Ahmad JUSOH, Khalil MD NOR, Zainab KHALIFAH, Norhayati ZAKWAN a Alireza VALIPOUR.** Multiple criteria decision-making techniques and their applications – a review of the literature from 2000 to 2014. *Economic Research – Ekonomska Istraživanja*. 2015, 28(1), 516–571. ISSN 1331-677X. DOI: 10.1080/1331677X.2015.1075139.  
  PDF uloženo: `literatura/AHP/Mardani_2015_MCDM_review.pdf` (Croatian Academic Repository, open access, staženo 19. 6. 2026).  
  Citováno v §6 (úvod — systematické zahrnutí kritérií do rozhodování) a §6.2 (výčet metod WSA/TOPSIS/ELECTRE). Přidáno 18. 6.

## 3. Inspirace a vzory, které necitovat jako zdroje

Tyto soubory jsou přesunuté do `literatura/inspirace`. Slouží pro orientaci, porovnání struktury, formulaci metodiky nebo praktický postup. Nemají být běžně uváděné v seznamu literatury práce.

### Inspirace k databázím a návrhu databáze

- `literatura/inspirace/DB/Kaspar_bc_final.pdf` - Zbyněk Kašpar, *Databázové systémy v praxi*, BP 2012.
- `literatura/inspirace/DB/Chotenovsky_Tvorba_datovych_modelu_2023.pdf` - Tomáš Chotěnovský, BP 2023. Inspirace (necitováno; §3 a návrh databáze jsou opřeny o Chlapek, Kučera a Palovská, 2019).
- `literatura/inspirace/DB/Smahel_Porovnani_CASE_nastroju_2018.pdf` - David Šmahel, *Porovnání CASE nástrojů se zaměřením na podporu návrhu databáze*, BP 2018.

### Inspirace k AHP a vícekriteriálnímu rozhodování
- `literatura/inspirace/AHP/Fruhauf_Vyber_dodavatele_MCDM_2025.pdf` - ukázka použití vícekriteriálního rozhodování.
- `literatura/inspirace/AHP/Jandova_AHP_jeji_silne_a_slabe_stranky.pdf` - Věra Jandová, DP 2012. Inspirace (necitováno).
- `literatura/inspirace/AHP/Mullerova_Vicekriterialni_rozhodovani_2020.pdf` - ukázka zpracování tématu vícekriteriálního rozhodování.
- `literatura/inspirace/AHP/Rysankova_Vicekriterialni_rozhodovani_2021.pdf` - ukázka zpracování tématu vícekriteriálního rozhodování.
- `literatura/inspirace/AHP/Vasileva_Metody_rozhodovani_2022.pdf` - ukázka metod vícekriteriálního rozhodování.
- `literatura/inspirace/AHP/Vohradsky_Pouziti_metod_vicekriterialniho_rozhodovani_pri_rizeni_podniku.pdf` - Marek Vohradský, DP 2016. Inspirace (necitováno).
- `literatura/inspirace/AHP/Zadina_Vicekriterialni_rozhodovani_2022.pdf` - ukázka použití vícekriteriálního rozhodování.
- `literatura/inspirace/AHP/Patykova_Vicekriterialni_rozhodovani_2017.pdf` - ukázka vícekriteriálního rozhodování ve firemní praxi.
- `literatura/inspirace/AHP/OPF_DP_2025_58108_Oberherrova_Nikol.pdf` - Nikol Oberherrová, DP 2025 (SU Opava). Orientace: potvrzuje Vaidya & Kumar (2006) [ref 21] jako použitelný zdroj; Ishizaka & Labib a Taherdoost (2022) také zmíněny.
- `literatura/inspirace/AHP/Urban_2022_vicekriterialniRozhodovani_klimatizace.pdf` - Daniel Urban, BP 2022 (ČZU Praha). Pouze české knihy + produktové weby, žádné nové akademické články — nízká hodnota pro nalezení zdrojů.


## 4. Materiály k zadání a požadavkům

- `zadani/vskp_-_zadani_vskp.pdf` - oficiální zadání BP.
- `zadani/vskp_-_udaje_o_vskp.pdf` - údaje o VŠKP ze STAGu.
- `Email konverzace.txt` - e-mailová komunikace s požadavky a poznámkami vedoucího.
- `POZADAVKY_UCITELE.md` - pracovní souhrn toho, co chtěl vedoucí a co z toho plyne pro práci.
- `oliva/pokyny/` - pravidla MES, metodické pokyny FIM UHK, citace a formát.
- `oliva/sablony/` - šablony seminární práce.

## 5. Kandidáti na doplnění

Přehled zdrojů, které nejsou v práci, ale hodí se pro BP. Každý má stav: ✅ staženo / 📚 sehnat v knihovně / 🔍 dohledat online.

---

### 5A. Databáze — doporučeno vedoucím (e-mail 17. 6. 2026) — prioritně sehnat

Tyto čtyři knihy vedoucí výslovně zmínil. Použití: SP 4 (základy, DBMS), SP 5 (modely, normalizace). Cíl BP: aspoň 2–3 z nich citovat.

Elmasri & Navathe je už citován jako 4. zdroj kapitoly 4 (viz sekce 1 výše) a vyřazen z tohoto seznamu kandidátů. Zbývající tři zůstávají jako kandidáti pro BP.

| Stav | Zdroj |
|---|---|
| 📚 sehnat | **CONNOLLY, Thomas a Carolyn BEGG.** *Database Systems: A Practical Approach to Design, Implementation, and Management*. 6th ed. London: Pearson, 2015. ISBN 978-1292061184. |
| 📚 sehnat | **GARCIA-MOLINA, Hector, Jeffrey D. ULLMAN a Jennifer WIDOM.** *Database Systems: The Complete Book*. 2nd ed. Upper Saddle River: Pearson Prentice Hall, 2008. ISBN 978-0131873254. |
| 📚 sehnat | **KORTH, Henry F., Abraham SILBERSCHATZ a S. SUDARSHAN.** *Database System Concepts*. 7th ed. New York: McGraw-Hill, 2020. ISBN 978-0078022159. |

---

### 5B. Databáze — další kandidáti (nižší priorita)

| Stav | Zdroj | Poznámka |
|---|---|---|
| ✅ staženo | **BUNRUAMKAEW, Chutarat.** *How to Do AHP Analysis in Excel* [online]. University of Tsukuba, 2012. Metodický návod. Umístění: `literatura/AHP/Bunruamkaew_How_to_do_AHP_analysis_in_Excel_2012.pdf`. | Praktický návod k výpočtu AHP v Excelu — hodí se pro praktickou část BP (sestavení matic, výpočet vah, CR). Necitovat jako vědecký zdroj. |
| ✅ staženo | **OTTE, Lukáš.** *Databázové systémy*. Ostrava: Vysoká škola báňská – Technická univerzita Ostrava, Fakulta strojní, 2013. ISBN 978-80-248-3054-4. Umístění: `literatura/DB/Otte_2013_Databazove_systemy_VSBTUO.pdf`. | Český učební text, 189 stran. Zatím necitováno — záloha pro BP pokud bude potřeba další český DB zdroj vedle Pokorného a Valenty. |
| ✅ staženo | **HRONEK, Jiří.** *Databázové systémy*. Olomouc: Univerzita Palackého, Přírodovědecká fakulta, 2007. Učební text. Umístění: `literatura/DB/Hronek_2007_Databazove_systemy_UPOL.pdf`. | Pokrývá ER model, relační model, normalizaci, SQL — překryv s kapitolami 4 a 5. Zatím necitováno — záloha pro BP. |
| 📚 sehnat | **DATE, C. J.** *An Introduction to Database Systems*. 8th ed. Pearson/Addison Wesley, 2004. | Klasická učebnice, ale starší; použít jen pokud nebude Connolly nebo Elmasri. |
| 📚 sehnat | **RAMAKRISHNAN, Raghu a Johannes GEHRKE.** *Database Management Systems*. 3rd ed. McGraw-Hill, 2002. | Podobná úroveň jako Elmasri; alternativa. |
| ✅ staženo (19. 6.) | **CODD, Edgar F.** A relational model of data for large shared data banks. *Communications of the ACM*. 1970, **13**(6), 377–387. DOI: 10.1145/362384.362685. PDF uloženo: `literatura/DB/Codd_1970_Relational_model.pdf`. | Citováno v §5.2 (atomické hodnoty relačního modelu) a §5.4 (normalizace — 1NF–3NF). Přidáno do bibliografie SP11. |

---

### 5C. MCDM a AHP — ✅ staženo

| Stav | Zdroj |
|---|---|
| ✅ staženo | **VELASQUEZ, Manuel a Patrick HESTER.** An Analysis of Multi-Criteria Decision Making Methods. *International Journal of Operations Research*. 2013, **10**(2), 56–66. Umístění: `literatura/AHP/Velasquez_Hester_2013_Analysis_MCDM_Methods.pdf` |
| ✅ staženo | **ISHIZAKA, Alessio a Ashraf LABIB.** Review of the main developments in the Analytic Hierarchy Process. *Expert Systems with Applications*. 2011, **38**(11), 14336–14345. DOI: 10.1016/j.eswa.2011.04.143. Umístění: `literatura/AHP/Ishizaka_Labib_2011_Review_AHP_Developments.pdf` |

Použití: **HOTOVO (18. 6.)** — přidáno do SP 6.2 (Velasquez a Hester: WSA/TOPSIS/ELECTRE; Ishizaka a Labib: CR konzistence AHP). Také přidány jako záznamy do SP 11 (bibliografie).

---

### 5C2. AHP aplikovaný — české recenzované články (✅ staženo)

| Stav | Zdroj | Poznámka |
|---|---|---|
| ✅ staženo | **TOMEŠ, Rostislav a Július ALCNAUER.** Konzistence matice párových porovnání při použití Analytického hierarchického procesu (AHP). *Business & IT*. 2014, (2), 114–?. ISSN ověřit. Umístění: `literatura/AHP/Tomes_Alcnauer_2014_AHP_konzistence_matice.pdf`. | Pokrývá sestavení matice párových porovnání, výpočet vlastního vektoru a ověření konzistence (CI, CR) na příkladech v Excelu. Zatím necitováno — záloha pro BP k sekci o konzistenci AHP, doplněk k Ishizaka & Labib (2011). Přidáno 6. 7. 2026. |

| Stav | Zdroj | Poznámka |
|---|---|---|
| ✅ staženo | **VLČKOVÁ, Jana a Lukáš FRIEBEL.** Využití metody AHP při výběru poskytovatele outsourcingu účetnictví. *Český finanční a účetní časopis*. 2015, **10**(2). ISSN 1802-2367. DOI: 10.18267/j.cfuc.439. Umístění: `literatura/AHP/Vlckova_Friebel_2015_AHP_outsourcing_uctectnictvi.pdf`. | Český recenzovaný open-access článek s aplikací AHP v praxi. Nenahrazuje obecnou teorii (Saaty, Ishizaka & Labib), ale doplňuje ji o doložitelný příklad. Citovat v BP v kapitole o AHP nebo metodice. Poznámka: ověřit čísla stran a přesné číslo ročníku v PDF. |

---

### 5D. MCDM a AHP — kandidáti k sehnání (nižší priorita)

| Stav | Zdroj | Poznámka |
|---|---|---|
| 📚 sehnat | **RAMÍK, Jiří.** *Vícekriteriální rozhodování: analytický hierarchický proces (AHP)*. Karviná: Slezská univerzita v Opavě, 1999. | Jediná česká kniha přímo o AHP; vhodná jako doplněk k Saatym. |
| 📚 sehnat | **FIALA, Petr.** *Modely a metody rozhodování*. Praha: Oeconomica, 2013. | Standardní česká učebnice MCDM; alternativa nebo doplněk k Soukopové. |
| 📚 sehnat | **FOTR, Jiří a Lenka ŠVECOVÁ.** *Manažerské rozhodování*. Praha: Ekopress, 2016. | Pokrývá MCDM šířeji; pro BP pokud bude potřeba více českých zdrojů. |

---

### 5E. AHP aplikovaný na výběr softwaru / DBMS — ✅ staženo

| Stav | Zdroj | Poznámka |
|---|---|---|
| ✅ staženo | **CATAK, F. Ozgur, Servet KARABAS a Serkan YILDIRIM.** Fuzzy Analytic Hierarchy Based DBMS Selection in Turkish National Identity Card Management Project. *International Journal of Information Sciences and Techniques*. 2012, **2**(4), 29–38. DOI: 10.5121/ijist.2012.2403. Umístění: `literatura/AHP/Catak_2012_Fuzzy_AHP_DBMS_selection.pdf`. | Aplikace fuzzy AHP na výběr DBMS pro projekt eID v Turecku. Přímo relevantní pro zdůvodnění metodiky BP. Citováno v §7.3 (oddělení vah kritérií od hodnocení alternativ). Přidáno do SP11 6. 7. 2026. |
| ✅ staženo | **EBRAHIMI, Seyed Babak a Maryam TAHERI.** Selection of Database Management System with Fuzzy-AHP for Electronic Medical Record. *I.J. Information Engineering and Electronic Business*. 2015, **7**(5), 1–9. DOI: 10.5815/ijieeb.2015.05.01. Umístění: `literatura/AHP/Ebrahimi_Taheri_2015_Fuzzy_AHP_DBMS_EMR.pdf`. | Výběr DBMS pro elektronické zdravotní záznamy pomocí fuzzy AHP; porovnává PostgreSQL, MySQL, Oracle, DB2, SQL Server. Alternativa nebo doplněk k Catak et al. Zatím necitováno v textu SP. |

---

### 5F. Ostatní (nízká priorita, spíše pro BP)

| Stav | Zdroj | Poznámka |
|---|---|---|
| 📚 sehnat | **SULLIVAN, Dan.** *NoSQL for Mere Mortals*. Addison-Wesley, 2015. ISBN 0-13-402321-8. | Jen pokud bude v BP kapitola o NoSQL. |

---

### 5G. Z knihovního seznamu UHK (předmět DB) — kandidáti (zadáno 17. 6. 2026)

Knihy z doporučené literatury kurzu v portálu UHK (`ucebny.uhk.cz` — interní, za přihlášením). **Connolly & Begg, Date a Sullivan jsou už výše** (5A / 5B / 5F), proto se zde neopakují.

| Stav | Zdroj | Relevance / poznámka |
|---|---|---|
| ✅ citováno (18. 6.) | **WATT, Adrienne a Nelson ENG.** *Database Design* [online]. 2nd ed. Victoria: BCcampus, 2014. Dostupné z: <https://opentextbc.ca/dbdesign01/>. Licence CC BY 4.0. | Volně dostupný open textbook. Citováno v SP 4.1 (databáze/DBMS) a SP 5.2 (relační model). Nalezeno přes reference Carvalho et al. (2022), ref [28]. |
| 🔍 online (zdarma) | **MONGE, Alvaro.** *Database Design with UML and SQL*. 4th ed. [online]. California State University Long Beach. Dostupné z: <http://web.csulb.edu/colleges/coe/cecs/dbdesign/> | Volně online; hodí se k SP 5 (notace ER/UML — Chen, Crow's Foot, UML). |
| 📚 sehnat | **ULLMAN, Jeffrey D. a Jennifer WIDOM.** *A First Course in Database Systems*. 3rd ed. Upper Saddle River: Prentice Hall, 2007. ISBN 978-0136006374. | Relační model a datové modelování; nižší priorita (podobné Garcia-Molina/Ullman/Widom v 5A). |
| 📚 sehnat | **BEAULIEU, Alan.** *Learning SQL: Generate, Manipulate, and Retrieve Data*. 3rd ed. Sebastopol: O'Reilly Media, 2020. ISBN 978-1492057611. | O psaní SQL; pro téma (návrhové nástroje) okrajové, spíš praktická část BP. |
| 📚 sehnat | **SHELDON, Robert.** *SQL: začínáme programovat*. Praha: Grada, 2005. | SQL základy (CZ); okrajové. |
| 📚 sehnat | **STEPHENS, Ryan K. a Ronald R. PLEW.** *Naučte se SQL za 28 dní*. Brno: Computer Press, 2010. | SQL tutoriál; okrajové. |
| — necitovat | Coursera — kurzy „database". <https://www.coursera.org/search?query=database> | Online kurzy, ne citovatelná literatura. |

Pravidlo: knihy o **návrhu databází** (Monge, Ullman & Widom) se hodí do teorie; knihy o **psaní SQL** (Beaulieu, Sheldon, Stephens & Plew) jsou pro toto téma okrajové.

## 6. Co zůstalo ve `smazat/`

Ve `smazat/` zůstaly hlavně duplicity, rozbité soubory, slabé materiály nebo soubory mimo téma.

- `smazat/Databázové systémy - Pokorný a Valenta - 4ca4af82-91fc-45cc-9e9c-46fd51abd17b.pdf` - duplicitní kopie knihy Pokorný a Valenta.
- `smazat/BuresO_VyuzitiVicekriterialniho_HB_2018.pdf` - rozbité stažení, soubor má jen několik KB.
- `smazat/MullerovaK_VicekriterialniRozhodovani_LK_2020.pdf` - rozbité nebo neúplné stažení.
- `smazat/RysankovaP_VicekriterialniRozhodovani_BH_2021.pdf` - rozbité nebo neúplné stažení.
- `smazat/Bures_Vyuziti_vicekriterialniho_hodnoceni.url` - zatím jen odkaz, před použitím je potřeba ověřit plný text.
- `smazat/Mullerova_Vicekriterialni_rozhodovani.url` - pouze odkaz, PDF je už v inspiraci.
- `smazat/Rysankova_Vicekriterialni_rozhodovani.url` - pouze odkaz, PDF je už v inspiraci.
- `smazat/PDBS2025.pdf` - prostorové databáze / Oracle Spatial, mimo hlavní zaměření práce.
- `smazat/E80817_01.zip` - archiv dokumentace Oracle, nyní nadbytečný vůči online dokumentaci.
- `smazat/Uvod_datove_modelovani.pdf` - slabší zdroj bez jasného bibliografického záznamu.
- `smazat/Vicekriterialni_metody_hodnoceni_2.pdf` - slidy; vhodnější je učební text Soukopové.
- `smazat/VRfinal.pdf` - slidy bez jasného bibliografického záznamu.
- `smazat/04-databazove-systemy.pdf` - přednáškové slidy (Honza Havelka, 5 stran), necitovatelné.
- `smazat/databazove_systemy.pdf` - skenované slidy (čistě obrázky), necitovatelné.
- `smazat/mcdm19(14)_7.pdf` - polský MCDM článek 2019, neidentifikovaný, není v ZDROJE.md.
- `smazat/pekin_et_al_ims2006.pdf` - neidentifikovaný konferenční článek 2006, skenované obrázky.
- `smazat/Codd_1970_A_relational_model.pdf` - duplicita, nahrazeno Codd_1970_Relational_model.pdf.
- `smazat/Codd_1970_A_relational_model (1).pdf` - duplicita z kořene literatura/.
- `smazat/Multiple criteria decision making techniques...pdf` - stará kopie Mardaniho, nahrazeno.
- `smazat/Alkahtani_2019_MCDM_supplier_selection_AHP_TOPSIS.pdf` - nezdokumentovaný soubor z inspirace.
- `smazat/fundamentals-of-database-systems.pdf` - menší duplicita Elmasriho, nahrazeno 7th Edition.
- `smazat/Ivanytska_DanceSport_scoring_2015.pdf` - práce o hodnocení tanečního sportu, tematicky zcela mimo.
- `smazat/Vopenka_Kvantitativni_analyza_projektu_2016.pdf` - práce o kvantitativní analýze projektů, tematicky mimo.

## 7. Poznámky k dalším úpravám textu práce

- **ROZHODNUTO (14. 6., finální):** všechny kvalifikační práce (Kašpar, Chotěnovský, Jandová, Vohradský, Jedlička) zůstávají jen jako **inspirace** a v textu se NEcitují. Citace jsou nahrazeny vlastněnými zdroji: §3 (návrh databází) → **Chlapek, Kučera a Palovská (2019)**; §8 (NoSQL) → **DB-Engines (2026)**; §7.3 (rank reversal) → **Saaty (2008)**.
- **Connolly & Begg (2015)** a **Sullivan (2015)** se zatím nedaří sehnat → přesunuty do sekce 5 (sehnat pro BP); v textu se NEcitují.
- V metodice je nyní potřeba hlídat, aby nebylo napsané, že práce vychází ze zdrojů, které jsou ve skutečnosti jen ve složce `literatura/inspirace`.
- **HOTOVO (16. 6.):** Seznam zdrojů je v souboru `Seminární práce 11.md`, seřazený abecedně a rozdělený na tištěné/internetové. Soubory `Seminární práce 12.md` a `13.md` jsou prázdné rezervy (NEPOUŽÍVAT).
- **HOTOVO (18. 6.):** Přidány 4 nové zdroje do bibliografie (SP 11) a zapracovány citace do kapitol 4–6: **Chen (1976)** — ER model, §5.1; **Watt a Eng (2014)** — open textbook BCcampus, §4.1, §4.3, §5.2; **Velasquez a Hester (2013)** — MCDM metody, §6.2; **Ishizaka a Labib (2011)** — AHP konzistence, §6.2. Celkem 18 citovaných zdrojů.
- **HOTOVO (18. 6., druhý průchod):** Přidány další 2 zdroje: **Codd (1970)** — relační model, §5.2 a §5.4; **Mardani et al. (2015)** — přehled MCDM, §6 úvod a §6.2. Navíc **Ishizaka a Labib (2011)** přidán i do §7.3. Celkem nyní **20 citovaných zdrojů**. PDF pro Codd a Mardani stáhnout ručně (viz sekce 5B a 2 výše). Zbývá sehnat knihy ze sekce 5A (Connolly, Elmasri, Garcia-Molina, Korth) pro BP.
