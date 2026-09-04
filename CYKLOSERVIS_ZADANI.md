# Zadání a rozsah: testovací databáze Cykloservis

Modelový scénář pro praktickou část BP — stejné zadání se použije ve všech
čtyřech srovnávaných nástrojích (Oracle SQL Developer Data Modeler, DBeaver
Community Edition, MySQL Workbench, pgModeler), aby bylo srovnání spravedlivé.
Navazuje na `PLAN.md` (blok 2 a 3) a `docker/` (databázové servery pro
reverse engineering).

## 1. Zadání (formulace jako od klienta)

> Malý cykloservis eviduje zákazníky a jejich kola, přijímá zakázky na opravy
> a servis, k zakázkám přiřazuje mechaniky, účtuje provedené služby a
> spotřebovaný materiál (náhradní díly) a k dokončeným zakázkám vystavuje
> faktury. Náhradní díly firma odebírá od několika dodavatelů a sleduje jejich
> skladové množství. Systém má evidovat historii oprav u konkrétního kola
> (více zakázek v čase) a umožnit dohledat, jaké služby a díly byly v rámci
> jedné zakázky použity, včetně jejich ceny v okamžiku zakázky (ceníkové ceny
> služeb a dílů se totiž v čase mění, takže cena musí být uložena i u položky
> zakázky).

Toto zadání je záměrně stručné a obecné — odpovídá rozsahu, jaký by dostal
junior databázový vývojář na začátku návrhu. Rozpracování do entit a atributů
je níže; je to jeden z výstupů, který se má v nástrojích modelovat.

## 2. Doporučený rozsah

**Jádro (10 entit)** — doporučený rozsah pro časově omezené kreslení „od
nuly" (viz `PLAN.md`, blok 3, krok 1). Zahrnuje záměrně:

- tři úrovně 1:N řetězené za sebou (Zákazník → Kolo → Zakázka),
- dvě vazby M:N řešené vlastní asociační entitou se složeným PK a extra
  atributy (množství, cena) — `Zakázka_Služba`, `Zakázka_Díl`,
- jednu nepovinnou (nullable) vazbu 1:N (mechanik u zakázky nemusí být hned
  přiřazen),
- jednu vazbu 1:1 (Zakázka–Faktura),
- unikátní atributy mimo PK (e-mail, sériové číslo kola, FK ve faktuře),
- enumerační/stavový atribut s kontrolou hodnot (stav zakázky, způsob
  platby).

Tato kombinace stačí k ověření, jak si každý nástroj poradí s M:N, složenými
klíči, nepovinnými vztahy a integritními omezeními — bez zbytečné velikosti,
která by vytváření struktury natáhla na hodiny.

**Rozšíření (volitelné, +2 entity)** — pokud po jádru zbude čas a chcete
nástroje otestovat důkladněji: `Objednávka_dodavateli` a
`Objednávka_položka` (M:N mezi Dodavatel a Díl, analogicky k
Zakázka_Díl). Není součástí základního testování, jen rezerva.

### Entity a atributy (jádro)

