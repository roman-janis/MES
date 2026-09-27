# Bakalářská práce – hlavní návod k úpravám, sestavení a pokračování

Aktualizace: 27. 9. 2026. Autor práce: Roman Janiš. Tento dokument je hlavní provozní návod pro autora i další relaci asistenta. Obsahuje stav, vysvětlení postupu, vazby souborů, příkazy, kontroly a postup při změnách. Starší `STAV_ROZPRACOVANI.md` je stručný historický záznam předání; pro postup práce začínej zde.

**Nejdůležitější pravidlo:** `bakalarsa_prace.md` je výstup generátoru. Pokud do něj něco napíšeš ručně a potom spustíš generátor, ruční změna se přepíše. Trvalou změnu je potřeba zanést i do příslušného zdroje uvedeného níže. Před každou regenerací vytvoř kopii celého pracovního balíku.

Tento MD sjednocuje návod, není náhradou zdrojových souborů, aplikace, knihoven ani literatury. Pro obnovu na jiném počítači je nutné uchovat také soubory ze seznamu zálohy v oddílu 4. U závislostí na dočasném prostředí jsou níže výslovně uvedeny limity obnovy.

## 1. Co je hotové a co není

Existuje souvislá pracovní práce `bakalarsa_prace.md`, aplikace v PHP, kontrolní sešit, sešit syntetického hodnocení, vstupní matice, referenční výpočty, tři citlivosti a protokoly. Předchozí sestavení uvádí přibližně 96 tisíc znaků těla bez srovnávacích poznámek, 30 bibliografických položek a 12 tabulek. Počet zdrojů sám o sobě nedokazuje jejich správné využití v textu.

Původní BP 0–10 a původní hodnoticí sešit nebyly oproti uloženým vstupním otiskům změněny. Text BP 4–6 je ve výsledné práci převzat doslova. Změny dalších převzatých pasáží jsou označeny původním zněním v hranatých závorkách; eviduje je také `pracovni_bp/zmeny_prevzateho_textu.json`.

Výsledky komparace jsou **syntetické**: 51 testových bloků × 4 nástroje = 204 náhodných pomocných známek. Skutečné testy produktů nebyly touto přípravou provedeny. Saatyho matice byly vytvořeny samostatně; nejsou přepočtem pomocných známek 1–5. Nebyly vymyšleny skutečné verze, ceny, naměřené časy ani důkazy.

Provedené technické ověření 27. 9. 2026:

| Kontrola | Doložený výsledek |
|---|---|
| PHP výpočty | 146 kontrol PASS, největší odchylka 1,78 × 10⁻¹⁵ |
| HTTP formuláře | 14 kontrol PASS |
| Kontrolní XLSX | 10 listů, 120 vzorců; 7 hlavních uložených výsledků odpovídá referenci |
| Syntetické XLSX | 13 listů, 354 vzorců; 17 hlavních uložených výsledků včetně citlivostí odpovídá referenci |
| Integrita XLSX | ZIP bez chyby; žádné uložené buňky typu error; opakované kontroly s odstupem |
| Původní BP a původní XLSX | 12 kontrolních otisků shodných |
| Prohlížeč | Dochovaný záznam PASS, 76 dvojic, bez chyb stránky; snímky v outputs |
| Opakovatelnost generování | V oddělené kopii nově spuštěn `generate_data.py` a `build_thesis.py`; výsledný text, demo, kontrolní data, reference i syntetický protokol obsahově shodné po normalizaci konců řádků |

Poslední zkouška nepřepsala hlavní práci. Neověřovala nové sestavení XLSX od nuly. Navazující kontrola XLSX četla uložené výsledky, nebyla osobním přepočtem autora v Excelu. Podrobnosti a důkazy: `vypocty/PROTOKOL_KONTROLNI_VYPOCET.md` a `outputs/bp_20260927/overeni/`.

Před odevzdáním zbývá: autorská revize, skutečné testy, zdůvodnění skutečných párů, přepočet a nová interpretace, osobní nezávislá kontrola, srovnání s dalším AHP nástrojem, závěr podle výsledků a formální DOCX. Veřejné nasazení ani kontrola vedoucím nejsou doloženy.

## 2. Z čeho se vycházelo a proč

