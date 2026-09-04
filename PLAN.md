# Plán přípravy bakalářské práce

Aktualizace: 28. 8. 2026.

## Stav

- Seminární práce **odevzdána** (12. 7. 2026, Oliva, KRCR-MES).
- Zápočtový test **absolvován**.
- **Zápočet MES zapsán** vedoucím do STAGu (datum 30. 6. 2026).
- Vedoucí odpověděl 13. 7. 2026 — schůzka v srpnu (týden od 17. nebo 24. 8.), FIM nebo Teams.
- 23. 7.: připraveno AHP zadání pro volbu AI, odkazy na AHP nástroje/Excel/PDF a staženy aktuální instalátory DBeaver 26.1.5 a MySQL Workbench 8.0.47. Historické podrobnosti: `archiv/priprava/AHP_AI_a_nastroje_priprava.md`.
- 23. 7.: ověřeno omezení pgModeleru — Community je zdrojový kód a reverse engineering je pouze v Plus. Před instalací je nutné rozhodnout, jak s ním bude práce nakládat.
- 13. 8.: **hotové Docker prostředí** se třemi databázovými servery (Oracle Database Free, MySQL 8.0, PostgreSQL 16) pro reverse engineering ve všech 4 nástrojích — `docker/` (spuštění, porty a přihlašovací údaje v `docker/README.md`).
- 13. 8.: **připraveno zadání a rozsah testovací databáze cykloservisu** (10 entit, DDL skripty pro PostgreSQL/MySQL/Oracle, postup a časový odhad testování) — `CYKLOSERVIS_ZADANI.md`.
- 13. 8.: **hotový český návod na Saatyho metodu (AHP)** s kompletně spočítaným kontrolním příkladem (3 kritéria × 3 alternativy, ověřitelné v Excelu) a postupem, jak z něj sestavit `AHP_vypocet.xlsx` — `AHP_NAVOD_SAATY.md`. Splňuje bod 1.3 níže.
- 28. 8.: pracovní obsah BP je rozdělen do kapitol `BP 0.md`–`BP 15.md`; teorie zachovává finální text seminární práce, praktické kapitoly obsahují úplnou strukturu s jednoznačnými nečíselnými zástupnými značkami. Pro vedoucího je připraven `PODKLAD_PRO_VEDOUCIHO.md`. Skutečné testy, AHP matice, výsledky a závěr zůstávají otevřené.
- 28. 8.: provedena úplná kontrola věcného souladu všech kapitol `BP 0.md`–`BP 15.md` proti požadavkům vedoucího, e-mailové komunikaci, `AHP_NAVOD_SAATY.md`, `CYKLOSERVIS_ZADANI.md` a `ZDROJE.md`. Opraveno: chybějící deklarace použití AI nástrojů v `BP 3.md` (zůstává jako otevřený `⟦DOPLNIT⟧`, nutno vyplnit skutečnými údaji), chybný neutrální placeholder v `BP 9.md` u referenční platformy DBeaveru (nahrazeno PostgreSQL podle `CYKLOSERVIS_ZADANI.md`), chybějící záznam Vaidya a Kumar (2006) v `ZDROJE.md`, nepřesná verze DBeaveru v tomto plánu (26.1.3 → 26.1.5 podle skutečně staženého instalátoru) a upřesněný komentář v `BP 14.md` k počtu a skladbě zdrojů (18 jednoznačných knih/článků z 27 položek, chybí ISSN u Catak a Ebrahimi). Žádná testovací data, AHP hodnoty ani závěry nebyly vymýšleny. Otevřené body k domluvě s vedoucím zůstávají tři z `PODKLAD_PRO_VEDOUCIHO.md` (DBeaver, pgModeler, rozsah AHP aplikace).

### ▶ Další krok (pokračovat odsud)