| Entita | Klíčové atributy | Typ vztahu |
|---|---|---|
| **Zákazník** | id_zakaznik (PK), jmeno, prijmeni, telefon, email (UNIQUE), adresa, datum_registrace | 1:N → Kolo |
| **Kolo** | id_kolo (PK), id_zakaznik (FK), znacka, model, typ, rok_vyroby, seriove_cislo (UNIQUE) | 1:N → Zakázka |
| **Zaměstnanec** | id_zamestnanec (PK), jmeno, prijmeni, pozice, telefon, datum_nastupu | 1:N → Zakázka (nullable FK) |
| **Zakázka** | id_zakazka (PK), id_kolo (FK), id_zamestnanec (FK, NULL), datum_prijeti, datum_dokonceni, stav, poznamka | 1:N → Zakázka_Služba, Zakázka_Díl; 1:1 → Faktura |
| **Služba** | id_sluzba (PK), nazev, popis, cena_zakladni, odhad_doby_min | 1:N → Zakázka_Služba |
| **Díl** | id_dil (PK), nazev, cena_prodejni, mnozstvi_sklad, id_dodavatel (FK) | 1:N → Zakázka_Díl |
| **Dodavatel** | id_dodavatel (PK), nazev, kontaktni_osoba, telefon, email | 1:N → Díl |
| **Zakázka_Služba** | id_zakazka (FK), id_sluzba (FK), mnozstvi, cena_za_jednotku — PK = (id_zakazka, id_sluzba) | M:N Zakázka↔Služba |
| **Zakázka_Díl** | id_zakazka (FK), id_dil (FK), mnozstvi, cena_za_jednotku — PK = (id_zakazka, id_dil) | M:N Zakázka↔Díl |
| **Faktura** | id_faktura (PK), id_zakazka (FK, UNIQUE), datum_vystaveni, castka_celkem, zpusob_platby, stav_platby | 1:1 ← Zakázka |

### Textové ER schéma vztahů

```
Zákazník ──1:N── Kolo ──1:N── Zakázka ──1:1── Faktura
                                  │  │
                        M:N (přes  │  M:N (přes
                     Zakázka_Služba)│ Zakázka_Díl)
                                  │  │
                              Služba  Díl ──N:1── Dodavatel

Zaměstnanec ──1:N (nullable)── Zakázka
```

## 3. DDL skripty (jádro)

Referenční schéma se nahraje do všech tří databázových serverů v `docker/`
*před* krokem reverse engineering (viz bod 4) — díky tomu všechny čtyři
nástroje pracují při této úloze s identickým schématem, což dělá srovnání
spravedlivé. Skripty NEPOUŽÍVEJTE pro krok 1 (vytvoření struktury) ani krok 2
(forward engineering) — tam se struktura vytváří a SQL generuje bez použití
referenčního skriptu.

### PostgreSQL (mes-postgres, port 5432) — pro pgModeler a DBeaver