1. Teoretický základ: schválená seminární práce a její kapitoly BP 0–10. Zachovává se tvoje formulace; nejde o plošné stylistické přepisování.
2. Zadání: aktuálnější e-mail vedoucího z 15. 9. v `EMAIL_KONVERZACE.md`. Cílem je aplikace podporující výběr nástroje pomocí AHP, ověření implementace a demonstrace na příkladu. `PLAN.md`, `CIL_BP.md` a `EMAIL.md` ze 13. 9. zachycují starší stav; tvrzení, že se teprve čeká na odpověď, již není aktuální. Stav schválení ve STAGu je nutné ověřit zvlášť.
3. Rozsah: čtyři nástroje, K1–K8, jeden Cykloservis, autor jako jediný hodnotitel, tři oddělené citlivosti. Bez účtů, administrace, další rozhodovací metody nebo skupinového AHP.
4. Nejprve byl specifikován výpočet a kontrolní příklad, potom vytvořena aplikace a kontrolní tabulky. Databázové testy nenahrazuje ověření programu.
5. Pro demonstraci byla vytvořena reprodukovatelná náhodná data, vypočteny priority a napsána praktická část. Označení syntetického původu zůstává všude, dokud nejsou data skutečně nahrazena.
6. Následovala kontrola aplikace, sešitů a zachování textů. Při navázání byly doplněny chybějící obrázky a kontrolní protokol, které původně zůstaly mimo projekt.

Model v aktuálním testovacím sešitu obsahuje 11 tabulek včetně elektrokola. Starší plán uvádí deset entit jádra. Při skutečných testech používej jednotné konkrétní zadání a ověř tuto návaznost, nepřepisuj počty naslepo podle staršího plánu.

## 3. Mapa souborů: co je zdroj a co výstup

| Soubor nebo složka | Úloha / způsob úpravy |
|---|---|
| `bakalarsa_prace.md` | Výsledná práce ke čtení; přegenerování ji přepíše |
| `BP 0.md`–`BP 10.md` | Zachované původní podklady; neupravovat bez vědomého rozhodnutí a uchování originálu |
| `seminární práce/` | Původní schválená práce, pouze ke čtení |
| `pracovni_bp/text_prakticka_cast.md` | Editovatelný zdroj kapitol 9–14; obsahuje značky `{{...}}` pro tabulky a komentáře |
| `pracovni_bp/build_thesis.py` | Sestavení textu, úvodních částí, změn BP 1–3 a 7–8, bibliografie a příloh; část textu je přímo uvnitř skriptu |
| `pracovni_bp/generate_data.py` | Generátor DEMO dat a referenční výpočet; spuštění přepíše demo, kontrolu, připravené seznamy a reference |
| `pracovni_bp/test_blocks.json` | Extrahované zadání 51 úloh; uchovat jako vstup generátoru |
| `pracovni_bp/build_workbooks.mjs` | Generátor obou XLSX, náhledů a kontrolních JSON; vyžaduje Artifact Tool |
| `pracovni_bp/visual_check.mjs` | Automatické ověření webu a snímky; potřebuje běžící HTTP server, Playwright a Chrome |
| `pracovni_bp/verify_handoff.py` | Čtecí kontrola předání bez přepisování souborů; Python bez dalších knihoven |
| `pracovni_bp/audit.py` | Jednorázová extrakce podkladů; zapisuje i původní otisky! Nespouštět jako běžnou kontrolu |
| `pracovni_bp/original_hashes.json` | Neměnná vstupní kontrola BP a původního XLSX; nepřepisovat pro zamaskování rozdílu |
| `pracovni_bp/bibliografie.json`, `thesis_stats.json`, `zmeny_prevzateho_textu.json` | Generované přehledy, ne hlavní místo editace |
| `ZDROJE.md` + `BP 10.md` | Bibliografické podklady; generátor používá i opravené citace v oddílu 5 ZDROJE |
| `app/src/AhpCalculator.php` | AHP matematika |
| `app/src/Evaluation.php` | Validace vstupního dokumentu a párů |
| `app/public/index.php` | Webové formuláře a výsledky |
| `app/public/assets/style.css` | Vzhled webu |
| `app/data/seed_criteria.json`, `seed_alternatives.json` | Nabídka připravených položek; změna nabídky nezmění automaticky již uložené demo |
| `app/data/demo.json`, `control.json` | Úplné vstupní modely pro demo a kontrolu |
| `vypocty/demo_reference.json`, `control_reference.json` | Nezávislé referenční výpočty; změna vstupů vyžaduje obnovit reference |
| `vypocty/synteticke_testy.json` | Náhodné pomocné známky a úlohy pro protokol a XLSX |
| `vypocty/kontrolni_priklad.xlsx` | Kontrolní model 3 × 3; vzorce i archivní etalon |
| `outputs/bp_20260927/hodnoceni_synteticke.xlsx` | Syntetické hodnocení; žluté vstupy, výsledky a citlivosti |
| `hodnoceni_4_nastroju.xlsx` | Původní pracovní sešit; generátory syntetické verze jej nenahrazují |
| `protokoly/` | Generované syntetické protokoly a vymezení kritérií; skutečné důkazy ukládat odděleně |
| `outputs/bp_20260927/overeni/` | Uchované výsledky kontrol; starý PASS není důkaz nové verze |

Tok dat:

```text
test_blocks.json + generate_data.py → demo/control/seed JSON + reference + syntetické známky
demo/control JSON + reference + známky → build_workbooks.mjs → XLSX + kontroly + náhledy
BP + e-mail + ZDROJE + praktický text + JSON/reference → build_thesis.py → bakalarsa_prace.md
demo/control JSON → PHP aplikace → výsledky + export JSON + snímky
```

Aplikace se generátorem textu nevytváří. Její zdrojové PHP soubory je nutné uchovat. Totéž platí pro literaturu a původní seminární práci. `spoj.ps1` vytváří starší `BP.md`, nikoliv tuto práci; pro tento balík jej nepoužívej jako náhradu `build_thesis.py`.

## 4. Záloha před úpravou a bezpečná pracovní kopie

Příkazy jsou pro PowerShell spuštěný v kořeni projektu. Ověř ho:

```powershell
Get-Location
Test-Path -LiteralPath '.\bakalarsa_prace.md'
```

Následující příkazy založí novou oddělenou kopii; nepřepisují předchozí zálohu:

```powershell
$bpRoot = (Get-Location).Path
$bpCopy = Join-Path $env:LOCALAPPDATA ('MES_BP_zalohy\' + (Get-Date -Format 'yyyyMMdd_HHmmss_fff'))
New-Item -ItemType Directory -Path $bpCopy -ErrorAction Stop | Out-Null
$bpItems = @('app','pracovni_bp','vypocty','protokoly','outputs',
  'bakalarsa_prace.md','NAVOD_K_PRACI_A_OPAKOVANI.md','STAV_ROZPRACOVANI.md',
  'EMAIL_KONVERZACE.md','ZDROJE.md','PLAN.md','CIL_BP.md','EMAIL.md',
  'AHP_NAVOD_SAATY.md','CYKLOSERVIS_ZADANI.md','hodnoceni_4_nastroju.xlsx')
foreach ($item in $bpItems) {
  Copy-Item -LiteralPath (Join-Path $bpRoot $item) -Destination $bpCopy -Recurse -ErrorAction Stop
}
Get-ChildItem -LiteralPath $bpRoot -Filter 'BP *.md' -File |
  Copy-Item -Destination $bpCopy -ErrorAction Stop
Write-Host "Kopie: $bpCopy"
```

Pro úplný dlouhodobý archiv uchovat navíc `seminární práce/`, `literatura/`, `oliva/`, `zadani/`, `z emailu/`, použité DDL a Docker konfiguraci. Přístupové údaje z `docker/.env` patří do soukromé zálohy, nikoliv do veřejného repozitáře. Návrat ze zálohy dělej do nové složky, ne automatickým přepsáním rozpracované práce.

První pokus o sestavení prováděj v `$bpCopy`. Absolutní adresář uvnitř skriptů se odvozuje od jejich umístění, takže kopie musí zachovat strukturu složek. Záloha na stejném disku chrání proti přepsání, nikoliv proti ztrátě disku; pro archiv uchovat také druhou kopii. TEMP není dlouhodobá záloha.

## 5. Prostředí a závislosti

Ověřeno na tomto počítači: Python 3.14.7, Node.js 24.19.0, přenosné PHP 8.5.11. PHP aplikace požaduje 8.2+. Výchozí příkaz `php` zde může ukazovat na PHP 7.0.

```powershell
python --version
node --version
$phpBp = Join-Path $env:TEMP 'mes-bp-20260927\php\php.exe'
if (-not (Test-Path -LiteralPath $phpBp)) { throw 'Vyber existující PHP 8.2+ a uprav $phpBp.' }
& $phpBp -v
```

Python generátory dat/textu a čtecí kontrola používají standardní knihovnu. `audit.py` navíc potřebuje `pypdf` a `openpyxl`, ale pro běžnou reprodukci s uloženým `test_blocks.json` jej není potřeba spouštět. Tyto balíčky nebyly při navazující kontrole dostupné ve výchozím Pythonu.

Export XLSX používá **`@oai/artifact-tool` 2.8.59**, jehož místní package.json označuje balík jako `private`. Nevycházej z předpokladu, že půjde stáhnout běžným `npm install`. Funkční kopie je nyní v `%TEMP%\mes-bp-20260927\node_modules`. V téže složce je Playwright 1.62.1; vizuální skript používá nainstalovaný Google Chrome. LibreOffice je na `C:\Program Files\LibreOffice\program\soffice.exe`.

Pro zachování nynějšího funkčního prostředí lze zkopírovat celé `php/` a celé `node_modules/` ze složky `%TEMP%\mes-bp-20260927` do soukromého trvalého adresáře, například `%LOCALAPPDATA%\MES_BP_runtime`. Předem ověř volné místo. Jde o lokální zálohu existujících závislostí, ne o jejich zveřejnění nebo přenos na jiný operační systém. Po změně cesty uprav proměnné níže. Automatický launcher stále hledá PHP v původním TEMP a poté v PATH.

