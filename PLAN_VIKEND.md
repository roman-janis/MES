# Plán práce na víkend 29.–30. srpna 2026

## Způsob práce se soubory bakalářské práce

Bakalářská práce zůstává rozdělena do samostatných kapitol `BP 0.md` až
`BP 15.md`. Upravují se vždy jednotlivé kapitoly, nikoli celý sloučený dokument.
Soubor `BP.md` slouží pouze jako automaticky vytvořený náhled celé práce a
obnovuje se příkazem:

```powershell
.\spoj.ps1
```

Rozdělení kapitol:

| Soubor | Obsah |
|---|---|
| `BP 0.md` | Titulní strany, abstrakt a klíčová slova |
| `BP 1.md` | Úvod |
| `BP 2.md` | Cíl práce a výzkumné otázky |
| `BP 3.md` | Metodika práce |
| `BP 4.md` | Databázové systémy |
| `BP 5.md` | Datové modely a návrh databáze |
| `BP 6.md` | Vícekriteriální rozhodování a AHP |
| `BP 7.md` | Porovnávané databázové nástroje |
| `BP 8.md` | Hodnoticí kritéria |
| `BP 9.md` | Praktická komparace |
| `BP 10.md` | Výsledky testování |
| `BP 11.md` | AHP vyhodnocení |
| `BP 12.md` | Diskuse |
| `BP 13.md` | Závěr |
| `BP 14.md` | Seznam zdrojů |
| `BP 15.md` | Přílohy |

## Hlavní cíl víkendu

Minimálním cílem je:

1. prostudovat tři použitelné zdroje a pořídit si z nich poznámky,
2. dokončit celý test alespoň jednoho databázového nástroje,
3. vytvořit a kontrolním příkladem ověřit základ souboru `AHP_vypocet.xlsx`,
4. průběžně ukládat skutečné výsledky, časy a snímky obrazovky.

Pokud zbude čas, dokončí se testování dalších dvou dostupných nástrojů.
Reálné AHP matice se nevyplňují dříve, než budou získány výsledky praktických
testů.

## Literatura ke studiu

### 1. Tomeš a Alcnauer – konzistence AHP

Prostudovat článek *Konzistence matice párových porovnání při použití
Analytického hierarchického procesu (AHP)*. Zaměřit se na:

- sestavení matice párových porovnání,
- výpočet vah,
- vlastní vektor,
- index konzistence CI,
- poměr konzistence CR,
- použití Excelu.

Vyřešeno (28. 8.): `literatura/AHP/Tomes_Alcnauer_2014_AHP_konzistence_matice.pdf`
byl nahrazen správným článkem staženým přímo z časopisu Business & IT:
<https://bit.fsv.cvut.cz/issues/02-14/full_02-14_06.pdf>.

Výstup: 5–8 vlastních poznámek použitelných v `BP 6.md` nebo `BP 11.md`.

### 2. Vlčková a Friebel – praktické použití AHP

Prostudovat místní soubor
`literatura/AHP/Vlckova_Friebel_2015_AHP_outsourcing_uctectnictvi.pdf`.
Ve skutečnosti jde o článek:

> VLČKOVÁ, Miroslava a Ludvík FRIEBEL. Návrh metodiky na hodnocení kvality
> dat finančního účetnictví metodou AHP. *Český finanční a účetní časopis*.
> 2015, 10(2), 58–69. DOI: 10.18267/j.cfuc.443.

Zaměřit se na:

- rozdělení rozhodovacího problému do hierarchie,
- výběr a seskupení kritérií,
- stanovení vah kritérií,
- použití expertního hodnocení,
- interpretaci výsledků.

Výstup: 5–8 vlastních poznámek použitelných v `BP 3.md`, `BP 6.md` nebo
`BP 12.md`.

### 3. Otte – databázové systémy

Prostudovat pouze relevantní části souboru
`literatura/DB/Otte_2013_Databazove_systemy_VSBTUO.pdf`, nikoli celých
189 stran. Zaměřit se na:

- konceptuální návrh databáze,
- entity, atributy a vztahy,
- kardinality a parcialitu,
- ER model,
- relační datový model,
- integritní omezení,
- přechod od návrhu k implementaci.

Výstup: poznámky použitelné v `BP 4.md`, `BP 5.md` a při zdůvodnění modelu
cykloservisu v `BP 9.md`.

Po skutečném použití těchto tří zdrojů bude možné doplnit bibliografické
záznamy do `BP 14.md`. Nestačí je pouze přidat do seznamu; v textu musí být
alespoň jednou věcně použity a citovány.

