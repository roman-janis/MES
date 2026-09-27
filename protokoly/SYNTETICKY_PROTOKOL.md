# Syntetický protokol – 27. 9. 2026

**Všech 204 známek je náhodných. Žádný z uvedených testů tímto záznamem není doložen jako provedený.**

Známky: 1 nejlepší, 5 nejhorší. Zdroj úloh: původní hodnoceni_4_nastroju.xlsx. AHP preference jsou samostatně generované vstupy; nejsou převodem známek.

## 1.1 – Založení prázdného modelu nebo diagramu (Krok 1 – vytvoření struktury)

Kritérium: K1

**Úloha:** Otevři nový projekt/model a prázdný ER diagram. Ulož jej, zavři a znovu otevři. Zatím nepoužívej import SQL ani existující databázi.

**Očekávání ze zadání:** Samostatný model lze uložit bez DB. Pokud edice offline model neumí, zapiš omezení a pro další úkony použij prázdné testovací schéma a dostupný editor tabulek. Tento DB-first postup výslovně rozlišuj.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 3 | 5 | 2 | 2 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Uložený model a snímek prázdného diagramu.

## 1.2 – Model-first bez živé databáze (Krok 1 – vytvoření struktury)

Kritérium: K1

**Úloha:** Odpoj databázi a zkus v modelu vytvořit tabulku zkouska se sloupcem id INT. Pak zkušební tabulku odstraň.

**Očekávání ze zadání:** Tabulka se vytvoří a uloží bez živé DB = model-first. Pokud je nutná DB, zapiš DB-first a skutečný postup. Neschopnost samostatného modelu nepřepisuj jako úspěch model-first.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 5 | 3 | 1 | 2 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Poznámka model-first / DB-first a případné chybové hlášení.

## 1.3 – Vytvoření všech 11 tabulek (Krok 1 – vytvoření struktury)

Kritérium: K1

**Úloha:** Vytvoř 11 tabulek podle následujících bodů 1.3a–1.3k. Použij stejné názvy ve všech nástrojích. Klíče a omezení potom nastav podle dalších testů.

**Očekávání ze zadání:** V modelu je přesně 11 tabulek. Původní známka tohoto bodu se vztahuje k dřívějšímu zadání 10 tabulek. Po rozšíření ji znovu posuď. Podrobný slovník je také v listu Model a pravidla.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 1 | 2 | 1 | 1 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Celý diagram se všemi 11 tabulkami.

## 1.3a – Vytvořit zakaznik

Kritérium: K1

**Úloha:** Vytvoř tabulku zakaznik a sloupce:
id_zakaznik : INT; NOT NULL
jmeno : VARCHAR(50); NOT NULL
prijmeni : VARCHAR(50); NOT NULL
telefon : VARCHAR(20); NULL povolen
email : VARCHAR(100); NULL povolen
adresa : VARCHAR(200); NULL povolen
datum_registrace : DATE; NOT NULL

**Očekávání ze zadání:** Přesné názvy a typy podle zadání. PK, FK, UNIQUE, DEFAULT a CHECK nastav v dalších bodech. Typ přizpůsob cílové DB podle Model a pravidla. Nevytvářej nevyžádané sloupce.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 2 | 2 | 2 | 5 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail tabulky. Známka dílčího vytvoření je volitelná; celkové vytvoření tabulek hodnoť v 1.3.

## 1.3b – Vytvořit zamestnanec

Kritérium: K1

**Úloha:** Vytvoř tabulku zamestnanec a sloupce:
id_zamestnanec : INT; NOT NULL
jmeno : VARCHAR(50); NOT NULL
prijmeni : VARCHAR(50); NOT NULL
pozice : VARCHAR(30); NOT NULL
telefon : VARCHAR(20); NULL povolen
datum_nastupu : DATE; NOT NULL

**Očekávání ze zadání:** Přesné názvy a typy podle zadání. PK, FK, UNIQUE, DEFAULT a CHECK nastav v dalších bodech. Typ přizpůsob cílové DB podle Model a pravidla. Nevytvářej nevyžádané sloupce.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 3 | 5 | 4 | 4 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail tabulky. Známka dílčího vytvoření je volitelná; celkové vytvoření tabulek hodnoť v 1.3.

## 1.3c – Vytvořit dodavatel

Kritérium: K1

