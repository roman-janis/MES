"""Jednorázová migrace zdrojů 27. 9. 2026; nespouštět při běžném sestavení."""
from pathlib import Path
import json, re, hashlib
ROOT=Path(__file__).resolve().parents[1]
def read(p): return (ROOT/p).read_text(encoding='utf-8-sig')
def write(p,s): (ROOT/p).write_text(s.rstrip()+'\n',encoding='utf-8')
def change(s,old,new):
    assert old in s,old[:120]
    return s.replace(old,new,1)
s=read('pracovni_bp/build_thesis.py')
s=change(s,"def original(s):return '\\n\\n[Pracovní poznámka – původní znění před úpravou, 27. 9. 2026; důvod: návaznost na cíl BP nebo zpřesnění doloženého stavu.\\n\\n'+s.strip()+'\\n]\\n'", """original_notes=[]
def original(s):
    original_notes.append(s.strip())
    return ''  # Historické formulace jsou až v příloze 5, mimo současný výklad.
""")
s=change(s,"approved=read('EMAIL_KONVERZACE.md').split('Finální text pro vložení do Stagu:')[1].split('Cíl práce\\n')[1].split('\\n\\nOsnova')[0].strip()", "approved=read('CIL_BP.md').split('## Cíl práce\\n')[1].split('\\n## Osnova')[0].strip()")
s=change(s,"[Pracovní poznámka: před konečnou sazbou vložit aktuální znění prohlášení z oficiální fakultní šablony, doplnit skutečné datum a podpis a přiložit aktuální zadávací list ze STAGu. Tato pracovní verze nevytváří podpis ani neprohlašuje, že již proběhla osobní kontrola autora nebo vedoucího. Rozsah využití AI je popsán v kapitole 3.]", """Prohlašuji, že jsem tuto bakalářskou práci vypracoval samostatně a uvedl jsem všechny použité prameny a literaturu. V případě využití nástrojů umělé inteligence jsem plně deklaroval způsob jejich využití při vypracování této práce.

V Hradci Králové dne …………………………

…………………………  
vlastnoruční podpis

> Prohlášení je připraveno podle fakultní šablony pro bakalářskou práci. Skutečné datum a podpis doplní autor až při dokončení a potvrzení prohlášení. Rozsah použití AI je uveden v oddílu 3.4. Platný podklad ze STAGu ze dne 23. 9. 2026 je připojen v příloze 4; závazné znění zadání přebírá tato práce ze souboru CIL_BP.md.""")
s=change(s,"ch3+='''", """old=parts[5]
new='Porovnávání vstupních preferencí je v aplikaci provedeno metodou AHP. Volba této metody vychází z možnosti propojit kvantitativní a kvalitativní kritéria v jednom hierarchickém modelu a kontrolovat vzájemnou konzistenci párových úsudků (Ishizaka a Labib, 2011; Moreno-Jiménez a Vargas, 2018; Velasquez a Hester, 2013). V této pracovní verzi byl celý výpočetní postup demonstrován na syntetických vstupech. Skutečná komparace vlastností nástrojů bude doplněna po provedení jednotných testů.'
ch3=replace(ch3,old,new,'BP 3.md')
ch3+='''""")
s=change(s,"Prostředí asistenta jej identifikuje jako agenta založeného na GPT-6; přesné dílčí označení modelu skutečně použitého pro tento běh nebylo samostatně doloženo.", "V uložených metadatech zpracování je model označen identifikátorem gpt-6-astra. Tento identifikátor je doložen polem model v záznamu turn_context původního běhu z 27. 9. 2026; jde o dostupné označení modelu, nikoli o údaj o interní revizi jeho vah.")
s=change(s,"a doplněna přesná evidence použité verze AI podle dostupných údajů", "a aktualizována evidence případného dalšího využití AI")
anchor="theory=[read(f'BP {i}.md').strip() for i in [4,5,6]]"
s=change(s,anchor,anchor+"""
theory[-1]+='''

## 6.4 Výpočetní postup použitý v této práci

Pro vlastní implementaci je z uvedených postupů zvolena metoda geometrického průměru řádků. Každý řádkový geometrický průměr je normalizován součtem geometrických průměrů všech řádků. Stejný postup je použit pro váhy kritérií i lokální priority alternativ, v PHP aplikaci, kontrolním sešitu i nezávislém referenčním výpočtu. Metoda vlastního vektoru je v předchozím výkladu uvedena jako teoretický postup AHP; v této aplikaci není algoritmem pro stanovení vah (Ishizaka a Labib, 2011).

Pro kontrolu konzistence je z geometrických vah vypočten průměr poměrů (Aw)_i/w_i. V další části práce je tato hodnota označována jako odhad λ. U obecné nekonzistentní matice nemusí být přesně rovna dominantnímu vlastnímu číslu λ_max. Ukazatele CI a CR jsou v implementaci odvozeny z tohoto odhadu. Porovnání s jiným nástrojem proto musí rozlišit shodu algoritmů od rozdílu způsobeného použitím vlastního vektoru nebo přesného vlastního čísla (Ishizaka a Labib, 2011; Tomeš a Alcnauer, 2014). Konkrétní vzorce, RI, výjimky pro rozměry 1 a 2 a tolerance jsou vymezeny v oddílu 9.3.
'''
""")
start=s.index("bp8=read('BP 8.md')")
end=s.index("practical=read('pracovni_bp/text_prakticka_cast.md')",start)
s=s[:start]+'''bp8=read('BP 8.md');ch8=re.split(r'\\n---\\s*\\n',bp8,maxsplit=1)[0].strip()
ch8=replace(ch8,'návrh a vývoj databáze. nikoli','návrh a vývoj databáze, nikoli','BP 8.md')
draft=bp8.split('## 8 Návrh hodnoticích kritérií')[1]
detail=draft[draft.index('| Kritérium | Název | Vymezení kritéria'):draft.index('Tabulka 2:')].strip()
old_table=ch8[ch8.index('| Kritérium | Název | Význam pro hodnocení |'):ch8.index('<span id=')].strip()
rows=[line.split('|')[1:-1] for line in detail.splitlines()[2:]]
compact=table(['Kritérium','Název','Význam pro hodnocení'],[[r[0].strip(),r[1].strip(),r[2].strip()] for r in rows])
ch8=replace(ch8,old_table,compact,'BP 8.md – tabulka 2')
ch8+='\\n\\n## 8.1 Vymezení kritérií a způsob posouzení\\n\\nTabulka 2 je závazným vymezením kritérií pro aplikaci i modelový případ. K1 zahrnuje modelování, nikoli generování DDL nebo reverse engineering. V K3 se pro každý DBMS rozlišuje podpora modelování, forward a reverse engineeringu; samotné připojení není dostatečné. K4 a K5 hodnotí kvalitu konkrétního převodu, zatímco K3 hodnotí rozsah podporovaných DBMS. Tentýž úspěšný DDL export se znovu neboduje v K7.\\n\\n'+table(['Kritérium','Název','Charakter posouzení'],[[r[0].strip(),r[1].strip(),r[3].strip()] for r in rows])+'\\n\\nCharakter posouzení neurčuje váhu kritéria. Váhy jsou samostatným vyjádřením preferencí rozhodovatele.\\n\\n'
more=draft[draft.index('### 8.1 Vazba'):].replace('### 8.1','## 8.2').replace('### 8.2','## 8.3')
ch8+=more

'''+s[end:]
# Control labels only: numbers remain unchanged.
s=s.replace("zip(['A','B','C'],cr['scores'])", "zip(['A1','A2','A3'],cr['scores'])")
s=s.replace("matrix_table(m,['A','B','C'])", "matrix_table(m,['A1','A2','A3'])")
s=change(s,"bib=read('BP 10.md').split('\\n\\n')[1:];bib=[x.strip() for x in bib if x.strip()]", "bib=read('BP 10.md').split('\\n---\\n',1)[0].split('\\n\\n')[1:];bib=[x.strip() for x in bib if x.strip()]")
# Bibliography is already consolidated and italicized in BP 10; preserve it as authoritative.
a=s.index("updates=re.findall(");b=s.index("bib.sort(key=sortkey)",a)
s=s[:a]+"bibnotes=[]\ndef sortkey(x):return unicodedata.normalize('NFKD',x).encode('ascii','ignore').decode().upper()\n"+s[b:]
s=s.replace("bibliography+='\\n\\n---\\n\\n[Pracovní poznámka – opravené bibliografické záznamy dle ZDROJE.md; původní znění pro srovnání, 27. 9. 2026:\\n\\n'+'\\n\\n'.join(old for _,old in bibnotes)+'\\n]\\n'", "")
s=change(s,"[Pracovní poznámka: přiložit aktuální oficiální zadání ze STAGu. Místní PDF ve složce zadani zachycuje starší znění; pro tuto pracovní verzi bylo použito novější zadání z e-mailu vedoucího z 15. 9. 2026. Aktuální stav schválení v IS nebyl tímto během ověřen.]", """Závazné zadání je uvedeno v CIL_BP.md, který je přepisem platného podkladu VŠKP z IS/STAG. Podklad byl exportován 23. 9. 2026 ve 20:40; student potvrdil jeho platnost v systému. Starší soubory ve složce zadani se pro tuto práci nepoužívají.

[Platný podklad VŠKP z IS/STAG, 23. 9. 2026](oliva/temata_vskp_-_podklady_pro_zadani_vskp.pdf)

![Podklad VŠKP ze systému IS/STAG](outputs/bp_20260927/zadani_stag.png)""")
s=change(s,"write('bakalarsa_prace.md',front+'\\n\\n'+body+'\\n\\n'+bibliography+'\\n\\n'+appendix)", """history='## Příloha 5 – Srovnání původního textu, pouze pro autorskou revizi\\n\\nNásledující bloky nejsou současnou metodikou ani součástí finální sazby. Zachovávají přesné původní pasáže pro porovnání.\\n\\n'
for i,note in enumerate(original_notes,1):
    history+=f'### Změna {i}\\n\\n---\\n\\n[Pracovní poznámka – původní znění před úpravou, 27. 9. 2026; důvod: návaznost na platné zadání nebo odstranění rozporu.\\n\\n{note}\\n]\\n\\n'
write('bakalarsa_prace.md',front+'\\n\\n'+body+'\\n\\n'+bibliography+'\\n\\n'+appendix+'\\n\\n'+history)""")
write('pracovni_bp/build_thesis.py',s)

