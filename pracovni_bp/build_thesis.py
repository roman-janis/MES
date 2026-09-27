from pathlib import Path
from fractions import Fraction
import json,re,hashlib,unicodedata

ROOT=Path(__file__).resolve().parents[1]
def read(p):return (ROOT/p).read_text(encoding='utf-8-sig')
def write(p,s):
    target=ROOT/p;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(s.rstrip()+'\n',encoding='utf-8')
def table(headers,rows):return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(str(x).replace('|','/') for x in row)+' |' for row in rows])
def f(x,n=4):return f'{x:.{n}f}'.replace('.',',')
original_notes=[]
def original(s):
    original_notes.append(s.strip())
    return ''  # Historické formulace jsou až v příloze 5, mimo současný výklad.

changes=[]
def replace(text,old,new,source):
    assert old in text,(source,old[:70]);changes.append({'source':source,'original':old,'replacement':new});return text.replace(old,new+original(old),1)
demo=json.loads(read('app/data/demo.json'));dr=json.loads(read('vypocty/demo_reference.json'));cr=json.loads(read('vypocty/control_reference.json'));control=json.loads(read('app/data/control.json'))
blocks=json.loads(read('vypocty/synteticke_testy.json'))

front='''# Univerzita Hradec Králové

Fakulta informatiky a managementu  
Katedra informatiky a kvantitativních metod

# Komparace nástrojů pro návrh a vývoj databázových systémů pomocí AHP

**Bakalářská práce – pracovní verze se syntetickými daty**

Autor: Roman Janiš  
Studijní program: Aplikovaná informatika  
Specializace: Softwarové inženýrství  
Vedoucí práce: Ing. et Ing. Martin Lněnička, Ph.D.  
Hradec Králové, 2026  
Pracovní zpracování: 27. 9. 2026

> **Stav dokumentu:** Souvislý pracovní text, skutečně vytvořená a lokálně zkoušená PHP aplikace, kontrolní sešity a vypočtené syntetické hodnocení. Testy čtyř databázových nástrojů v této verzi provedeny nebyly. Číselné výsledky jejich hodnocení nejsou empirickým zjištěním. Před odevzdáním se musí nahradit vstupy, přepočítat výsledky a upravit také slovní interpretace, abstrakt a závěr. Dokument zatím není finální odevzdávanou verzí.

> **Zachování původního textu:** Kapitoly 4–6 jsou převzaty ze souborů BP beze změny vět. Kapitola 7 je zachována s označenými změnami vět o plánovaných verzích. Původní část kapitoly 8 je zachována a doplněna podrobnějším vymezením. U upravených převzatých pasáží je původní text uveden v hranatých závorkách. Nové praktické kapitoly nemají předchozí znění. Srovnávací poznámky se nezahrnou do finální sazby.

# Prohlášení a zadání práce

Prohlašuji, že jsem tuto bakalářskou práci vypracoval samostatně a uvedl jsem všechny použité prameny a literaturu. V případě využití nástrojů umělé inteligence jsem plně deklaroval způsob jejich využití při vypracování této práce.

V Hradci Králové dne …………………………

…………………………  
vlastnoruční podpis

> Prohlášení je připraveno podle fakultní šablony pro bakalářskou práci. Skutečné datum a podpis doplní autor až při dokončení a potvrzení prohlášení. Rozsah použití AI je uveden v oddílu 3.4. Platný podklad ze STAGu ze dne 23. 9. 2026 je připojen v příloze 4; závazné znění zadání přebírá tato práce ze souboru CIL_BP.md.

# Abstrakt

Práce se zabývá návrhem a implementací webové aplikace pro podporu výběru nástrojů určených pro návrh a vývoj databázových systémů pomocí metody AHP. Teoretická část vymezuje databázové systémy, datové modelování a vícekriteriální rozhodování. Praktická část popisuje hodnoticí kritéria, datový návrh aplikace, výpočet geometrických vah a kontrolu konzistence párových porovnání. Aplikace v jazyce PHP umožňuje využít připravené i vlastní položky, zadat preference, vypočítat pořadí a uložit hodnocení. Výpočty byly porovnány s nezávislým kontrolním skriptem a tabulkovými vzorci. Demonstrace používá modelový případ Cykloservis, čtyři nástroje, osm kritérií a tři samostatné změny důležitosti kritérií. V této pracovní verzi jsou produktová hodnocení syntetická. Výsledné pořadí proto dokládá postup zpracování vstupů, nikoli skutečnou vhodnost porovnávaných produktů. Diskuse vymezuje omezení řešení a podmínky nahrazení zkušebních údajů reálnými testy.

Klíčová slova: databázový systém, návrh databází, datové modelování, AHP, párové porovnávání, PHP.

# Abstract

This thesis presents the design and implementation of a web application supporting the selection of database system design and development tools using the Analytic Hierarchy Process. The theoretical part introduces database systems, data modelling and multi-criteria decision making. The practical part describes evaluation criteria, application data structures, geometric-mean priority calculation and consistency assessment. The PHP application supports predefined and custom items, pairwise comparisons, ranking and evaluation export. Calculations were compared with an independent reference script and spreadsheet formulas. The demonstration uses a bicycle service case, four tools, eight criteria and three separate changes in criterion importance. Product evaluations in this working version are synthetic. The resulting ranking therefore demonstrates the processing workflow and does not establish the actual suitability of the products. The discussion outlines limitations and the steps required to replace synthetic inputs with evidence from real tests.

Keywords: database system, database design, data modelling, AHP, pairwise comparison, PHP.
'''
oldabstract=read('BP 0.md').split('# Anotace\n\n')[1].split('\n\nKlíčová slova:')[0]
front=front.replace('\n# Abstract\n',original(oldabstract)+'\n# Abstract\n')
ch1=read('BP 1.md').strip()
old='Tato práce se proto zaměřuje na přípravu teoretických východisek pro porovnání nástrojů pro návrh a vývoj databází.'
ch1=replace(ch1,old,'Tato bakalářská práce se proto zaměřuje na vytvoření webové aplikace, která podpoří výběr nástroje pro návrh a vývoj databázových systémů.', 'BP 1.md')
old=ch1.split('\n\n')[-1]
ch1=replace(ch1,old,'Teoretická část práce vychází z dříve zpracované seminární práce. Na vymezení databázových systémů, datových modelů a metody AHP navazuje návrh hodnoticích kritérií a vlastní aplikace. V praktické části je popsána implementace, ověření výpočtů a demonstrace na modelovém případu Cykloservis. Pracovní demonstrace používá syntetická data, která umožňují připravit celý postup zpracování. Skutečné vlastnosti nástrojů a jejich vhodnost pro daný případ musí být posouzeny až po provedení jednotných testů.','BP 1.md')