**Mez opakovatelnosti:** data a Markdown lze znovu sestavit pouze s Pythonem a uchovanými zdroji. XLSX od nuly vyžaduje uchovaný funkční Artifact Tool nebo nové prostředí, které jej poskytne. Bez něj lze používat a přepočítávat existující sešity v Excelu/Calc; stávající generátor XLSX od nuly nespustíš. Návod tuto závislost nenahrazuje.

## 6. Chci práci jen číst a opravovat formulace

1. Otevři `bakalarsa_prace.md` v editoru Markdown s náhledem.
2. Poznámky můžeš dočasně dělat do kopie výsledku. Před sestavením je přenes do zdroje podle následující tabulky.
3. Změnu formulace odděl od změny faktu nebo výsledku. Čísla nepřepisuj ručně jen ve výsledné tabulce.

| Chci změnit | Trvalé místo změny |
|---|---|
| Kapitoly 9–14, diskusi, závěr | `pracovni_bp/text_prakticka_cast.md` |
| Titulní údaje, abstrakt, anglický abstract, předmluvu k pracovnímu stavu | Řetězec `front` v `build_thesis.py` |
| Nové znění úvodu a metodiky | Proměnné `ch1`, `ch3` a náhrady v `build_thesis.py` |
| Cíl | Schválený zdroj v e-mailu; generátor jej čte z oddílu finálního textu. Historický e-mail nepřepisuj kvůli změně cíle; novou verzi zadání ulož samostatně a vědomě změň zdroj generátoru |
| Nové texty kritérií a přílohy | Příslušné bloky `ch8`, `appendix` v `build_thesis.py` |
| Teorii BP 4–6 | Nejdříve uchovat originál. Preferovat explicitní náhradu v generátoru s původním zněním v hranaté poznámce. Záměrná změna znamená, že kontrola doslovného převzetí už nebude platit |
| Bibliografický údaj | Udržet soulad `BP 10.md` a `ZDROJE.md`; původní znění uchovat. `bibliografie.json` je jen výstup |
| Tabulku vah/pořadí | Změnit skutečný vstup, přepočítat reference, potom sestavit; nikoliv ručně editovat výstupní čísla |

Značky `{{CONTROL_TABLE}}`, `{{CRITERIA_TABLE}}`, `{{LOCAL_TABLE}}`, `{{RANKING_TABLE}}`, `{{SENSITIVITY_TABLE}}` a komentáře nech v praktickém zdroji, pokud chceš automatické doplňování. Generátor je nahradí. Neznámá značka způsobí zastavení pomocí assert.

**Pozor na konkrétní ručně napsaný komentář:** `CRITERIA_COMMENT` v generátoru tvrdí, že nejvyšší váhu mají K1/K3/K6 a nejnižší K4. To platí pro nynější demo; při změně dat se jména nejvyšších/nejnižších kritérií sama nepřehodnotí. Musíš upravit tento text podle nových výsledků. Další části jsou pevně psány pro čtyři alternativy a osm kritérií. Nejde o obecný generátor práce pro libovolný počet položek.

Při úpravě převzaté věty zachovej její přesný originál, datum a důvod, například:

```text
Nové znění věty.

[Pracovní poznámka – původní znění před úpravou, datum; důvod: ...
Přesná původní věta.
]
```

Při finální sazbě se tyto poznámky odstraní až po tvé revizi, nikoli hromadným mazáním všech hranatých závorek.

## 7. Znovu sestavit pouze text

Nejdříve záloha podle oddílu 4. Pokud upravuješ jen formulace, **nespouštěj generátor dat**.

```powershell
python .\pracovni_bp\build_thesis.py
if ($LASTEXITCODE -ne 0) { throw 'Sestavení textu selhalo; zkontroluj chybovou zprávu.' }
python .\pracovni_bp\verify_handoff.py
```

`build_thesis.py` zapíše `bakalarsa_prace.md`, tři přehledové JSON v pracovni_bp a také `protokoly/SYNTETICKY_PROTOKOL.md`, `K_OPERACIONALIZACE.md`, `README.md`. Do těchto generovaných protokolů proto neukládej jediné kopie reálných poznámek. Příkaz nepočítá nové reference z upravených vstupních matic: čte existující reference. Nekonzistentní dvojice vstup/reference by vedla k chybnému textu.

Po sestavení porovnej starou a novou práci v editoru, zkontroluj české znaky, nadpisy, cíle, tabulky, obrázky a srovnávací poznámky. `verify_handoff.py` neprovádí jazykovou ani citační kontrolu. Když se změní čísla, zkontroluj i abstrakt, komentáře, diskusi a závěr.

## 8. Obnovit přesně nynější syntetický příklad

Provádět nejprve v oddělené kopii. Generátor přepíše ruční změny dat.

