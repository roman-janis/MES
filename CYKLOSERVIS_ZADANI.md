# Jednotné zadání Cykloservis – 11 tabulek

Platná pracovní verze pro všechny čtyři nástroje: 27. 9. 2026. Toto je jediné aktuální technické zadání modelu; nahrazuje původní desetientitové jádro. Archiv starého zadání je `archiv/CYKLOSERVIS_ZADANI_pred_sjednocenim_20260927.md`. Nejde o druhý scénář, ale o sjednocení již připraveného testovacího sešitu a textu práce.

## Rozhodovací situace a společný postup

Vývojář vybírá nástroj pro návrh a vývoj databázového systému malého cykloservisu před konečnou volbou DBMS. V každém nástroji vytvoří stejný model od začátku. Z něj vygeneruje vlastní DDL a ověří jeho omezení. Teprve při testu reverse engineeringu použije referenční SQL uvedené níže. Poté ověří přenos modelu, kompatibilitu, dokumentaci a licenci testované edice. Pomocné známky nejsou Saatyho vstupy.

Malý cykloservis eviduje zákazníky, kola a jejich servisní zakázky, zaměstnance, provedené služby, spotřebované díly, dodavatele a faktury. Historická cena služby či dílu se ukládá také do položky zakázky. Elektrokolo představuje nepovinné rozšíření údajů konkrétního kola. Nejde o objednávkový systém dodavatelů; další tabulky se nepřidávají.

## Závazný seznam a důvod rozsahu

`zakaznik`, `zamestnanec`, `dodavatel`, `kolo`, `elektrokolo`, `sluzba`, `dil`, `zakazka`, `zakazka_sluzba`, `zakazka_dil`, `faktura`.

Vztah zakázka–faktura testuje samostatný PK a UNIQUE FK. Vztah kolo–elektrokolo testuje sdílený PK/FK. V obou případech smí rodič existovat bez potomka; z pohledu rodiče tedy jde o 1 ku 0..1. Přidané elektrokolo umožňuje ověřit druhou realizaci této vazby podle požadavku na podrobné testování. M:N je řešeno tabulkami zakazka_sluzba a zakazka_dil. U zakázky je přípustný dosud nepřiřazený zaměstnanec.

## Přesná pravidla a atributy

Model Cykloservisu – 11 tabulek

Zákazník vlastní kola; kolo má zakázky. Elektrokolo rozšiřuje jedno kolo o motor a baterii. Mechanik zakázky a hlavní dodavatel dílu mohou být neurčeni.

Zakázka–Faktura a Kolo–Elektrokolo jsou 1 ku 0..1. Faktura používá vlastní PK a FK UNIQUE; elektrokolo používá jediný sdílený PK/FK. Rodič smí existovat bez potomka.

Služba/díl je na zakázce jednou, počet vyjadřuje množství. Cena položky je historická cena při opravě. Celková částka faktury je zadaná hodnota; její výpočet zde netestujeme.

Typy: MySQL použije DATETIME místo TIMESTAMP; Oracle NUMBER(10) místo INT, NUMBER(5) místo SMALLINT, NUMBER(p,s) místo DECIMAL a VARCHAR2 místo VARCHAR. Automatické ID: AUTO_INCREMENT v MySQL, identity v PostgreSQL/Oracle.

NULL dovoluje chybějící hodnotu; NOT NULL ji zakazuje. DEFAULT se použije při vynechání hodnoty. PK identifikuje řádek, FK odkazuje na rodiče, UNIQUE zakazuje duplicity vyplněných hodnot, CHECK kontroluje podmínku.