approved=read('CIL_BP.md').split('## Cíl práce\n')[1].split('\n## Osnova')[0].strip()
ch2='''# 2 Cíl práce a výzkumné otázky

'''+approved+'''

Hlavní cíl je rozpracován do následujících dílčích cílů:

- vymezit teoretická východiska návrhu databází a rozhodování metodou AHP;
- konkretizovat kritéria K1–K8 a čtyři porovnávané nástroje;
- stanovit jednoznačný výpočetní postup a datovou strukturu hodnocení;
- vytvořit aplikaci s připravenými i vlastními položkami a párovými porovnáními;
- ověřit výpočty a obsluhu vstupů na kontrolních případech;
- demonstrovat použití na jednom modelovém případu a posoudit tři změny vah;
- zhodnotit přínos, omezení a možnosti dalšího rozvoje.

Výzkumné a návrhové otázky vyjadřují, co má být před dokončením práce doloženo:

- **VO1:** Jak vymezit kritéria pro výběr nástroje pro návrh a vývoj databázových systémů tak, aby se jejich význam zbytečně nepřekrýval?
- **VO2:** Jak implementovat párové porovnávání, výpočet priorit a kontrolu konzistence tak, aby byl výsledek dohledatelný a nezávisle kontrolovatelný?
- **VO3:** Jak se při použití aplikace na modelovém případu projeví rozdílné preference a tři samostatné změny významu kritérií?

Na první otázku navazuje vymezení kritérií a protokolu. Druhá otázka je řešena návrhem a ověřením aplikace. Třetí otázka je v této pracovní verzi zpracována na syntetických vstupech; věcný závěr o nástrojích bude možný až po jejich skutečném testování. Cílem není nalézt univerzálně nejlepší produkt bez ohledu na potřeby rozhodovatele.
'''+original(read('BP 2.md').split('\n',1)[1])
parts=read('BP 3.md').strip().split('\n\n')
ch3='\n\n'.join(parts)
old=parts[4]
new='Na základě prostudovaných zdrojů byly vybrány nástroje a navržena hodnoticí kritéria. Pro jejich následné skutečné testování je připraven jednotný protokol modelového případu. V této pracovní verzi jsou pomocné známky a párové preference nahrazeny dvěma oddělenými syntetickými sadami. Údaje neslouží k doložení vlastností produktů, ale k přípravě a ověření jejich zpracování v aplikaci a v kontrolním sešitu.'
ch3=replace(ch3,old,new,'BP 3.md')
old=parts[-1];new='Pro provádění výpočtů, práci s hodnoticími maticemi a prezentaci výsledků byla vytvořena jednoduchá webová aplikace v PHP. Její rozsah, výpočetní postup a provedené zkoušky jsou popsány v praktické části.'
ch3=replace(ch3,old,new,'BP 3.md')
old=parts[5]
new='Porovnávání vstupních preferencí je v aplikaci provedeno metodou AHP. Volba této metody vychází z možnosti propojit kvantitativní a kvalitativní kritéria v jednom hierarchickém modelu a kontrolovat vzájemnou konzistenci párových úsudků (Ishizaka a Labib, 2011; Moreno-Jiménez a Vargas, 2018; Velasquez a Hester, 2013). V této pracovní verzi byl celý výpočetní postup demonstrován na syntetických vstupech. Skutečná komparace vlastností nástrojů bude doplněna po provedení jednotných testů.'
ch3=replace(ch3,old,new,'BP 3.md')
ch3+='''

## 3.1 Postup vývoje a ověření

Praktická část byla připravována v pořadí specifikace, kontrolní příklad, implementace a ověření. Nejprve byly jednoznačně stanoveny povolené vstupy, způsob normalizace, výpočet konzistence a zacházení s chybami. Malý příklad se třemi kritérii byl přepočten nezávislým skriptem. Následně vznikl sešit s viditelnými vzorci a až poté PHP implementace. Tím byl omezen postup, ve kterém by se kontrolní hodnoty dodatečně přizpůsobovaly již vytvořenému programu.

Ověření obsahuje porovnání mezivýsledků i výsledných priorit. Vedle platných matic jsou zkoušeny chybné vstupy a záměrně nekonzistentní preference. Uživatelský průchod je ověřen požadavky HTTP a samostatnou automatizovanou zkouškou v prohlížeči. Vývojové ověření je v textu odlišeno od osobního kontrolního přepočtu autora a od případného posouzení vedoucím práce. Tyto pozdější kontroly nejsou předem prohlašovány za provedené.

## 3.2 Postup hodnocení nástrojů

Pro věcné hodnocení je stanoven jeden modelový případ. V každém nástroji má být podle stejného zadání vytvořen nový model, provedeno generování DDL, zpětné načtení referenční databáze a ověřeny možnosti přenosu modelu. Zápis zahrnuje pozorovaný stav, postup, případné omezení a důkaz. Praktické pozorování se odděluje od informace deklarované v dokumentaci. Pomocná známka 1–5 je pouze součástí záznamu a nestává se automaticky poměrem na Saatyho škále.

Hodnotitelem při následném skutečném srovnání bude autor práce. Jedná se o omezení, protože předchozí zkušenosti a osobní preference mohou ovlivnit zejména použitelnost. Nejde o dotazníkové šetření ani o skupinovou AHP. Vhodnost nástroje bude posuzována pro zadanou situaci a přesnou edici, nikoli obecně pro všechny možné způsoby používání.

## 3.3 Pracovní syntetická data

Syntetické vstupy byly vytvořeny výslovně pro přípravu zpracování. Při jejich generování nebyly provedeny testy databázových nástrojů. Náhodné hodnoty jsou označeny ve vstupních souborech, sešitu, aplikaci i v příslušných částech textu. Při nahrazení skutečnými údaji se budou měnit nejen tabulky, ale také jejich interpretace a závěr. Reprodukovatelnost zajišťuje uložený generátor s pevným inicializačním číslem a úplné vstupní matice.

## 3.4 Využití umělé inteligence

Při přípravě této pracovní verze byl dne 27. 9. 2026 použit nástroj OpenAI Codex. V uložených metadatech zpracování je model označen identifikátorem gpt-6-astra. Tento identifikátor je doložen polem model v záznamu turn_context původního běhu z 27. 9. 2026; jde o dostupné označení modelu, nikoli o údaj o interní revizi jeho vah. AI byla využita pro audit místních podkladů, návrh datové a výpočetní struktury, vytvoření PHP aplikace, kontrolních skriptů a sešitů, generování označených syntetických dat a sestavení nových praktických kapitol. Původní teoretické pasáže byly převzaty ze souborů BP; změny převzatých vět jsou označeny původním zněním.

Vygenerovaný kód a výpočty byly kontrolovány automatickými zkouškami a přepočtem ve více výpočetních prostředích. Tyto kroky nejsou zaměňovány za osobní nezávislou kontrolu autora. Před odevzdáním musí být výstupy kriticky posouzeny, matematika ručně ověřena, syntetické produktové hodnoty nahrazeny skutečnými testy a aktualizována evidence případného dalšího využití AI. Zde popsaný rozsah je záměrně širší než jazyková korektura, protože AI podstatně přispěla také k implementaci a k nové praktické části textu.
'''