```powershell
python .\pracovni_bp\generate_data.py
if ($LASTEXITCODE -ne 0) { throw 'Generování dat selhalo.' }
python .\pracovni_bp\build_thesis.py
if ($LASTEXITCODE -ne 0) { throw 'Sestavení textu selhalo.' }
```

Seed je `20260927`. Generují se latentní preference, poměry se zaokrouhlí na Saatyho škálu a přijímají se matice s CR ≤ 0,10. Tato filtrace slouží pouze demonstračním náhodným datům. Skutečné úsudky se nesmějí náhodně regenerovat, dokud nevyjde příjemné CR nebo pořadí.

Výstupy generátoru dat: `app/data/demo.json`, `control.json`, oba seed seznamy, `vypocty/demo_reference.json`, `control_reference.json`, `synteticke_testy.json`. Dále je potřeba sestavit XLSX podle oddílu 9, ověřit aplikaci a případně obnovit snímky. Samotný seed nestačí bez stejného skriptu, pořadí operací a seznamu úloh; uchovej celý balík.

## 9. Znovu sestavit XLSX a ověřit přepočet

Tento postup popisuje stávající generátor, nevytváří novou metodiku. Pracuj mimo synchronizovaný Drive a výsledky přenes až po kontrole. Nejdříve ověř dostupnost závislostí podle oddílu 5.

```powershell
$bpRoot = (Get-Location).Path
$bpRuntime = Join-Path $env:TEMP 'mes-bp-20260927'
$bpBuild = Join-Path $env:LOCALAPPDATA ('MES_BP_build\' + (Get-Date -Format 'yyyyMMdd_HHmmss_fff'))
New-Item -ItemType Directory -Path $bpBuild -ErrorAction Stop | Out-Null
if (-not (Test-Path -LiteralPath (Join-Path $bpRuntime 'node_modules/@oai/artifact-tool/package.json'))) {
  throw 'Chybí Artifact Tool. Obnov funkční prostředí; nepokračuj s prázdnými výstupy.'
}
Copy-Item -LiteralPath '.\pracovni_bp\build_workbooks.mjs' -Destination $bpRuntime
node (Join-Path $bpRuntime 'build_workbooks.mjs') $bpRoot $bpBuild
if ($LASTEXITCODE -ne 0) { throw 'Export XLSX selhal.' }
```

Skript je kopírován vedle funkčního `node_modules`, protože Node řeší import podle umístění skriptu. Výstup: oba XLSX, `*_verification.json`, PNG náhledy listů. Generátor kontroluje reference s tolerancí 1e-9 a změnu vstupu se zpětným obnovením. Prohlédni náhledy, zvláště list Testy; náhled nezachycuje automaticky všechny řádky rozsáhlého listu.

Nezávislé otevření a přepočet v LibreOffice (alternativou je ruční otevření v Excelu a úplný přepočet):

```powershell
$bpCalc = Join-Path $bpBuild 'prepocet'
New-Item -ItemType Directory -Path $bpCalc -ErrorAction Stop | Out-Null
$bpProfilePath = Join-Path $bpBuild 'lo-profile'
$bpProfileUri = ([System.Uri]$bpProfilePath).AbsoluteUri
$bpSoffice = 'C:\Program Files\LibreOffice\program\soffice.exe'
& $bpSoffice "-env:UserInstallation=$bpProfileUri" --headless --convert-to xlsx --outdir $bpCalc (Join-Path $bpBuild 'kontrolni_priklad.xlsx') (Join-Path $bpBuild 'hodnoceni_synteticke.xlsx')
```

Počkej na dokončení a ověř existenci obou souborů; úspěšné spuštění programu není důkaz přepočtu. Cílový adresář je odlišný od vstupního. Pokud převod selže, nepřenášej neexistující soubory a nevydávej výsledek za ověřený. Přepočtené soubory otevři, porovnej výsledky s reference JSON a kontrolním listem 9_souhrn.

Po záloze původních výstupů přenes nové sešity a příslušné kontrolní JSON:

```powershell
Copy-Item -LiteralPath (Join-Path $bpCalc 'kontrolni_priklad.xlsx') -Destination '.\vypocty\kontrolni_priklad.xlsx'
Copy-Item -LiteralPath (Join-Path $bpCalc 'hodnoceni_synteticke.xlsx') -Destination '.\outputs\bp_20260927\hodnoceni_synteticke.xlsx'
Copy-Item -LiteralPath (Join-Path $bpBuild 'kontrolni_priklad_verification.json'),(Join-Path $bpBuild 'hodnoceni_synteticke_verification.json') -Destination '.\outputs\bp_20260927\overeni'
python .\pracovni_bp\verify_handoff.py
```

Kontrolu proveď znovu po několika sekundách; Drive může soubory změnit asynchronně. Ponech známou dobrou kopii mimo Drive. Nové verification JSON patří ke konkrétnímu běhu a nesmějí sloužit jako zástěrka změny vstupů: před jejich převzetím musí reference i PHP kontrola odpovídat stejným maticím.

