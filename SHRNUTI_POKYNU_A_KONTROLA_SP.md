# Shrnutí pokynů a kontrola seminární práce

Ověřeno: 8. 7. 2026 (přímým čtením zdrojových souborů, ne z paměti).

## Použité podklady

- `oliva/vzory/` — 6 ukázkových seminárních prací (PDF), různé roky a obory (cestovní ruch, ekologie). Slouží jen jako orientační příklad formátu, ne jako závazný vzor — praxe se mezi nimi liší (viz níže u seznamu zdrojů).
- `oliva/sablony/` — 3 soubory, ale reálně **2 různé šablony**:
  - `Sablona pro tvorbu SP.docx` a `Sablona SP.docx` jsou byte-identické (stejný MD5 součet) — jde o **jednu a tutéž šablonu pro seminární práci**.
  - `šablona( nová (1).docx` je šablona pro **bakalářskou/diplomovou práci** (struktura Abstrakt/Abstract, Cíl a metodika práce, Shrnutí a diskuse výsledků atd. — přesně odpovídá struktuře z Metodických pokynů níže). Pro seminární práci se nepoužívá.
  - → Otevřená otázka z `PLAN.md` ("která šablona je správná pro MES") je tímto vyřešena: pro SP je správná `Sablona SP.docx`.
- `oliva/pokyny/Metodické pokyny pro vypracování bakalářských a diplomových prací (1).pdf` — použita verze s `(1)` (12 stran, výnos děkanky FIM č. 9/2025, platnost od 1. 9. 2025). Jde o obecný fakultní předpis pro BP/DP, na seminární práci se vztahuje jen rámcově/analogicky.
- `oliva/pokyny/Seminární práce - pojyny pro absolvovnání předmětu.pdf` — přímé pokyny ke KRCR-MES.
- `POZADAVKY_UCITELE.md`, `Email konverzace.md` — konkrétní požadavky vedoucího práce (nadřazené obecným pokynům, pokud si odporují).

## Požadovaná struktura seminární práce

Podle šablony `Sablona SP.docx`: titulní strana (bez zvláštního vzoru — jen název, forma studia, obor, ročník, vedoucí, datum, autor), anotace + klíčová slova, obsah, úvod (důvod výběru tématu, cíl), teoretická východiska, metodický postup, vlastní část, závěr, seznam zdrojů, přílohy.

Podle konkrétních pokynů vedoucího práce (Ing. et Ing. Martina Lněničky, viz `POZADAVKY_UCITELE.md`) se pro tuto seminární práci **vynechávají prvky bakalářské práce** (prohlášení, poděkování, anglický abstrakt) a **vynechává se praktická část** (empirické šetření, hypotézy, Saatyho matice, výpočty) — ta patří až do navazující bakalářské práce. Místo hypotéz se používají cíl práce + výzkumné otázky. To je záměrná a odsouhlasená odchylka od obecné šablony, ne chyba.

## Formát — ověřeno přímo v šabloně `Sablona SP.docx`

- Stránka: A4 (21 × 29,7 cm).
- Okraje: 2,5 cm ze všech stran (šablona SP je nemá asymetrické — asymetrické okraje 3,5/2 cm jsou jen v Metodických pokynech pro tištěnou/vázanou BP/DP, na SP se nevztahují).
- Písmo běžného textu: šablona SP používá Times New Roman 12. Obecné Metodické pokyny FIM ale výslovně povolují **Cambria nebo Times New Roman**, velikost 12 — Cambria tedy není chyba.
- Nadpisy: šablona SP má Nadpis 1 = 14 pt tučně, Nadpis 2 = 13 pt tučně (bez explicitně nastaveného písma, tedy dědí základní patkové písmo). Bezpatkové písmo (Verdana/Arial) pro nadpisy je podle obecných pokynů jen volitelné ("může být použito"), ne povinné.
- Řádkování 1,5, zarovnání do bloku, odsazení prvního řádku odstavce — potvrzeno v šabloně i v aktuální práci.
- Číslování stran: dole uprostřed. Kapitola "Úvod" musí začínat na straně 1 (výslovný požadavek Metodických pokynů, bod ad 5). Strany před Úvodem (titulka, anotace, obsah) se číslovat nemusí.
- Nadpisy číslované, max. 3 úrovně — potvrzeno.
- Seznam zdrojů — v reálné praxi se liší i mezi ukázkovými pracemi: šablona SP i jedna ukázka (Červenková) dělí zdroje na "Tištěné"/"Internetové", jiná ukázka (Havlínová) má jeden abecední seznam. Novější fakultní Metodické pokyny (2025) explicitně žádají seznam **bez třídění podle typu zdrojů**. Ponecháno jako jeden abecední seznam — odpovídá novějšímu a obecně závaznějšímu předpisu i části reálné praxe.

