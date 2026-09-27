"""Export jednotného modelu 11 tabulek z uchovaného pracovního sešitu (čtení XLSX)."""
from pathlib import Path
import openpyxl, hashlib, re
ROOT=Path(__file__).resolve().parents[1]
source=ROOT/'hodnoceni_4_nastroju.xlsx'
w=openpyxl.load_workbook(source,data_only=True,read_only=True)
rows=list(w['Model a pravidla'].values)
idx=next(i for i,r in enumerate(rows) if r[0]=='Tabulka' and r[1]=='Sloupec')
headers=rows[idx][:7]
data=[r[:7] for r in rows[idx+1:] if r and isinstance(r[0],str) and re.fullmatch(r'[a-z_]+',r[0]) and len(r)>1 and r[1]]
tables=list(dict.fromkeys(r[0] for r in data))
assert len(tables)==11,tables
def table(h,rs):
 return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x if x is not None else '').replace('|','/') for x in r)+' |' for r in rs])
parts=['''# Jednotné zadání Cykloservis – 11 tabulek

Platná pracovní verze pro všechny čtyři nástroje: 27. 9. 2026. Toto je jediné aktuální technické zadání modelu; nahrazuje původní desetientitové jádro. Archiv starého zadání je `archiv/CYKLOSERVIS_ZADANI_pred_sjednocenim_20260927.md`. Nejde o druhý scénář, ale o sjednocení již připraveného testovacího sešitu a textu práce.

## Rozhodovací situace a společný postup

Vývojář vybírá nástroj pro návrh a vývoj databázového systému malého cykloservisu před konečnou volbou DBMS. V každém nástroji vytvoří stejný model od začátku. Z něj vygeneruje vlastní DDL a ověří jeho omezení. Teprve při testu reverse engineeringu použije referenční SQL uvedené níže. Poté ověří přenos modelu, kompatibilitu, dokumentaci a licenci testované edice. Pomocné známky nejsou Saatyho vstupy.

Malý cykloservis eviduje zákazníky, kola a jejich servisní zakázky, zaměstnance, provedené služby, spotřebované díly, dodavatele a faktury. Historická cena služby či dílu se ukládá také do položky zakázky. Elektrokolo představuje nepovinné rozšíření údajů konkrétního kola. Nejde o objednávkový systém dodavatelů; další tabulky se nepřidávají.

## Závazný seznam a důvod rozsahu

''', ', '.join('`'+str(t)+'`' for t in tables)+'.\n\n', '''Vztah zakázka–faktura testuje samostatný PK a UNIQUE FK. Vztah kolo–elektrokolo testuje sdílený PK/FK. V obou případech smí rodič existovat bez potomka; z pohledu rodiče tedy jde o 1 ku 0..1. Přidané elektrokolo umožňuje ověřit druhou realizaci této vazby podle požadavku na podrobné testování. M:N je řešeno tabulkami zakazka_sluzba a zakazka_dil. U zakázky je přípustný dosud nepřiřazený zaměstnanec.

## Přesná pravidla a atributy

''']
for r in rows[:idx]:
 if r and r[0] and not str(r[0]).startswith('Model –') and 'rozšiřuje starší' not in str(r[0]):parts.append(str(r[0])+'\n\n')
parts.append(table([str(x) for x in headers],data)+'\n\n')
parts.append('## Referenční SQL pro reverse engineering\n\nSkripty jsou převzaty z pracovního sešitu; jejich vytvoření ani tento export nedokládá běh databáze. Před skutečnými testy je nutné ověřit vytvoření 11 tabulek, 10 FK a omezení. Používat pouze samostatné prázdné testovací schéma.\n\n')
outdir=ROOT/'protokoly/reference_sql';outdir.mkdir(parents=True,exist_ok=True)
for name,filename in [('SQL MySQL','cykloservis_mysql.sql'),('SQL PostgreSQL','cykloservis_postgresql.sql'),('SQL Oracle','cykloservis_oracle.sql')]:
 lines=[str(r[0]) if r and r[0] is not None else '' for r in list(w[name].values)[4:]]
 sql='\n'.join(lines).strip()+'\n'
 assert len(re.findall(r'CREATE\s+TABLE',sql,re.I))==11,name
 assert len(re.findall(r'FOREIGN\s+KEY',sql,re.I))==10,name
 (outdir/filename).write_text(sql,encoding='utf-8')
 parts.append('### '+name+'\n\n```sql\n'+sql+'```\n\n')
parts.append('## Původ a změny\n\nZdroj atributů a SQL: `hodnoceni_4_nastroju.xlsx`, listy Model a pravidla a SQL MySQL/PostgreSQL/Oracle. SHA-256 zdroje: `'+hashlib.sha256(source.read_bytes()).hexdigest()+'`. Změna tohoto zadání musí být před skutečnými testy promítnuta do všech tří SQL, protokolu a textu práce; starý a nový model se nesmějí v jednom srovnání míchat.\n')
(ROOT/'CYKLOSERVIS_ZADANI.md').write_text(''.join(parts),encoding='utf-8')
print('11 tables; three SQL dialects; 10 foreign keys each; runtime execution not claimed')