## 10. Spustit web, upravit preference a uložit práci

```powershell
.\app\spustit.ps1
```

Otevři `http://127.0.0.1:8080`. Okno PowerShellu nech běžet; Ctrl+C server zastaví. Pokud launcher nenajde vhodné PHP, použij explicitní cestu k PHP 8.2+ a parametr `-S 127.0.0.1:8080 -t app/public` podle README; zkontroluj zapisovatelnou složku PHP session.

Načti demo nebo kontrolní příklad, případně založ vlastní hodnocení. Vlastní položky se zadávají po řádcích jako `název | popis | https://odkaz`. Po změně párů spusť výpočet a zkontroluj CR. Volba Export JSON uchová vstupy i výsledky. Export ulož před zavřením prohlížeče – PHP session není dlouhodobý archiv. Pro obnovení použij import na úvodu, vlož obsah JSON. Aplikace výsledky při importu přepočítá.

Změna ve webu **automaticky nezmění** `app/data/demo.json`, XLSX, reference ani Markdown. Změna v Excelu se také automaticky nepřenese do webu. Pro srovnání musí obě prostředí dostat stejné matice, stejné pořadí kritérií i alternativ a stejnou metodu.

## 11. Výpočet – co znamenají výsledky a co měnit společně

Saatyho škála: 1, 2, …, 9 a převrácené hodnoty. Vyšší hodnota znamená vyšší preferenci řádkového prvku vůči sloupcovému. U K8 znamená preferenci výhodnějších nákladů, nikoliv vyšší cenu. Diagonála je 1; spodní trojúhelník reciproční. Prázdný vstup není rovnost.

```text
GM_i = (součin prvků řádku i)^(1/n)
w_i = GM_i / součet GM
Aw_i = součet_j a_ij * w_j
lambda_odhad = průměr_i (Aw_i / w_i)
CI = max(0, (lambda_odhad - n)/(n-1))
CR = CI / RI(n)
P_a = součet_k w_k * lokální_váha(a,k)
```

PHP používá logaritmy v double, referenční Python součin a Decimal s přesností 50 číslic, Excel GEOMEAN. Při geometrických vahách je lambda odhad, nikoliv vždy přesná dominantní vlastní hodnota. Pro n=1/2 je v implementaci CI=CR=0 a RI se nedělí. RI pro n=3…10: 0,58; 0,90; 1,12; 1,24; 1,32; 1,41; 1,45; 1,49. CR nad 0,10 vyvolá varování; nízké CR nepotvrzuje pravdivost preferencí.

Citlivosti jsou tři samostatné změny vůči základu: K8 ×2, K1 ×2, K3 ×2. Pro zesílené kritérium t je nová váha `2*w_t/(1+w_t)`, ostatní `w_j/(1+w_t)`. Matice alternativ se nemění. Nevznikají nové Saatyho matice kritérií, proto se pro tyto přímé změny vah neuvádí nové CR. Nejde o kombinaci všech tří změn naráz.

Pokud měníš metodu výpočtu, změň společně specifikaci, PHP jádro, nezávislou referenci, vzorce XLSX, testy a popis v práci. Novou metodu neověřuj tím, že opíšeš výstup stejného PHP kódu jako údajně nezávislý etalon.

## 12. Přechod ze syntetických dat na skutečné testy

Tento přechod **není hotové tlačítko generátoru**. Současné skripty a texty jsou výslovně určené pro syntetickou verzi. Postupuj po oddělených krocích:

1. Uchovej celé demo jako uzavřenou zálohu. Skutečné protokoly piš do samostatných souborů, které nepřepisuje `build_thesis.py`.
2. U každého produktu zaznamenej skutečnou edici, verzi, datum, prostředí, postup a důkaz. Používej stejné modelové zadání a stejné testové úlohy. Nejasnost zapiš jako neověřeno.
3. Pomocné známky 1–5 doplň podle důkazů. Z těchto známek nedělej automaticky průměr nebo převod na Saatyho škálu.
4. Sestav a slovně zdůvodni 28 párů kritérií a 8 × 6 párů alternativ. Dohromady 76 preferencí pro model 8 × 4. Zkontroluj CR každé matice.
5. Zadej model do aplikace a exportuj jej do nového souboru, například `vypocty/realne_hodnoceni.json`. Označení synthetic vypni až pro skutečné údaje. Název souboru není sám důkazem původu.
6. Pro nové matice vytvoř oddělený nezávislý přepočet. Současný `generate_data.py` při importu i spuštění vytváří demo – **neimportuj ho jen kvůli funkci result**, protože má zapisující kód na nejvyšší úrovni. Nejdříve vytvoř samostatný čtecí výpočetní skript nebo odděl funkce od generování. Uchovej kontrolní příklad 3 × 3 jako neměnnou regresní zkoušku.
7. Uprav vstupní cesty generátoru XLSX a textu na skutečný model a jeho reference. Změň syntetická označení pouze tam, kde již existuje skutečný důkaz. Přizpůsob protokoly, titulní varování, AI metodiku, pevně napsané komentáře a závěr. Zachovej původní demo samostatně.
8. Zadej stejné matice do kontrolního sešitu, přepočti a porovnej váhy, CR, priority i citlivosti. Zapiš skutečné rozdíly a toleranci, datum, verze a jméno kontrolujícího.
9. Proveď srovnání se specializovanou AHP aplikací. Před interpretací rozdílů zkontroluj metodu vah, RI a konzistenci.
10. Aktualizuj všechny výsledkové tabulky a slovní tvrzení, abstrakt, diskusi a závěr. Nové pořadí nepřebírá automaticky platnost starých vysvětlení.