```sql
CREATE TABLE zakaznik (
    id_zakaznik      SERIAL PRIMARY KEY,
    jmeno            VARCHAR(50) NOT NULL,
    prijmeni         VARCHAR(50) NOT NULL,
    telefon          VARCHAR(20),
    email            VARCHAR(100) UNIQUE,
    adresa           VARCHAR(200),
    datum_registrace DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE zamestnanec (
    id_zamestnanec   SERIAL PRIMARY KEY,
    jmeno            VARCHAR(50) NOT NULL,
    prijmeni         VARCHAR(50) NOT NULL,
    pozice           VARCHAR(30) NOT NULL,
    telefon          VARCHAR(20),
    datum_nastupu    DATE NOT NULL
);

CREATE TABLE dodavatel (
    id_dodavatel     SERIAL PRIMARY KEY,
    nazev            VARCHAR(100) NOT NULL,
    kontaktni_osoba  VARCHAR(100),
    telefon          VARCHAR(20),
    email            VARCHAR(100)
);

CREATE TABLE kolo (
    id_kolo          SERIAL PRIMARY KEY,
    id_zakaznik      INTEGER NOT NULL REFERENCES zakaznik(id_zakaznik),
    znacka           VARCHAR(50) NOT NULL,
    model            VARCHAR(50),
    typ              VARCHAR(30),
    rok_vyroby       SMALLINT,
    seriove_cislo    VARCHAR(50) UNIQUE
);

CREATE TABLE sluzba (
    id_sluzba        SERIAL PRIMARY KEY,
    nazev            VARCHAR(100) NOT NULL,
    popis            VARCHAR(300),
    cena_zakladni    NUMERIC(10,2) NOT NULL,
    odhad_doby_min   INTEGER
);

CREATE TABLE dil (
    id_dil           SERIAL PRIMARY KEY,
    nazev            VARCHAR(100) NOT NULL,
    cena_prodejni    NUMERIC(10,2) NOT NULL,
    mnozstvi_sklad   INTEGER NOT NULL DEFAULT 0,
    id_dodavatel     INTEGER REFERENCES dodavatel(id_dodavatel)
);

CREATE TABLE zakazka (
    id_zakazka       SERIAL PRIMARY KEY,
    id_kolo          INTEGER NOT NULL REFERENCES kolo(id_kolo),
    id_zamestnanec   INTEGER REFERENCES zamestnanec(id_zamestnanec),
    datum_prijeti    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    datum_dokonceni  TIMESTAMP,
    stav             VARCHAR(20) NOT NULL DEFAULT 'přijato'
                     CHECK (stav IN ('přijato','v opravě','hotovo','vyzvednuto','stornováno')),
    poznamka         VARCHAR(500)
);

CREATE TABLE zakazka_sluzba (
    id_zakazka       INTEGER NOT NULL REFERENCES zakazka(id_zakazka),
    id_sluzba        INTEGER NOT NULL REFERENCES sluzba(id_sluzba),
    mnozstvi         INTEGER NOT NULL DEFAULT 1,
    cena_za_jednotku NUMERIC(10,2) NOT NULL,
    PRIMARY KEY (id_zakazka, id_sluzba)
);

CREATE TABLE zakazka_dil (
    id_zakazka       INTEGER NOT NULL REFERENCES zakazka(id_zakazka),
    id_dil           INTEGER NOT NULL REFERENCES dil(id_dil),
    mnozstvi         INTEGER NOT NULL DEFAULT 1,
    cena_za_jednotku NUMERIC(10,2) NOT NULL,
    PRIMARY KEY (id_zakazka, id_dil)
);

CREATE TABLE faktura (
    id_faktura       SERIAL PRIMARY KEY,
    id_zakazka       INTEGER NOT NULL UNIQUE REFERENCES zakazka(id_zakazka),
    datum_vystaveni  DATE NOT NULL DEFAULT CURRENT_DATE,
    castka_celkem    NUMERIC(10,2) NOT NULL,
    zpusob_platby    VARCHAR(20) NOT NULL CHECK (zpusob_platby IN ('hotově','kartou','převodem')),
    stav_platby      VARCHAR(20) NOT NULL DEFAULT 'nezaplaceno' CHECK (stav_platby IN ('zaplaceno','nezaplaceno'))
);
```

Spuštění na kontejneru (viz `docker/README.md` pro přihlašovací údaje):

```powershell
Get-Content .\cykloservis_postgres.sql | docker exec -i mes-postgres psql -U postgres -d mes_demo
```

### MySQL (mes-mysql, port 3306) — pro MySQL Workbench

Stejné schéma, upraveno na dialekt MySQL 8.0 (`AUTO_INCREMENT` místo
`SERIAL`, `ENGINE=InnoDB` kvůli cizím klíčům):