## Sobota 29. srpna 2026

### Dopoledne – zdroje

| Čas | Úkol | Očekávaný výstup |
|---|---|---|
| 9:00–10:00 | Tomeš a Alcnauer | Poznámky ke konzistenci AHP |
| 10:15–11:30 | Vlčková a Friebel | Poznámky k praktickému použití AHP |
| 11:45–12:30 | Vybrané části Otteho | Poznámky k návrhu databáze |

U každého zdroje zapsat:

- úplný bibliografický údaj,
- hlavní myšlenku zdroje,
- 3–5 tvrzení využitelných v práci,
- kapitolu BP, do které tvrzení patří,
- číslo strany, na které se tvrzení nachází.

### Odpoledne – příprava a první praktický test

| Čas | Úkol | Očekávaný výstup |
|---|---|---|
| 14:00–15:00 | Zkontrolovat Docker a instalace nástrojů | Připravené databáze a alespoň jeden funkční nástroj |
| 15:00–17:00 | Kompletní test MySQL Workbench | Časy, pozorování, DDL, diagram a snímky |
| 17:00–17:30 | Uspořádat výsledky | Vyplněný protokol a pojmenované snímky |

Při testu zaznamenat:

1. čas vytvoření struktury cykloservisu,
2. postup a problémy při forward engineeringu,
3. výsledek reverse engineeringu,
4. dostupné možnosti exportu,
5. pozorování ke kritériím K1–K8,
6. přesnou verzi a edici nástroje.

## Neděle 30. srpna 2026

### Dopoledne – další nástroje

| Čas | Úkol | Očekávaný výstup |
|---|---|---|
| 9:00–10:30 | Test Oracle SQL Developer Data Modeler | Protokol, DDL, diagram a snímky |
| 10:45–12:15 | Test DBeaver Community | Protokol včetně omezení modelování |

U DBeaveru výslovně zaznamenat, zda použitá komunitní edice umožňuje
model-first návrh, nebo pouze práci s diagramem nad databázovým schématem.
Nedostupnou funkci neobcházet bez uvedení změny pracovního postupu.

### Odpoledne – kontrolní AHP Excel a shrnutí

| Čas | Úkol | Očekávaný výstup |
|---|---|---|
| 13:30–15:30 | Založit `AHP_vypocet.xlsx` podle `AHP_NAVOD_SAATY.md` | Listy a vzorce pro matice, váhy, CI a CR |
| 15:30–16:30 | Ověřit Excel kontrolním příkladem | Shoda s výsledky v kapitole 5 návodu |
| 16:45–17:30 | Sepsat shrnutí víkendu | Hotové výsledky a seznam otevřených bodů |

Reálné hodnoty do matic K1–K8 a hodnocení čtyř nástrojů zatím nevymýšlet.
Budou sestaveny až podle dokončených protokolů všech nástrojů.

## pgModeler

O víkendu ověřit, jaká přesná verze a edice je skutečně dostupná. Community
Edition nemusí poskytovat reverse engineering a hotový instalační balíček pro
Windows. Pokud nebude možné porovnat stejný rozsah funkcí jako u ostatních
nástrojů, zapsat tuto skutečnost jako otevřenou otázku pro vedoucího. Bez
výslovného uvedení se nesmí zaměnit Community a Plus.

## Kontrola na konci víkendu

- [ ] Správné PDF Tomeše a Alcnauera je získané a přečtené.
- [ ] U tří zdrojů existují poznámky včetně čísel stran.
- [ ] Je dokončen alespoň jeden celý test nástroje.
- [ ] U každého testu jsou zaznamenané skutečné časy a problémy.
- [ ] Snímky obrazovky jsou pojmenované podle nástroje a kroku.
- [ ] `AHP_vypocet.xlsx` dává na kontrolním příkladu správné výsledky.
- [ ] Do reálných AHP matic nebyly doplněny vymyšlené hodnoty.
- [ ] Je sepsán seznam otevřených otázek pro vedoucího.

## Co má být v neděli večer hotové

### Minimální varianta

- tři prostudované zdroje s použitelnými poznámkami,
- jeden kompletně otestovaný nástroj,
- funkční základ AHP Excelu ověřený kontrolním příkladem.

### Ideální varianta

- splněná minimální varianta,
- dokončené testy MySQL Workbench, Oracle Data Modeleru a DBeaveru,
- připravené shrnutí výsledků a otázka k edici pgModeleru pro vedoucího.