theory=[read(f'BP {i}.md').strip() for i in [4,5,6]]
theory[-1]+='''

## 6.4 Výpočetní postup použitý v této práci

Pro vlastní implementaci je z uvedených postupů zvolena metoda geometrického průměru řádků. Každý řádkový geometrický průměr je normalizován součtem geometrických průměrů všech řádků. Stejný postup je použit pro váhy kritérií i lokální priority alternativ, v PHP aplikaci, kontrolním sešitu i nezávislém referenčním výpočtu. Metoda vlastního vektoru je v předchozím výkladu uvedena jako teoretický postup AHP; v této aplikaci není algoritmem pro stanovení vah (Ishizaka a Labib, 2011).

Pro kontrolu konzistence je z geometrických vah vypočten průměr poměrů (Aw)_i/w_i. V další části práce je tato hodnota označována jako odhad λ. U obecné nekonzistentní matice nemusí být přesně rovna dominantnímu vlastnímu číslu λ_max. Ukazatele CI a CR jsou v implementaci odvozeny z tohoto odhadu. Porovnání s jiným nástrojem proto musí rozlišit shodu algoritmů od rozdílu způsobeného použitím vlastního vektoru nebo přesného vlastního čísla (Ishizaka a Labib, 2011; Tomeš a Alcnauer, 2014). Konkrétní vzorce, RI, výjimky pro rozměry 1 a 2 a tolerance jsou vymezeny v oddílu 9.3.
'''

