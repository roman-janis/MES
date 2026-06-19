# Plán další práce

Aktualizace: 18. 6. 2026.

Pracuje se po kapitolách v souborech `Seminární práce 0.md` – `Seminární práce 11.md`. Finální `Seminární práce.md` a `.docx` se z nich jen generují (viz `PŘEHLED.md`).

---

## 1. Seminární práce — co zbývá udělat

### Co je hotovo

- ✅ Struktura a číslování kapitol 0–11.
- ✅ 22 citovaných zdrojů, vše spárované se seznamem (SP 11).
- ✅ Rosenthal a Reiner (1994) přidán do SP 4 a SP 11.
- ✅ Velasquez & Hester (2013) a Ishizaka & Labib (2011) — do SP 6, SP 11.
- ✅ Chen (1976) — do SP 5.1, SP 11.
- ✅ Watt & Eng (2014) — do SP 4 a SP 5.2, SP 11.
- ✅ Codd (1970) — do SP 5.2 a SP 5.4, SP 11.
- ✅ Mardani et al. (2015) — do SP 6 úvod a SP 6.2, SP 11.
- ✅ Ishizaka & Labib (2011) přidán i do SP 7.3.
- ✅ Vaidya & Kumar (2006) — do SP 7 intro, SP 11.
- ✅ Ho (2008) — do SP 7.3, SP 11.
- ✅ Jazyková revize, typografie, terminologie.
- ✅ Poslána první verze vedoucímu — zpětná vazba přijata 17. 6. 2026.

### Co je hotovo — stav kapitol po zdrojích

| Kapitola | Zdrojů | Stav |
|---|---|---|
| 4 Databázové systémy | 3 | ⚠️ slabá — přidat 4. zdroj |
| 5 Datové modely | 5 | ✅ |
| 6 MCDM | 6 | ✅ |
| 7 AHP | 5 | ✅ |

---

### Co musí být hotovo PŘED odesláním vedoucímu (druhá verze)

Seřazeno od nejnutnějšího:

**1. Smazat větu o citacích z metodiky** (`Seminární práce 1.md`)
Smazat: *„Citace jsou v textu uváděny harvardským způsobem, tedy ve tvaru autor a rok. Seznam zdrojů je zpracován podle normy ČSN ISO 690:2022. U webových zdrojů je uvedeno datum citace."*

**2. Přidat MCDM články do metodiky** (`Seminární práce 1.md`)
Přidat 1–2 věty do zdůvodnění volby AHP s citacemi (Velasquez a Hester 2013; Ishizaka a Labib 2011).

**3. Sehnat 4. zdroj do kapitoly 4** (`Seminární práce 4.md`)
Aktuálně jen 3 zdroje — vedoucí chce 4–5. Nejrychlejší cesta je jedna z těchto knih přes školní knihovnu:
- **Connolly & Begg** — Database Systems (2015), ISBN 978-1292061184
- **Elmasri & Navathe** — Fundamentals of Database Systems (2016), ISBN 978-0133970777
Po sehnání přidat citaci do SP 4 (§4.1 nebo §4.3) a SP 11.

**4. ✅ Stáhnout PDF pro Codd (1970) a Mardani et al. (2015)** — HOTOVO (19. 6. 2026)
- `literatura/DB/Codd_1970_Relational_model.pdf` — staženo
- `literatura/AHP/Mardani_2015_MCDM_review.pdf` — staženo

**5. Rozepsat kapitoly 4.1–4.4** (`Seminární práce 4.md`)
Každá podkapitola min. 2–3 odstavce s citacemi.

**6. Sekce scénáře/aplikace zkrátit na ~1 stranu**
Explicitně označit jako základ pro navazující bakalářskou práci.

**7. Přepsat „seminární práce" → „práce"** v celém textu.

**8. Přesunout do šablony SP z Olivy** (`oliva/sablony/`)
Vložit text do šablony, zkontrolovat formátování.

**9. Spojit a vygenerovat výstupní soubory**
```
.\spoj.ps1
```
nebo
```
python sestavit_seminarni_praci.py
```

**10. Ověřit rozsah**
Teorie (kapitoly 4–7) musí mít ≥ 10 stran.

**11. Smazat `NAVRHY_CITACI_KAPITOLY_4-7.md`** — obsah je zapracovaný.

**12. Odeslat vedoucímu v šabloně**

---

### Po schválení vedoucím

- Odevzdat v Olivě.
- Splnit zápočtový test v Olivě.

---

## 2. Paralelně: STAG zadávací list (do 31. 8. 2026)

Vyplnit ve STAGu:
- anglický název: *Comparison of Database Design and Development Tools Using AHP*
- 4–5 zdrojů (alespoň 2–3 knihy + článek/web), citace dle ISO 690:2022
- odeslat ke schválení

Navrhované zdroje pro STAG: Pokorný a Valenta (2020), Chlapek, Kučera a Palovská (2019), Saaty (1990), Saaty (2008), Soukopová (2016).

---

## 3. Bakalářská práce — následně

Seminárka slouží jako teoretický základ. BP doplní:
1. Instalace a testování nástrojů (MySQL Workbench, Oracle SQL Developer Data Modeler, DBeaver CE, pgModeler).
2. Jednotný testovací scénář (model → SQL → reverzní inženýrství).
3. AHP výpočty: Saatyho matice, váhy, CR < 0,1, analýza citlivosti.
4. Doporučení pro praxi.
5. Rozšíření literatury na min. 30 zdrojů (20 knih/článků).

---

## 4. Milníky

| Termín | Úkol |
|---|---|
| červen 2026 | Zapracovat připomínky, odeslat druhou verzi vedoucímu v šabloně. |
| červen/srpen 2026 | Odevzdat v Olivě, splnit zápočtový test. |
| do 31. 8. 2026 | Doplnit a odeslat STAG zadávací list. |
| podzim 2026 | Otestovat nástroje, připravit AHP výpočty. |
| dle plánu BP | Dokončit a odevzdat bakalářskou práci. |