| Tabulka | Sloupec | Typ | NULL? | DEFAULT | Klíč / vazba | Přesné nastavení |
| --- | --- | --- | --- | --- | --- | --- |
| zakaznik | id_zakaznik | INT | NE | žádný | PK | Zapnout automatické číslování. |
| zakaznik | jmeno | VARCHAR(50) | NE | žádný |  | Bez automatického číslování. |
| zakaznik | prijmeni | VARCHAR(50) | NE | žádný |  | Bez automatického číslování. |
| zakaznik | telefon | VARCHAR(20) | ANO | žádný |  | Bez automatického číslování. |
| zakaznik | email | VARCHAR(100) | ANO | žádný | UNIQUE | Bez automatického číslování. |
| zakaznik | adresa | VARCHAR(200) | ANO | žádný |  | Bez automatického číslování. |
| zakaznik | datum_registrace | DATE | NE | CURRENT_DATE |  | Bez automatického číslování. |
| zamestnanec | id_zamestnanec | INT | NE | žádný | PK | Zapnout automatické číslování. |
| zamestnanec | jmeno | VARCHAR(50) | NE | žádný |  | Bez automatického číslování. |
| zamestnanec | prijmeni | VARCHAR(50) | NE | žádný |  | Bez automatického číslování. |
| zamestnanec | pozice | VARCHAR(30) | NE | žádný |  | Bez automatického číslování. |
| zamestnanec | telefon | VARCHAR(20) | ANO | žádný |  | Bez automatického číslování. |
| zamestnanec | datum_nastupu | DATE | NE | žádný |  | Bez automatického číslování. |
| dodavatel | id_dodavatel | INT | NE | žádný | PK | Zapnout automatické číslování. |
| dodavatel | nazev | VARCHAR(100) | NE | žádný |  | Bez automatického číslování. |
| dodavatel | kontaktni_osoba | VARCHAR(100) | ANO | žádný |  | Bez automatického číslování. |
| dodavatel | telefon | VARCHAR(20) | ANO | žádný |  | Bez automatického číslování. |
| dodavatel | email | VARCHAR(100) | ANO | žádný |  | Bez automatického číslování. |
| kolo | id_kolo | INT | NE | žádný | PK | Zapnout automatické číslování. |
| kolo | id_zakaznik | INT | NE | žádný | FK → zakaznik.id_zakaznik | Bez automatického číslování. |
| kolo | znacka | VARCHAR(50) | NE | žádný |  | Bez automatického číslování. |
| kolo | model | VARCHAR(50) | ANO | žádný |  | Bez automatického číslování. |
| kolo | typ | VARCHAR(30) | ANO | žádný |  | Bez automatického číslování. |
| kolo | rok_vyroby | SMALLINT | ANO | žádný |  | Bez automatického číslování. |
| kolo | seriove_cislo | VARCHAR(50) | ANO | žádný | UNIQUE | Bez automatického číslování. |
| elektrokolo | id_kolo | INT | NE | žádný | PK; FK → kolo.id_kolo | Jeden sloupec tvoří celý PK i FK. Bez automatického ID. |
| elektrokolo | vyrobce_motoru | VARCHAR(80) | NE | žádný |  | Bez automatického číslování. |
| elektrokolo | vykon_motoru_w | INT | NE | žádný |  | Bez automatického číslování. |
| elektrokolo | kapacita_baterie_wh | DECIMAL(8,2) | NE | žádný |  | Bez automatického číslování. |
| elektrokolo | CHECK | integritní omezení | — | — | CHECK (vykon_motoru_w > 0) | Vytvoř v Constraints / Checks; později ověř v DDL i při vložení neplatné hodnoty. |
| elektrokolo | CHECK | integritní omezení | — | — | CHECK (kapacita_baterie_wh > 0) | Vytvoř v Constraints / Checks; později ověř v DDL i při vložení neplatné hodnoty. |
| sluzba | id_sluzba | INT | NE | žádný | PK | Zapnout automatické číslování. |
| sluzba | nazev | VARCHAR(100) | NE | žádný |  | Bez automatického číslování. |
| sluzba | popis | VARCHAR(300) | ANO | žádný |  | Bez automatického číslování. |
| sluzba | cena_zakladni | DECIMAL(10,2) | NE | žádný |  | Bez automatického číslování. |
| sluzba | odhad_doby_min | INT | ANO | žádný |  | Bez automatického číslování. |
| sluzba | CHECK | integritní omezení | — | — | CHECK (cena_zakladni >= 0) | Vytvoř v Constraints / Checks; později ověř v DDL i při vložení neplatné hodnoty. |
| sluzba | CHECK | integritní omezení | — | — | CHECK (odhad_doby_min IS NULL OR odhad_doby_min > 0) | Vytvoř v Constraints / Checks; později ověř v DDL i při vložení neplatné hodnoty. |
| dil | id_dil | INT | NE | žádný | PK | Zapnout automatické číslování. |
| dil | nazev | VARCHAR(100) | NE | žádný |  | Bez automatického číslování. |
| dil | cena_prodejni | DECIMAL(10,2) | NE | žádný |  | Bez automatického číslování. |
| dil | mnozstvi_sklad | INT | NE | 0 |  | Bez automatického číslování. |
| dil | id_dodavatel | INT | ANO | žádný | FK → dodavatel.id_dodavatel | Bez automatického číslování. |
| dil | CHECK | integritní omezení | — | — | CHECK (cena_prodejni >= 0) | Vytvoř v Constraints / Checks; později ověř v DDL i při vložení neplatné hodnoty. |
| dil | CHECK | integritní omezení | — | — | CHECK (mnozstvi_sklad >= 0) | Vytvoř v Constraints / Checks; později ověř v DDL i při vložení neplatné hodnoty. |
| zakazka | id_zakazka | INT | NE | žádný | PK | Zapnout automatické číslování. |
| zakazka | id_kolo | INT | NE | žádný | FK → kolo.id_kolo | Bez automatického číslování. |
| zakazka | id_zamestnanec | INT | ANO | žádný | FK → zamestnanec.id_zamestnanec | Bez automatického číslování. |
| zakazka | datum_prijeti | TIMESTAMP | NE | CURRENT_TIMESTAMP |  | Bez automatického číslování. |
| zakazka | datum_dokonceni | TIMESTAMP | ANO | žádný |  | Bez automatického číslování. |
| zakazka | stav | VARCHAR(20) | NE | 'přijato' |  | Bez automatického číslování. |
| zakazka | poznamka | VARCHAR(500) | ANO | žádný |  | Bez automatického číslování. |
| zakazka | CHECK | integritní omezení | — | — | CHECK (stav IN ('přijato','v opravě','hotovo','vyzvednuto','stornováno')) | Vytvoř v Constraints / Checks; později ověř v DDL i při vložení neplatné hodnoty. |
| zakazka | CHECK | integritní omezení | — | — | CHECK (datum_dokonceni IS NULL OR datum_dokonceni >= datum_prijeti) | Vytvoř v Constraints / Checks; později ověř v DDL i při vložení neplatné hodnoty. |
| zakazka_sluzba | id_zakazka | INT | NE | žádný | část složeného PK; FK → zakazka.id_zakazka | Společný PK (id_zakazka, id_sluzba). Bez automatického ID. |
| zakazka_sluzba | id_sluzba | INT | NE | žádný | část složeného PK; FK → sluzba.id_sluzba | Společný PK (id_zakazka, id_sluzba). Bez automatického ID. |
| zakazka_sluzba | mnozstvi | INT | NE | 1 |  | Bez automatického číslování. |
| zakazka_sluzba | cena_za_jednotku | DECIMAL(10,2) | NE | žádný |  | Bez automatického číslování. |
| zakazka_sluzba | CHECK | integritní omezení | — | — | CHECK (mnozstvi > 0) | Vytvoř v Constraints / Checks; později ověř v DDL i při vložení neplatné hodnoty. |
| zakazka_sluzba | CHECK | integritní omezení | — | — | CHECK (cena_za_jednotku >= 0) | Vytvoř v Constraints / Checks; později ověř v DDL i při vložení neplatné hodnoty. |
| zakazka_dil | id_zakazka | INT | NE | žádný | část složeného PK; FK → zakazka.id_zakazka | Společný PK (id_zakazka, id_dil). Bez automatického ID. |
| zakazka_dil | id_dil | INT | NE | žádný | část složeného PK; FK → dil.id_dil | Společný PK (id_zakazka, id_dil). Bez automatického ID. |
| zakazka_dil | mnozstvi | INT | NE | 1 |  | Bez automatického číslování. |
| zakazka_dil | cena_za_jednotku | DECIMAL(10,2) | NE | žádný |  | Bez automatického číslování. |
| zakazka_dil | CHECK | integritní omezení | — | — | CHECK (mnozstvi > 0) | Vytvoř v Constraints / Checks; později ověř v DDL i při vložení neplatné hodnoty. |
| zakazka_dil | CHECK | integritní omezení | — | — | CHECK (cena_za_jednotku >= 0) | Vytvoř v Constraints / Checks; později ověř v DDL i při vložení neplatné hodnoty. |
| faktura | id_faktura | INT | NE | žádný | PK | Zapnout automatické číslování. |
| faktura | id_zakazka | INT | NE | žádný | FK → zakazka.id_zakazka; UNIQUE | Bez automatického číslování. |
| faktura | datum_vystaveni | DATE | NE | CURRENT_DATE |  | Bez automatického číslování. |
| faktura | castka_celkem | DECIMAL(10,2) | NE | žádný |  | Bez automatického číslování. |
| faktura | zpusob_platby | VARCHAR(20) | NE | žádný |  | Bez automatického číslování. |
| faktura | stav_platby | VARCHAR(20) | NE | 'nezaplaceno' |  | Bez automatického číslování. |
| faktura | CHECK | integritní omezení | — | — | CHECK (castka_celkem >= 0) | Vytvoř v Constraints / Checks; později ověř v DDL i při vložení neplatné hodnoty. |
| faktura | CHECK | integritní omezení | — | — | CHECK (zpusob_platby IN ('hotově','kartou','převodem')) | Vytvoř v Constraints / Checks; později ověř v DDL i při vložení neplatné hodnoty. |
| faktura | CHECK | integritní omezení | — | — | CHECK (stav_platby IN ('zaplaceno','nezaplaceno')) | Vytvoř v Constraints / Checks; později ověř v DDL i při vložení neplatné hodnoty. |

