# Přehled stavu práce a složky

Aktualizace: 14. 6. 2026.

Tento dokument říká, co je kde uloženo a co s tím dál. Staré pracovní soubory `Bakalářská práce.docx`, `Bakalářská práce.md` a `Seminární práce.txt` byly odstraněny.

## 1. Aktuální stav

Hlavní dokument je:

- `Seminární práce.docx` — **hlavní (single source of truth)**. Od 14. 6. 2026 se všechny úpravy dělají přímo zde. Obsahuje poslední 4 citační opravy.
- `Seminární práce.md` — **archiv**. Obsahově shodný k 14. 6. 2026, dál se do něj nepíše.

> **Pracovní režim:** Romi edituje ručně přímo v docx ve Wordu (lze zapnout Revize → Sledovat změny). Claude na vyžádání edituje rovněž přímo docx a po úpravě kontroluje shodu citací text↔seznam. Markdown už neudržujeme.

Seminární práce je obsahově kompletní jako první verze. Obsahuje titulní část, prohlášení, poděkování, abstrakt CZ/EN, úvod, cíl, výzkumné otázky, metodiku, teoretická východiska, AHP, návrh nástrojů a kritérií, metodický rámec navazující komparace, diskusi, závěr a seznam zdrojů.

Zbývá hlavně:

- vizuální kontrola `Seminární práce.docx` ve Wordu,
- aktualizace obsahu přes F9,
- korektura pravopisu a stylu,
- kontrola citací a seznamu zdrojů,
- odeslání vedoucímu,
- následné odevzdání v Olivě.

## 2. Kořen složky

| Soubor | Stav | Účel |
|---|---|---|
| `Seminární práce.docx` | ponechat | Aktuální Word výstup pro kontrolu a odevzdání. |
| `Seminární práce.md` | ponechat | Hlavní editovatelný zdroj seminární práce. |
| `PŘEHLED.md` | ponechat | Tento rozcestník a stav projektu. |
| `PLAN.md` | ponechat | Aktuální plán práce. |
| `ZDROJE.md` | ponechat | Přehled literatury, zdrojů a citačních poznámek. |
| `CLAUDE.md` | volitelné | Kontext pro Claude/AI asistenty. Lze ponechat nebo později archivovat. |
| `GEMINI.md` | volitelné | Kontext pro Gemini/AI asistenty. Lze ponechat nebo později archivovat. |
| `Email konverzace.txt` | ponechat | Požadavky a termíny od vedoucího. |

## 3. Složky

| Složka | Obsah | Doporučení |
|---|---|---|
| `zadani/` | Oficiální zadání a údaje VŠKP ze STAGu. | Ponechat. |
| `oliva/` | Pokyny, šablony, lekce a vzory pro MES. | Ponechat do odevzdání seminární práce. |
| `literatura/DB/` | Databázová literatura, dokumentace a URL zdroje. | Ponechat, bude potřeba i pro BP. |
| `literatura/AHP/` | Zdroje k AHP a vícekriteriálním metodám. | Ponechat, bude potřeba i pro BP. |
| `vzory_praci/` | Vzorové BP/DP k AHP a databázím. | Ponechat jako inspiraci a zdroje. |
| `nastroje/` | Instalátory MySQL Workbench, DBeaver a Oracle Data Modeler. | Ponechat pro praktickou část BP. |
| `prezentace/` | Slidy k databázovým předmětům. | Ponechat jako podpůrný materiál. |
| `na smazání/` | Jeden pomocný soubor k ruční kontrole. | Zkontrolovat a případně smazat později. |
| `.claude/` | Pomocná data nástrojů. | Neřešit, pokud nepřekáží. |

## 4. Co bylo při tvorbě seminární práce použito

### Zadání a pokyny

- `zadani/vskp_-_zadani_vskp.pdf` - oficiální zadání BP.
- `zadani/vskp_-_udaje_o_vskp.pdf` - údaje o VŠKP.
- `Email konverzace.txt` - požadavky vedoucího.
- `oliva/pokyny/` - pravidla MES a metodické pokyny FIM UHK.
- `oliva/sablony/` - šablony pro Word dokument.

### Hlavní odborné zdroje

- `literatura/DB/Pokorny_Valenta_Databazove_systemy_2020.pdf`
- `literatura/AHP/Saaty_1990_How_to_make_a_decision_AHP.pdf`
- `literatura/AHP/Saaty_2008_Decision_making_with_AHP.pdf`
- `literatura/AHP/Vicekriterialni_metody_hodnoceni_2.pdf`
- `vzory_praci/AHP/Jandova_AHP_jeji_silne_a_slabe_stranky.pdf`
- `vzory_praci/AHP/Vohradsky_Pouziti_metod_vicekriterialniho_rozhodovani_pri_rizeni_podniku.pdf`
- `vzory_praci/DB/Kaspar_bc_final.pdf`
- `vzory_praci/DB/zaverecna_prace.pdf`
- `vzory_praci/DB/JED0050_FEI_N2647_2612T025_2024.pdf`
- dokumentace nástrojů v `literatura/DB/*.url`

Podrobnější rozpis je v `ZDROJE.md`.

## 5. Otevřené body před odevzdáním MES

Hotovo k 14. 6. 2026 (úpravy provedeny v `Seminární práce.md`, **NE** v docx):

- ✅ Shoda citací text ↔ seznam zkontrolována (19 zdrojů, vše páruje).
- ✅ Doplněn chybějící zdroj Carvalho et al. (2022) do seznamu.
- ✅ Vyřešen PostgreSQL: doplněna in-text citace (kap. 8.4) a sjednocen autor.
- ✅ Doplněn podpůrný zdroj Simanavičienė a Vdovinskienė (2023) k AHP výběru SW.
- ✅ Citace metodických pokynů FIM UHK je v seznamu i v textu (kap. 3).

Priorita 1 — zbývá:

- Zkontrolovat deklaraci AI podle skutečně použitých nástrojů (kap. 3 uvádí ChatGPT a Claude).
- Udělat jazykovou korekturu.
- Zvážit abecední řazení seznamu zdrojů, příp. rozdělení na tištěné/internetové dle šablony.

Priorita 2 — až při tvorbě nového docx:

- Z `Seminární práce.md` znovu vygenerovat docx (současný docx zatím beze změn!).
- Aktualizovat obsah ve Wordu (F9).
- Zkontrolovat stránkování a formát podle pokynů FIM.
- Doplnit datum v prohlášení.
- Odeslat první verzi vedoucímu.

Priorita 3:

- Po připomínkách vedoucího vytvořit finální verzi.
- Odevzdat v Olivě.
- Splnit zápočtový test.

## 6. Návaznost na bakalářskou práci

Seminární práce je teoretický a metodický základ. Pro bakalářskou práci bude potřeba doplnit hlavně praktickou část:

1. Instalace a testování čtyř nástrojů.
2. Jednotný testovací scénář.
3. Saatyho matice pro kritéria a alternativy.
4. Výpočet vah, priorit a konzistence.
5. Analýza citlivosti.
6. Praktická doporučení.
7. Rozšíření literatury a teorie.

## 7. Návrh na další úklid

- `CLAUDE.md` a `GEMINI.md` jsou jen pomocné kontexty pro AI. Pokud je nebudeš používat, lze je přesunout do archivu nebo smazat.
- `na smazání/` zkontrolovat ručně a po potvrzení odstranit.
- Po odevzdání MES vytvořit archivní složku pro finální odevzdanou verzi.
- Pro bakalářku založit nový dokument až podle schváleného zadávacího listu ve STAGu.