Výběr vítěze není cílem opravy dat. Nezměněné pořadí při citlivosti je platný výsledek. Přechod zaznamenej do deníku na konci tohoto dokumentu; staré PASS protokoly označ jako historické, nikoliv jako kontrolu nových dat.

## 13. Jak zopakovat kontroly a snímky

Po změně matematiky nebo dat:

```powershell
& $phpBp .\app\tests\test_calculator.php
if ($LASTEXITCODE -ne 0) { throw 'Výpočetní test selhal.' }
```

Po změně PHP formulářů/validace:

```powershell
Get-NetTCPConnection -LocalPort 18763 -State Listen -ErrorAction SilentlyContinue
python .\app\tests\http_smoke.py $phpBp
if ($LASTEXITCODE -ne 0) { throw 'HTTP test selhal.' }
```

Port 18763 musí být před testem volný. Je-li obsazen, zjisti příkazovou řádku vlastnícího procesu a zastav pouze vlastní starý testovací server. Test sám port volný nekontroluje a mohl by jinak mluvit se starým serverem. Test ukládá PID a log do `%TEMP%\mes-bp-20260927`; server nechává běžet pro snímky. Po dokončení jej lze ukončit podle PID, ale nejdříve ověř, že stále patří danému PHP serveru.

Snímky a prohlížečová kontrola, pouze při dostupném Playwright a Chrome:

```powershell
$bpRuntime = Join-Path $env:TEMP 'mes-bp-20260927'
$bpVisual = Join-Path $env:LOCALAPPDATA ('MES_BP_visual\' + (Get-Date -Format 'yyyyMMdd_HHmmss_fff'))
Copy-Item -LiteralPath '.\pracovni_bp\visual_check.mjs' -Destination $bpRuntime
node (Join-Path $bpRuntime 'visual_check.mjs') $bpVisual
if ($LASTEXITCODE -ne 0) { throw 'Prohlížečová kontrola selhala.' }
```

Prohlédni `app_home.png`, `app_results.png`, `app_mobile.png`. Až potom nahraď obrázky ve `outputs/bp_20260927/` a ulož nový `browser_tests.json` do `overeni/`. Skript očekává původní demo a 76 dvojic; při vědomé změně rozsahu je nutné změnit i očekávání testu, nikoliv bezmyšlenkovitě ignorovat chybu.

Čtecí kontrola předání:

```powershell
python .\pracovni_bp\verify_handoff.py
```

Kontroluje původní otisky, doslovnou teorii 4–6, existenci odkazovaných obrázků, konec řádku, XLSX strukturu, chybové buňky a uložené číselné hodnoty. Nespouští Excel ani browser. Pokud změníš teorii, původní kontrola doslovnosti oprávněně selže; změnu dolož a uprav očekávání cíleně. `audit.py` nespouštěj k tomu, aby vytvořil nové „původní“ otisky a skryl rozdíl.

## 14. Časté problémy a co přesně dělat

| Problém | Postup |
|---|---|
| Ruční text po sestavení zmizel | Vzít rozdíl ze zálohy, přenést do zdroje podle oddílu 6 a znovu sestavit |
| `AssertionError` v textovém generátoru | Zjistit, která očekávaná původní věta nebo značka chybí; přizpůsobit konkrétní náhradu, ne odmazat všechny kontroly |
| Chybné české znaky | Soubory číst/zapisovat UTF-8; při porovnání rozlišit problém kódování od rozdílných konců řádků |
| `Cannot find package @oai/artifact-tool` | Spouštět kopii skriptu vedle funkčního node_modules; obnovit prostředí, ne vymýšlet veřejný instalační příkaz |
| PHP parse error / nesplněná verze | Zjistit skutečný PHP executable; použít 8.2+, ne místní výchozí 7.0 |
| PHP a reference se neshodují | Ověřit stejné vstupy, pořadí, reciproky, metodu a aktuálnost reference; nenahrazovat referenci slepě výstupem PHP |
| Excel ukazuje staré hodnoty | Provést úplný přepočet, uložit novou kopii a znovu zkontrolovat výsledky; statická cache není živý výpočet |
| Po přenosu na Drive je XLSX poškozený | Zachovat funkční kopii mimo Drive, porovnat hash, obnovit až po ověření a kontrolovat znovu s odstupem |
| Port testu obsazený | Ověřit proces, ukončit pouze vlastní testovací server, potom spustit nový test |
| Jiný AHP nástroj dává jiná čísla | Porovnat geometrickou metodu versus vlastní vektor, RI, výpočet CR, vstupní pořadí a zaokrouhlení |
| Změněna data, text tvrdí starý výsledek | Aktualizovat reference, sestavit a ručně zkontrolovat pevné komentáře i závěr |