**Úloha:** Vytvoř tabulku dodavatel a sloupce:
id_dodavatel : INT; NOT NULL
nazev : VARCHAR(100); NOT NULL
kontaktni_osoba : VARCHAR(100); NULL povolen
telefon : VARCHAR(20); NULL povolen
email : VARCHAR(100); NULL povolen

**Očekávání ze zadání:** Přesné názvy a typy podle zadání. PK, FK, UNIQUE, DEFAULT a CHECK nastav v dalších bodech. Typ přizpůsob cílové DB podle Model a pravidla. Nevytvářej nevyžádané sloupce.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 2 | 5 | 1 | 3 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail tabulky. Známka dílčího vytvoření je volitelná; celkové vytvoření tabulek hodnoť v 1.3.

## 1.3d – Vytvořit kolo

Kritérium: K1

**Úloha:** Vytvoř tabulku kolo a sloupce:
id_kolo : INT; NOT NULL
id_zakaznik : INT; NOT NULL
znacka : VARCHAR(50); NOT NULL
model : VARCHAR(50); NULL povolen
typ : VARCHAR(30); NULL povolen
rok_vyroby : SMALLINT; NULL povolen
seriove_cislo : VARCHAR(50); NULL povolen

**Očekávání ze zadání:** Přesné názvy a typy podle zadání. PK, FK, UNIQUE, DEFAULT a CHECK nastav v dalších bodech. Typ přizpůsob cílové DB podle Model a pravidla. Nevytvářej nevyžádané sloupce.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 4 | 5 | 2 | 5 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail tabulky. Známka dílčího vytvoření je volitelná; celkové vytvoření tabulek hodnoť v 1.3.

## 1.3e – Vytvořit elektrokolo

Kritérium: K1

**Úloha:** Vytvoř tabulku elektrokolo a sloupce:
id_kolo : INT; NOT NULL
vyrobce_motoru : VARCHAR(80); NOT NULL
vykon_motoru_w : INT; NOT NULL
kapacita_baterie_wh : DECIMAL(8,2); NOT NULL

**Očekávání ze zadání:** Přesné názvy a typy podle zadání. PK, FK, UNIQUE, DEFAULT a CHECK nastav v dalších bodech. Typ přizpůsob cílové DB podle Model a pravidla. Nevytvářej nevyžádané sloupce.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 2 | 5 | 2 | 4 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail tabulky. Známka dílčího vytvoření je volitelná; celkové vytvoření tabulek hodnoť v 1.3.

## 1.3f – Vytvořit sluzba

Kritérium: K1

**Úloha:** Vytvoř tabulku sluzba a sloupce:
id_sluzba : INT; NOT NULL
nazev : VARCHAR(100); NOT NULL
popis : VARCHAR(300); NULL povolen
cena_zakladni : DECIMAL(10,2); NOT NULL
odhad_doby_min : INT; NULL povolen

**Očekávání ze zadání:** Přesné názvy a typy podle zadání. PK, FK, UNIQUE, DEFAULT a CHECK nastav v dalších bodech. Typ přizpůsob cílové DB podle Model a pravidla. Nevytvářej nevyžádané sloupce.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 4 | 1 | 1 | 1 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail tabulky. Známka dílčího vytvoření je volitelná; celkové vytvoření tabulek hodnoť v 1.3.

## 1.3g – Vytvořit dil

Kritérium: K1

**Úloha:** Vytvoř tabulku dil a sloupce:
id_dil : INT; NOT NULL
nazev : VARCHAR(100); NOT NULL
cena_prodejni : DECIMAL(10,2); NOT NULL
mnozstvi_sklad : INT; NOT NULL
id_dodavatel : INT; NULL povolen

**Očekávání ze zadání:** Přesné názvy a typy podle zadání. PK, FK, UNIQUE, DEFAULT a CHECK nastav v dalších bodech. Typ přizpůsob cílové DB podle Model a pravidla. Nevytvářej nevyžádané sloupce.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 4 | 5 | 4 | 2 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail tabulky. Známka dílčího vytvoření je volitelná; celkové vytvoření tabulek hodnoť v 1.3.

## 1.3h – Vytvořit zakazka

Kritérium: K1

**Úloha:** Vytvoř tabulku zakazka a sloupce:
id_zakazka : INT; NOT NULL
id_kolo : INT; NOT NULL
id_zamestnanec : INT; NULL povolen
datum_prijeti : TIMESTAMP; NOT NULL
datum_dokonceni : TIMESTAMP; NULL povolen
stav : VARCHAR(20); NOT NULL
poznamka : VARCHAR(500); NULL povolen

