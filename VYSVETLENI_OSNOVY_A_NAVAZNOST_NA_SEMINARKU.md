# Podrobné vysvětlení osnovy BP a návaznost na seminární práci

Tento dokument podrobně vysvětluje jednotlivé body navržené osnovy (Zásad pro vypracování) do IS/STAG, přesně vymezuje, co který bod obsahuje, a ukazuje, kde je použita již hotová teorie ze seminární práce a kde začíná nová praktická část.

---

## 1. Souhrnná tabulka: Co je hotová seminárka a co je nová praxe

| Bod osnovy do STAGu | Co přesně v tomto bodu bude | Návaznost na seminární práci vs. Nová část |
|---|---|---|
| **1. Vymezit problematiku návrhu relačních databází a charakterizovat vybrané nástroje s využitím teoretického základu seminární práce.** | **Čistá teorie databází a popis nástrojů:**<br>• Základní pojmy: data, databáze, DBMS, architektura ANSI/SPARC, schéma a instance.<br>• Fáze životního cyklu návrhu databáze: konceptuální, logický a fyzický návrh.<br>• Konceptuální modelování: ER a EER model dle Chena.<br>• Relační modelování: Coddův relační model, integritní omezení, relační operace a normalizace (1NF až BCNF).<br>• Charakteristika 4 vybraných nástrojů: Oracle SQL Developer Data Modeler, DBeaver Community Edition, MySQL Workbench Community Edition a pgModeler (historie, zaměření, licenční model). | **100 % HOTOVO ZE SEMINÁRKY**<br><br>Jedná se o hotové a vedoucím schválené kapitoly 4, 5 a 7 ze seminární práce. Není potřeba nic nového rešeršovat ani vymýšlet. Text se pouze stylisticky adaptuje pro potřeby BP (stane se z něj Kapitola 2). |
| **2. Popsat metodu AHP a zhodnotit existující softwarová řešení z hlediska použitelnosti a potřeb navrhované aplikace.** | **Čistá teorie AHP + stručná rešerše softwaru:**<br>• Principy vícekriteriálního rozhodování (MCDM), pojmy alternativa, kritérium, váha.<br>• Metoda Analytic Hierarchy Process (AHP) Thomase L. Saatyho: princip hierarchické dekompozice, Saatyho fundamentální stupnice 1–9, sestavení párových matic a vlastnost reciprocity.<br>• Výpočet priorit (metoda geometrického průměru řádků, normalizace vah), výpočet vlastního čísla $\lambda_{\max}$, indexu konzistence $CI$, tabulky náhodných indexů $RI$ a poměru konzistence $CR$ ($CR \le 0{,}10$).<br>• **Rešerše existujících řešení:** Stručné zhodnocení 2–3 stávajících kalkulátorů a excelových šablon (např. AHP-OS, Excel šablony) z hlediska jejich limitů (příliš technické, chybějící vysvětlení pro běžné uživatele, slabé varování při chybách – přesně dle pokynu vedoucího z e-mailu 13. 7.). | **85 % HOTOVO ZE SEMINÁRKY**<br><br>Celá teorie vícekriteriálního rozhodování a matematiky AHP je hotová z kapitoly 6 seminárky. Nově se pouze doplní cca 1–2 strany srovnání existujících šablon a programů jako zdůvodnění vzniku vlastní aplikace. |
| **3. Stanovit funkční a nefunkční požadavky na webovou aplikaci, připravenou sadu alternativ a hodnoticích kritérií.** | **Most mezi teorií a aplikací (specifikace zadání):**<br>• Seznam 8 hodnoticích kritérií K1–K8 (funkcionalita modelování, použitelnost, DBMS kompatibilita, forward engineering, reverse engineering, dokumentace/komunita, import/export, náklady a licence).<br>• Seznam 4 přednastavených nástrojů s popisy a odkazy na dokumentaci.<br>• Funkční požadavky na aplikaci: výběr položek, možnost zadat vlastní kritéria/alternativy, formulář párového srovnání, výpočet vah, zobrazení pořadí alternativ.<br>• Nefunkční požadavky: přehlednost, srozumitelná chybová hlášení při logických rozporech ($CR > 0{,}10$). | **50 % HOTOVO ZE SEMINÁRKY**<br><br>Kritéria K1–K8 a alternativy jsou hotové z kapitoly 8 seminární práce. Nově se pouze sepíší konkrétní požadavky na funkce a rozhraní webové aplikace. |
| **4. Navrhnout a implementovat webovou aplikaci v PHP včetně datového modelu, párového porovnávání, kontroly konzistence a výpočetního jádra.** | **Vývoj aplikace (programátorská část):**<br>• Datový návrh: struktura tabulek / JSON struktur pro ukládání kritérií, alternativ, matic hodnocení a výsledků.<br>• Architektura aplikace v PHP bez zbytečného frameworkového balastu (čisté PHP, jednoduché šablony, přehledné formulářové kroky).<br>• Implementace výpočetního algoritmu AHP (geometrický průměr řádků, normalizace, výpočet $\lambda_{\max}$, $CI$, $CR$). | **ZCELA NOVÁ ČÁST**<br><br>Vlastní programátorská realizace webové aplikace v PHP. |
| **5. Ověřit správnost výpočtů aplikace, zpracování neúplných či nekonzistentních vstupů a splnění stanovených požadavků.** | **Ověření a testování aplikace:**<br>• Matematická verifikace: srovnání výpočtů aplikace s publikovanými referenčními příklady Thomase Saatyho z literatury (důkaz pro komisi, že aplikace počítá přesně).<br>• Testování stability a chybových stavů: ověření, že při zadání nekonzistentní matice ($CR > 0{,}10$), neúplných polí nebo chybných znaků aplikace nespadne, ale zobrazí uživateli srozumitelné upozornění.<br>• Ošetření hraničních stavů matic (rozměr 1×1, 2×2, $RI = 0$). | **ZCELA NOVÁ ČÁST**<br><br>Doložení technické a výpočetní kvality aplikace a splnění požadavků vedoucího práce. |
| **6. Demonstrovat použití aplikace na modelovém scénáři výběru databázového nástroje pro malou firmu a provést tři změny vah kritérií pro posouzení citlivosti výsledku.** | **Praktická komparace a citlivost:**<br>• Modelový scénář: projekt „Cykloservis“ pro malou firmu (návrh databáze pro zakázky, zákazníky, díly a mechaniky bez předem určeného DBMS).<br>• Praktické ověření 4 nástrojů na tomto zadání (tvorba modelu, DDL, reverse engineering) a vytvoření věcných podkladů pro párové srovnání.<br>• Základní průchod aplikací: zadání preferencí scénáře do aplikace a zjištění vítězného nástroje.<br>• Analýza citlivosti: 3 samostatné změny preferencí (důraz na nízké náklady K8, důraz na modelování K1, důraz na podporu více DBMS K3) a vyhodnocení, jak se změnilo pořadí nástrojů. | **ZCELA NOVÁ ČÁST**<br><br>Praktická demonstrace aplikace na reálných datech a testovacím scénáři. |
| **7. Zhodnotit přínosy a omezení řešení a popsat možnosti dalšího rozvoje a rozšiřitelnosti aplikace.** | **Závěrečná diskuse a zhodnocení:**<br>• Diskuse dosažených výsledků: vliv subjektivity hodnotitele na výsledek AHP, omezení hodnocení jedním autorem.<br>• Rozšiřitelnost aplikace: popis a návrh toho, jak by se aplikace dala snadno přepnout na jinou rozhodovací doménu (např. výběr cloudové platformy, výběr CMS) díky oddělené datové struktuře (přesně dle pokynu vedoucího z 2. 9.).<br>• Shrnutí splnění cílů práce a zodpovězení výzkumných otázek. | **ZCELA NOVÁ ČÁST**<br><br>Závěrečné vyhodnocení, diskuse a výhled do budoucna. |

