# Plán další práce

Aktualizace: 14. 6. 2026.

Současný stav: staré pracovní soubory `Bakalářská práce.docx`, `Bakalářská práce.md` a `Seminární práce.txt` byly odstraněny. Hlavní výstup je `Seminární práce.docx`; zdrojová verze je `Seminární práce.md`.

## 1. Priorita teď: dokončit seminární práci MES

Seminární práce je obsahově hotová jako první verze. Zbývá hlavně kontrola, drobné úpravy a odeslání vedoucímu.

### Hotovo k 14. 6. 2026 (jen v `Seminární práce.md`)

- ✅ Porovnány citace v textu se seznamem zdrojů — vše páruje (19 zdrojů).
- ✅ Doplněn chybějící Carvalho et al. (2022).
- ✅ Vyřešen `PostgreSQL Documentation` (in-text citace v 8.4 + sjednocen autor).
- ✅ Doplněn podpůrný zdroj Simanavičienė a Vdovinskienė (2023).

**Pracovní režim od 14. 6. 2026:** hlavní soubor je `Seminární práce.docx`, edituje se přímo v něm (md je archiv). Citační opravy už jsou v docx zapsané.

### Před odesláním vedoucímu — zbývá (vše přímo v docx)

1. Otevřít docx ve Wordu a aktualizovat obsah (klik do obsahu → F9).
2. Zkontrolovat stránkování, záhlaví/zápatí, čísla stran, okraje, fonty a řádkování.
3. Doplnit datum v prohlášení.
4. Projít pravopis a stylistiku.
5. Zkontrolovat formulace v pasivu a odstranit zbytečné výskyty „autor“ mimo prohlášení/metodiku.
6. Ověřit, že deklarace AI odpovídá skutečně použitým nástrojům.
7. Zvážit abecední řazení seznamu zdrojů, příp. rozdělení na tištěné/internetové dle šablony SP.

### Odeslání

1. Poslat první verzi vedoucímu Ing. et Ing. Martinu Lněničkovi, Ph.D.
2. Počkat na připomínky.
3. Zapracovat připomínky do `Seminární práce.md`.
4. Znovu vygenerovat nebo ručně aktualizovat `Seminární práce.docx`.
5. Odevzdat v Olivě.
6. Splnit zápočtový test v Olivě.

## 2. Paralelně: STAG zadávací list

Termín podle e-mailu vedoucího: do konce srpna 2026.

Vyplnit ve STAGu:

- anglický název: *Comparison of Database Design and Development Tools Using AHP*,
- 4-5 literárních zdrojů,
- případně upravený cíl a osnovu podle aktuální seminární práce,
- odeslat ke schválení.

Doporučený výběr zdrojů pro STAG:

1. Pokorný a Valenta (2020) - databázové systémy.
2. Saaty (1990) - původní/průlomový článek k AHP.
3. Saaty (2008) - přehled rozhodování pomocí AHP.
4. Soukopová (2016) - český učební text k vícekriteriálním metodám.
5. Jedna oficiální dokumentace nástroje, například MySQL Workbench nebo Oracle SQL Developer Data Modeler.

## 3. Následně: bakalářská práce

Seminární práce se použije jako teoretický a metodický základ. Bakalářská práce už musí doplnit praktické testování a výpočty.

### Praktická část BP

1. Nainstalovat a otestovat nástroje:
   - MySQL Workbench,
   - Oracle SQL Developer Data Modeler,
   - DBeaver Community Edition,
   - pgModeler.
2. Připravit jednotný testovací scénář.
3. Pro každý nástroj zaznamenat:
   - podporované modelování,
   - forward engineering,
   - reverse engineering,
   - kompatibilitu DBMS,
   - import/export,
   - validaci modelu,
   - použitelnost,
   - cenu/licenci.
4. Sestavit AHP hierarchii.
5. Sestavit Saatyho matici kritérií.
6. Sestavit matice alternativ pro každé kritérium.
7. Vypočítat váhy, lokální a globální priority.
8. Zkontrolovat konzistenci pomocí CR.
9. Udělat analýzu citlivosti.
10. Formulovat doporučení pro praxi.

### Rozšíření teorie pro BP

- Doplnit ověřené knižní zdroje k databázím.
- Doplnit ověřené knižní zdroje k AHP a vícekriteriálním metodám.
- Rozšířit historický vývoj databázových systémů.
- Zpřesnit hodnoticí kritéria a případně je rozdělit na subkritéria.
- Rozhodnout, zda vznikne vlastní podpůrná aplikace pro výpočet AHP.

## 4. Milníky

| Termín | Úkol |
|---|---|
| červen 2026 | Poslat první verzi seminární práce vedoucímu. |
| červen/srpen 2026 | Odevzdat seminární práci v Olivě a splnit zápočtový test. |
| do 31. 8. 2026 | Doplnit a odeslat STAG zadávací list. |
| září-říjen 2026 | Prakticky otestovat nástroje a připravit AHP výpočty. |
| listopad 2026 | Dokončit a odevzdat bakalářskou práci. |

## 5. Návrh na další aktualizaci složky

- Přesunout staré pomocné AI kontexty `CLAUDE.md` a `GEMINI.md` do archivu, pokud je nebudeš používat.
- Složku `na smazání/` zkontrolovat a případně odstranit, pokud v ní není nic potřebného.
- Po odevzdání seminární práce vytvořit novou složku `archiv/MES/` a uložit do ní finální odevzdanou verzi.
- Pro BP založit nový pracovní soubor až ve chvíli, kdy bude schválený STAG zadávací list.