## Referenční SQL pro reverse engineering

Skripty jsou převzaty z pracovního sešitu; jejich vytvoření ani tento export nedokládá běh databáze. Před skutečnými testy je nutné ověřit vytvoření 11 tabulek, 10 FK a omezení. Používat pouze samostatné prázdné testovací schéma.

### SQL MySQL

```sql
-- Cykloservis: 11 tabulek. Pouze testovaci schema.
CREATE TABLE zakaznik (
    id_zakaznik INT AUTO_INCREMENT NOT NULL,
    jmeno VARCHAR(50) NOT NULL,
    prijmeni VARCHAR(50) NOT NULL,
    telefon VARCHAR(20),
    email VARCHAR(100),
    adresa VARCHAR(200),
    datum_registrace DATE DEFAULT (CURRENT_DATE) NOT NULL,
    PRIMARY KEY (id_zakaznik),
    UNIQUE (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE zamestnanec (
    id_zamestnanec INT AUTO_INCREMENT NOT NULL,
    jmeno VARCHAR(50) NOT NULL,
    prijmeni VARCHAR(50) NOT NULL,
    pozice VARCHAR(30) NOT NULL,
    telefon VARCHAR(20),
    datum_nastupu DATE NOT NULL,
    PRIMARY KEY (id_zamestnanec)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE dodavatel (
    id_dodavatel INT AUTO_INCREMENT NOT NULL,
    nazev VARCHAR(100) NOT NULL,
    kontaktni_osoba VARCHAR(100),
    telefon VARCHAR(20),
    email VARCHAR(100),
    PRIMARY KEY (id_dodavatel)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE kolo (
    id_kolo INT AUTO_INCREMENT NOT NULL,
    id_zakaznik INT NOT NULL,
    znacka VARCHAR(50) NOT NULL,
    model VARCHAR(50),
    typ VARCHAR(30),
    rok_vyroby SMALLINT,
    seriove_cislo VARCHAR(50),
    PRIMARY KEY (id_kolo),
    UNIQUE (seriove_cislo),
    FOREIGN KEY (id_zakaznik) REFERENCES zakaznik (id_zakaznik)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE elektrokolo (
    id_kolo INT NOT NULL,
    vyrobce_motoru VARCHAR(80) NOT NULL,
    vykon_motoru_w INT NOT NULL,
    kapacita_baterie_wh DECIMAL(8,2) NOT NULL,
    PRIMARY KEY (id_kolo),
    FOREIGN KEY (id_kolo) REFERENCES kolo (id_kolo),
    CHECK (vykon_motoru_w > 0),
    CHECK (kapacita_baterie_wh > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE sluzba (
    id_sluzba INT AUTO_INCREMENT NOT NULL,
    nazev VARCHAR(100) NOT NULL,
    popis VARCHAR(300),
    cena_zakladni DECIMAL(10,2) NOT NULL,
    odhad_doby_min INT,
    PRIMARY KEY (id_sluzba),
    CHECK (cena_zakladni >= 0),
    CHECK (odhad_doby_min IS NULL OR odhad_doby_min > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE dil (
    id_dil INT AUTO_INCREMENT NOT NULL,
    nazev VARCHAR(100) NOT NULL,
    cena_prodejni DECIMAL(10,2) NOT NULL,
    mnozstvi_sklad INT DEFAULT 0 NOT NULL,
    id_dodavatel INT,
    PRIMARY KEY (id_dil),
    FOREIGN KEY (id_dodavatel) REFERENCES dodavatel (id_dodavatel),
    CHECK (cena_prodejni >= 0),
    CHECK (mnozstvi_sklad >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE zakazka (
    id_zakazka INT AUTO_INCREMENT NOT NULL,
    id_kolo INT NOT NULL,
    id_zamestnanec INT,
    datum_prijeti DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    datum_dokonceni DATETIME,
    stav VARCHAR(20) DEFAULT 'přijato' NOT NULL,
    poznamka VARCHAR(500),
    PRIMARY KEY (id_zakazka),
    FOREIGN KEY (id_kolo) REFERENCES kolo (id_kolo),
    FOREIGN KEY (id_zamestnanec) REFERENCES zamestnanec (id_zamestnanec),
    CHECK (stav IN ('přijato','v opravě','hotovo','vyzvednuto','stornováno')),
    CHECK (datum_dokonceni IS NULL OR datum_dokonceni >= datum_prijeti)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE zakazka_sluzba (
    id_zakazka INT NOT NULL,
    id_sluzba INT NOT NULL,
    mnozstvi INT DEFAULT 1 NOT NULL,
    cena_za_jednotku DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_zakazka, id_sluzba),
    FOREIGN KEY (id_zakazka) REFERENCES zakazka (id_zakazka),
    FOREIGN KEY (id_sluzba) REFERENCES sluzba (id_sluzba),
    CHECK (mnozstvi > 0),
    CHECK (cena_za_jednotku >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE zakazka_dil (
    id_zakazka INT NOT NULL,
    id_dil INT NOT NULL,
    mnozstvi INT DEFAULT 1 NOT NULL,
    cena_za_jednotku DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_zakazka, id_dil),
    FOREIGN KEY (id_zakazka) REFERENCES zakazka (id_zakazka),
    FOREIGN KEY (id_dil) REFERENCES dil (id_dil),
    CHECK (mnozstvi > 0),
    CHECK (cena_za_jednotku >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE faktura (
    id_faktura INT AUTO_INCREMENT NOT NULL,
    id_zakazka INT NOT NULL,
    datum_vystaveni DATE DEFAULT (CURRENT_DATE) NOT NULL,
    castka_celkem DECIMAL(10,2) NOT NULL,
    zpusob_platby VARCHAR(20) NOT NULL,
    stav_platby VARCHAR(20) DEFAULT 'nezaplaceno' NOT NULL,
    PRIMARY KEY (id_faktura),
    UNIQUE (id_zakazka),
    FOREIGN KEY (id_zakazka) REFERENCES zakazka (id_zakazka),
    CHECK (castka_celkem >= 0),
    CHECK (zpusob_platby IN ('hotově','kartou','převodem')),
    CHECK (stav_platby IN ('zaplaceno','nezaplaceno'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### SQL PostgreSQL

```sql
-- Cykloservis: 11 tabulek. Pouze testovaci schema.
CREATE TABLE zakaznik (
    id_zakaznik INT GENERATED BY DEFAULT AS IDENTITY NOT NULL,
    jmeno VARCHAR(50) NOT NULL,
    prijmeni VARCHAR(50) NOT NULL,
    telefon VARCHAR(20),
    email VARCHAR(100),
    adresa VARCHAR(200),
    datum_registrace DATE DEFAULT CURRENT_DATE NOT NULL,
    PRIMARY KEY (id_zakaznik),
    UNIQUE (email)
);

