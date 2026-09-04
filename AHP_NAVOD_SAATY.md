# Návod: Saatyho metoda (AHP) krok za krokem s kontrolním příkladem

Cíl tohoto souboru: projít celý výpočet AHP ručně na malém, ale kompletním
příkladu (3 kritéria × 3 alternativy) tak, aby výsledná čísla šla použít jako
**kontrola vlastního Excelu** — než se stejný postup použije na reálný
problém s 8 kritérii (K1–K8) a 4 nástroji podle `PLAN.md` (blok 1, bod 3–4).
Odpovídá úkolu „projít 1 kompletní AHP příklad ze Saaty (1990, s. 9–26) ručně"
z `PLAN.md`.

Zdroje: Saaty (1990), Saaty (2008), Ishizaka a Labib (2011) — viz `ZDROJE.md`,
sekce 2.

## 1. Princip metody

AHP (Analytic Hierarchy Process) rozkládá rozhodovací problém do hierarchie:

```
Cíl (výběr nejvhodnějšího nástroje)
 ├─ Kritérium 1
 ├─ Kritérium 2
 └─ Kritérium 3
      ├─ Alternativa A
      ├─ Alternativa B
      └─ Alternativa C
```

Na každé úrovni se prvky porovnávají **po dvojicích** (párové porovnání):
kolikrát je prvek i důležitější / lepší než prvek j vzhledem k nadřazenému
prvku (Saaty, 1990; Saaty, 2008). Výsledkem jsou:

1. váhy kritérií (jak moc na každém kritériu záleží),
2. lokální váhy alternativ vzhledem ke každému kritériu (jak dobrá je
   alternativa v tomto jednom ohledu),
3. globální skóre alternativ = vážený součet lokálních vah přes všechna
   kritéria → konečné pořadí.

## 2. Saatyho škála

| Hodnota | Význam |
|---|---|
| 1 | Stejná důležitost |
| 3 | Mírně důležitější |
| 5 | Silně důležitější |
| 7 | Velmi silně důležitější |
| 9 | Extrémně důležitější |
| 2, 4, 6, 8 | Mezistupně |
| 1/3, 1/5, 1/7, 1/9 ... | Opačný směr (j je důležitější než i) |

Matice je vždy **reciproční**: pokud a_ij = x, pak a_ji = 1/x. Na diagonále
je vždy 1 (prvek je stejně důležitý sám sobě).

## 3. Výpočet vah — metoda geometrického průměru řádků

Pro matici n×n s prvky a_ij:

1. Geometrický průměr řádku i: `GM_i = (a_i1 × a_i2 × ... × a_in)^(1/n)`
2. Váha: `w_i = GM_i / Σ GM_i` (normalizace na součet 1)

Tato metoda je aproximace přesné metody vlastního vektoru, kterou Saaty
používal v originále; pro ruční výpočet a malé matice dává prakticky shodné
výsledky a je běžně používaná (Ishizaka a Labib, 2011). V Excelu odpovídá
funkci `GEOMEAN()` po řádcích.

## 4. Kontrola konzistence

Člověk není dokonale konzistentní (pokud A > B a B > C, nemusí být A oproti
C přesně tak silné, jak by matematicky vyplývalo). AHP to měří:

1. Vypočítej `A·w` (matice krát vektor vah) — pro každý řádek i:
   `(Aw)_i = Σ_j a_ij × w_j`
2. `λmax = (1/n) × Σ_i [ (Aw)_i / w_i ]`
3. Index konzistence: `CI = (λmax − n) / (n − 1)`
4. Poměr konzistence: `CR = CI / RI`, kde RI je náhodný index pro danou
   velikost matice (tabulka níže, Saaty, 1990).
5. **CR < 0,1 → matice je dostatečně konzistentní**, výsledek lze použít.
   CR ≥ 0,1 → párová porovnání je třeba přehodnotit.

### Tabulka náhodného indexu RI

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| RI | 0 | 0 | 0,58 | 0,90 | 1,12 | 1,24 | 1,32 | 1,41 | 1,45 | 1,49 |

Pro reálnou práci potřebujete RI(8) = 1,41 (matice kritérií K1–K8) a
RI(4) = 0,90 (matice 4 nástrojů pro každé kritérium).