## 15. Jak dokončit odevzdávanou práci

Po skutečných výsledcích provést kontrolu zdrojů a jejich použití, přezkoumat metodiku a pravdivé vymezení AI (nástroj, dostupná verze, účel, postup a rozsah). Nepřipisovat autorovi nebo vedoucímu kontrolu, která neproběhla.

Použít fakultní šablonu `oliva/sablony/šablona( nová (1).docx`, nikoliv seminární šablonu. Finální Word není dosud automatickým výstupem tohoto sestavení. Bude potřeba vložit text do stylů šablony, nastavit obsah, seznamy tabulek a obrázků, číslování od úvodu, doplnit zadání a skutečné prohlášení. Formát ověřit podle fakultních pokynů: text 12 pt, řádkování 1,5, levý okraj 3,5 cm a ostatní 2 cm. Rozsah zkontrolovat až v sazbě; počet znaků není počet stran.

Odstranit pracovní srovnávací bloky, nikoliv bibliografické údaje nebo potřebné odkazy. Vyhledat zbývající `BP-DOPLNIT`, `BP-OVĚŘIT`, `⟦...⟧`, `{{...}}` a pracovní poznámky. Pojem syntetická data může legitimně zůstat v popisu testování programu, i když produktová komparace již používá skutečná data. Finální DOCX/PDF vizuálně zkontrolovat a uchovat známou dobrou kopii mimo Drive.

## 16. Deník změn a předání po výpadku

Po každé podstatné změně přidej záznam sem; nepřepisuj historii. Tím tento dokument zůstane jediným hlavním návodem. Zapisuj:

```text
Datum a autor:
Co jsem chtěl změnit a proč:
Změněné zdrojové soubory:
Vstupní data / zda skutečná nebo syntetická:
Záloha před změnou (přesná cesta):
Spuštěné příkazy:
Výsledek kontrol + cesta k novým důkazům:
Co se automaticky nepřepočítalo / co zbývá:
Přesný nejbližší krok:
```

### 27. 9. 2026 – vytvoření jednotného návodu

Přečteny skutečné generátory dat, textu, sešitů, testy a specifikace. Ověřeny místní verze a závislosti. V oddělené složce `C:\Users\janis\AppData\Local\Temp\mes-rebuild-check-d336k605` byly znovu vytvořeny demo vstupy, reference, syntetický protokol a Markdown; sedm porovnaných textových výstupů bylo po normalizaci konců řádků shodných. Hlavní práce, data, aplikace a sešity se tímto ověřením nepřepisovaly. Nové sestavení XLSX a nové prohlížečové zkoušky se při psaní tohoto návodu nespouštěly. Nejbližší krok autora: vytvořit zálohu, číst práci, zapisovat opravy do zdrojů podle oddílu 6 a sestavovat pouze text podle oddílu 7.

### Text pro zahájení příští relace

### Předání na zítřek – domluva 27. 9. 2026

Uživatel požádal uložit kontext přímo v tomto projektu a pokračovat zítra (28. 9. 2026). Pracovní text, aplikace, sešity a syntetická data jsou připravené; jednotný návod byl dokončen a opakovatelnost textu a dat ověřena v oddělené kopii. Další krok: začít autorským čtením a úpravami práce, podle uživatelem vybrané části. Před změnami vytvořit zálohu podle oddílu 4, určit zdroj textu podle oddílu 6 a případně sestavit pouze text podle oddílu 7. Nezačínat znovu od nuly a automaticky nespouštět generátory. Nejprve ověřit případné ruční úpravy od posledního předání. Skutečné produktové testy a finální výsledky stále nejsou hotové. Tento zápis není nastavení automatické připomínky.

> Přečti NAVOD_K_PRACI_A_OPAKOVANI.md a poslední záznam deníku. Zjisti, zda jsem ručně upravil bakalarsa_prace.md nebo zdrojové soubory. Před jakýmkoliv přegenerováním porovnej změny a zachovej je. Pokračuj od posledního nedokončeného kroku. Nespouštěj zbytečně audit.py ani generátor náhodných dat. Po práci doplň tento návod a nové důkazy kontrol.
