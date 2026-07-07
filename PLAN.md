# Plán další práce

Aktualizace: 7. 7. 2026.

Text seminární práce je obsahově hotový a zkontrolovaný (viz `KONTROLA_OPRAVY.md`). Zbývají technické kroky sestavení dokumentu a odevzdání.

---

## 1. Sestavit finální dokument (nyní)

Soubory kapitol 0–11 jsou hotové, soubory `4x–7x.md` existují.

**Co chybí:**
- `Seminární práce.md` — spustit `spoj.ps1`
- `Seminární práce.docx` — spustit pandoc se šablonou

**Postup:**
```powershell
.\spoj.ps1 0 1 2 3 4x 5x 6x 7x 8 9 10 11 -Out "Seminární práce.md"
```

Pak pandoc — **pozor:** v `oliva/sablony/` jsou tři soubory šablon, je potřeba zjistit, která je správná pro MES:
- `Sablona pro tvorbu SP.docx`
- `šablona( nová (1).docx`
- `Sablona SP.docx`

```powershell
pandoc "Seminární práce.md" -o "Seminární práce.docx" --reference-doc="oliva/sablony/<SPRÁVNÁ ŠABLONA>.docx"
```

---

## 2. Zkontrolovat Word dokument

- Teorie (kapitoly 4–7) musí mít **min. 10 normostran** (úvodní strana, abstrakt, obsah se nepočítají).
- Zkontrolovat nadpisy jako styly, obsah, zalomení stran, tabulky, seznam zdrojů.
- Zkontrolovat, že citace v textu odpovídají seznamu v kapitole 11.

---

## 3. Odeslat vedoucímu (co nejdříve, nejpozději do konce července)

Vedoucí (email 26. 6.) řekl: pošle zpět verzi upravenou po formální stránce pro odevzdání.

→ Odeslat `Seminární práce.docx` na martin.lnenicka@uhk.cz.

---

## 4. Po obdržení verze od vedoucího

- Odevzdat v Olivě (kurz KRCR-MES).
- Splnit zápočtový test v Olivě.

---

## 5. STAG — zadávací list (do 31. 8. 2026)

Vyplnit ve STAGu:
- Anglický název: *Comparison of Database Design and Development Tools Using AHP*
- 4–5 zdrojů (alespoň 2–3 knihy + článek/web), citace dle ISO 690:2022
- Odeslat ke schválení vedoucímu

---

## 6. Bakalářská práce (podzim 2026 / 2027)

Seminárka slouží jako teoretický základ. BP doplní:
1. Instalace a testování nástrojů (MySQL Workbench, Oracle SQL Developer Data Modeler, DBeaver CE, pgModeler).
2. Jednotný testovací scénář (model → SQL → reverzní inženýrství).
3. AHP výpočty: Saatyho matice, váhy, CR < 0,1, analýza citlivosti.
4. Jednoduchá podpůrná aplikace pro výpočet AHP.
5. Doporučení pro praxi (scénáře malá / střední firma).
6. Rozšíření literatury na min. 30 zdrojů (20 knih/článků).

---

## Milníky

| Termín | Úkol | Stav |
|---|---|---|
| 26. 6. 2026 | Poslat vedoucímu průběžnou ukázku. | ✅ Splněno |
| 7. 7. 2026 | Sestavit finální dokument a odeslat vedoucímu. | ⏳ Dnes |
| červenec 2026 | Obdržet verzi od vedoucího, odevzdat v Olivě, splnit test. | ⏳ |
| do 31. 8. 2026 | Vyplnit a odeslat zadávací list do STAGu. | ⏳ |
| podzim 2026 / 2027 | Realizace praktické části bakalářské práce. | ⏳ |
