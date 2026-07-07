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

Prohlašuji, že jsem tuto práci vypracoval samostatně a uvedl jsem všechny použité prameny a literaturu.

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

V práce se zaměřuje na teoretická a metodická východiska porovnání nástrojů pro návrh a vývoj databázových systémů s využitím metody vícekriteriálního rozhodování AHP (Analytic Hierarchy Process). Na začátku jsou vysvětleny základní pojmy z oblasti databázových systémů a popsány jednotlivé fáze návrhu databáze. Zároveň jsou vysvětleny datové modely používané při návrhu, a dále pak relační model, na který se entitně-relační převádí. Další část je věnována vícekriteriálnímu rozhodování, vymezení pojmů alternativa, kritérium a váha kritéria. Následuje podrobný rozbor metody AHP, hlavně párového porovnávání, Saatyho škály a kontroly konzistence. V poslední kapitole se pak práce věnuje porovnáváným nástrojům, navrhuje hodnoticí kritéria a ukazuje na co se zaměřit v praktické části. Výstupem práce je teoretický a metodický základ, na který přímo naváže praktická část práce.

**Klíčová slova:** databázový systém, návrh databází, datové modelování, vícekriteriální rozhodování, Analytic Hierarchy Process.

&nbsp;

# Abstract

**Title:** Comparison of Database Design and Development Tools Using AHP – Theoretical Background

The thesis focuses on the theoretical and methodological foundations for comparing tools used in the design and development of database systems, employing the multi-criteria decision-making method AHP (Analytic Hierarchy Process). First, basic concepts from the field of database systems are explained, and the individual phases of database design are described. At the same time, the data models used in the design are clarified, namely the entity-relationship model and the relational model, to which the entity-relationship model is converted. Another part is devoted to multi-criteria decision-making, defining the terms alternative, criterion, and criterion weight. This is followed by a detailed analysis of the AHP method, focusing mainly on pairwise comparisons, Saaty's scale, and consistency control. The final chapter addresses the tools to be compared, proposes evaluation criteria, and indicates what to focus on in the practical part. The outcome of the thesis is a theoretical and methodological foundation, which will be directly followed by the practical part.

**Keywords:** database system, database design, data modelling, multi-criteria decision making, Analytic Hierarchy Process.


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
<w:p><w:pPr><w:pStyle w:val="Nadpisobsahu"/></w:pPr><w:r><w:t>Obsah</w:t></w:r></w:p>
<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/><w:instrText xml:space="preserve"> TOC \o "1-3" \h \z \u </w:instrText><w:fldChar w:fldCharType="separate"/><w:t>Pole obsahu – ve Wordu klikněte do pole pravým tlačítkem a zvolte „Aktualizovat pole", případně stiskněte F9.</w:t><w:fldChar w:fldCharType="end"/></w:r></w:p>
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