## Kontrola `Seminární práce.DOCX` — stav k 8. 7. 2026

### V pořádku (ověřeno)

- Formát stránky A4, okraje 2,5 cm ze všech stran — odpovídá šabloně SP.
- Písmo Cambria 12, řádkování 1,5, zarovnání do bloku — v souladu s obecnými pokyny (Cambria je povolená varianta).
- Nadpisy 14/13 pt tučně, číslované, max. 3 úrovně (např. 5.1.1) — odpovídá šabloně SP.
- Obsah je skutečné pole TOC (ne statický text), nadpisy jsou opravdové styly.
- Vlastní tabulkové objekty pro Tabulku 1 (nástroje) a Tabulku 2 (kritéria), s popiskem nad tabulkou a uvedeným zdrojem — odpovídá konvenci.
- Titulní strana neobsahuje prohlášení, poděkování ani anglický abstrakt — v souladu se specifickým pokynem vedoucího práce pro tuto seminárku.
- Seznam zdrojů: jeden abecední seznam, 26 položek, autor–rok styl citací v textu — odpovídá novějším fakultním pokynům.
- Rozsah: cca 50 900 znaků vč. mezer ≈ 28 normostran vlastního textu (bez titulky/anotace/obsahu) — splňuje požadavek min. 10 stran teorie i orientační rozsah cca 27 normostran zmíněný vedoucím.

### Nalezené a opravené chyby

- **Číslování stran nebylo restartováno na kapitole Úvod.** Dokument čísloval strany souvisle od titulní strany, takže Úvod vycházel na stranu 5 místo na stranu 1, což je v přímém rozporu s bodem ad 5 Metodických pokynů ("kapitola Úvod začíná na straně 1"). Opraveno vložením `w:pgNumType w:start="1"` do sekce, která začíná Úvodem.
- **Sekce s Úvodem měla zapnuté "jiné záhlaví/zápatí pro první stránku" (titlePg).** I po restartu čísel se proto na stránce s Úvodem (logická strana 1) nezobrazovalo žádné číslo — číslo se poprvé objevilo až na druhé straně sekce, popsané jako "2". Opraveno vypnutím `different_first_page_header_footer` u této sekce, takže se stejné zápatí s polem `PAGE` použije i na první straně. Ověřeno převodem do PDF (LibreOffice): fyzická strana s Úvodem má v zápatí "1", další strany navazují 2, 3, …
- **Prázdné vlastní XML metadata (`customXml/item1.xml`)** — nevyužitý datastore pro Wordovu funkci Citace a bibliografie (styl APA, bez záznamů), pozůstatek ze šablony/pandoc generování. Neobsahoval žádný text práce ani skutečná metadata. Odstraněn i s příslušnou relací v `word/_rels/document.xml.rels`, aby to Word při kontrole dokumentu už nehlásil.

Zálohovaná verze před těmito opravami: `Seminární práce.záloha před opravou stránkování 2026-07-08.DOCX`.

### Zbývá udělat ručně ve Wordu před odevzdáním

- **Aktualizovat pole Obsahu** (klik pravým tlačítkem do obsahu → Aktualizovat pole → Aktualizovat celou tabulku), protože se čísla stran v Obsahu posunula o 4 strany zpět (staré hodnoty typu "Úvod…5" se po opravě mají zobrazit jako "Úvod…1"). Bez otevření ve Wordu to nejde spolehlivě přepočítat automaticky.
- Po aktualizaci Obsahu ještě jednou vizuálně projít zalomení stran a případné osiřelé nadpisy na konci stránky.
- Doplnit datum do prohlášení/titulní strany, pokud tam zůstalo placeholder.

## Předchozí zjištění (z dřívější kontroly, potvrzeno jako již opravené)

- Formát Letter → A4: opraveno.
- Statický obsah se špatným stránkováním, titulka/prohlášení/poděkování jako kapitoly v obsahu: opraveno.
- Ruční seznamy s pomlčkami místo skutečných seznamů: opraveno.
- Chybějící tabulkové objekty: doplněny.