CREATE TABLE zamestnanec (
    id_zamestnanec INT GENERATED BY DEFAULT AS IDENTITY NOT NULL,
    jmeno VARCHAR(50) NOT NULL,
    prijmeni VARCHAR(50) NOT NULL,
    pozice VARCHAR(30) NOT NULL,
    telefon VARCHAR(20),
    datum_nastupu DATE NOT NULL,
    PRIMARY KEY (id_zamestnanec)
);

CREATE TABLE dodavatel (
    id_dodavatel INT GENERATED BY DEFAULT AS IDENTITY NOT NULL,
    nazev VARCHAR(100) NOT NULL,
    kontaktni_osoba VARCHAR(100),
    telefon VARCHAR(20),
    email VARCHAR(100),
    PRIMARY KEY (id_dodavatel)
);

CREATE TABLE kolo (
    id_kolo INT GENERATED BY DEFAULT AS IDENTITY NOT NULL,
    id_zakaznik INT NOT NULL,
    znacka VARCHAR(50) NOT NULL,
    model VARCHAR(50),
    typ VARCHAR(30),
    rok_vyroby SMALLINT,
    seriove_cislo VARCHAR(50),
    PRIMARY KEY (id_kolo),
    UNIQUE (seriove_cislo),
    FOREIGN KEY (id_zakaznik) REFERENCES zakaznik (id_zakaznik)
);