```sql
CREATE TABLE zakaznik (
    id_zakaznik      INT AUTO_INCREMENT PRIMARY KEY,
    jmeno            VARCHAR(50) NOT NULL,
    prijmeni         VARCHAR(50) NOT NULL,
    telefon          VARCHAR(20),
    email            VARCHAR(100) UNIQUE,
    adresa           VARCHAR(200),
    datum_registrace DATE NOT NULL DEFAULT (CURRENT_DATE)
) ENGINE=InnoDB;

CREATE TABLE zamestnanec (
    id_zamestnanec   INT AUTO_INCREMENT PRIMARY KEY,
    jmeno            VARCHAR(50) NOT NULL,
    prijmeni         VARCHAR(50) NOT NULL,
    pozice           VARCHAR(30) NOT NULL,
    telefon          VARCHAR(20),
    datum_nastupu    DATE NOT NULL
) ENGINE=InnoDB;

CREATE TABLE dodavatel (
    id_dodavatel     INT AUTO_INCREMENT PRIMARY KEY,
    nazev            VARCHAR(100) NOT NULL,
    kontaktni_osoba  VARCHAR(100),
    telefon          VARCHAR(20),
    email            VARCHAR(100)
) ENGINE=InnoDB;

CREATE TABLE kolo (
    id_kolo          INT AUTO_INCREMENT PRIMARY KEY,
    id_zakaznik      INT NOT NULL,
    znacka           VARCHAR(50) NOT NULL,
    model            VARCHAR(50),
    typ              VARCHAR(30),
    rok_vyroby       SMALLINT,
    seriove_cislo    VARCHAR(50) UNIQUE,
    FOREIGN KEY (id_zakaznik) REFERENCES zakaznik(id_zakaznik)
) ENGINE=InnoDB;

CREATE TABLE sluzba (
    id_sluzba        INT AUTO_INCREMENT PRIMARY KEY,
    nazev            VARCHAR(100) NOT NULL,
    popis            VARCHAR(300),
    cena_zakladni    DECIMAL(10,2) NOT NULL,
    odhad_doby_min   INT
) ENGINE=InnoDB;

CREATE TABLE dil (
    id_dil           INT AUTO_INCREMENT PRIMARY KEY,
    nazev            VARCHAR(100) NOT NULL,
    cena_prodejni    DECIMAL(10,2) NOT NULL,
    mnozstvi_sklad   INT NOT NULL DEFAULT 0,
    id_dodavatel     INT,
    FOREIGN KEY (id_dodavatel) REFERENCES dodavatel(id_dodavatel)
) ENGINE=InnoDB;

CREATE TABLE zakazka (
    id_zakazka       INT AUTO_INCREMENT PRIMARY KEY,
    id_kolo          INT NOT NULL,
    id_zamestnanec   INT,
    datum_prijeti    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    datum_dokonceni  DATETIME,
    stav             VARCHAR(20) NOT NULL DEFAULT 'přijato'
                     CHECK (stav IN ('přijato','v opravě','hotovo','vyzvednuto','stornováno')),
    poznamka         VARCHAR(500),
    FOREIGN KEY (id_kolo) REFERENCES kolo(id_kolo),
    FOREIGN KEY (id_zamestnanec) REFERENCES zamestnanec(id_zamestnanec)
) ENGINE=InnoDB;

CREATE TABLE zakazka_sluzba (
    id_zakazka       INT NOT NULL,
    id_sluzba        INT NOT NULL,
    mnozstvi         INT NOT NULL DEFAULT 1,
    cena_za_jednotku DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_zakazka, id_sluzba),
    FOREIGN KEY (id_zakazka) REFERENCES zakazka(id_zakazka),
    FOREIGN KEY (id_sluzba) REFERENCES sluzba(id_sluzba)
) ENGINE=InnoDB;

CREATE TABLE zakazka_dil (
    id_zakazka       INT NOT NULL,
    id_dil           INT NOT NULL,
    mnozstvi         INT NOT NULL DEFAULT 1,
    cena_za_jednotku DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_zakazka, id_dil),
    FOREIGN KEY (id_zakazka) REFERENCES zakazka(id_zakazka),
    FOREIGN KEY (id_dil) REFERENCES dil(id_dil)
) ENGINE=InnoDB;

CREATE TABLE faktura (
    id_faktura       INT AUTO_INCREMENT PRIMARY KEY,
    id_zakazka       INT NOT NULL UNIQUE,
    datum_vystaveni  DATE NOT NULL DEFAULT (CURRENT_DATE),
    castka_celkem    DECIMAL(10,2) NOT NULL,
    zpusob_platby    VARCHAR(20) NOT NULL CHECK (zpusob_platby IN ('hotově','kartou','převodem')),
    stav_platby      VARCHAR(20) NOT NULL DEFAULT 'nezaplaceno' CHECK (stav_platby IN ('zaplaceno','nezaplaceno')),
    FOREIGN KEY (id_zakazka) REFERENCES zakazka(id_zakazka)
) ENGINE=InnoDB;
```