**Očekávání ze zadání:** Přesné názvy a typy podle zadání. PK, FK, UNIQUE, DEFAULT a CHECK nastav v dalších bodech. Typ přizpůsob cílové DB podle Model a pravidla. Nevytvářej nevyžádané sloupce.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 3 | 2 | 4 | 1 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail tabulky. Známka dílčího vytvoření je volitelná; celkové vytvoření tabulek hodnoť v 1.3.

## 1.3i – Vytvořit zakazka_sluzba

Kritérium: K1

**Úloha:** Vytvoř tabulku zakazka_sluzba a sloupce:
id_zakazka : INT; NOT NULL
id_sluzba : INT; NOT NULL
mnozstvi : INT; NOT NULL
cena_za_jednotku : DECIMAL(10,2); NOT NULL

**Očekávání ze zadání:** Přesné názvy a typy podle zadání. PK, FK, UNIQUE, DEFAULT a CHECK nastav v dalších bodech. Typ přizpůsob cílové DB podle Model a pravidla. Nevytvářej nevyžádané sloupce.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 4 | 4 | 3 | 5 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail tabulky. Známka dílčího vytvoření je volitelná; celkové vytvoření tabulek hodnoť v 1.3.

## 1.3j – Vytvořit zakazka_dil

Kritérium: K1

**Úloha:** Vytvoř tabulku zakazka_dil a sloupce:
id_zakazka : INT; NOT NULL
id_dil : INT; NOT NULL
mnozstvi : INT; NOT NULL
cena_za_jednotku : DECIMAL(10,2); NOT NULL

**Očekávání ze zadání:** Přesné názvy a typy podle zadání. PK, FK, UNIQUE, DEFAULT a CHECK nastav v dalších bodech. Typ přizpůsob cílové DB podle Model a pravidla. Nevytvářej nevyžádané sloupce.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 5 | 4 | 1 | 2 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail tabulky. Známka dílčího vytvoření je volitelná; celkové vytvoření tabulek hodnoť v 1.3.

## 1.3k – Vytvořit faktura

Kritérium: K1

**Úloha:** Vytvoř tabulku faktura a sloupce:
id_faktura : INT; NOT NULL
id_zakazka : INT; NOT NULL
datum_vystaveni : DATE; NOT NULL
castka_celkem : DECIMAL(10,2); NOT NULL
zpusob_platby : VARCHAR(20); NOT NULL
stav_platby : VARCHAR(20); NOT NULL

**Očekávání ze zadání:** Přesné názvy a typy podle zadání. PK, FK, UNIQUE, DEFAULT a CHECK nastav v dalších bodech. Typ přizpůsob cílové DB podle Model a pravidla. Nevytvářej nevyžádané sloupce.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 5 | 1 | 4 | 1 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail tabulky. Známka dílčího vytvoření je volitelná; celkové vytvoření tabulek hodnoť v 1.3.

## 1.4 – Primární klíče a automatické číslování (Krok 1 – vytvoření struktury)

Kritérium: K1

**Úloha:** Nastav automaticky číslované PK: zakaznik.id_zakaznik; zamestnanec.id_zamestnanec; dodavatel.id_dodavatel; kolo.id_kolo; sluzba.id_sluzba; dil.id_dil; zakazka.id_zakazka; faktura.id_faktura.

**Očekávání ze zadání:** Těchto osm tabulek má jeden jednosloupcový PK a automatické ID. Elektrokolo automatické ID NEMÁ. Spojovací tabulky nemají samostatné id: použijí složený PK v 1.5.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 1 | 1 | 2 | 2 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail nastavení PK u jedné běžné tabulky.

## 1.5 – Složené primární klíče v asociačních tabulkách (Krok 1 – vytvoření struktury)

Kritérium: K1

**Úloha:** V zakazka_sluzba propoj id_zakazka → zakazka.id_zakazka a id_sluzba → sluzba.id_sluzba. OBA sloupce společně označ jako JEDEN PK. V zakazka_dil proveď totéž pro id_zakazka a id_dil → dil.id_dil.

**Očekávání ze zadání:** PRIMARY KEY (id_zakazka, id_sluzba) a PRIMARY KEY (id_zakazka, id_dil). Každá tabulka má dva FK, ale jeden složený PK. Oba sloupce jsou NOT NULL. Žádné třetí automatické id ani dva oddělené primární klíče.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 5 | 3 | 1 | 3 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail PRIMARY indexu obou asociačních tabulek.