## 5. Kontrolní příklad — 3 kritéria, 3 alternativy

Fiktivní zjednodušený problém: **Funkcionalita (F)**, **Použitelnost (P)**,
**Cena (C)** jako kritéria; nástroje **A**, **B**, **C** jako alternativy.
Čísla jsou zvolena tak, aby šla ručně zkontrolovat a aby výsledek vyšel
smysluplně konzistentní — použijte je k ověření vlastního Excelu, ne jako
skutečné hodnocení nástrojů z BP.

### 5.1 Matice kritérií (F, P, C)

| | F | P | C |
|---|---|---|---|
| **F** | 1 | 3 | 5 |
| **P** | 1/3 | 1 | 3 |
| **C** | 1/5 | 1/3 | 1 |

Geometrické průměry řádků:

- F: (1 × 3 × 5)^(1/3) = 15^(1/3) = **2,4662**
- P: (1/3 × 1 × 3)^(1/3) = 1^(1/3) = **1,0000**
- C: (1/5 × 1/3 × 1)^(1/3) = (1/15)^(1/3) = **0,4055**

Součet = 3,8717 → váhy:

- **w_F = 2,4662 / 3,8717 = 0,6370**
- **w_P = 1,0000 / 3,8717 = 0,2583**
- **w_C = 0,4055 / 3,8717 = 0,1047**

(součet vah = 1,0000 ✓)

Kontrola konzistence:

- (Aw)_F = 1×0,6370 + 3×0,2583 + 5×0,1047 = 1,9355
- (Aw)_P = 1/3×0,6370 + 1×0,2583 + 3×0,1047 = 0,7848
- (Aw)_C = 1/5×0,6370 + 1/3×0,2583 + 1×0,1047 = 0,3182

Podíly (Aw)_i / w_i: 1,9355/0,6370 = 3,039; 0,7848/0,2583 = 3,038;
0,3182/0,1047 = 3,039 → **λmax = 3,039**

- CI = (3,039 − 3) / (3 − 1) = **0,0193**
- RI(3) = 0,58
- **CR = 0,0193 / 0,58 = 0,033** → CR < 0,1, matice je konzistentní ✓

### 5.2 Matice alternativ vzhledem ke kritériu F (Funkcionalita)

| | A | B | C |
|---|---|---|---|
| **A** | 1 | 2 | 4 |
| **B** | 1/2 | 1 | 2 |
| **C** | 1/4 | 1/2 | 1 |

Tato matice je záměrně **plně konzistentní** (A je 2× lepší než B, B je 2×
lepší než C, tedy A je 4× lepší než C — přesně sedí s zadanou hodnotou 4).

Geometrické průměry: A = (1×2×4)^(1/3) = 2; B = (0,5×1×2)^(1/3) = 1;
C = (0,25×0,5×1)^(1/3) = 0,5. Součet = 3,5 → váhy:

**w_A = 0,5714, w_B = 0,2857, w_C = 0,1429** (CI = 0, CR = 0 — dokonale
konzistentní, protože λmax = n přesně).

### 5.3 Matice alternativ vzhledem ke kritériu P (Použitelnost)

| | A | B | C |
|---|---|---|---|
| **A** | 1 | 1/2 | 2 |
| **B** | 2 | 1 | 4 |
| **C** | 1/2 | 1/4 | 1 |

Opět plně konzistentní (B je 2× lepší než A, A je 2× lepší než C → B je 4×
lepší než C). Váhy: **w_A = 0,2857, w_B = 0,5714, w_C = 0,1429** (CR = 0).

### 5.4 Matice alternativ vzhledem ke kritériu C (Cena)

Nižší cena = lepší, takže poměry vyjadřují „výhodnost ceny": C je nejlevnější
(nejlepší), pak A, pak B.

| | A | B | C |
|---|---|---|---|
| **A** | 1 | 2 | 1/3 |
| **B** | 1/2 | 1 | 1/6 |
| **C** | 3 | 6 | 1 |

Plně konzistentní (C je 3× lepší než A, A je 2× lepší než B → C je 6× lepší
než B). Váhy: **w_A = 0,2222, w_B = 0,1111, w_C = 0,6667** (CR = 0).