---

## 2. Proč je Bod 1 formulován právě takto a co přesně obsahuje?

V bodu 1 je uvedeno:  
> *„1. Vymezit problematiku návrhu relačních databází a charakterizovat vybrané nástroje s využitím teoretického základu seminární práce.“*

### Důvody této formulace:
1. **Akademický standard FIM UHK:** Bakalářská práce nemůže začít rovnou zdrojovým kódem v PHP. Musí nejprve prokázat studentovo porozumění oboru, ve kterém má aplikace pomáhat. Protože aplikace slouží pro výběr nástrojů na návrh databází, musí práce nejprve jasně vymezit, co to návrh relační databáze je a jaké nástroje se k němu používají.
2. **Plné využití hotové práce:** Slova *„s využitím teoretického základu seminární práce“* přímo v osnově oficiálně deklarují vedoucímu i komisi, že stavíte na již obhájeném a recenzovaném teoretickém základu z předmětu KRCR-MES.
3. **Co konkrétně tvoří obsah tohoto bodu v textu BP:**
   * **Úvod do databází:** Data vs. informace, pojem databáze, architektura DBMS ANSI/SPARC (úroveň interní, konceptuální, externí), schéma databáze vs. instance dat.
   * **Životní cyklus a fáze návrhu:** Konceptuální návrh (sběr požadavků a jejich strukturování), logický návrh (transformace do tabulek a vztahů), fyzický návrh (indexy, tabulkové prostory, konkrétní DBMS).
   * **Datové modelování:** Chenův entitně-relační model (entity, atributy, kardinality 1:1, 1:N, M:N), Coddův relační model (relace, relátory, primární a cizí klíče, referenční integrita, normalizace 1NF–BCNF).
   * **Čtyři vybrané nástroje:** Stručné představení Oracle SQL Developer Data Modeler, DBeaver Community Edition, MySQL Workbench Community Edition a pgModeler (pro koho jsou určeny, pod jakou licencí fungují a jaké platformy podporují).

---

## 3. Rozdělení celkového rozsahu bakalářské práce (cca 50 stran)

```
┌────────────────────────────────────────────────────────────────────────┐
│ TEORIE (cca 18–20 stran) — PŘEVZATO ZE SEMINÁRKY                      │
│ • Úvod a cíle (2 s.)                                                   │
│ • Návrh databází a charakteristika nástrojů [Bod 1 osnovy] (10–12 s.)  │
│ • Metoda AHP a existující řešení [Bod 2 osnovy] (6–8 s.)               │
├────────────────────────────────────────────────────────────────────────┤
│ PRAXE A APLIKACE (cca 28–32 stran) — ZCELA NOVÁ PRÁCE                  │
│ • Požadavky a návrh aplikace [Bod 3 osnovy] (6–8 s.)                   │
│ • Implementace v PHP a testování [Body 4 a 5 osnovy] (10–12 s.)        │
│ • Demonstrace Cykloservis a citlivost [Bod 6 osnovy] (10–12 s.)        │
│ • Diskuse, rozšiřitelnost a závěr [Bod 7 osnovy] (4–5 s.)              │
└────────────────────────────────────────────────────────────────────────┘
```

Tento poměr (cca 40 % teorie : 60 % vlastní praktická realizace a demonstrace) přesně odpovídá ideálnímu standardu odborné bakalářské práce na FIM UHK.
