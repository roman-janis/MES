# Přehled stavu práce a složky

Aktualizace: 28. 8. 2026.

## Stav

Seminární práce je **dokončena a odevzdána** (12. 7. 2026, kurz KRCR-MES v Olivě). Finální verze od učitele: `seminární práce/MES_Janis_final.docx`. Zápočtový test absolvován. Pracovní bakalářská práce je rozdělena do souborů `BP 0.md` až `BP 15.md`; `BP.md` je jejich sloučený pracovní dokument. Teoretické kapitoly zachovávají text finální seminární práce v co největším rozsahu. Praktické kapitoly mají připravenou úplnou strukturu, ale skutečné testy a AHP výpočty dosud nejsou dokončeny; viditelné značky `⟦NEZAZNAMENÁNO⟧`, `⟦NEVYHODNOCENO⟧` a `⟦NV⟧` proto nejsou výsledky. Pro konzultaci s vedoucím je připraven soubor `PODKLAD_PRO_VEDOUCIHO.md`.

## Složky

| Složka / soubor | Účel |
|---|---|
| `seminární práce/` | Archiv SP — odevzdaná verze, moje verze, zdrojové MD soubory. Needitovat. |
| `BP 0.md`–`BP 15.md` | Pracovní kapitoly úplné BP: úvodní část, teorie, praktická komparace, AHP, diskuse, závěr, zdroje a přílohy. |
| `BP.md` | Sloučený pracovní text vytvořený skriptem `spoj.ps1`. |
| `zadani/` | Oficiální zadání a údaje VŠKP ze STAGu. |
| `oliva/` | Pokyny, šablony a vzory MES. Ponechat jako referenci. |
| `literatura/DB/` | Databázová literatura — bude potřeba v BP. |
| `literatura/AHP/` | Zdroje k AHP a MCDM — bude potřeba v BP. |
| `literatura/inspirace/` | Vzorové BP/DP a další inspirace k AHP a databázím; běžně necitovat jako použité zdroje. |
| `nastroje/` | Instalátory 4 porovnávaných nástrojů. |
| `prezentace UHK/` | Slidy k databázovým předmětům. |
| `PLAN.md` | Aktuální plán přípravy BP. |
| `POZADAVKY_UCITELE.md` | Požadavky vedoucího na BP. |
| `ZDROJE.md` | Přehled zdrojů. |
| `archiv/seminarni-prace/ROZDILY_VERZI_SP.md` | Archivní srovnání mé verze SP a finální verze od učitele. |
| `archiv/` | Historické přípravy, porovnání verzí a později uzavřené konzultační podklady. |
| `docker/` | Docker prostředí — 3 databázové servery (Oracle Database Free, MySQL 8.0, PostgreSQL 16) pro reverse engineering ve 4 srovnávaných nástrojích. |
| `CYKLOSERVIS_ZADANI.md` | Zadání, rozsah a DDL skripty testovací databáze cykloservisu — společný modelový příklad pro všechny 4 nástroje. |
| `AHP_NAVOD_SAATY.md` | Český návod na Saatyho metodu (AHP) s kompletně spočítaným kontrolním příkladem a postupem pro `AHP_vypocet.xlsx`. |

## Nástroje porovnávané v BP

- MySQL Workbench 8.0
- Oracle SQL Developer Data Modeler 24.3
- DBeaver Community Edition 26.0
- pgModeler 1.2.3
