# Přehled stavu práce a složky

Aktualizace: 6. 7. 2026.

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

## 2. Jak vyrobit finální dokument

Kapitoly 4–7 mají dvě vrstvy:
- `Seminární práce 4.md` – `7.md` — zdrojové soubory s textem **a** citačními bloky (řádky začínající `>`). Citační bloky jsou viditelné v Obsidianu a slouží jako reference při psaní, ale do exportu se nezahrnují.
- `Seminární práce 4x.md` – `7x.md` — čisté exportní verze bez citačních bloků, generované skriptem `extrahuj.ps1`.
- `Seminární práce 4z.md` – `7z.md` — záložní kopie zdrojových souborů (záloha struktury pro případ potřeby).

Postup sestavení:

```powershell
.\extrahuj.ps1                          # vygeneruje 4x–7x z 4–7 (odstraní řádky začínající ">")
.\spoj.ps1 0 1 2 3 4x 5x 6x 7x 8 9 10 11 -Out "Seminární práce.md"
pandoc "Seminární práce.md" -o "Seminární práce.docx" --reference-doc="oliva/sablony/sablona_MES.docx"
```

Ve Wordu pak aktualizovat pole obsahu (F9), doplnit datum v prohlášení a odeslat vedoucímu.

> Pozn.: Google Disk při živém synchronizování občas dočasně „usekne" soubor nebo do něj vloží NUL byty. Skript `sestavit_seminarni_praci.py` to ošetřuje. Po spojení vždy zkontroluj, že dokument končí seznamem zdrojů a že kapitola 9 obsahuje kritérium K8.

## 3. Stav obsahu (k 6. 7. 2026)

Seminární práce je obsahově **kompletní a připravená na finální sloučení a formátování**:

- **Struktura** odpovídá šabloně MES: obsahuje abstrakt, klíčová slova, úvod, cíl, metodiku, teoretickou rešerši (databáze, modely, rozhodování, AHP), charakteristiku 4 nástrojů, návrh 8 hodnoticích kritérií a metodický rámec pro navazující komparaci.
- **Teoretická i metodická část** je dostatečně hluboká a splňuje požadavky na rozsah (min. 10 normostran teorie).
- **Zdroje:** Celkem 23 unikátních zdrojů, in-text citace jsou spárované se seznamem. Na každou teoretickou kapitolu připadá požadovaných 4–5 odborných zdrojů.
- **Opravy:** Byly odstraněny téměř všechny dříve zjištěné gramatické a stylistické chyby (včetně nesouladů rodů v kap. 10 a chyb v citacích u Cataka).

Zbývá (finální kroky):

- **Opravit nově vzniklé chyby a překlepy** z nedávných úprav (překlepy v kap. 0 a 2, gramatické chyby v kap. 3 a zmatený text `Tento datábázový systém který usnadňuje...` v kap. 4).
- **Dočistit Kapitolu 11 (Seznam zdrojů):** Odstranit pomocné indexy `[101]`, `[102]` u zdrojů Catak a Ebrahimi a seřadit je správně abecedně.
- **Převést spojený dokument do oficiální Word šablony** a provést závěrečnou vizuální kontrolu.

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

## 5. Návaznost na bakalářskou práci

Seminární práce tvoří ucelený teoretický a metodický základ. Pro praktickou část bakalářské práce (BP) bude následovat:
1. Instalace a testování 4 nástrojů nad navrženým testovacím scénářem (tvorba modelu, generování SQL schématu, reverzní inženýrství).
2. Matematické vyhodnocení pomocí metody AHP (sestavení Saatyho matic, výpočet vah kritérií i variant, ověření poměru konzistence CR < 0,1).
3. Provedení analýzy citlivosti vah kritérií a modelování různých scénářů (např. s ohledem na omezený rozpočet nebo specifické technologické nároky).
4. Rozšíření seznamu literatury na minimálně 30 odborných zdrojů.
