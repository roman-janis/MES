# Kontrola pracovní implementace AHP

Datum navazující kontroly: 27. 9. 2026. Účel: ověřit existující pracovní výstupy a uchovat důkazy po přerušení relace.

## Nově provedené kontroly

| Kontrola | Výsledek |
|---|---|
| `app/tests/test_calculator.php`, PHP 8.5.11 | PASS, 146 kontrol, největší absolutní rozdíl 1,7763568394002505 × 10⁻¹⁵ |
| `app/tests/http_smoke.py` | PASS, 14 kontrol: demo, kontrolní příklad, import/export, vlastní položky, chybné vstupy, CSRF a vysoké CR |
| Integrita původních BP 0–10 a původního hodnoticího XLSX | Všech 12 SHA-256 odpovídá uloženým vstupním otiskům |
| Převzaté kapitoly BP 4–6 | Celé původní texty jsou ve výsledné práci přítomny beze změny |
| Kontrolní XLSX | ZIP bez chyby, 10 listů, 120 vzorců, 7 hlavních uložených výsledků proti referenci, největší rozdíl 4,03 × 10⁻¹⁶ |
| Syntetické XLSX | ZIP bez chyby, 13 listů, 354 vzorců, 17 hlavních uložených výsledků včetně citlivosti proti referenci, největší rozdíl 1,12 × 10⁻¹⁶ |
| Chybové buňky v uložených XLSX | Žádná buňka s typem Excel error |
| Obrázky odkazované z práce | Doplněny do projektu a ověřena existence |

Kontrola XLSX v tomto navazujícím běhu čte uložené výsledky vzorců. Sama nedokazuje nové přepočtení v Microsoft Excelu. Opakovatelné ověření souborů provádí `python pracovni_bp/verify_handoff.py`.

## Dochované důkazy předchozího běhu

Ve složce `outputs/bp_20260927/overeni/` jsou uloženy `kontrolni_priklad_verification.json`, `hodnoceni_synteticke_verification.json` a `browser_tests.json`. První dva obsahují srovnání výsledků a změnu vstupu s obnovením původního výsledku. Prohlížečový záznam uvádí PASS, 76 dvojic a žádné chyby stránky. Snímky úvodní stránky, výsledků a mobilního zobrazení jsou v nadřazené složce. Tento běh převzal existující prohlížečový záznam; znovu provedl HTTP testy, nikoliv interaktivní prohlížečové testy.

Existují také dočasné přepočtené kopie obou sešitů v `%TEMP%\mes-bp-20260927\recalculated`. Dočasná složka není trvalým úložištěm. Rozhodující předávané sešity jsou `vypocty/kontrolni_priklad.xlsx` a `outputs/bp_20260927/hodnoceni_synteticke.xlsx`.

## Vstupy a reprodukce

Vstupní matice jsou v `app/data/control.json` a `app/data/demo.json`, referenční výsledky v `vypocty/control_reference.json` a `vypocty/demo_reference.json`. Metodu vymezuje `vypocty/AHP_SPECIFIKACE.md`; referenční výpočet je součástí `pracovni_bp/generate_data.py`. Generátor nespouštět kvůli pouhé kontrole: zapisuje data a mohl by přepsat pozdější ruční úpravy.

Z kořene projektu v PowerShellu:

```powershell
$phpBp = Join-Path $env:TEMP 'mes-bp-20260927\php\php.exe'
& $phpBp app/tests/test_calculator.php
python app/tests/http_smoke.py $phpBp
python pracovni_bp/verify_handoff.py
```

HTTP test zanechá místní server na portu 18763. PID uloží do `%TEMP%\mes-bp-20260927\server_pid.txt`; před ukončením ověřit, že PID stále patří testovacímu PHP procesu. Pro běžné používání spustit `./app/spustit.ps1`, otevřít `http://127.0.0.1:8080` a server ukončit Ctrl+C. Pokud přenosné PHP z TEMP zmizí, zajistit PHP 8.2+; výchozí PHP 7.0 nestačí.

## Omezení

Neproběhly skutečné produktové testy, osobní ruční přepočet autora, kontrola vedoucím, ověření další specializovanou AHP aplikací ani veřejné nasazení. Syntetické priority dokazují pouze zpracování zadaných dat. Nová kontrola struktury a uložených výsledků sešitů nenahrazuje jejich ruční přepočet. Finální verze vyžaduje skutečná data a odpovídající úpravu interpretací.
