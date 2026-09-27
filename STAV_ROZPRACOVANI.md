# Stav práce a navázání po výpadku

**Hlavní návod je nyní `NAVOD_K_PRACI_A_OPAKOVANI.md`.** Obsahuje tento stav v souvislostech, mapu zdrojů, opakovatelné příkazy, postupy změn a deník. Při další práci začni tam; tento soubor zůstává stručným záznamem předání.

Aktualizace: 27. 9. 2026. Stav: hlavní pracovní výstupy se syntetickými daty existují; navazující technická kontrola dokončena. Nejde o finální práci k odevzdání.

## Zadání uživatele

Připravit souvislou bakalářskou práci v `bakalarsa_prace.md`, PHP webovou aplikaci, kontrolní Excel a demonstraci AHP na náhodných testovacích datech. Testovací data musí být označena jako syntetická, nikoliv vydávána za provedené testy. Skutečné testy a závěry následně doplní autor. Věty ze seminární práce zachovat; při změně uvést přesný původní text v hranatých závorkách. Původní soubory BP nepřepisovat. Průběžně aktualizovat tento soubor, aby po výpadku nebylo potřeba práci vytvářet znovu.

## Co již existuje – aktuálně zjištěno na disku

- `bakalarsa_prace.md` – 132 508 bajtů, souvislá pracovní verze včetně teorie, praktických kapitol, výsledků a pracovního závěru; výslovně označuje syntetická data.
- `app/` – PHP aplikace, formuláře, výpočet, import/export, připravené i vlastní položky, demo a kontrolní příklad; testy v `app/tests/`.
- `vypocty/AHP_SPECIFIKACE.md`, `app/SPEC.md` – matematický a datový návrh.
- `vypocty/kontrolni_priklad.xlsx` – kontrolní sešit.
- `outputs/bp_20260927/hodnoceni_synteticke.xlsx` – sešit syntetického hodnocení.
- `vypocty/control_reference.json`, `vypocty/demo_reference.json`, `app/data/` – vstupy a referenční výsledky.
- `protokoly/SYNTETICKY_PROTOKOL.md` – 204 náhodných známek; výslovně uvádí, že testy nebyly provedeny.
- `pracovni_bp/` – generátory dat, sešitů a textu, zdroj praktické části, původní kontrolní otisky, statistiky a přehled změn.

Existence souboru sama o sobě neznamená ověření jeho správnosti. Následující kontroly byly skutečně provedeny v navazujícím běhu; jejich rozsah a omezení zachycuje `vypocty/PROTOKOL_KONTROLNI_VYPOCET.md`.

## Dokončeno při navázání 27. 9. 2026

- Znovu spuštěno 146 výpočetních kontrol PHP: PASS, největší rozdíl proti referenci 1,78 × 10⁻¹⁵.
- Znovu spuštěno 14 HTTP kontrol: PASS (včetně importu/exportu, vlastních položek, chyb a vysokého CR).
- Ověřeny SHA-256 všech původních BP 0–10 a původního XLSX proti uloženým vstupním otiskům: žádná změna.
- Ověřeno doslovné převzetí celých kapitol BP 4–6 do práce.
- Ověřena integrita XLSX, 10 a 13 listů, 120 a 354 vzorců, žádné uložené chybové buňky. Celkem 24 hlavních uložených výsledků odpovídá referencím v toleranci 1e-9. Nejde o nový přepočet v Microsoft Excelu.
- Obnoveny chybějící obrázky odkazované z práce; uloženy z TEMP do `outputs/bp_20260927/`.
- Dochované záznamy ověření sešitů a prohlížeče uloženy trvale do `outputs/bp_20260927/overeni/`. Prohlížečový PASS je převzatý záznam, HTTP a PHP kontroly byly nové.
- Doplněn chybějící `vypocty/PROTOKOL_KONTROLNI_VYPOCET.md`, na který již odkazovala příloha práce.
- Přidán nedestruktivní kontrolní skript `pracovni_bp/verify_handoff.py` (pouze standardní Python; nic nepřepisuje).

## Důležité zjištění z podkladů

`PLAN.md` z 13. 9. je zastaralý. `EMAIL_KONVERZACE.md` obsahuje zprávu vedoucího z 15. 9. s finálním zněním cíle a osnovy pro STAG. Vedoucí požaduje nezávislý ruční/Excel přepočet a také srovnání s existujícím nástrojem. Schválení ve STAGu nebylo v tomto běhu ověřeno.

## Původní kontrolní kroky – dokončené a zbývající

1. Hotovo: nalezeno PHP 8.5.11 v `%TEMP%\mes-bp-20260927\php\php.exe` a dřívější záznamy. Dočasný runtime může být odstraněn úklidem Windows; aplikace vyžaduje PHP 8.2+.
2. Hotovo: původní BP nezměněny, teorie BP 4–6 převzata doslova. Změny dalších pasáží eviduje `pracovni_bp/zmeny_prevzateho_textu.json` a hranaté závorky v práci.
3. Hotovo: nové PHP/HTTP testy, kontrola integrity a uložených výsledků XLSX, doplnění protokolu a obrázků.
4. Další obsahový krok: autorská revize celého textu, bibliografie a slovních interpretací; nejde o úkol znovu vytvořit aplikaci či text. Nový úplný audit všech citací v tomto navazujícím běhu neproběhl. Statistika předchozího sestavení uvádí 30 položek a přibližně 96 tisíc znaků těla bez srovnávacích poznámek.
5. Hotovo: uložen tento stav a přesné příkazy v kontrolním protokolu.

## Jak bez ztráty pokračovat

- Pro čtení otevřít `bakalarsa_prace.md`; pro běžné spuštění webu `./app/spustit.ps1`.
- Pro opakovanou nedestruktivní kontrolu spustit `python pracovni_bp/verify_handoff.py`.
- Neupravovat hotovou práci a poté bez rozmyslu spouštět `build_thesis.py`: generátor přepisuje výsledný Markdown. Nové praktické pasáže mají zdroj v `pracovni_bp/text_prakticka_cast.md`; další části generuje `build_thesis.py`.
- `audit.py` znovu nespouštět pro pouhou kontrolu: přepisuje vstupní kontrolní otisky. Použít `verify_handoff.py`.
- PHP a HTTP zkoušky i omezení jsou v `vypocty/PROTOKOL_KONTROLNI_VYPOCET.md`.
- Po skutečných testech nahradit jak pomocné známky, tak samostatné párové matice; známky 1–5 nejsou automatický vstup AHP. Přepočítat rovněž tři citlivosti a upravit komentáře, abstrakt a závěr.

## Co zbývá před odevzdáním

Skutečné testy čtyř nástrojů, přesné verze a důkazy; náhrada syntetických párových matic; nový přepočet a slovní interpretace; osobní nezávislá kontrola autora a další AHP nástroj; finální závěr; formální sazba do fakultní DOCX šablony, prohlášení a zadávací list. Veřejné nasazení aplikace není doloženo.

## Pokyn pro další relaci

Nejprve čti tento soubor, poté dokumentaci `app/README.md`, specifikaci a aktuální výsledky kontrol. Nezačínej znovu generovat vše. Před spuštěním generátorů zkontroluj, zda nepřepíšou ruční úpravy. Neměň původní `hodnoceni_4_nastroju.xlsx` ani zálohu. Nezaměň existující syntetické protokoly za skutečné testy. Po dokončení každého významného kroku aktualizuj tento záznam.
