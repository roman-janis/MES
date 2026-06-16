# Zdroje a literatura

Aktualizace: 16. 6. 2026.

V práci je nyní **14 citovaných zdrojů**; v seznamu jsou seřazené abecedně a rozdělené na tištěné (Carvalho et al.; Chlapek, Kučera a Palovská; Pokorný a Valenta; Saaty 1990; Saaty 2008; Simanavičienė a Vdovinskienė) a internetové (DBeaver; DB-Engines; Laranjeiro a Pinto; MySQL; Oracle; pgModeler; PostgreSQL; Soukopová). Všechny in-text citace párují se seznamem.

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
  Umístění: `literatura/DB/4IT218-skripta-datové-modelování_ekniha.pdf`

- **JEDLIČKA, Jan.** *Key-value databázové systémy*. Ostrava, 2024. Diplomová práce. VŠB-TUO.  
  Umístění: `literatura/DB/JED0050_FEI_N2647_2612T025_2024.pdf`  
  Poznámka: ponecháno jako možný zdroj k širšímu přehledu databázových systémů. Pokud se v textu nebude řešit key-value / NoSQL oblast, není nutné ho citovat.

- **ROSENTHAL, Arnon a David S. REINER.** *Tools and Transformations - Rigorous and Otherwise - for Practical Database Design*. ACM Transactions on Database Systems, 1994.  
  Umístění: `literatura/DB/176567.176568.pdf`  
  Poznámka: vhodné spíše pro BP, pokud se bude řešit návrh databáze, transformace modelů a nástroje podporující návrh.

- **CARVALHO, Gonçalo, Sergii MYKOLYSHYN, Bruno CABRAL, Jorge BERNARDINO a Vasco PEREIRA.** Comparative Analysis of Data Modeling Design Tools. *IEEE Access*. 2022, 10, 3351-3365. DOI: 10.1109/ACCESS.2021.3139071.  
  Umístění: `literatura/DB/Comparative_Analysis_of_Data_Modeling_Design_Tools.pdf`

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
  Umístění: `literatura/AHP/Studijni_text_metody_vicekriterialniho_rozhodovani.pdf`

- **SAATY, Thomas L.** How to make a decision: The Analytic Hierarchy Process. *European Journal of Operational Research*. 1990, 48(1), 9-26.  
  Umístění: `literatura/AHP/Saaty_1990_How_to_make_a_decision_AHP.pdf`

- **SAATY, Thomas L.** Decision making with the analytic hierarchy process. *International Journal of Services Sciences*. 2008, 1(1), 83-98.  
  Umístění: `literatura/AHP/Saaty_2008_Decision_making_with_AHP.pdf`

- **SIMANAVIČIENĖ, Rūta a Sonata VDOVINSKIENĖ.** Selection of Computer-Aided Design Software Systems Using the AHP Method. *Baltic Journal of Modern Computing*. 2023, 11(2), 272-284. DOI: 10.22364/bjmc.2023.11.2.04.  
  Umístění: `literatura/AHP/11_2_04_Simanaviciene.pdf`

## 3. Inspirace a vzory, které necitovat jako zdroje

Tyto soubory jsou přesunuté do `literatura/inspirace`. Slouží pro orientaci, porovnání struktury, formulaci metodiky nebo praktický postup. Nemají být běžně uváděné v seznamu literatury práce.

### Inspirace k databázím a návrhu databáze

- `literatura/inspirace/DB/Kaspar_bc_final.pdf` - Zbyněk Kašpar, *Databázové systémy v praxi*, BP 2012.
- `literatura/inspirace/DB/Chotenovsky_Tvorba_datovych_modelu_2023.pdf` - Tomáš Chotěnovský, BP 2023. Inspirace (necitováno; §3 a návrh databáze jsou opřeny o Chlapek, Kučera a Palovská, 2019).
- `literatura/inspirace/DB/Smahel_Porovnani_CASE_nastroju_2018.pdf` - David Šmahel, *Porovnání CASE nástrojů se zaměřením na podporu návrhu databáze*, BP 2018.

### Inspirace k AHP a vícekriteriálnímu rozhodování

- `literatura/inspirace/AHP/Bunruamkaew_How_to_do_AHP_analysis_in_Excel_2012.pdf` - praktický návod k výpočtu AHP v Excelu.
- `literatura/inspirace/AHP/Fruhauf_Vyber_dodavatele_MCDM_2025.pdf` - ukázka použití vícekriteriálního rozhodování.
- `literatura/inspirace/AHP/Jandova_AHP_jeji_silne_a_slabe_stranky.pdf` - Věra Jandová, DP 2012. Inspirace (necitováno).
- `literatura/inspirace/AHP/Mullerova_Vicekriterialni_rozhodovani_2020.pdf` - ukázka zpracování tématu vícekriteriálního rozhodování.
- `literatura/inspirace/AHP/Rysankova_Vicekriterialni_rozhodovani_2021.pdf` - ukázka zpracování tématu vícekriteriálního rozhodování.
- `literatura/inspirace/AHP/Vasileva_Metody_rozhodovani_2022.pdf` - ukázka metod vícekriteriálního rozhodování.
- `literatura/inspirace/AHP/Vohradsky_Pouziti_metod_vicekriterialniho_rozhodovani_pri_rizeni_podniku.pdf` - Marek Vohradský, DP 2016. Inspirace (necitováno).
- `literatura/inspirace/AHP/Zadina_Vicekriterialni_rozhodovani_2022.pdf` - ukázka použití vícekriteriálního rozhodování.
- `literatura/inspirace/AHP/Patykova_Vicekriterialni_rozhodovani_2017.pdf` - ukázka vícekriteriálního rozhodování ve firemní praxi.