### 5.5 Syntéza — globální skóre

Globální skóre alternativy = Σ (váha kritéria × lokální váha alternativy
vzhledem k tomuto kritériu).

| Kritérium | Váha kritéria | w_A (lokální) | w_B (lokální) | w_C (lokální) |
|---|---|---|---|---|
| F | 0,6370 | 0,5714 | 0,2857 | 0,1429 |
| P | 0,2583 | 0,2857 | 0,5714 | 0,1429 |
| C | 0,1047 | 0,2222 | 0,1111 | 0,6667 |

- **Skóre A** = 0,6370×0,5714 + 0,2583×0,2857 + 0,1047×0,2222 = 0,3640 +
  0,0738 + 0,0233 = **0,4611**
- **Skóre B** = 0,6370×0,2857 + 0,2583×0,5714 + 0,1047×0,1111 = 0,1820 +
  0,1476 + 0,0116 = **0,3412**
- **Skóre C** = 0,6370×0,1429 + 0,2583×0,1429 + 0,1047×0,6667 = 0,0910 +
  0,0369 + 0,0698 = **0,1977**

Součet ≈ 1,0000 (kontrola). **Výsledné pořadí: A (0,461) > B (0,341) >
C (0,198).**

Pokud tato čísla vyjdou (v rámci zaokrouhlení na 3–4 desetinná místa) i ve
vašem vlastním Excelu se stejnými vstupními maticemi, je výpočetní postup
(GEOMEAN + normalizace + CI/CR + syntéza) správně sestavený a lze ho použít
na reálný problém K1–K8 × 4 nástroje.

## 6. Jak přenést postup do `AHP_vypocet.xlsx`

Podle struktury naplánované v `PLAN.md` (blok 1, bod 4):

| List | Obsah | Rozměr |
|---|---|---|
| List 1 | Matice kritérií K1–K8 + váhy (GEOMEAN + normalizace) + CI/CR | 8×8 |
| Listy 2–9 | Matice 4 nástrojů, jeden list na kritérium (K1 až K8) + váhy + CR | 4×4 (RI = 0,90) |
| List 10 | Syntéza — tabulka nástroj × kritérium s lokálními váhami, násobení váhou kritéria, součet po řádku | 4 nástroje × 8 kritérií |
| List 11 | Analýza citlivosti — změna váhy K1 nebo K8 (dle zadání vedoucího, `POZADAVKY_UCITELE.md`), přepočet ostatních vah tak, aby součet zůstal 1, a sledování, zda se změní vítěz | — |

Praktické tipy pro Excel:

- Geometrický průměr řádku: `=GEOMEAN(B2:I2)` (pro matici v B2:I9).
- Normalizace: podíl GM řádku / SUMA GM všech řádků.
- `Aw` (matice krát vektor vah) lze spočítat maticovou funkcí `=MMULT(matice; vahy)` nebo součtem součinů po řádcích.
- CR pod 0,1 zvýrazněte podmíněným formátováním (zelená/červená) — hned je
  vidět, které matice je třeba přehodnotit.
- Do listu 10 (syntéza) doporučeno propojit vzorci na listy 2–9 (odkaz na
  buňku s váhou), ne přepisovat čísla ručně — při změně jedné matice se pak
  automaticky přepočítá vše až po finální pořadí, což se hodí i pro list 11
  (citlivost).

## 7. Dva scénáře podle zadání vedoucího

Podle `POZADAVKY_UCITELE.md`: dva modelové scénáře se liší jen ve váhách
kritérií K1–K8 (matice alternativ pro každé kritérium zůstávají stejné —
mění se jen to, jak moc na daném kritériu záleží):

- **Scénář A — malá firma / cykloservis**: vyšší váha K2 Použitelnost a
  K8 Náklady.
- **Scénář B — střední firma / výrobní**: vyšší váha K1 Funkcionalita a
  K3 Kompatibilita.

V Excelu to znamená mít **dvě verze Listu 1** (dvě různé matice kritérií
K1–K8, každá s jinými poměry ve prospěch daných kritérií), zbytek (Listy
2–9 s hodnocením nástrojů) je pro oba scénáře stejný — mění se jen váhy,
kterými se násobí ve Listu 10.