Spuštění:

```powershell
Get-Content .\cykloservis_mysql.sql | docker exec -i mes-mysql mysql -uroot -pmes_mysql_pw mes_demo
```

### Oracle Database Free (mes-oracle, port 1521, service `FREEPDB1`) — pro Oracle SQL Developer Data Modeler

Oracle nemá `SERIAL`/`AUTO_INCREMENT` — použity identity sloupce (Oracle
12c+, v `gvenzl/oracle-free:23-slim` dostupné), `VARCHAR2` místo `VARCHAR`,
`NUMBER` místo `INTEGER`/`DECIMAL`, `DATE` pokrývá i čas:

```sql
CREATE TABLE zakaznik (
    id_zakaznik      NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    jmeno            VARCHAR2(50) NOT NULL,
    prijmeni         VARCHAR2(50) NOT NULL,
    telefon          VARCHAR2(20),
    email            VARCHAR2(100) UNIQUE,
    adresa           VARCHAR2(200),
    datum_registrace DATE DEFAULT SYSDATE NOT NULL
);

CREATE TABLE zamestnanec (
    id_zamestnanec   NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    jmeno            VARCHAR2(50) NOT NULL,
    prijmeni         VARCHAR2(50) NOT NULL,
    pozice           VARCHAR2(30) NOT NULL,
    telefon          VARCHAR2(20),
    datum_nastupu    DATE NOT NULL
);

CREATE TABLE dodavatel (
    id_dodavatel     NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nazev            VARCHAR2(100) NOT NULL,
    kontaktni_osoba  VARCHAR2(100),
    telefon          VARCHAR2(20),
    email            VARCHAR2(100)
);

CREATE TABLE kolo (
    id_kolo          NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_zakaznik      NUMBER NOT NULL REFERENCES zakaznik(id_zakaznik),
    znacka           VARCHAR2(50) NOT NULL,
    model            VARCHAR2(50),
    typ              VARCHAR2(30),
    rok_vyroby       NUMBER(4),
    seriove_cislo    VARCHAR2(50) UNIQUE
);

CREATE TABLE sluzba (
    id_sluzba        NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nazev            VARCHAR2(100) NOT NULL,
    popis            VARCHAR2(300),
    cena_zakladni    NUMBER(10,2) NOT NULL,
    odhad_doby_min   NUMBER
);

CREATE TABLE dil (
    id_dil           NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nazev            VARCHAR2(100) NOT NULL,
    cena_prodejni    NUMBER(10,2) NOT NULL,
    mnozstvi_sklad   NUMBER DEFAULT 0 NOT NULL,
    id_dodavatel     NUMBER REFERENCES dodavatel(id_dodavatel)
);

CREATE TABLE zakazka (
    id_zakazka       NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_kolo          NUMBER NOT NULL REFERENCES kolo(id_kolo),
    id_zamestnanec   NUMBER REFERENCES zamestnanec(id_zamestnanec),
    datum_prijeti    DATE DEFAULT SYSDATE NOT NULL,
    datum_dokonceni  DATE,
    stav             VARCHAR2(20) DEFAULT 'přijato' NOT NULL
                     CHECK (stav IN ('přijato','v opravě','hotovo','vyzvednuto','stornováno')),
    poznamka         VARCHAR2(500)
);

CREATE TABLE zakazka_sluzba (
    id_zakazka       NUMBER NOT NULL REFERENCES zakazka(id_zakazka),
    id_sluzba        NUMBER NOT NULL REFERENCES sluzba(id_sluzba),
    mnozstvi         NUMBER DEFAULT 1 NOT NULL,
    cena_za_jednotku NUMBER(10,2) NOT NULL,
    PRIMARY KEY (id_zakazka, id_sluzba)
);

CREATE TABLE zakazka_dil (
    id_zakazka       NUMBER NOT NULL REFERENCES zakazka(id_zakazka),
    id_dil           NUMBER NOT NULL REFERENCES dil(id_dil),
    mnozstvi         NUMBER DEFAULT 1 NOT NULL,
    cena_za_jednotku NUMBER(10,2) NOT NULL,
    PRIMARY KEY (id_zakazka, id_dil)
);

CREATE TABLE faktura (
    id_faktura       NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_zakazka       NUMBER NOT NULL UNIQUE REFERENCES zakazka(id_zakazka),
    datum_vystaveni  DATE DEFAULT SYSDATE NOT NULL,
    castka_celkem    NUMBER(10,2) NOT NULL,
    zpusob_platby    VARCHAR2(20) NOT NULL CHECK (zpusob_platby IN ('hotově','kartou','převodem')),
    stav_platby      VARCHAR2(20) DEFAULT 'nezaplaceno' NOT NULL CHECK (stav_platby IN ('zaplaceno','nezaplaceno'))
);
```