### Ostatní inspirace

- `literatura/inspirace/ostatni/Ivanytska_DanceSport_scoring_2015.pdf` - spíše ukázka kvantitativního hodnocení, tematicky mimo databázové nástroje.
- `literatura/inspirace/ostatni/Vopenka_Kvantitativni_analyza_projektu_2016.pdf` - spíše ukázka kvantitativní analýzy, tematicky mimo databázové nástroje.

## 4. Materiály k zadání a požadavkům

- `zadani/vskp_-_zadani_vskp.pdf` - oficiální zadání BP.
- `zadani/vskp_-_udaje_o_vskp.pdf` - údaje o VŠKP ze STAGu.
- `Email konverzace.txt` - e-mailová komunikace s požadavky a poznámkami vedoucího.
- `POZADAVKY_UCITELE.md` - pracovní souhrn toho, co chtěl vedoucí a co z toho plyne pro práci.
- `oliva/pokyny/` - pravidla MES, metodické pokyny FIM UHK, citace a formát.
- `oliva/sablony/` - šablony seminární práce.

## 5. Zdroje vhodné dohledat nebo doplnit pro BP

Tyto zdroje zatím nejsou uložené jako soubory, ale mohou se hodit pro silnější teoretickou oporu BP.

- **CONNOLLY, Thomas a Carolyn BEGG.** *Database Systems: A Practical Approach to Design, Implementation, and Management*. 6th ed. Pearson, 2015. — **SEHNAT** (silný zdroj k návrhu databází; zatím nedohledán, ISBN ověřit).
- **SULLIVAN, Dan.** *NoSQL for Mere Mortals*. Addison-Wesley, 2015. ISBN 0-13-402321-8. — **SEHNAT** (k NoSQL; zatím nedohledán).
- **RAMÍK, Jiří.** *Vícekriteriální rozhodování: analytický hierarchický proces (AHP)*. Karviná: Slezská univerzita v Opavě, 1999.
- **FIALA, Petr.** *Modely a metody rozhodování*. Praha: Oeconomica, 2013.
- **FOTR, Jiří a Lenka ŠVECOVÁ.** *Manažerské rozhodování*. Praha: Ekopress, 2016.
- **DATE, C. J.** *An Introduction to Database Systems*. 8th ed. Pearson/Addison Wesley, 2004.
- **RAMAKRISHNAN, Raghu a Johannes GEHRKE.** *Database Management Systems*. 3rd ed. McGraw-Hill, 2002.
- **CODD, Edgar F.** A Relational Model for Large Shared Data Banks. *Communications of the ACM*. 1970.
- **CATAK, M. Kemal, N. KARABAS a S. YILDIRIM.** A Fuzzy AHP-based Decision Model for Database Management System Selection. *IJASUC*. 2012, 3(4), 19-30. DOI: 10.5121/ijasuc.2012.3402.
- **EBRAHIMI, Seyed Babak a Maryam TAHERI.** Selection of Database Management System Using Fuzzy AHP. *IJIEEB*. 2015, 7(2), 34-40. DOI: 10.5815/ijieeb.2015.02.05.

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

## 7. Poznámky k dalším úpravám textu práce

- **ROZHODNUTO (14. 6., finální):** všechny kvalifikační práce (Kašpar, Chotěnovský, Jandová, Vohradský, Jedlička) zůstávají jen jako **inspirace** a v textu se NEcitují. Citace jsou nahrazeny vlastněnými zdroji: §3 (návrh databází) → **Chlapek, Kučera a Palovská (2019)**; §8 (NoSQL) → **DB-Engines (2026)**; §7.3 (rank reversal) → **Saaty (2008)**.
- **Connolly & Begg (2015)** a **Sullivan (2015)** se zatím nedaří sehnat → přesunuty do sekce 5 (sehnat pro BP); v textu se NEcitují.
- V metodice je nyní potřeba hlídat, aby nebylo napsané, že práce vychází ze zdrojů, které jsou ve skutečnosti jen ve složce `literatura/inspirace`.
- **HOTOVO (16. 6.):** Seznam zdrojů je v souboru `Seminární práce 11.md`, seřazený abecedně a rozdělený na tištěné/internetové. Soubory `Seminární práce 12.md` a `13.md` jsou prázdné rezervy (NEPOUŽÍVAT).