## 1.6 – Vlastní atributy asociačních tabulek (Krok 1 – vytvoření struktury)

Kritérium: K1

**Úloha:** V obou spojovacích tabulkách nastav mnozstvi INT NOT NULL a cena_za_jednotku DECIMAL(10,2) NOT NULL.

**Očekávání ze zadání:** Množství ani cena nejsou součástí PK/FK. Jedna dvojice zakázka–služba/díl se vyskytuje jednou; opakování vyjadřuje množství. Cena je cena při opravě, nezávislá na pozdější změně ceníku.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 3 | 2 | 3 | 5 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail sloupců obou asociačních tabulek.

## 1.7 – Běžné cizí klíče a směry vazeb (Krok 1 – vytvoření struktury)

Kritérium: K1

**Úloha:** Propoj kolo.id_zakaznik → zakaznik.id_zakaznik; zakazka.id_kolo → kolo.id_kolo; dil.id_dodavatel → dodavatel.id_dodavatel. První dva FK jsou NOT NULL; dodavatel dílu může být NULL.

**Očekávání ze zadání:** FK leží na straně N. Kolo musí mít zákazníka a zakázka kolo. Nástroj nesmí vytvořit další sloupec pro vazbu vedle již připraveného FK. Ve všech vazbách ponech zákaz mazání odkazovaného rodiče, bez kaskády.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 4 | 5 | 4 | 5 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Diagram s čitelnými kardinalitami a detail Foreign Keys.

## 1.8 – Nepovinný cizí klíč zaměstnance u zakázky (Krok 1 – vytvoření struktury)

Kritérium: K1

**Úloha:** V zakazka propoj id_zamestnanec → zamestnanec.id_zamestnanec. U tohoto sloupce vypni NOT NULL / NN.

**Očekávání ze zadání:** Zakázka smí mít id_zamestnanec = NULL. Pokud ID vyplníš, musí existovat odpovídající zaměstnanec. NULL není číslo 0 ani prázdný text.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 5 | 3 | 2 | 5 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail nullable FK zakazka.id_zamestnanec.

## 1.9 – Vazba 1:1 Zakázka–Faktura (Krok 1 – vytvoření struktury)

Kritérium: K1

**Úloha:** Ve faktura ponech id_faktura jako vlastní PK. Sloupec id_zakazka nastav jako FK → zakazka.id_zakazka, NOT NULL a samostatné UNIQUE.

**Očekávání ze zadání:** Zakázka má 0 nebo 1 fakturu; každá faktura právě jednu zakázku. faktura.id_zakazka NENÍ PK. Pokud tlačítko 1:1 změní PK, oprav to a zapiš zásah.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 3 | 5 | 5 | 5 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail PK, FK a UNIQUE v tabulce faktura.

## 1.10 – UNIQUE mimo primární klíč (Krok 1 – vytvoření struktury)

Kritérium: K1

**Úloha:** Vytvoř samostatné UNIQUE pro zakaznik.email, kolo.seriove_cislo a faktura.id_zakazka. První dva sloupce mohou být NULL, třetí je NOT NULL.

**Očekávání ze zadání:** Jde o tři oddělená omezení. Dva stejné VYPLNĚNÉ e-maily či sériová čísla nejsou dovoleny. Nejde o jeden složený klíč.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 3 | 1 | 4 | 4 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Seznam UNIQUE constraintů/indexů.

## 1.11 – Omezení povolených stavových hodnot (Krok 1 – vytvoření struktury)

Kritérium: K1

**Úloha:** V Constraints / Checks nastav: zakazka.stav IN ('přijato','v opravě','hotovo','vyzvednuto','stornováno'); faktura.zpusob_platby IN ('hotově','kartou','převodem'); faktura.stav_platby IN ('zaplaceno','nezaplaceno'). Všechny tři sloupce jsou NOT NULL.

**Očekávání ze zadání:** Vzniknou tři CHECK constraints. Pokud GUI CHECK neumí, napiš to. Náhradní ENUM či ruční SQL zaznamenej jako odlišný postup, nikoli jako úspěšné vytvoření CHECK v modelu.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 5 | 4 | 3 | 1 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail omezení a později odpovídající úsek DDL.

## 1.12 – Výchozí hodnoty (Krok 1 – vytvoření struktury)