# Refine justification independent of results.
p=read('pracovni_bp/text_prakticka_cast.md')
p=p.replace('alternativami A, B a C','alternativami A1, A2 a A3').replace('preference A a B','preference A1 a A2').replace('je A, B, C.','je A1, A2, A3.')
p=p.replace('Tato citlivost pracuje přímo s vahami.', 'Tato citlivost pracuje přímo s vahami. Faktor dva je předem zvolený scénář relativního zesílení jednoho hlediska, nikoli nový pozorovaný údaj nebo úsudek ze Saatyho škály. Po normalizaci zůstává součet vah jedna a poměry všech nezesílených kritérií mezi sebou se zachovají. Tři samostatné zásahy tak umožňují sledovat vliv konkrétní preference bez současné změny lokálního hodnocení nástrojů. Stejný postup bude použit i po nahrazení syntetických dat skutečnými vstupy.')
p=p.replace('Pro ověření byl zvolen malý model se třemi kritérii F, P a C a třemi abstraktními alternativami A1, A2 a A3.', 'Pro ověření byl zvolen malý model se třemi kritérii F, P a C a třemi abstraktními alternativami A1, A2 a A3. Označení alternativ bylo sjednoceno v textu, aplikaci i sešitu, aby se kritérium C nezaměňovalo s třetí alternativou. Jde pouze o přejmenování; matice a číselné výsledky kontrolního příkladu se nemění.')
write('pracovni_bp/text_prakticka_cast.md',p)

