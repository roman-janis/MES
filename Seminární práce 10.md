# 10 Metodický rámec navazující praktické komparace

V navazující bakalářské práci bude postup praktické komparace strukturován do následujících kroků:

1. **Sestavení hierarchie AHP.** Na nejvyšší úrovni cíl „Výběr nejvhodnějšího nástroje pro návrh a vývoj databází", na druhé úrovni kritéria K1–K8, na třetí úrovni alternativy (Oracle SQL Developer Data Modeler, DBeaver, MySQL Workbench, pgModeler).
2. **Párové porovnání kritérií.** Sestavení Saatyho matice 8×8, výpočet vah jednotlivých kritérií metodou geometrického průměru řádků, kontrola konzistence (CR < 0,1).
3. **Testování nástrojů.** Na pracovní stanici autora budou nainstalovány nástroje z instalátorů uložených ve složce `nastroje/`. Na každém z nich bude proveden jednotný testovací scénář: vytvoření konceptuálního modelu malé doménové oblasti (např. evidenci objednávek), převod do relačního schématu, generování SQL skriptu pro PostgreSQL a MySQL, reverzní inženýrství z existujícího schématu.
4. **Párové porovnání alternativ vzhledem ke každému kritériu.** Pro každé kritérium vznikne Saatyho matice 4×4. U kritérií K3, K4 a K8 budou hodnoty opřeny o ověřitelná měřítka (počet podporovaných DBMS, počet kroků pro generování SQL, cena); u kritérií K2 a K6 půjde o kvalitativní hodnocení.
5. **Syntéza lokálních a globálních priorit.** Výsledné pořadí nástrojů vznikne jako vážený součet lokálních priorit přes všechna kritéria.
6. **Analýza citlivosti.** Bude sledováno, jak se mění výsledné pořadí při změně vah klíčových kritérií, zejména K1 (Funkcionalita) a K8 (Cena a licence).
7. **Doporučení pro praxi.** Na základě výsledků budou formulována doporučení pro typové scénáře malé a střední firmy, kde lze očekávat odlišné váhy kritérií než v scénáři čistě technickém.