Kritérium: K1

**Úloha:** Nastav DEFAULT: zakaznik.datum_registrace = CURRENT_DATE; zakazka.datum_prijeti = CURRENT_TIMESTAMP; zakazka.stav = 'přijato'; dil.mnozstvi_sklad = 0; mnozstvi v obou spojovacích tabulkách = 1; faktura.datum_vystaveni = CURRENT_DATE; faktura.stav_platby = 'nezaplaceno'.

**Očekávání ze zadání:** Funkce a čísla nejsou text v uvozovkách. Textové stavy jsou SQL řetězce. MySQL: datum jako (CURRENT_DATE); Oracle: TRUNC(CURRENT_DATE). DEFAULT se použije při vynechání hodnoty, nenahrazuje vložené NULL.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 1 | 2 | 4 | 5 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail defaultů v modelu a odpovídající DDL.

## 1.14 – Elektrokolo: jeden sloupec současně PK i FK

Kritérium: K1

**Úloha:** V elektrokolo označ id_kolo jako jediný PK. TENTÝŽ sloupec připoj jako FK → kolo.id_kolo. Nastav NOT NULL a vypni identity / auto-increment. Nevytvářej další id.

**Očekávání ze zadání:** Kolo má 0 nebo 1 rozšiřující záznam elektrokolo. Elektrokolo používá již existující ID kola. Jde o jinou konstrukci než vlastní PK + FK UNIQUE u faktury.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 1 | 3 | 2 | 5 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail PK, FK a vypnutého automatického číslování.

## 1.15 – CHECK čísel a dvou sloupců

Kritérium: K1

**Úloha:** V obou spojovacích tabulkách nastav CHECK (mnozstvi > 0) a CHECK (cena_za_jednotku >= 0). Dále: cena_zakladni >= 0; cena_prodejni >= 0; mnozstvi_sklad >= 0; castka_celkem >= 0; vykon_motoru_w > 0; kapacita_baterie_wh > 0. U sluzba: (odhad_doby_min IS NULL OR odhad_doby_min > 0). U zakazka: (datum_dokonceni IS NULL OR datum_dokonceni >= datum_prijeti).

**Očekávání ze zadání:** Vzniknou skutečné CHECK constraints. Ceny a množství jsou NOT NULL. Odhad doby a datum dokončení smí chybět. Poslední CHECK porovnává dva sloupce téhož řádku a nelze jej nahradit ENUM.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 1 | 5 | 1 | 2 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Výrazy v editoru CHECK a jejich výstup do DDL.

## 1.13 – Celková použitelnost modelování (Krok 1 – vytvoření struktury)

Kritérium: K2

**Úloha:** Po nových bodech 1.14 a 1.15 shrň ovládání, hledání voleb, obchvaty a chyby u všech 11 tabulek.

**Očekávání ze zadání:** Popis opři o konkrétní zkušenost: složený PK, FK + UNIQUE, PK = FK, CHECK a DEFAULT. Rozliš „nástroj neumí“ a „volbu jsem nenašel“. Původní známka se zachovala jako dosavadní záznam.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 2 | 4 | 2 | 1 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Čas kroku 1 a konkrétní příklady problémů.

## 2.1 – Vygenerování DDL z modelu (Krok 2 – forward engineering)

Kritérium: K4

**Úloha:** Z VLASTNÍHO modelu vygeneruj DDL pro zvolenou DB. Referenční SQL z tohoto sešitu při tomto kroku nepoužívej.

**Očekávání ze zadání:** Výstup obsahuje 11 tabulek a jejich omezení. U DB-first postupu exportuj vlastní schéma a rozdíl zapiš; neoznačuj jej za generování z offline modelu.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 5 | 4 | 4 | 1 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Vygenerovaný SQL soubor a snímek průvodce/výsledku.

## 2.2 – Spuštění vygenerovaného DDL bez chyby (Krok 2 – forward engineering)

Kritérium: K4

**Úloha:** V samostatné PRÁZDNÉ testovací databázi/schématu spusť neupravené vlastní vygenerované DDL. Nepoužívej schéma s daty, která potřebuješ.

**Očekávání ze zadání:** DDL doběhne bez chyby a vznikne 11 tabulek. MySQL: SHOW TABLES. PostgreSQL: Tables v cílovém schématu nebo information_schema.tables. Oracle: USER_TABLES u testovacího uživatele.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 3 | 3 | 3 | 3 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Výstup spuštění a seznam 11 tabulek, případně přesná chyba.