1. Nainstalovat 4 nástroje (blok 2, bod 1) — instalátory už jsou stažené v `nastroje/`, jen před pgModelerem rozhodnout edici.
2. Nahrát DDL skripty z `CYKLOSERVIS_ZADANI.md` na kontejnery v `docker/` (příkazy jsou přímo v souboru u každého skriptu).
3. Podle toho spustit testování 4 nástrojů (blok 3) postupem z `CYKLOSERVIS_ZADANI.md`, sekce 4.
4. Souběžně/kdykoliv mezitím: sestavit `AHP_vypocet.xlsx` podle `AHP_NAVOD_SAATY.md`, sekce 6, a zkontrolovat proti kontrolnímu příkladu ze sekce 5.

Docker kontejnery (`mes-oracle`, `mes-mysql`, `mes-postgres`) aktuálně **běží** na pozadí. Pokud se v práci nebude pokračovat hned, lze je zastavit (`docker compose down` ve složce `docker/` — data ve volumes zůstanou zachována) a znovu nastartovat příště (`docker compose up -d`).

---

## 1. AHP — šablony, výpočet, Excel
**22. 7. – 31. 7. 2026**

1. ✅ Vyhledány AHP weby, Excel/Google Sheets zdroje a PDF návody; historický podklad k porovnání Codexu/ChatGPT, Gemini a Claude je uložen v `archiv/priprava/AHP_AI_a_nastroje_priprava.md`.
2. ⏳ Otevřít BPMSG a prakticky otestovat nejméně 3 weby a BPMSG Excel šablonu: zapsat CR, chybové hlášky, přehlednost a použitelnost pro laika. Teprve pak napsat odstavec srovnání do BP.
3. ✅ Projít 1 kompletní AHP příklad ze Saaty (1990, s. 9–26) ručně — sestavit matici → geometrický průměr → váhy → CR. Hotovo v `AHP_NAVOD_SAATY.md` (kontrolní příklad 3×3 + 3×3×3, plně dopočítaný).
4. ⏳ Sestavit `AHP_vypocet.xlsx`: List 1 matice kritérií 8×8 + váhy + CR; Listy 2–9 matice nástrojů 4×4 (1 list / kritérium); List 10 syntéza; List 11 analýza citlivosti K1 nebo K8 (mění se jedna váha, ne obě zároveň). Struktura a Excel vzorce popsány v `AHP_NAVOD_SAATY.md`, sekce 6.

---

## 2. Instalace nástrojů + testovací DB
**1. 8. – 10. 8. 2026**

1. ⏳ Nainstalovat nástroje: Oracle SQL Developer Data Modeler 24.3.1 (již rozbalen), DBeaver Community 26.1.5 a MySQL Workbench 8.0.47. **Před pgModelerem rozhodnout přesnou verzi a edici:** Community není hotový Windows instalátor; aktuální produktové členění označuje reverse engineering jako funkci Plus, ale dostupnost je nutné ověřit přímo v použité sestavě. Plus vyžaduje licenci nebo zkušební klíč.
2. ✅ Připravit testovací DB cykloservisu: zadání, rozsah (10 entit), ER přehled a hotové DDL skripty pro PostgreSQL/MySQL/Oracle — `CYKLOSERVIS_ZADANI.md`. ✅ Lokální DB servery běží v Dockeru (`docker/`, viz Stav výše) — zbývá jen nahrát skripty a nainstalovat nástroje z bodu 1.

---

## 3. Testování 4 nástrojů na cykloservisu
**11. 8. – 16. 8. 2026**

Pro každý ze 4 nástrojů projít 4 kroky se stejným cílovým rozsahem:
1. Vytvořit strukturu cykloservisu podle textového zadání — u modelovacích nástrojů od prázdného modelu, u edice bez samostatného návrhu nejbližším podporovaným postupem na prázdném schématu; rozdíl výslovně zaznamenat.
2. Forward engineering nebo ekvivalentní export DDL — skript spustit na prázdné lokální DB a zapsat nutné opravy.
3. Reverse engineering — připojit k živé referenční DB a sestavit model nebo diagram; nedostupnost v přesné edici zaznamenat, nikoli nahrazovat jinou edicí bez uvedení změny.
4. Export do skutečně dostupných formátů; odlišit nativní PDF/PNG od tisku nebo převodu.