Spuštění (sqlplus přes kontejner, uživatel `mes_app`):

```powershell
Get-Content .\cykloservis_oracle.sql | docker exec -i mes-oracle sqlplus -S mes_app/mes_app_pw@localhost/FREEPDB1
```

## 4. Postup testování (4 kroky × 4 nástroje)

Navazuje na `PLAN.md`, blok 3. Zápis výsledků do
`nastroje/hodnoceni_NAZEV.md` (sloupce: krok, čas začátku, čas konce,
pozorování, screenshot).

| Krok | Co se dělá | Cílová DB / poznámka |
|---|---|---|
| 1. Vytvoření struktury podle zadání | Vytvořit celé jádro (10 entit) jen podle bodů 1–2, bez referenčního SQL skriptu. U nástrojů se samostatným modelem začít prázdným modelem. Pokud testovaná edice nabízí diagram pouze nad živým schématem, vytvořit objekty nejbližším podporovaným postupem na prázdné DB a tuto odchylku výslovně zaznamenat. | DBeaver Community nemá být automaticky považován za plnohodnotný model-first nástroj; ověřit přesný pracovní postup v testované verzi. |
| 2. Forward engineering | Z vlastního modelu vygenerovat DDL a spustit jej na příslušném serveru. U databázově orientovaného postupu vyexportovat DDL vytvořeného schématu a ověřit jeho spuštěním na novém prázdném schématu; rozdíl popsat. | Oracle DM → mes-oracle · MySQL WB → mes-mysql · pgModeler → mes-postgres · DBeaver → mes-postgres |
| 3. Reverse engineering | Nejprve na server nahrát **referenční skript z bodu 3** (stejné schéma pro všechny nástroje), pak se nástrojem připojit a nechat sestavit model nebo diagram ze živé DB. | Stejné cílové servery jako výše. U pgModeleru ověřit dostupnost v přesné použité verzi a edici; nedostupnost zapsat jako výsledek a nenahrazovat ji jinou edicí bez uvedení změny. |
| 4. Export | Exportovat diagram do skutečně dostupných formátů. Odlišit nativní export od tisku do PDF nebo následného převodu. | — |

Doporučené pořadí cílové DB pro DBeaver: PostgreSQL (`mes-postgres`) jako
hlavní, protože umožní nezávisle ověřit referenční schéma i výstup, který
pgModeler ve kroku 2 vygeneroval. Pokud
zbude čas, lze DBeaver dodatečně vyzkoušet i proti `mes-mysql` /
`mes-oracle` jako doklad univerzálnosti nástroje (K3 Kompatibilita).

### Odhad času

10 entit → vytvoření struktury cca 30–45 min, forward engineering nebo export DDL 10–15 min,
reverse engineering 15–20 min, export 5 min → **cca 60–90 min na nástroj**,
tedy 4–6 hodin celkem na všechny čtyři nástroje (odpovídá bloku
11.–16. 8. v `PLAN.md`).