ch7=read('BP 7.md').strip()
for sentence in re.findall(r'Pro účely navazující práce bude testována[^\n]+',ch7):
    ch7=replace(ch7,sentence,'Přesná verze a edice použitá při praktickém testování bude doložena v testovacím protokolu. V syntetické demonstraci není žádná verze označena za skutečně otestovanou.','BP 7.md')
ch7+='\n\n[Pracovní poznámka: charakteristiky a historická data citování v této kapitole jsou zachovány ze seminární práce. Nepředstavují nový audit produktových funkcí k 27. 9. 2026. Před empirickou interpretací je potřeba zkontrolovat funkce a licence přesně testovaných edic.]\n'
bp8=read('BP 8.md');ch8=re.split(r'\n---\s*\n',bp8,maxsplit=1)[0].strip()
ch8=replace(ch8,'návrh a vývoj databáze. nikoli','návrh a vývoj databáze, nikoli','BP 8.md')
draft=bp8.split('## 8 Návrh hodnoticích kritérií')[1]
detail=draft[draft.index('| Kritérium | Název | Vymezení kritéria'):draft.index('Tabulka 2:')].strip()
old_table=ch8[ch8.index('| Kritérium | Název | Význam pro hodnocení |'):ch8.index('<span id=')].strip()
rows=[line.split('|')[1:-1] for line in detail.splitlines()[2:]]
compact=table(['Kritérium','Název','Význam pro hodnocení'],[[r[0].strip(),r[1].strip(),r[2].strip()] for r in rows])
ch8=replace(ch8,old_table,compact,'BP 8.md – tabulka 2')
ch8+='\n\n## 8.1 Vymezení kritérií a způsob posouzení\n\nTabulka 2 je závazným vymezením kritérií pro aplikaci i modelový případ. K1 zahrnuje modelování, nikoli generování DDL nebo reverse engineering. V K3 se pro každý DBMS rozlišuje podpora modelování, forward a reverse engineeringu; samotné připojení není dostatečné. K4 a K5 hodnotí kvalitu konkrétního převodu, zatímco K3 hodnotí rozsah podporovaných DBMS. Tentýž úspěšný DDL export se znovu neboduje v K7.\n\n'+table(['Kritérium','Název','Charakter posouzení'],[[r[0].strip(),r[1].strip(),r[3].strip()] for r in rows])+'\n\nCharakter posouzení neurčuje váhu kritéria. Váhy jsou samostatným vyjádřením preferencí rozhodovatele.\n\n'
more=draft[draft.index('### 8.1 Vazba'):].replace('### 8.1','## 8.2').replace('### 8.2','## 8.3')
ch8+=more