CREATE TABLE elektrokolo (
    id_kolo INT NOT NULL,
    vyrobce_motoru VARCHAR(80) NOT NULL,
    vykon_motoru_w INT NOT NULL,
    kapacita_baterie_wh DECIMAL(8,2) NOT NULL,
    PRIMARY KEY (id_kolo),
    FOREIGN KEY (id_kolo) REFERENCES kolo (id_kolo),
    CHECK (vykon_motoru_w > 0),
    CHECK (kapacita_baterie_wh > 0)
);

CREATE TABLE sluzba (
    id_sluzba INT GENERATED BY DEFAULT AS IDENTITY NOT NULL,
    nazev VARCHAR(100) NOT NULL,
    popis VARCHAR(300),
    cena_zakladni DECIMAL(10,2) NOT NULL,
    odhad_doby_min INT,
    PRIMARY KEY (id_sluzba),
    CHECK (cena_zakladni >= 0),
    CHECK (odhad_doby_min IS NULL OR odhad_doby_min > 0)
);

CREATE TABLE dil (
    id_dil INT GENERATED BY DEFAULT AS IDENTITY NOT NULL,
    nazev VARCHAR(100) NOT NULL,
    cena_prodejni DECIMAL(10,2) NOT NULL,
    mnozstvi_sklad INT DEFAULT 0 NOT NULL,
    id_dodavatel INT,
    PRIMARY KEY (id_dil),
    FOREIGN KEY (id_dodavatel) REFERENCES dodavatel (id_dodavatel),
    CHECK (cena_prodejni >= 0),
    CHECK (mnozstvi_sklad >= 0)
);

