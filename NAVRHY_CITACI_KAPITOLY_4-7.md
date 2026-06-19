# Navrhy citaci a zdroju pro kapitoly 4-7

Pracovni soubor podle poznamky vedouciho z `Email konverzace.txt`: teorii je potreba vice opirat o literaturu, idealne 4-5 zdroju na kapitolu, u dulezitych tvrzeni i 2-3 zdroje najednou.

## Dulezite pravidlo k prebirani citaci

Neni v poradku vzit citaci z cizi bakalarske/diplomove prace a v textu se tvarit, ze jsem puvodni knihu nebo clanek sam cetl. Bezpecny postup je:

1. Cizi praci pouzit jen jako stopu k dohledani puvodniho zdroje.
2. Puvodni zdroj overit aspon pres DOI, stranku vydavatele, Google Scholar, knihovni katalog nebo dostupny nahled.
3. Teprve potom citovat puvodni zdroj.
4. Pokud puvodni zdroj nelze overit, pouzit sekundarni citaci ve tvaru napr. `(Connolly a Begg, 2015, cit. dle Novak, 2022)` a v seznamu literatury uvest zdroj, ktery byl skutecne pouzit. Pro BP je ale lepsi se sekundarnim citacim vyhnout.

Samotne bibliograficke udaje lze z jine prace pouzit jako voditko, ale text ani formulace z te prace se nekopiruji. Vlastni text prace musi byt parafraze oprena o dohledany zdroj.

## Soucasny stav kapitol 4-7

| Kapitola | Soucasne opory | Stav |
|---|---|---|
| 4 Databazove systemy | Pokorny a Valenta; Watt a Eng; Rosenthal a Reiner | Pouzitelne, ale pro pozadavek vedouciho by se hodil jeste jeden klasicky zdroj k DBMS/architekture/navrhu. |
| 5 Datove modely | Pokorny a Valenta; Chen; Chlapek, Kucera a Palovska; Watt a Eng | Uz relativne dobre. Nejlepsi doplneni je Codd (1970) k relacnimu modelu a normalizaci. |
| 6 Vicekriterialni rozhodovani | Saaty 1990; Saaty 2008; Soukopova; Velasquez a Hester; Ishizaka a Labib | Pocet zdroju je dobry, ale uvodni obecna definice MCDM je moc postavena na Saatym. Doporucuji pridat prehledovy clanek Mardani et al. |
| 7 Metoda AHP | Saaty 1990; Saaty 2008 | Nejslabsi kapitola z hlediska diverzity zdroju. Je potreba doplnit Ishizaka a Labib, Vaidya a Kumar, Ho, pripadne Simanaviciene a Vdovinskiene nebo Ebrahimi a Taheri. |

## Kandidati k doplneni bez shaneni knih

### Databaze a datove modely