## 2.3 – Zachování klíčů a omezení v DDL (Krok 2 – forward engineering)

Kritérium: K4

**Úloha:** Ve vytvořené DB prověř 8 automatických PK, 2 složené PK, elektrokolo.id_kolo jako PK i FK, všechny FK, NULL, UNIQUE, CHECK a DEFAULT podle Model a pravidla.

**Očekávání ze zadání:** Omezení existují ve vytvořené DB, nestačí čáry v diagramu. Elektrokolo nemá automatické číslování. Chování s daty ověř také v novém bodě 2.6.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 1 | 3 | 5 | 3 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Výpisy pro zakazka_sluzba, zakazka_dil, faktura a zakazka.

## 2.4 – Nutné ruční zásahy do DDL (Krok 2 – forward engineering)

Kritérium: K4

**Úloha:** Při selhání uschovej původní SQL. Každou změnu zapiš: chyba, původní řádek, opravený řádek, důvod. Opravenou kopii spusť v jiném prázdném testovacím schématu.

**Očekávání ze zadání:** Původní výstup a ruční oprava jsou oddělené výsledky. Pokud zásah nebyl nutný, napiš „žádné“.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 1 | 3 | 1 | 4 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Chybové hlášení a diff původního/opravovaného SQL.

## 2.5 – Export DDL do souboru (Krok 2 – forward engineering)

Kritérium: K4

**Úloha:** Ulož celé vlastní DDL do UTF-8 .sql, zavři a znovu otevři soubor.

**Očekávání ze zadání:** Soubor obsahuje všech 11 tabulek a omezení. Název rozlišuje nástroj a původní/opravovanou variantu. Stejný doklad použij v 4.3.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 4 | 1 | 5 | 1 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Cesta k uloženému .sql souboru.

## 2.6 – Skutečné vynucení omezení

Kritérium: K4

**Úloha:** V odděleném testovacím schématu vlož platného zákazníka, kolo, zakázku, službu a položku. Vyplň povinné sloupce a používej skutečně přidělená ID. Pak jednotlivě proveď pokusy z listu Kontrolní data.

**Očekávání ze zadání:** Platné řádky projdou. NULL mechanik projde; neexistující FK, duplicitní dvojice PK, druhá faktura na stejnou zakázku, neplatný stav, nulové množství a záporná cena se odmítnou. Elektrokolo používá existující ID kola.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 2 | 5 | 4 | 2 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Skutečný výsledek a chybové hlášení každého pokusu, bez hesel.

## 3.1 – Připojení k referenční databázi (Krok 3 – reverse engineering)

Kritérium: K5

**Úloha:** V jiném prázdném testovacím schématu spusť referenční SQL z listu SQL MySQL, SQL PostgreSQL nebo SQL Oracle. Připoj k němu nástroj; přihlašovací údaje do hodnocení nepiš.

**Očekávání ze zadání:** Reference je nezávislá na tvém DDL z kroku 2 a obsahuje 11 tabulek. Zapiš skutečný server, verzi a DB/schéma. Referenční skripty jsou připravený návrh; jejich spuštění zatím není doložené.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 3 | 2 | 5 | 4 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Úspěšný test připojení nebo přesné chybové hlášení.

## 3.2 – Rozpoznání všech 11 tabulek (Krok 3 – reverse engineering)

Kritérium: K5

**Úloha:** V novém modelu/diagramu načti všech 11 tabulek z referenčního schématu.

**Očekávání ze zadání:** Vznikne 11 tabulek včetně elektrokolo. Rozliš editovatelný samostatný model a diagram nad živou DB. Neotvírej jako výsledek původní model z kroku 1.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 2 | 1 | 5 | 4 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Snímek celého reverse-engineered diagramu.

## 3.3 – Rozpoznání složených PK (Krok 3 – reverse engineering)

Kritérium: K5

**Úloha:** Otevři indexy/klíče tabulek zakazka_sluzba a zakazka_dil.

**Očekávání ze zadání:** V každé tabulce musí PRIMARY KEY obsahovat právě dva FK sloupce. Ověř pořadí a členství sloupců; samostatné id nebo obyčejný index místo PK je chyba importu.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 2 | 5 | 5 | 2 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail PRIMARY indexů obou tabulek.

## 3.4 – Rozpoznání FK a kardinalit (Krok 3 – reverse engineering)