CREATE TABLE zakazka (
    id_zakazka INT GENERATED BY DEFAULT AS IDENTITY NOT NULL,
    id_kolo INT NOT NULL,
    id_zamestnanec INT,
    datum_prijeti TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    datum_dokonceni TIMESTAMP,
    stav VARCHAR(20) DEFAULT 'přijato' NOT NULL,
    poznamka VARCHAR(500),
    PRIMARY KEY (id_zakazka),
    FOREIGN KEY (id_kolo) REFERENCES kolo (id_kolo),
    FOREIGN KEY (id_zamestnanec) REFERENCES zamestnanec (id_zamestnanec),
    CHECK (stav IN ('přijato','v opravě','hotovo','vyzvednuto','stornováno')),
    CHECK (datum_dokonceni IS NULL OR datum_dokonceni >= datum_prijeti)
);

CREATE TABLE zakazka_sluzba (
    id_zakazka INT NOT NULL,
    id_sluzba INT NOT NULL,
    mnozstvi INT DEFAULT 1 NOT NULL,
    cena_za_jednotku DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_zakazka, id_sluzba),
    FOREIGN KEY (id_zakazka) REFERENCES zakazka (id_zakazka),
    FOREIGN KEY (id_sluzba) REFERENCES sluzba (id_sluzba),
    CHECK (mnozstvi > 0),
    CHECK (cena_za_jednotku >= 0)
);

CREATE TABLE zakazka_dil (
    id_zakazka INT NOT NULL,
    id_dil INT NOT NULL,
    mnozstvi INT DEFAULT 1 NOT NULL,
    cena_za_jednotku DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_zakazka, id_dil),
    FOREIGN KEY (id_zakazka) REFERENCES zakazka (id_zakazka),
    FOREIGN KEY (id_dil) REFERENCES dil (id_dil),
    CHECK (mnozstvi > 0),
    CHECK (cena_za_jednotku >= 0)
);

