# Datový a funkční návrh – 27. 9. 2026

Nejprve specifikace AHP a kontrolní sešit, poté PHP. Aplikace má jednoho uživatele v rámci session; neobsahuje účty, role ani REST API. PHP 8.2+, serverové HTML, CSS, minimální JavaScript není nutný. Předdefinované položky v JSON mimo public, výběr a vstupy v PHP session. JSON export/import umožní přenos mezi demonstrací a vlastním měřením bez databázového serveru.

Datový dokument: schema_version, title, synthetic (povinný boolean), criteria a alternatives (id/name/description/link), criteria_matrix a alternative_matrices v pořadí kritérií. Volitelné seed a generation identifikují demo. Výsledky se vždy znovu vypočtou; importovaný výsledek není autoritativní. Max. 10 prvků každého typu kvůli pracnosti a RI tabulce; min. 2. Jedna vlastní položka každého typu na řádek (název | popis | https odkaz); prázdný odkaz přípustný. Jedinečné identifikátory a neprázdné názvy.

Tok: úvod a volba demo/kontrola/vlastní → výběr položek a doplnění vlastních → popisy a párová porovnání → výsledky, CR, váhy, pořadí → změna vstupů/přepočet/export. Vlastní hodnocení začíná nevyplněnými páry. Demo je viditelně označeno na všech relevantních stránkách a v exportu. Import musí zachovat příznak syntetických dat. Změna složení hodnocení znamená nové matice.

Oddělení: src/AhpCalculator.php čistá matematika; src/Evaluation.php validace dokumentu; public/index.php obsluha formulářů a výstup; public/assets/style.css vzhled; data/* připravené seznamy a výpočetní příklady; tests/* nezávislé srovnání a HTTP testy.

Ochrana: escapování HTML, povolené http/https odkazy, CSRF token pro změny, omezení importu na 1 MB, žádné provádění importovaného kódu, serverová validace všech vstupů. Lokální spuštění na 127.0.0.1; veřejné nasazení není součástí tohoto běhu. Před zveřejněním nutné HTTPS a kontrola nastavení hostingu. Citlivost se zobrazí při přítomnosti K1/K3/K8 podle specifikace.