Kritérium: K5

**Úloha:** Prověř všechny FK podle Model a pravidla. Zvlášť zakazka.id_zamestnanec a dil.id_dodavatel s NULL a faktura.id_zakazka s UNIQUE.

**Očekávání ze zadání:** Zachovaly se směry i povinnost vazeb. Faktura je 0..1 na zakázku. Elektrokolo ověř v 3.9. Kontroluj klíče i kresbu.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 1 | 2 | 4 | 2 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Diagram kardinalit a detail nullable FK.

## 3.5 – Rozpoznání UNIQUE omezení (Krok 3 – reverse engineering)

Kritérium: K5

**Úloha:** Zkontroluj jedinečné indexy/constrainty po importu.

**Očekávání ze zadání:** Ověř zakaznik.email, kolo.seriove_cislo a faktura.id_zakazka. U každého zapiš, zda se načetl jako UNIQUE constraint, unique index, nebo se ztratil.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 5 | 3 | 2 | 4 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Seznam importovaných UNIQUE omezení.

## 3.6 – Rozpoznání CHECK/ENUM omezení (Krok 3 – reverse engineering)

Kritérium: K5

**Úloha:** Prověř importované CHECK stavů z 1.11 a číselných/datových pravidel z 1.15. U elektrokola ověř kladný výkon i kapacitu.

**Očekávání ze zadání:** Zachovaly se stejné výrazy. Ztrátu CHECK, převod na ENUM nebo nezobrazené omezení výslovně zapiš. Pouhá poznámka v diagramu není CHECK.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 3 | 3 | 5 | 3 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail importovaných omezení a DDL náhled.

## 3.7 – Rozdíly proti referenčnímu schématu (Krok 3 – reverse engineering)

Kritérium: K5

**Úloha:** Porovnej všech 11 tabulek s Model a pravidla: sloupce, typy, PK, FK, NULL, UNIQUE, CHECK, DEFAULT a automatické číslování.

**Očekávání ze zadání:** Při shodě uveď skutečně porovnané skupiny objektů. Při rozdílu zapiš tabulku, sloupec a původní versus načtenou definici.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 5 | 3 | 1 | 4 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Stručný seznam rozdílů nebo doložené „bez rozdílu“.

## 3.8 – Dostupnost funkce v testované edici (Krok 3 – reverse engineering)

Kritérium: K5

**Úloha:** Ověř, že reverse engineering byl proveden ve stejné edici, kterou hodnotíš.

**Očekávání ze zadání:** Zapiš přesný název edice a verzi. Pokud funkce chybí, je omezená nebo byla použita trial/placená edice, popiš to; výsledek jiné edice nepřipisuj Community/free edici.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 5 | 4 | 3 | 5 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Verze/edice a případné licenční hlášení.

## 3.9 – Načtení PK = FK elektrokola

Kritérium: K5

**Úloha:** V importované tabulce elektrokolo otevři PK, FK a definici id_kolo.

**Očekávání ze zadání:** Jediný id_kolo zůstal PK i FK na kolo.id_kolo, bez automatického číslování. Výkon a kapacita mají NOT NULL a CHECK kladnosti. Nepřibyl další sloupec pro vazbu.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 2 | 3 | 3 | 2 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Detail importovaného elektrokola.

## 4.1 – Nativní export diagramu (Krok 4 – export)

Kritérium: K7

**Úloha:** V nabídce Export vyzkoušej všechny formáty diagramu, které nástroj nabízí.

**Očekávání ze zadání:** Ulož alespoň jeden výstup a vypiš přesné nabízené formáty, například PNG, SVG nebo PDF. Každý soubor otevři a ověř čitelnost názvů tabulek, sloupců a vazeb.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 3 | 4 | 2 | 2 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Exportovaný diagram a seznam nativních formátů.

## 4.2 – Nativní export versus tisk do PDF (Krok 4 – export)

Kritérium: K7

**Úloha:** Porovnej příkaz Export s příkazem Print/Tisk.

**Očekávání ze zadání:** Za nativní PDF označ jen formát přímo nabízený funkcí Export. Microsoft Print to PDF nebo jiný systémový tisk zapiš zvlášť jako tisk, nikoli jako nativní export nástroje.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 5 | 2 | 3 | 1 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Nabídka Export a nabídka Tisk.

## 4.3 – Export SQL/DDL (Krok 4 – export)

Kritérium: K4