CREATE TABLE faktura (
    id_faktura INT GENERATED BY DEFAULT AS IDENTITY NOT NULL,
    id_zakazka INT NOT NULL,
    datum_vystaveni DATE DEFAULT CURRENT_DATE NOT NULL,
    castka_celkem DECIMAL(10,2) NOT NULL,
    zpusob_platby VARCHAR(20) NOT NULL,
    stav_platby VARCHAR(20) DEFAULT 'nezaplaceno' NOT NULL,
    PRIMARY KEY (id_faktura),
    UNIQUE (id_zakazka),
    FOREIGN KEY (id_zakazka) REFERENCES zakazka (id_zakazka),
    CHECK (castka_celkem >= 0),
    CHECK (zpusob_platby IN ('hotově','kartou','převodem')),
    CHECK (stav_platby IN ('zaplaceno','nezaplaceno'))
);
```

### SQL Oracle

```sql
-- Cykloservis: 11 tabulek. Pouze testovaci schema.
CREATE TABLE zakaznik (
    id_zakaznik NUMBER(10) GENERATED BY DEFAULT AS IDENTITY NOT NULL,
    jmeno VARCHAR2(50) NOT NULL,
    prijmeni VARCHAR2(50) NOT NULL,
    telefon VARCHAR2(20),
    email VARCHAR2(100),
    adresa VARCHAR2(200),
    datum_registrace DATE DEFAULT TRUNC(CURRENT_DATE) NOT NULL,
    PRIMARY KEY (id_zakaznik),
    UNIQUE (email)
);

CREATE TABLE zamestnanec (
    id_zamestnanec NUMBER(10) GENERATED BY DEFAULT AS IDENTITY NOT NULL,
    jmeno VARCHAR2(50) NOT NULL,
    prijmeni VARCHAR2(50) NOT NULL,
    pozice VARCHAR2(30) NOT NULL,
    telefon VARCHAR2(20),
    datum_nastupu DATE NOT NULL,
    PRIMARY KEY (id_zamestnanec)
);

CREATE TABLE dodavatel (
    id_dodavatel NUMBER(10) GENERATED BY DEFAULT AS IDENTITY NOT NULL,
    nazev VARCHAR2(100) NOT NULL,
    kontaktni_osoba VARCHAR2(100),
    telefon VARCHAR2(20),
    email VARCHAR2(100),
    PRIMARY KEY (id_dodavatel)
);

CREATE TABLE kolo (
    id_kolo NUMBER(10) GENERATED BY DEFAULT AS IDENTITY NOT NULL,
    id_zakaznik NUMBER(10) NOT NULL,
    znacka VARCHAR2(50) NOT NULL,
    model VARCHAR2(50),
    typ VARCHAR2(30),
    rok_vyroby NUMBER(5),
    seriove_cislo VARCHAR2(50),
    PRIMARY KEY (id_kolo),
    UNIQUE (seriove_cislo),
    FOREIGN KEY (id_zakaznik) REFERENCES zakaznik (id_zakaznik)
);

CREATE TABLE elektrokolo (
    id_kolo NUMBER(10) NOT NULL,
    vyrobce_motoru VARCHAR2(80) NOT NULL,
    vykon_motoru_w NUMBER(10) NOT NULL,
    kapacita_baterie_wh NUMBER(8,2) NOT NULL,
    PRIMARY KEY (id_kolo),
    FOREIGN KEY (id_kolo) REFERENCES kolo (id_kolo),
    CHECK (vykon_motoru_w > 0),
    CHECK (kapacita_baterie_wh > 0)
);

CREATE TABLE sluzba (
    id_sluzba NUMBER(10) GENERATED BY DEFAULT AS IDENTITY NOT NULL,
    nazev VARCHAR2(100) NOT NULL,
    popis VARCHAR2(300),
    cena_zakladni NUMBER(10,2) NOT NULL,
    odhad_doby_min NUMBER(10),
    PRIMARY KEY (id_sluzba),
    CHECK (cena_zakladni >= 0),
    CHECK (odhad_doby_min IS NULL OR odhad_doby_min > 0)
);

