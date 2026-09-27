# AHP – výběr databázového nástroje

Pracovní aplikace k BP. PHP 8.2 nebo novější, rozšíření JSON a session (standardní instalace). Bez Composeru, databáze a sestavování frontendu.

Z kořene projektu:

```powershell
php -S 127.0.0.1:8080 -t app/public
```

Otevřít http://127.0.0.1:8080. Na tomto počítači příkaz `php` původně míří na PHP 7.0, proto použijte `app/spustit.ps1`, který ověří verzi a najde také přenosné PHP připravené při zpracování.

1. **Načíst demo:** 4 nástroje, K1–K8, náhodné údaje, viditelné označení syntetického původu.
2. **Kontrolní příklad:** F/P/C a A1/A2/A3 z kontrolního sešitu.
3. **Vlastní hodnocení:** připravené i vlastní položky, prázdné páry, následný výpočet. Volbu syntetických dat vypněte až u skutečného hodnocení.
4. **Upravit preference:** změnit páry a přepočítat. Obrácená hodnota se dopočítá.
5. **Export JSON:** uložit vstupy i výsledky; na úvodní stránce vložit obsah do importu. Výsledky se při importu vždy přepočítají.

Sešity: `vypocty/kontrolni_priklad.xlsx` a `outputs/bp_20260927/hodnoceni_synteticke.xlsx`. Zdrojové demo `app/data/demo.json`; nezávislé kontrolní hodnoty `vypocty/*_reference.json`. Známky z protokolu 1–5 nevstupují do AHP automaticky.

Test výpočtů: `php app/tests/test_calculator.php`. HTTP test: spustit `app/tests/http_smoke.py` Pythonem s cestou k PHP jako argumentem; lokální testovací server zůstane na portu 18763 pro vizuální kontrolu. Ukončení jeho PID je popsáno ve vygenerovaném testovacím protokolu.

Soubor SPEC.md popisuje rozsah; matematika je v `vypocty/AHP_SPECIFIKACE.md`. Horní limit 10 kritérií i alternativ odpovídá tabulce RI a zabraňuje neúměrnému počtu párů. Jedna vlastní položka = `název | popis | https://odkaz`.

Veřejné nasazení zatím nebylo provedeno. Pro hosting použijte document root `app/public`, HTTPS, podporované PHP a zapisovatelný adresář session mimo document root. Vestavěný PHP server slouží k místnímu ověření. Před nasazením znovu proveďte kontrolní příklad v cílovém prostředí.
