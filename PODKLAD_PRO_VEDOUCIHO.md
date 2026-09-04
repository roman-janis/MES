# Návrh obsahu bakalářské práce pro konzultaci

**Student:** Roman Janiš  
**Vedoucí:** Ing. et Ing. Martin Lněnička, Ph.D.  
**Pracovní název:** Komparace nástrojů pro návrh a vývoj databázových systémů pomocí AHP  
**Anglický název:** Comparison of Database Design and Development Tools Using AHP  
**Stav podkladu:** 28. 8. 2026

Tento podklad shrnuje navržený obsah a metodiku bakalářské práce. Teoretická část vychází z finální verze seminární práce a při převodu byly zachovány její původní formulace v co největším rozsahu. Kapitoly praktických výsledků, AHP vyhodnocení, diskuse a závěru mají připravenou úplnou strukturu, ale neobsahují smyšlená data; chybějící údaje jsou v pracovní verzi zřetelně označeny.

## Cíl práce

Hlavním cílem bakalářské práce je porovnat vybrané nástroje pro návrh a vývoj databázových systémů pomocí metody AHP a na základě výsledků formulovat doporučení pro jejich využití ve dvou modelových situacích. Porovnávány jsou Oracle SQL Developer Data Modeler, DBeaver Community Edition, MySQL Workbench Community Edition a pgModeler.

## Výzkumné otázky

- **VO1:** Jak se vybrané nástroje liší podle stanovených hodnoticích kritérií při provedení stejných modelovacích úloh?
- **VO2:** Který z porovnávaných nástrojů je podle metody AHP nejvhodnější pro modelovou malou organizaci a který pro modelovou středně velkou organizaci?
- **VO3:** Jak stabilní je výsledné pořadí nástrojů při změně vah vybraných kritérií?

## Navržená osnova

1. Úvod
2. Cíl práce a výzkumné otázky
3. Metodika práce
4. Databázové systémy
5. Datové modely
6. Vícekriteriální rozhodování
7. Nástroje pro návrh a vývoj databází
8. Návrh hodnoticích kritérií
9. Praktická komparace
10. Výsledky praktického testování
11. Vyhodnocení nástrojů metodou AHP
12. Diskuse výsledků a doporučení
13. Závěr
14. Seznam zdrojů
15. Přílohy

Tato osnova odpovídá bodům oficiálního zadání: vymezení problému a cíle, teoretická východiska, charakteristika nástrojů, definice kritérií, praktická komparace a vyhodnocení výsledků.

## Návrh zásad pro vypracování do STAGu

- Vymezit problém, cíl práce a výzkumné otázky.
- Zpracovat teoretická východiska databázových systémů, datového modelování a vícekriteriálního rozhodování.
- Charakterizovat vybrané nástroje pro návrh a vývoj databázových systémů a zdůvodnit jejich výběr.
- Definovat a operacionalizovat hodnoticí kritéria.
- Provést praktickou komparaci nástrojů na jednotném modelovém příkladu a výsledky vyhodnotit metodou AHP.
- Porovnat dva modelové scénáře, provést analýzu citlivosti a formulovat doporučení pro praxi.

## Navržený praktický postup

Společným modelovým příkladem je databáze malého cykloservisu s deseti entitami. Obsahuje vazby 1:N, dvě vazby M:N řešené asociačními entitami, vazbu 1:1, složené primární klíče, nepovinný cizí klíč, unikátní omezení a kontrolní omezení.

U každého nástroje budou ověřeny tyto oblasti:

1. vytvoření databázové struktury podle stejného textového zadání;
2. generování a spuštění DDL;
3. reverse engineering stejného referenčního schématu;
4. export diagramu a SQL;
5. záznam času, chyb, nutných zásahů, omezení edice a dokladů.

Výsledky budou hodnoceny podle osmi kritérií: K1 Funkcionalita, K2 Použitelnost, K3 Kompatibilita s DBMS, K4 Forward engineering, K5 Reverse engineering, K6 Dokumentace a komunitní podpora, K7 Import a export modelu a K8 Náklady a licenční omezení.

AHP bude zpracována pro dva scénáře. Scénář A představuje malou organizaci s vyšším významem použitelnosti a nákladů. Scénář B představuje středně velkou organizaci s vyšším významem funkcionality a kompatibility. U všech párových matic bude ověřena konzistence pomocí CR a na výsledky naváže analýza citlivosti.

## Body k odsouhlasení

1. **DBeaver Community Edition:** [Oficiální dokumentace DBeaver](https://dbeaver.com/docs/dbeaver/Edit-mode/) uvádí, že editace databázových objektů přímo v ER diagramu je funkcí edic Enterprise a Ultimate. V Community Edition proto navrhuji vytvořit stejnou strukturu na prázdném schématu přes dostupný editor databázových objektů a následně ji zobrazit v automaticky vytvořeném diagramu. Rozdíl proti samostatnému modelování bude součástí výsledku, nikoli skrytá odchylka protokolu.
2. **pgModeler:** [Aktuální produktové členění pgModeleru](https://www.pgmodeler.io/?source=true) v roce 2026 uvádí reverse engineering mezi funkcemi edice Plus, přičemž dostupnost se může lišit podle přesné verze a sestavení. Je vhodnější použít pro srovnání dostupnou Community variantu a nedostupnost funkce hodnotit jako omezení, nebo použít časově omezenou licenci Plus?
3. **Podpůrná aplikace:** Je dostačující správně zpracované AHP v kontrolovatelném výpočtovém souboru, nebo má být jednoduchá aplikace pevnou součástí výsledků práce?

## Návrh literatury pro zadávací list

1. ELMASRI, Ramez a Shamkant B. NAVATHE. *Fundamentals of Database Systems*. 7th ed. Boston: Pearson, 2016. ISBN 978-0-13-397077-7.
2. POKORNÝ, Jaroslav a Michal VALENTA. *Databázové systémy*. Praha: České vysoké učení technické v Praze, 2020. ISBN 978-80-01-06708-6.
3. CHLAPEK, Dušan, Jan KUČERA a Helena PALOVSKÁ. *Datové modelování a návrh relační databáze: Sbírka řešených úloh*. Praha: Vysoká škola ekonomická v Praze, Nakladatelství Oeconomica, 2019. ISBN 978-80-245-2331-6.
4. CARVALHO, Gonçalo, Sergii MYKOLYSHYN, Bruno CABRAL, Jorge BERNARDINO a Vasco PEREIRA. Comparative Analysis of Data Modeling Design Tools. *IEEE Access*. 2022, 10, 3351–3365. DOI: 10.1109/ACCESS.2021.3139071.
5. SAATY, Thomas L. How to make a decision: The Analytic Hierarchy Process. *European Journal of Operational Research*. 1990, 48(1), 9–26.

## Krátký text do e-mailu

Dobrý den,

posílám návrh cíle, výzkumných otázek, osnovy a praktického postupu bakalářské práce. Teoretická část vychází z finální seminární práce a snažil jsem se v ní zachovat původní text v co největším rozsahu. Praktické kapitoly mám zatím připravené strukturou; skutečné výsledky a AHP hodnoty doplním až po provedení testů.

Prosím zejména o názor na tři body uvedené v části „Body k odsouhlasení“: způsob zahrnutí DBeaver Community Edition, volbu edice pgModeleru a rozsah podpůrné AHP aplikace.

Děkuji.

S pozdravem  
Roman Janiš
