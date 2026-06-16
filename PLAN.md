# Plán další práce

Aktualizace: 16. 6. 2026.

Pracuje se po kapitolách v souborech `Seminární práce 0.md` – `Seminární práce 11.md`. Finální `Seminární práce.md` a `.docx` se z nich jen generují (viz `PŘEHLED.md`). Soubory `Seminární práce 12.md` a `13.md` jsou nepoužívané rezervy.

## 1. Priorita teď: dokončit a odeslat seminární práci MES

Seminární práce je obsahově hotová jako první verze. Zbývá technické dokončení a odeslání.

### Hotovo k 16. 6. 2026

- ✅ Struktura sjednocena podle šablony MES; kapitoly číslovány souvisle 0–11 (bez děr).
- ✅ Citace v textu spárovány se seznamem zdrojů (14 zdrojů, vše páruje).
- ✅ Seznam zdrojů seřazen abecedně a rozdělen na tištěné a internetové zdroje (dle šablony SP).
- ✅ Jazyková a stylistická revize, omezení šablonovitých formulací, sjednocení typografie (česká pomlčka, normální spojovníky).
- ✅ Sjednocena terminologie návrh/vývoj databáze (kap. 4.4).
- ✅ Ošetřeno poškození souborů z Google Disku (odstraněny NUL byty, doplněna useknutá místa).

### Před odesláním vedoucímu – zbývá

1. Spojit kapitoly (`python sestavit_seminarni_praci.py` nebo `.\spoj.ps1`) do `Seminární práce.md`.
2. Převést `Seminární práce.md` do `Seminární práce.docx`.
3. Ve Wordu aktualizovat pole obsahu (klik do obsahu → F9), zkontrolovat stránkování, okraje, fonty, řádkování.
4. Doplnit datum v prohlášení.
5. Ověřit rozsah: teorie včetně seznamu zdrojů má mít ≥ 10 stran (titulka, abstrakt, klíčová slova a obsah se nepočítají).
6. Poslat první verzi vedoucímu Ing. et Ing. Martinu Lněničkovi, Ph.D.

### Po připomínkách

1. Zapracovat připomínky do kapitolových souborů.
2. Znovu spojit a vygenerovat `.docx`.
3. Odevzdat v Olivě a splnit zápočtový test.

## 2. Paralelně: STAG zadávací list (do 31. 8. 2026)

Vyplnit ve STAGu:

- anglický název: *Comparison of Database Design and Development Tools Using AHP*,
- 4–5 literárních zdrojů (alespoň 2–3 knihy + článek/web), citace dle ISO 690:2022,
- případně upravený cíl a osnovu,
- odeslat ke schválení.

Doporučený výběr zdrojů pro STAG: Pokorný a Valenta (2020), Chlapek, Kučera a Palovská (2019), Saaty (1990), Saaty (2008), Soukopová (2016), případně jedna oficiální dokumentace nástroje.

## 3. Následně: bakalářská práce

Seminární práce slouží jako teoretický a metodický základ. BP doplní praktickou část:

1. Instalace a testování nástrojů (MySQL Workbench, Oracle SQL Developer Data Modeler, DBeaver CE, pgModeler).
2. Jednotný testovací scénář (model → SQL → reverzní inženýrství).
3. Sestavení AHP hierarchie, Saatyho matice kritérií i alternativ.
4. Výpočet vah, lokálních a globálních priorit, kontrola konzistence (CR < 0,1).
5. Analýza citlivosti.
6. Doporučení pro praxi (modelové scénáře malé a střední firmy).
7. Rozšíření literatury a teorie; zvážit vlastní podpůrnou aplikaci pro AHP.

## 4. Milníky

| Termín | Úkol |
|---|---|
| červen 2026 | Poslat první verzi seminární práce vedoucímu. |
| červen/srpen 2026 | Odevzdat seminární práci v Olivě a splnit zápočtový test. |
| do 31. 8. 2026 | Doplnit a odeslat STAG zadávací list. |
| podzim 2026 | Prakticky otestovat nástroje a připravit AHP výpočty. |
| dle plánu BP | Dokončit a odevzdat bakalářskou práci. |
