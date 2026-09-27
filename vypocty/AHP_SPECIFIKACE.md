# Specifikace AHP – pracovní implementace 27. 9. 2026

Vychází z PLAN fáze B, BP 6 a novějšího e-mailu vedoucího z 15. 9. 2026. Demo není empirické hodnocení nástrojů. Osobní kontrolní přepočet autora a porovnání s existujícím AHP nástrojem zůstávají samostatnými kroky.

## Vstupy a kontrola

2–10 kritérií a 2–10 alternativ v uživatelském rozhraní; matematické jádro podporuje také n=1. Jediné přípustné preference: 1/9, 1/8, …, 1/2, 1, 2, …, 9. Horní trojúhelník zadává uživatel, diagonála je 1, dolní trojúhelník je přesně reciproční. Kladnost, konečnost, úplnost, rozměr, škála a reciprocita se kontrolují na serveru. Číselná tolerance 1e-9. Prázdná položka není rovnost. Větší hodnota vždy znamená vyšší preferenci řádkového prvku; u ceny se vyjadřuje výhodnost, nikoli vyšší cena.

## Výpočet

GM_i = exp(sum_j ln(a_ij)/n); w_i = GM_i / sum(GM). Kontrolní sešit používá GEOMEAN, nezávislý Python součin s Decimal (50 míst). PHP používá logaritmy v double. Po celou dobu se nezaokrouhlují mezivýsledky. Zobrazení 4 desetinná místa.

Aw_i = sum_j a_ij*w_j. LambdaEstimate = average_i(Aw_i/w_i). CI = max(0,(LambdaEstimate−n)/(n−1)); CR = CI/RI. Pro n=1 a n=2 se uvádí CI=CR=0 a informace, že se poměr konzistence pro tyto rozměry nehodnotí. Matice musejí projít validací i pro n=1/2. Nulový RI se nikdy nedělí.

**LambdaEstimate je při geometrických vahách odhad dominantního vlastního čísla**, nikoli obecně přesný lambda_max. Specifikace tedy neslibuje rovnost s vlastními vektory. Kontrola cizím nástrojem musí zohlednit použitou metodu vah a tabulku RI.

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| RI | 0 | 0 | 0,58 | 0,90 | 1,12 | 1,24 | 1,32 | 1,41 | 1,45 | 1,49 |

P_a = sum_k w_k*l_ak. Součty vah i priorit mají být 1 s tolerancí 1e-9. Pořadí sestupně; shodné hodnoty s tolerancí 1e-12 dostávají společné pořadí. CR ≤ 0,10 je pracovní hranice, nad ní se zobrazí varování a výsledek zůstane dostupný. Nízké CR nedokazuje pravdivost vstupů.

## Citlivost

Tři oddělené zásahy vůči základnímu běhu: K8 ×2, K1 ×2, K3 ×2. w'_t=2w_t/(1+w_t), ostatní w'_j=w_j/(1+w_t). Lokální matice a váhy alternativ zůstávají stejné. Jde o přímou citlivost vah, nikoli o další Saatyho vstupní matice: neuvádí se pro ni nově vypočtené CR kritérií. Nikdy se nekombinují všechny tři změny současně.

## Kontrolní příklad a syntetická data

Vstupní matice z oddílu 5 AHP_NAVOD_SAATY.md jsou v app/data/control.json. Přesně přepočtený etalon je vypocty/control_reference.json; list 9_souhrn kontrolního sešitu obsahuje vedle vzorců také archivní hodnoty. Starší zaokrouhlené hodnoty návodu se nepoužívají jako etalon.

Demo: Python random.Random(20260927), latentní preference náhodně v intervalu 1–5, poměry s logaritmickou odchylkou ±0,20, zaokrouhlení na nejbližší Saatyho hodnotu v logaritmické vzdálenosti. Přijímají se pouze matice CR ≤ 0,10; počty pokusů jsou v JSON. Toto omezení slouží ukázce výpočtu, nesmí být použito k umělému vylepšování skutečných úsudků. Pomocné známky 1–5 pro 51 bloků jsou generovány odděleně a nejsou převáděny na Saatyho vstupy. Žádné náhodné ceny, verze ani údajné důkazy se nevytvářejí.

## Akceptace

PHP vs Decimal vs tabulkový výpočet: max absolutní odchylka vah, priorit a CR ≤ 1e-9; projektový limit vah 0,001. Ověřit konzistentní i nekonzistentní matice, obrácení preferencí, chybné vstupy, n=1/2, shodu pořadí, součty a citlivost. Ověření uživatelského formuláře musí proběhnout HTTP cestou, ne jen voláním třídy.