Výsledky zapsat do `nastroje/hodnoceni_NAZEV.md` (sekce K1–K8 + screenshoty). MySQL Workbench navíc: reverse engineering na firemním MySQL serveru.

---

## 🏖 Dovolená: 17. 8. – 21. 8. 2026

---

## 4. AHP výpočty — 2 scénáře + citlivost
**22. 8. – 26. 8. 2026**

1. Vyplnit AHP matice na základě výsledků testování nástrojů.
2. Scénář A (malá firma / cykloservis): vyšší váha K2 Použitelnost + K8 Náklady → výpočet → pořadí nástrojů.
3. Scénář B (střední firma / výrobní): vyšší váha K1 Funkcionalita + K3 Kompatibilita → výpočet → pořadí.
4. Analýza citlivosti: změnit 1 váhu → sledovat změnu pořadí alternativ.

---

## 5. Zadávací list STAG + příprava schůzky
**27. 8. – 31. 8. 2026**

1. Vyplnit zadávací list ve STAGu: anglický název práce + 4–5 zdrojů ISO 690:2022 (min. 2–3 knihy + 1 článek). Odeslat vedoucímu ke schválení.
2. Připravit podklady na schůzku s vedoucím (týden od 17. nebo 24. 8., FIM nebo Teams): shrnutí testování nástrojů (1 strana) + 3–5 otázek (rozsah testování v BP, počet scénářů, forma aplikace, anonymizace firemních dat).

---

## 6. AHP aplikace — programování
**1. 9. – 30. 9. 2026**

Naprogramovat podpůrnou AHP kalkulačku (Python nebo JS):
1. Vstup: Saatyho matice n×n.
2. Výpočet vah: geometrický průměr řádků → normalizace.
3. Výpočet CR → hlásit, zda CR < 0,1 (konzistence přijatelná).
4. Zobrazit výsledné pořadí alternativ.
5. Analýza citlivosti: posuvník váhy → přepočet pořadí v reálném čase.

---

## 7. Psaní BP
**říjen – podzim 2026**

Teorie ze SP + praktická část: testování nástrojů, AHP výpočty, 2 scénáře, aplikace. Cíl: min. 40 stran bez příloh.

---

## Milníky

| Termín | Úkol | Stav |
|---|---|---|
| 12. 7. 2026 | Odevzdat SP + test + email vedoucímu. | ✅ |
| 13. 7. 2026 | Zápočet MES zapsán vedoucím do STAGu. | ✅ |
| 31. 7. 2026 | AHP — šablony, výpočet, Excel. | 🟡 Zdroje, zadání a ruční kontrolní příklad hotové; praktický test webů a vlastní `AHP_vypocet.xlsx` čekají. |
| 10. 8. 2026 | Instalace nástrojů + testovací DB. | 🟡 Testovací DB (zadání, DDL, docker servery) hotová; instalace nástrojů a rozhodnutí o pgModeleru čekají. |
| 16. 8. 2026 | Testování 4 nástrojů na cykloservisu. | ⏳ |
| 17.–21. 8. 2026 | Dovolená. | — |
| 26. 8. 2026 | AHP výpočty — 2 scénáře + citlivost. | ⏳ |
| 31. 8. 2026 | Zadávací list STAG + příprava schůzky. | ⏳ |
| srpen 2026 | Schůzka s vedoucím (FIM nebo Teams). | ⏳ |
| 30. 9. 2026 | AHP aplikace — programování. | ⏳ |
| podzim 2026 | Psaní a odevzdání BP. | ⏳ |
