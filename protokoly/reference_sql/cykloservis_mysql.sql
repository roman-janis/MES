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