1. **CODD, Edgar F.** A relational model of data for large shared data banks. *Communications of the ACM*. 1970, 13(6), 377-387. DOI: [10.1145/362384.362685](https://dl.acm.org/doi/10.1145/362384.362685).  
   Pouziti: kapitola 5.2 relacni model, 5.4 normalizace. Je to puvodni clanek k relacnimu modelu, lepsi nez odkazovat jen na ucebnici.

2. **MONGE, Alvaro.** *Database Design with UML and SQL*. 4th ed. [online]. California State University Long Beach. Dostupne z: <http://web.csulb.edu/colleges/coe/cecs/dbdesign/>.  
   Pouziti: kapitola 5.1 a 5.3, hlavne notace UML/ER a prechod k relacnimu modelu. Je to online ucebni text, ne clanek, ale muze pomoct jako dostupny zdroj.

3. **MARIA DB.** *Database Design Phase 2: Conceptual Design* [online]. MariaDB, 2026. Dostupne z: <https://mariadb.com/docs/general-resources/database-theory/database-design/database-design-phase-2-conceptual-design>.  
   Pouziti: jen doplnkove k fazim navrhu v kapitole 4.4. Neni to akademicky clanek, proto ho brat spis jako slabsi internetovy zdroj.

### MCDM a AHP

4. **MARDANI, Abbas, Ahmad JUSOH, Khalil MD NOR, Zainab KHALIFAH, Norhayati ZAKWAN a Alireza VALIPOUR.** Multiple criteria decision-making techniques and their applications - a review of the literature from 2000 to 2014. *Economic Research-Ekonomska Istraživanja*. 2015, 28(1), 516-571. DOI: [10.1080/1331677X.2015.1075139](https://www.tandfonline.com/doi/full/10.1080/1331677X.2015.1075139).  
   Pouziti: kapitola 6 uvod a 6.2; vhodne jako prehledovy clanek na podporu tvrzeni, ze MCDM zahrnuje vice kvantitativnich i kvalitativnich hledisek a ze AHP/TOPSIS/ELECTRE patri mezi pouzivane metody.

5. **VAIDYA, Omkarprasad S. a Sushil KUMAR.** Analytic hierarchy process: An overview of applications. *European Journal of Operational Research*. 2006, 169(1), 1-29. DOI: 10.1016/j.ejor.2004.04.028. Zaznam: <https://ideas.repec.org/a/eee/ejores/v169y2006i1p1-29.html>.  
   Pouziti: kapitola 7 uvod a 7.3; podpora tvrzeni, ze AHP je siroce aplikovana metoda vicekriterialniho rozhodovani.

6. **HO, William.** Integrated analytic hierarchy process and its applications: a literature review. *European Journal of Operational Research*. 2008, 186(1), 211-228. DOI: [10.1016/j.ejor.2007.01.004](https://doi.org/10.1016/j.ejor.2007.01.004). Zaznam: <https://research.aston.ac.uk/en/publications/integrated-analytic-hierarchy-process-and-its-applications-a-lite/>.  
   Pouziti: kapitola 7.3; AHP lze kombinovat s dalsimi metodami a vyuziva se v ruznych rozhodovacich ulohach.

7. **EBRAHIMI, Mahnaz a Masoud TAHERI.** Selection of Database Management System with Fuzzy-AHP for Electronic Medical Record. *International Journal of Information Engineering and Electronic Business*. 2015, 7(5), 1-6. DOI: [10.5815/ijieeb.2015.05.01](https://www.mecs-press.org/ijieeb/ijieeb-v7-n5/v7n5-1.html).  
   Pouziti: kapitola 7 nebo metodika BP; velmi relevantni, protoze se primo tyka vyberu DBMS metodou Fuzzy-AHP.
   Pozor: v `ZDROJE.md` je u tohoto zdroje uvedeno pravdepodobne chybne DOI `10.5815/ijieeb.2015.02.05` a strany `34-40`. Pred vlozenim do bibliografie opravit podle stranky casopisu.

8. **CATAK, Ferhat Ozgur, Seyma KARABAS a Selcuk YILDIRIM.** Fuzzy analytic hierarchy based DBMS selection in Turkish National Identity Card Management Project. 2012.  
   Pouziti: potenciálně kapitola 7/metodika BP, ale zatim nedoporucuji citovat, dokud nebude overena primarni publikace. Zatim jen stopa z referenci jinych clanku.

## Navrhy konkretniho zapracovani

### Kapitola 4

Soucasne ma 3 zdroje. Bez knih typu Connolly/Elmasri bych ji zatim neposiloval nasilu slabymi weby. Pokud je potreba rychle navysit oporu, pouzit MariaDB jen u fazi navrhu databaze, ale hlavni opora ma zustat Pokorny a Valenta + Watt a Eng + Rosenthal a Reiner.

Ukazka vlastni formulace:

> Faze navrhu databaze lze chapat jako postupne zpřesnovani popisu dat od konceptualniho pohledu pres logicke schema az po fyzickou implementaci v konkretnim DBMS. Toto cleneni pomaha oddelit pochopeni aplikační domeny od technickych detailu ulozeni dat, coz podporuje lepsi udrzitelnost navrhu (Pokorny a Valenta, 2020; Watt a Eng, 2014; Rosenthal a Reiner, 1994).

### Kapitola 5

Doporuceni: pridat Codd (1970) do 5.2 a 5.4.

Ukazka vlastni formulace pro 5.2:

> Relacni model patri mezi zakladni teoreticke kameny modernich databazovych systemu. Codd jej formuloval jako model zalozeny na relacich, ktery oddeluje logicky pohled na data od jejich fyzicke reprezentace a vytvari zaklad pro dotazovani, integritu a normalizaci dat (Codd, 1970; Pokorny a Valenta, 2020).

Ukazka vlastni formulace pro 5.4:

> Normalizace navazuje na snahu omezit redundanci a anomálie v relacnich schematech. V prakticke rovine se v uvodnim navrhu nejcasteji pracuje s prvni az treti normalni formou, protoze ty postihují hlavni problemy opakujicich se skupin, castečnych zavislosti a tranzitivnich zavislosti (Codd, 1970; Chlapek, Kucera a Palovska, 2019; Pokorny a Valenta, 2020).

### Kapitola 6

Doporuceni: pridat Mardani et al. (2015) do uvodu kapitoly 6 a 6.2. Tim se splni pokyn vedouciho k vyhledani prehledovych clanku o MCDM.

Ukazka vlastni formulace:

> Vicekriterialni rozhodovani se pouziva v ulohach, kde nelze kvalitu variant posoudit podle jedineho ukazatele. Prehledova literatura ukazuje, ze metody MCDM se pouzivaji napric technickymi, ekonomickymi i manazerskymi oblastmi a casto kombinuji kvantitativni i kvalitativni hlediska (Mardani et al., 2015; Velasquez a Hester, 2013; Soukopova, 2016).

### Kapitola 7

Doporuceni: doplnit nejmene 3 zdroje mimo Saatyho: Ishizaka a Labib (2011), Vaidya a Kumar (2006), Ho (2008). Pro vazbu na tema DBMS doplnit Ebrahimi a Taheri (2015).

Ukazka vlastni formulace pro uvod kapitoly:

> AHP je v literature popisovana jako rozsirena metoda vicekriterialniho rozhodovani, ktera prevadi rozhodovaci problem do hierarchicke struktury a pracuje s parovym porovnavanim prvku. Vedle puvodnich praci Saatyho existuje rada prehledovych clanku, ktere dokladaji siroke vyuziti AHP v praktickych rozhodovacich ulohach (Saaty, 1990; Saaty, 2008; Vaidya a Kumar, 2006; Ishizaka a Labib, 2011).

Ukazka vlastni formulace pro omezeni AHP:

> Praktickou vyhodou AHP je srozumitelny postup stanoveni priorit a moznost kontroly konzistence. Soucasne je ale metoda citliva na kvalitu subjektivnich usudku a pri vetsim poctu kriterii nebo alternativ rychle roste pocet potrebnych parovych porovnani (Saaty, 2008; Ishizaka a Labib, 2011; Ho, 2008).

Ukazka vlastni formulace pro vazbu na tema prace:

> V kontextu vyberu databazoveho reseni je AHP vhodna proto, ze umoznuje porovnavat technicka, ekonomicka i provozni kriteria v jedne rozhodovaci strukture. Podobny princip vyuzili Ebrahimi a Taheri pri vyberu DBMS pro elektronickou zdravotni dokumentaci, kde databazovy system hodnotili pomoci fuzzy rozsireni AHP (Ebrahimi a Taheri, 2015).

## Prioritni ukoly pred zapracovanim do hlavni prace

1. Opravit udaje Ebrahimi a Taheri v `ZDROJE.md`, pokud se budou pouzivat.
2. Pridat Codd (1970), Mardani et al. (2015), Vaidya a Kumar (2006), Ho (2008) a Ebrahimi a Taheri (2015) do `Seminární práce 11.md`.
3. Doplneni delat jen tam, kde text skutecne tvrzeni vyuziva. Nepridavat zdroj jen jako ozdobu za vetu.
4. Kvalifikacni prace z `literatura/inspirace` pouzivat jen jako orientacni stopu, ne jako zdroj textu a ne jako necitovanou predlohu.