practical=read('pracovni_bp/text_prakticka_cast.md')
ct=table(['Ukazatel','Přepočtená hodnota'],[(f'Váha {x}',f(v,10)) for x,v in zip(['F','P','C'],cr['criteria']['weights'])]+[('CR kritérií',f(cr['criteria']['cr'],10))]+[(f'Priorita {x}',f(v,10)) for x,v in zip(['A1','A2','A3'],cr['scores'])])
kt=table(['Kód','Kritérium','Váha','CR alternativ'],[(x['id'],x['name'],f(dr['criteria']['weights'][k]),f(dr['local'][k]['cr'])) for k,x in enumerate(demo['criteria'])])
lt=table(['Alternativa']+[x['id'] for x in demo['criteria']],[(a['name'],*[f(dr['local'][k]['weights'][i]) for k in range(8)]) for i,a in enumerate(demo['alternatives'])])
order=sorted(range(4),key=lambda i:-dr['scores'][i])
rt=table(['Pořadí','Alternativa','Globální priorita'],[(rank+1,demo['alternatives'][i]['name'],f(dr['scores'][i])) for rank,i in enumerate(order)])
st=table(['Alternativa','Základ','K8 ×2','K1 ×2','K3 ×2'],[(a['name'],f(dr['scores'][i]),*[f(v['scores'][i]) for v in dr['sensitivity']]) for i,a in enumerate(demo['alternatives'])])
sc=[]
for v in dr['sensitivity']:
    k=next(i for i,x in enumerate(demo['criteria']) if x['id']==v['criterion']);o=sorted(range(4),key=lambda i:-v['scores'][i]);same=o==order
    sc.append(f"Při zesílení {v['criterion']} se jeho váha změnila z {f(dr['criteria']['weights'][k])} na {f(v['weights'][k])}. "+('Pořadí všech čtyř alternativ zůstalo stejné.' if same else 'Pořadí se změnilo.')+f" První alternativa {demo['alternatives'][o[0]]['name']} dosáhla priority {f(v['scores'][o[0]])}. Jde o důsledek syntetických preferencí, nikoli o zjištěnou vlastnost produktu.")
values={'CONTROL_TABLE':ct,'CRITERIA_TABLE':kt,'LOCAL_TABLE':lt,'RANKING_TABLE':rt,'SENSITIVITY_TABLE':st,'SENSITIVITY_COMMENT':'\n\n'.join(sc),'CRITERIA_COMMENT':f"V demonstračním běhu mají shodnou nejvyšší váhu K1, K3 a K6, přibližně {f(dr['criteria']['weights'][0])}. Nejnižší váha připadá K4 ({f(dr['criteria']['weights'][3])}). CR matice kritérií činí {f(dr['criteria']['cr'])}. Toto rozložení je výsledkem generátoru; není vydáváno za zdůvodněné skutečné priority vývojáře.",'RANKING_COMMENT':f"V syntetickém výpočtu je první {demo['alternatives'][order[0]]['name']} s prioritou {f(dr['scores'][order[0]])}. Rozdíl vůči druhé alternativě činí {f(dr['scores'][order[0]]-dr['scores'][order[1]])}. Tento náskok vzniká kombinací zadaných lokálních priorit a vah. Nepředstavuje měřený rozdíl kvality produktů a neopravňuje k jejich praktickému doporučení."}
for k,v in values.items():practical=practical.replace('{{'+k+'}}',v)
assert '{{' not in practical

