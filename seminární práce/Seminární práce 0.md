# Univerzita Hradec Králové

## Fakulta informatiky a managementu

### Katedra informatiky a kvantitativních metod

&nbsp;

&nbsp;

&nbsp;

# Komparace nástrojů pro návrh a vývoj databázových systémů pomocí AHP

## Teoretická a metodická východiska

&nbsp;

Práce v předmětu KRCR-MES Metodologický seminář

&nbsp;

&nbsp;

| | |
|---|---|
| **Autor:** | Roman Janiš |
| **Osobní číslo:** | I2400792 |
| **Studijní program:** | B0613A140033 Aplikovaná informatika |
| **Specializace:** | Softwarové inženýrství |
| **Vedoucí práce:** | Ing. et Ing. Martin Lněnička, Ph.D. |
| **Pracoviště vedoucího:** | Katedra informatiky a kvantitativních metod |

&nbsp;

&nbsp;

Hradec Králové, červen 2026


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Prohlášení

Prohlašuji, že jsem tuto práci vypracoval samostatně a uvedl jsem všechny použité prameny a literaturu. V případě využití nástrojů umělé inteligence jsem plně deklaroval(a) způsob jejich využití při vypracování této práce.

&nbsp;

&nbsp;

V Hradci Králové dne ………………………… &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ……………………………………

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Roman Janiš


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Poděkování

Tímto bych rád poděkoval vedoucímu práce Ing. et Ing. Martinu Lněničkovi, Ph.D., za odborné vedení, věcné připomínky a konzultace, které přispěly ke zpracování této práce.


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Abstrakt

Práce představuje teoretická a metodická východiska porovnání nástrojů pro návrh a vývoj databázových systémů s využitím metody vícekriteriálního rozhodování AHP (Analytic Hierarchy Process). V první části jsou vymezeny základní pojmy z oblasti databázových systémů, popsány fáze návrhu databáze a vysvětleny datové modely používané při návrhu, zejména entitně-relační model a model relační. Druhá část je věnována vícekriteriálnímu rozhodování, vymezení pojmů alternativa, kritérium a váha kritéria a podrobnému výkladu metody AHP, včetně párového porovnávání, Saatyho škály a kontroly konzistence. Třetí část představuje nástroje, které budou předmětem navazující praktické komparace v bakalářské práci, navrhuje hodnoticí kritéria a popisuje metodický rámec dalšího postupu. Výstupem práce je teoretický a metodický základ, na který naváže praktická část práce.

**Klíčová slova:** databázový systém, návrh databází, datové modelování, vícekriteriální rozhodování, Analytic Hierarchy Process.

&nbsp;

# Abstract

This paper presents the theoretical and methodological background of a bachelor thesis focused on the comparison of tools for the design and development of database systems using the Analytic Hierarchy Process, a multi-criteria decision-making method. The first part defines fundamental terms related to database systems, describes the phases of database design and explains the data models used in design, in particular the entity-relationship model and the relational model. The second part addresses multi-criteria decision-making, defines the terms alternative, criterion and criterion weight, and provides a detailed explanation of the AHP method, including pairwise comparison, Saaty's scale and consistency checking. The third part introduces the tools that will be the subject of the follow-up practical comparison in the bachelor thesis, proposes evaluation criteria and describes the methodological framework of further work. The result is a theoretical and methodological foundation on which the practical part of the bachelor thesis will directly build.

**Keywords:** database system, database design, data modelling, multi-criteria decision making, Analytic Hierarchy Process.


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
<w:p><w:pPr><w:pStyle w:val="Nadpisobsahu"/></w:pPr><w:r><w:t>Obsah</w:t></w:r></w:p>
<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/><w:instrText xml:space="preserve"> TOC \o "1-3" \h \z \u </w:instrText><w:fldChar w:fldCharType="separate"/><w:t>Pole obsahu – ve Wordu klikněte do pole pravým tlačítkem a zvolte „Aktualizovat pole", případně stiskněte F9.</w:t><w:fldChar w:fldCharType="end"/></w:r></w:p>
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

