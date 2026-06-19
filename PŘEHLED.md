# Přehled stavu práce a složky

Aktualizace: 19. 6. 2026.

Tento dokument říká, co je kde uloženo a jak se s tím pracuje.

## 1. Pracovní režim (důležité)

Seminární práce se píše **po kapitolách** v souborech `Seminární práce <N>.md`. Tyto kapitolové soubory jsou **jediný zdroj pravdy**:

| Soubor | Obsah |
|---|---|
| `Seminární práce 0.md` | Titulní strana, prohlášení, poděkování, abstrakt CZ/EN, klíčová slova, pole obsahu (TOC). |
| `Seminární práce 1.md` | 1 Úvod |
| `Seminární práce 2.md` | 2 Cíl práce a výzkumné otázky |
| `Seminární práce 3.md` | 3 Metodika práce |
| `Seminární práce 4.md` | 4 Databázové systémy |
| `Seminární práce 5.md` | 5 Datové modely |
| `Seminární práce 6.md` | 6 Vícekriteriální rozhodování |
| `Seminární práce 7.md` | 7 Metoda AHP |
| `Seminární práce 8.md` | 8 Nástroje pro návrh a vývoj databází |
| `Seminární práce 9.md` | 9 Návrh hodnoticích kritérií |
| `Seminární práce 10.md` | 10 Závěry a doporučení |
| `Seminární práce 11.md` | Seznam zdrojů |
| `Seminární práce 12.md`, `13.md` | **NEPOUŽÍVAT** – prázdné rezervy, do dokumentu nepatří. |

Kapitoly jdou číselně po sobě (0–11), bez děr. Žádné jiné soubory s textem práce se needitují.

**Generované soubory (needitovat ručně, jen se přegenerují):**

- `Seminární práce.md` – vznikne spojením kapitol 0–11.
- `Seminární práce.docx` – Word výstup pro odevzdání (z `Seminární práce.md`).
- `Seminární práce - pro vedoucího.md` / `.DOCX` – starší generované verze, ignorovat.

## 2. Jak vyrobit finální dokument

Ze složky práce stačí jedno z:

- `python sestavit_seminarni_praci.py` – spojí 0–11 do `Seminární práce.md` a po cestě odstraní případné NUL byty z Google Disku.
- `.\spoj.ps1` – totéž v PowerShellu (výchozí rozsah 0–11).
- `.\spojit.ps1` – automaticky najde kapitoly a sám přeskočí rezervy 12 a 13.

Pak se `Seminární práce.md` převede do `.docx`, ve Wordu se aktualizuje pole obsahu (F9), doplní datum v prohlášení a soubor se odešle vedoucímu.

> Pozn.: Google Disk při živém synchronizování občas dočasně „usekne" soubor nebo do něj vloží NUL byty. Skript `sestavit_seminarni_praci.py` to ošetřuje. Po spojení vždy zkontroluj, že dokument končí seznamem zdrojů a že kapitola 9 obsahuje kritérium K8.

## 3. Stav obsahu (k 16. 6. 2026)

Seminární práce je obsahově **kompletní jako první verze**:

- struktura odpovídá šabloně MES (Oliva): abstrakt + klíčová slova, úvod, cíl a výzkumné otázky, metodika, teoretická východiska, závěry a doporučení, seznam zdrojů;
- praktická část a diskuse výsledků se zde vynechávají – jde o rešerši, výsledky patří až do bakalářské práce (vedoucí to v e-mailu výslovně připustil);
- 14 citovaných zdrojů, in-text autor–rok, seznam podle ČSN ISO 690:2022, rozdělený na tištěné a internetové zdroje; všechny citace párují se seznamem;
- jazyk projitý, sjednocená typografie (česká pomlčka), bez šablonovitých výčtů.

Zbývá (po e-mailu vedoucího 17. 6. 2026):

- **Smazat z metodiky** větu o citacích (vedoucí výslovně požadoval).
- **Doplnit zdroje:** ideálně 4–5 zdrojů na každou teoretickou kapitolu; priorita: sehnat DB knihy ze `ZDROJE.md` §5A (Connolly, Elmasri, Garcia-Molina, Korth).
- **Dohledat 2–3 MCDM survey články** pro zdůvodnění volby AHP v metodice (Google Scholar: „A survey on multi criteria decision making methods").
- **Vložit práci do šablony z Olivy** — vedoucí chce příště dostat práci v officiálním Word dokumentu šablony, ne holý konvertovaný .docx.
- Po vložení do šablony ověřit rozsah (min. 10 stran teorie) a odeslat vedoucímu.
- Po připomínkách odevzdat v Olivě a splnit zápočtový test.

## 4. Složky

| Složka | Obsah | Doporučení |
|---|---|---|
| `zadani/` | Oficiální zadání a údaje VŠKP ze STAGu. | Ponechat. |
| `oliva/` | Pokyny, šablony, lekce a vzory pro MES. | Ponechat do odevzdání. |
| `literatura/DB/` | Databázová literatura, dokumentace a URL zdroje. | Ponechat, bude potřeba i pro BP. |
| `literatura/AHP/` | Zdroje k AHP a vícekriteriálním metodám. | Ponechat, bude potřeba i pro BP. |
| `vzory_praci/` | Vzorové BP/DP k AHP a databázím. | Ponechat jako inspirace. |
| `nastroje/` | Instalátory porovnávaných nástrojů. | Ponechat pro praktickou část BP. |
| `prezentace UHK/` | Slidy k databázovým předmětům. | Podpůrný materiál. |
| `smazat/` | Duplicity a slabé materiály. | Zkontrolovat a smazat později. |

## 5. Návaznost na bakalářskou práci

Seminární práce je teoretický a metodický základ. Pro BP se založí nový dokument (až podle schváleného zadávacího listu ve STAGu) a doplní se praktická část: instalace a testování čtyř nástrojů, jednotný testovací scénář, Saatyho matice kritérií i alternativ, výpočet vah a konzistence (CR), analýza citlivosti, doporučení pro praxi a rozšíření literatury.
