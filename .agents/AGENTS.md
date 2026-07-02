# AGENTS.md

Pracovní kontext a pravidla pro AI asistenty (Antigravity). Složka není kódový projekt, ale pracovní adresář pro seminární a následně bakalářskou práci.

## Aktuální hlavní soubory

- `Seminární práce.docx` - aktuální Word dokument pro kontrolu, vedoucího a odevzdání.
- `Seminární práce.md` - zdrojová Markdown verze seminární práce.
- `PŘEHLED.md` - mapa složky a stav projektu.
- `PLAN.md` - plán dalších kroků.
- `ZDROJE.md` - literatura, zdroje a poznámky k citacím.

Staré pracovní soubory `Bakalářská práce.docx`, `Bakalářská práce.md` a `Seminární práce.txt` byly odstraněny.

## Téma

**Komparace nástrojů pro návrh a vývoj databázových systémů pomocí AHP**

Hlavní oblasti:

1. Databázové systémy, datové modelování, ER/EER, relační model, normalizace.
2. Vícekriteriální rozhodování a metoda AHP.
3. Praktická komparace nástrojů v navazující bakalářské práci.

## Porovnávané nástroje

- MySQL Workbench
- Oracle SQL Developer Data Modeler
- DBeaver Community Edition
- pgModeler

## Důležitá pravidla

- Pracovat česky a akademickým stylem.
- Citace držet podle ISO 690:2022.
- Pro seminární práci neupravovat praktickou část do podoby hotové komparace; má jít hlavně o teoretický a metodický základ.
- Před odevzdáním kontrolovat shodu citací v textu a seznamu zdrojů.

## Struktura kapitol a vrstev v MD souborech

Kapitolové soubory (`Seminární práce <N>.md`, 0–11) mají specifickou strukturu textových bloků oddělených `---`. Každý blok obsahuje dvě vrstvy oddělené `****`:

1. **Vrstva 1 (nad prvním `****`):** Finální, stylisticky a jazykově vyhlazená akademická verze textu. Citace jsou sloučené na koncích odstavců (např. `(ZdrojA; ZdrojB)`), aby text plynule navazoval.
2. **Vrstva 2 (mezi prvním a druhým `****`):** Pracovní a verifikační verze. Citace jsou striktně rozděleny přímo za jednotlivé věty, pro které platí (věta po větě). Tato vrstva se skriptem `extrahuj.ps1` ukládá do verzí s příponou `x` (např. `Seminární práce 6x.md`) a slouží k sestavení finální kontrolované verze.
3. **Zdrojové úryvky (pod druhým `****`):** Doslovné citáty z cizojazyčného originálu literatury, které slouží jako věcný podklad pro obě vrstvy.