**Úloha:** Použij soubor z 2.5 a znovu ověř jeho otevření mimo relaci nástroje.

**Očekávání ze zadání:** Obsahuje všech 11 tabulek. Jde o stejný doklad jako 2.5; stejnou schopnost při souhrnném hodnocení nezapočítávej dvakrát.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 5 | 1 | 2 | 5 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Uložený .sql soubor.

## 4.4 – Import cizího formátu (Krok 4 – export)

Kritérium: K7

**Úloha:** V novém projektu zkus offline import referenčního SQL pro cílovou DB. Jiný modelový formát případně zapiš zvlášť.

**Očekávání ze zadání:** Při importu SQL vznikne 11 tabulek. Prověř složený PK, FK + UNIQUE u faktury, PK = FK u elektrokola a CHECK. Pokud offline import edice neumí, zapiš nedostupnost; živá DB patří do kroku 3.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 3 | 2 | 2 | 5 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Importovaný model nebo přesné omezení funkce.

## K3.1 – Nativně podporované DBMS (K3 – kompatibilita s DBMS)

Kritérium: K3

**Úloha:** Zjisti seznam DBMS, pro které nástroj umí modelování a generování/reverse engineering.

**Očekávání ze zadání:** Použij oficiální dokumentaci testované verze. Rozliš pouhé databázové připojení od podpory datového modelování. Zapiš seznam DBMS, URL zdroje a datum ověření.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 5 | 3 | 1 | 4 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Oficiální URL a datum přístupu.

## K3.2 – Praktický test jiné DBMS (K3 – kompatibilita s DBMS)

Kritérium: K3

**Úloha:** Pokud je to v rozsahu práce, zopakuj malý test proti jiné než primární DBMS.

**Očekávání ze zadání:** Použij stejný jednoduchý model s PK, FK a UNIQUE. Vygeneruj nebo reverse-engineeruj schéma a zapiš, co fungovalo odlišně. Pokud jiná DBMS testována nebyla, napiš „netestováno“ místo odhadu.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 5 | 2 | 2 | 5 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Použitá DBMS, výsledek a případný DDL/diagram.

## K6.1 – Kvalita oficiální dokumentace (K6 – dokumentace a komunita)

Kritérium: K6

**Úloha:** V oficiální dokumentaci vyhledej postup pro model, forward engineering, reverse engineering a export.

**Očekávání ze zadání:** Zapiš, zda návody odpovídají testované verzi, obsahují konkrétní kroky a řeší omezení. Ulož URL a datum přístupu; hodnocení opři o to, kolik kroků bylo nutné dohledat jinde.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 2 | 5 | 3 | 3 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Oficiální URL, datum a krátké věcné zjištění.

## K6.2 – Aktivita komunity (K6 – dokumentace a komunita)

Kritérium: K6

**Úloha:** Prověř oficiální fórum, issue tracker nebo GitHub projektu.

**Očekávání ze zadání:** Najdi témata k modelování, FK/PK, forward/reverse engineering a exportu. Zapiš datum poslední relevantní aktivity, zda jsou dotazy zodpovídány a URL. Neposuzuj komunitu jen podle celkového počtu výsledků vyhledávání.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 2 | 1 | 2 | 3 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** URL, datum poslední relevantní aktivity a příklad tématu.

## K8.1 – Cena a přesná edice (K8 – náklady a licence)

Kritérium: K8

**Úloha:** Zapiš plný název, verzi, edici a cenu použité varianty.

**Očekávání ze zadání:** Ověř údaje na oficiální stránce produktu nebo licence. U bezplatné edice napiš cenu 0 a typ licence; u předplatného uveď období a měnu. Přidej URL a datum ověření.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 5 | 3 | 1 | 4 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Oficiální cenová/licenční stránka a datum.

## K8.2 – Omezení bezplatné edice (K8 – náklady a licence)

Kritérium: K8

**Úloha:** Porovnej Community/free edici s placenou variantou jen v funkcích důležitých pro tento test.

**Očekávání ze zadání:** Ověř model-first, forward engineering, reverse engineering, podporované DBMS a exportní formáty. U každého omezení uveď, zda se projevilo v praktickém testu, nebo pochází pouze z dokumentace.

| OSDM | DBEAVER | MYSQL | PGMODELER |
| --- | --- | --- | --- |
| 2 | 4 | 1 | 2 |

**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.

**Co uložit při skutečném testu:** Oficiální porovnání edic a vazba na praktický test.