# Bibliografie: zapracovat připravené opravy z auditu, zachovat původní znění v poznámkách.
bib=read('BP 10.md').split('\n---\n',1)[0].split('\n\n')[1:];bib=[x.strip() for x in bib if x.strip()]
bibnotes=[]
def sortkey(x):return unicodedata.normalize('NFKD',x).encode('ascii','ignore').decode().upper()
bib.sort(key=sortkey)
bibliography='# Seznam zdrojů\n\n'+'\n\n'.join(bib)


appendix='# Přílohy\n\n## Příloha 1 – Úplné matice syntetického běhu\n\nVšechny následující matice jsou syntetické. Pořadí alternativ: OSDM, DBEAVER, MYSQL, PGMODELER. Zlomky jsou uvedeny přesně na Saatyho škále.\n\n'
def matrix_table(m,labels):return table(['Prvek']+labels,[[labels[i]]+[str(Fraction(v).limit_denominator(9)) for v in row] for i,row in enumerate(m)])
appendix+='### Kritéria\n\n'+matrix_table(demo['criteria_matrix'],[x['id'] for x in demo['criteria']])+'\n\n'
for k,m in enumerate(demo['alternative_matrices']):appendix+='### '+demo['criteria'][k]['id']+'\n\n'+matrix_table(m,[x['id'] for x in demo['alternatives']])+'\n\n'
appendix+='## Příloha 2 – Kontrolní vstupní matice\n\n'+matrix_table(control['criteria_matrix'],['F','P','C'])+'\n\n'
for k,m in enumerate(control['alternative_matrices']):appendix+='### Alternativy vzhledem ke kritériu '+['F','P','C'][k]+'\n\n'+matrix_table(m,['A1','A2','A3'])+'\n\n'
appendix+='''## Příloha 3 – Elektronické součásti a návod k navázání

| Součást | Umístění | Účel |
|---|---|---|
| Aplikace | app/ | PHP zdrojové kódy, připravená data, spuštění |
| Specifikace AHP | vypocty/AHP_SPECIFIKACE.md | Jednoznačný algoritmus a akceptace |
| Kontrolní sešit | vypocty/kontrolni_priklad.xlsx | Malý přepočitatelný příklad |
| Syntetické hodnocení | outputs/bp_20260927/hodnoceni_synteticke.xlsx | 51 bloků, matice, priority, citlivost |
| Vstupy demonstrace | app/data/demo.json | Úplné reprodukovatelné preference |
| Protokoly | protokoly/ | Označené syntetické záznamy a plán skutečných důkazů |
| Ověření | vypocty/PROTOKOL_KONTROLNI_VYPOCET.md | Skutečně provedené kontroly a jejich omezení |

Při navázání skutečnými výsledky zkopírovat pracovní sešit, doplnit důkazy a nahradit syntetické známky. Poté samostatně vytvořit a zdůvodnit Saatyho matice. Do aplikace lze přenést JSON; výpočty musejí vycházet ze stejných matic jako Excel. Po přepočtu aktualizovat všechny výsledkové tabulky, slovní komentáře, abstrakt a závěr. Odstranit pracovní srovnávací poznámky až po autorské kontrole změn.

## Příloha 4 – Zadávací list

Závazné zadání je uvedeno v CIL_BP.md, který je přepisem platného podkladu VŠKP z IS/STAG. Podklad byl exportován 23. 9. 2026 ve 20:40; student potvrdil jeho platnost v systému. Starší soubory ve složce zadani se pro tuto práci nepoužívají.

[Platný podklad VŠKP z IS/STAG, 23. 9. 2026](oliva/temata_vskp_-_podklady_pro_zadani_vskp.pdf)

![Podklad VŠKP ze systému IS/STAG](outputs/bp_20260927/zadani_stag.png)
'''