CREATE TABLE dil (
    id_dil NUMBER(10) GENERATED BY DEFAULT AS IDENTITY NOT NULL,
    nazev VARCHAR2(100) NOT NULL,
    cena_prodejni NUMBER(10,2) NOT NULL,
    mnozstvi_sklad NUMBER(10) DEFAULT 0 NOT NULL,
    id_dodavatel NUMBER(10),
    PRIMARY KEY (id_dil),
    FOREIGN KEY (id_dodavatel) REFERENCES dodavatel (id_dodavatel),
    CHECK (cena_prodejni >= 0),
    CHECK (mnozstvi_sklad >= 0)
);

CREATE TABLE zakazka (
    id_zakazka NUMBER(10) GENERATED BY DEFAULT AS IDENTITY NOT NULL,
    id_kolo NUMBER(10) NOT NULL,
    id_zamestnanec NUMBER(10),
    datum_prijeti TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    datum_dokonceni TIMESTAMP,
    stav VARCHAR2(20) DEFAULT 'přijato' NOT NULL,
    poznamka VARCHAR2(500),
    PRIMARY KEY (id_zakazka),
    FOREIGN KEY (id_kolo) REFERENCES kolo (id_kolo),
    FOREIGN KEY (id_zamestnanec) REFERENCES zamestnanec (id_zamestnanec),
    CHECK (stav IN ('přijato','v opravě','hotovo','vyzvednuto','stornováno')),
    CHECK (datum_dokonceni IS NULL OR datum_dokonceni >= datum_prijeti)
);

CREATE TABLE zakazka_sluzba (
    id_zakazka NUMBER(10) NOT NULL,
    id_sluzba NUMBER(10) NOT NULL,
    mnozstvi NUMBER(10) DEFAULT 1 NOT NULL,
    cena_za_jednotku NUMBER(10,2) NOT NULL,
    PRIMARY KEY (id_zakazka, id_sluzba),
    FOREIGN KEY (id_zakazka) REFERENCES zakazka (id_zakazka),
    FOREIGN KEY (id_sluzba) REFERENCES sluzba (id_sluzba),
    CHECK (mnozstvi > 0),
    CHECK (cena_za_jednotku >= 0)
);

CREATE TABLE zakazka_dil (
    id_zakazka NUMBER(10) NOT NULL,
    id_dil NUMBER(10) NOT NULL,
    mnozstvi NUMBER(10) DEFAULT 1 NOT NULL,
    cena_za_jednotku NUMBER(10,2) NOT NULL,
    PRIMARY KEY (id_zakazka, id_dil),
    FOREIGN KEY (id_zakazka) REFERENCES zakazka (id_zakazka),
    FOREIGN KEY (id_dil) REFERENCES dil (id_dil),
    CHECK (mnozstvi > 0),
    CHECK (cena_za_jednotku >= 0)
);

CREATE TABLE faktura (
    id_faktura NUMBER(10) GENERATED BY DEFAULT AS IDENTITY NOT NULL,
    id_zakazka NUMBER(10) NOT NULL,
    datum_vystaveni DATE DEFAULT TRUNC(CURRENT_DATE) NOT NULL,
    castka_celkem NUMBER(10,2) NOT NULL,
    zpusob_platby VARCHAR2(20) NOT NULL,
    stav_platby VARCHAR2(20) DEFAULT 'nezaplaceno' NOT NULL,
    PRIMARY KEY (id_faktura),
    UNIQUE (id_zakazka),
    FOREIGN KEY (id_zakazka) REFERENCES zakazka (id_zakazka),
    CHECK (castka_celkem >= 0),
    CHECK (zpusob_platby IN ('hotově','kartou','převodem')),
    CHECK (stav_platby IN ('zaplaceno','nezaplaceno'))
);
```

## Původ a změny

Zdroj atributů a SQL: `hodnoceni_4_nastroju.xlsx`, listy Model a pravidla a SQL MySQL/PostgreSQL/Oracle. SHA-256 zdroje: `107416a1992434c9d33110a9e74dcec2f1027d68fb2a1fcc1f6f4430a2745b07`. Změna tohoto zadání musí být před skutečnými testy promítnuta do všech tří SQL, protokolu a textu práce; starý a nový model se nesmějí v jednom srovnání míchat.