g=read('pracovni_bp/generate_data.py').replace("for k in ['A','B','C']", "for k in ['A1','A2','A3']")
write('pracovni_bp/generate_data.py',g)
c=json.loads(read('app/data/control.json'))
for i,a in enumerate(c['alternatives'],1):a['id']=a['name']=f'A{i}'
write('app/data/control.json',json.dumps(c,ensure_ascii=False,indent=2))
w=read('pracovni_bp/build_workbooks.mjs').replace("['A','B','C']","['A1','A2','A3']").replace('A/B/C','A1/A2/A3')
write('pracovni_bp/build_workbooks.mjs',w)
for name in ['app/README.md','vypocty/AHP_SPECIFIKACE.md']:
 write(name,read(name).replace('A/B/C','A1/A2/A3'))

# Audit and typography: 21 books/journal articles; conference paper/preprint/web are separate.
bib=json.loads(read('pracovni_bp/bibliografie.json'))
titles={
'CARVALHO':'IEEE Access','CATAK':'International Journal of Information Sciences and Techniques','CHEN':'ACM Transactions on Database Systems',
'CHLAPEK':'Datové modelování a návrh relační databáze: Sbírka řešených úloh','CODD':'Communications of the ACM',
'DB-ENGINES':'DB-Engines Ranking','DBEAVER':'DBeaver Documentation','EBRAHIMI':'International Journal of Information Engineering and Electronic Business',
'ELMASRI':'Fundamentals of Database Systems','FEINBERG':"Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems (CHI '17)",
'HO':'European Journal of Operational Research','ISHIZAKA':'Expert Systems with Applications','LARANJEIRO':'ONDA: ONLine Database Architect',
'MARDANI':'Economic Research – Ekonomska Istraživanja','MORENO-JIMÉNEZ':'Estudios de Economía Aplicada','MYSQL':'MySQL Workbench Manual',
'ORACLE':'Oracle SQL Developer Data Modeler','PGMODELER':'pgModeler – PostgreSQL Database Modeler','POKORNÝ':'Databázové systémy',
'POSTGRESQL':'PostgreSQL Documentation','ROSENTHAL':'ACM Transactions on Database Systems','SIMANAVIČIENĖ':'Baltic Journal of Modern Computing',
'SOUKOPOVÁ':'Vícekriteriální metody hodnocení','TOMEŠ':'Business & IT','VAIDYA':'European Journal of Operational Research',
'VELASQUEZ':'International Journal of Operations Research','VLČKOVÁ':'Český finanční a účetní časopis','WATT':'Database Design'}
new=[];audit=[]
books={'CHLAPEK','ELMASRI','POKORNÝ','WATT'}
other={'DB-ENGINES','DBEAVER','LARANJEIRO','MYSQL','ORACLE','PGMODELER','POSTGRESQL','SOUKOPOVÁ','FEINBERG'}
for b in bib:
 key=b.split(',')[0].split('.')[0]
 title=titles.get(key)
 if key=='SAATY':title='European Journal of Operational Research' if '1990,' in b else 'International Journal of Services Sciences'
 assert title and title in b,(key,title)
 new.append(b.replace(title,'*'+title+'*',1))
 audit.append({'author':key,'type':'kniha' if key in books else 'ostatní' if key in other else 'časopisecký článek','record':new[-1]})
old=read('BP 10.md')
write('BP 10.md','# Seznam zdrojů\n\n'+'\n\n'.join(new)+'\n\n---\n\n[Pracovní poznámka – původní znění před úpravou, 27. 9. 2026; důvod: sjednocení 30 záznamů a kurzívy názvů.\n\n'+old.strip()+'\n]\n')
write('pracovni_bp/bibliografie_audit.json',json.dumps(audit,ensure_ascii=False,indent=2))
write('pracovni_bp/revision_hashes.json',json.dumps({'BP 10.md':hashlib.sha256((ROOT/'BP 10.md').read_bytes()).hexdigest()},indent=2))
print('Source revision applied; bibliography',len(new),'books/articles',sum(x['type']!='ostatní' for x in audit))