body='\n\n'.join([ch1,ch2,ch3,*theory,ch7,ch8,practical])
headings=re.findall(r'^(#{1,3}) (\d+(?:\.\d+)* .+)$',body,re.M)
contents='# Obsah\n\n'+'\n'.join('  '*(len(h)-1)+'- '+title for h,title in headings)+'\n- Seznam zdrojů\n- Přílohy\n'
tables=re.findall(r'^(?:<[^\n]*?>)?(Tabulka \d+: .+)$',body,re.M)
front+='\n'+contents+'\n# Seznam tabulek a obrázků\n\n'+'\n\n'.join(tables)+'\n\nObrázek 1: Úvodní stránka aplikace\n\nObrázek 2: Výsledek syntetického příkladu\n'
history='## Příloha 5 – Srovnání původního textu, pouze pro autorskou revizi\n\nNásledující bloky nejsou současnou metodikou ani součástí finální sazby. Zachovávají přesné původní pasáže pro porovnání.\n\n'
for i,note in enumerate(original_notes,1):
    history+=f'### Změna {i}\n\n---\n\n[Pracovní poznámka – původní znění před úpravou, 27. 9. 2026; důvod: návaznost na platné zadání nebo odstranění rozporu.\n\n{note}\n]\n\n'
write('bakalarsa_prace.md',front+'\n\n'+body+'\n\n'+bibliography+'\n\n'+appendix+'\n\n'+history)
write('pracovni_bp/zmeny_prevzateho_textu.json',json.dumps(changes,ensure_ascii=False,indent=2))
write('pracovni_bp/bibliografie.json',json.dumps(bib,ensure_ascii=False,indent=2))
clean=re.sub(r'\[Pracovní poznámka.*?\n\]', '',body,flags=re.S)
stats={'body_characters_without_original_notes':len(clean),'bibliography_count':len(bib),'original_chapters_4_6_present_verbatim':all(t in body for t in theory),'tables':len(tables),'headings':len(headings)}
write('pracovni_bp/thesis_stats.json',json.dumps(stats,ensure_ascii=False,indent=2));print(stats)

# Přehled důkazů a 51 syntetických bloků mimo vlastní text.
protocol='# Syntetický protokol – 27. 9. 2026\n\n**Všech 204 známek je náhodných. Žádný z uvedených testů tímto záznamem není doložen jako provedený.**\n\nZnámky: 1 nejlepší, 5 nejhorší. Zdroj úloh: původní hodnoceni_4_nastroju.xlsx. AHP preference jsou samostatně generované vstupy; nejsou převodem známek.\n\n'
for b in blocks:
    protocol+='## '+b['title']+'\n\nKritérium: '+b['criterion']+'\n\n**Úloha:** '+b['task']+'\n\n**Očekávání ze zadání:** '+b['expected']+'\n\n'+table(['OSDM','DBEAVER','MYSQL','PGMODELER'],[b['scores']])+'\n\n**Stav:** SYNTETICKÉ – neprovedeno. **Důkaz:** žádný.\n\n**Co uložit při skutečném testu:** '+str(b['evidence'])+'\n\n'
write('protokoly/SYNTETICKY_PROTOKOL.md',protocol)
write('protokoly/K_OPERACIONALIZACE.md','# Operacionalizace K1–K8\n\n'+detail+'\n\n'+more+'\n\nV tomto běhu byly připraveny pouze syntetické hodnoty. Skutečné testy čekají na provedení.\n')
write('protokoly/README.md','''# Protokoly

SYNTETICKY_PROTOKOL.md obsahuje 51 převzatých úloh a 204 zkušebních známek. Testy nebyly provedeny. K_OPERACIONALIZACE.md vymezuje osm kritérií a vazbu na úlohy.

Před skutečnými testy založte pro každou přesnou edici záznam verze, OS, data, licence, ceny a odkazů. Přidejte vlastní postup, skutečný výsledek a cestu k důkazu. Původní sešit obsahuje i starší vyplněné známky nejednoznačného původu; tento běh je nepřevzal jako ověřené.
''')
