from pathlib import Path
import json, re, hashlib
from pypdf import PdfReader
import openpyxl

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'pracovni_bp'
w=openpyxl.load_workbook(ROOT/'hodnoceni_4_nastroju.xlsx',read_only=True,data_only=True)
rows=list(w.worksheets[0].values)
blocks=[]
for i,r in enumerate(rows):
    if r and isinstance(r[0],str) and re.match(r'^(?:[1-4]\.\d+[a-z]?|K[368]\.\d+)\s*[–—-]',r[0]):
        blocks.append({'title':r[0], 'task':rows[i+1][1], 'expected':rows[i+2][1], 'evidence':rows[i+3][1], 'source_row':i+1})
(OUT/'test_blocks.json').write_text(json.dumps(blocks,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'model_workbook.txt').write_text('\n'.join(' | '.join(str(x or '') for x in r) for r in w.worksheets[1].values),encoding='utf-8')
files=[]
for p in ROOT.rglob('*'):
    if p.is_file() and not any(s in p.parts for s in ['.git','.tmp-pdf-venv','.obsidian','.serena','pracovni_bp','nastroje']):
        files.append({'path':str(p.relative_to(ROOT)), 'bytes':p.stat().st_size})
(OUT/'inventory.json').write_text(json.dumps(files,ensure_ascii=False,indent=2),encoding='utf-8')
for pattern in ['literatura/AHP/Tomes*','literatura/AHP/Vlckova*','literatura/DB/Feinberg*','literatura/AHP/Ishizaka*','literatura/AHP/Saaty_1990*']:
    for p in ROOT.glob(pattern):
        pages=[x.extract_text() or '' for x in PdfReader(p).pages]
        (OUT/(p.stem+'.txt')).write_text('\n\n'.join(f'PAGE {i+1}\n{s}' for i,s in enumerate(pages)),encoding='utf-8')
hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.glob('BP *.md')}
hashes['hodnoceni_4_nastroju.xlsx']=hashlib.sha256((ROOT/'hodnoceni_4_nastroju.xlsx').read_bytes()).hexdigest()
(OUT/'original_hashes.json').write_text(json.dumps(hashes,indent=2),encoding='utf-8')
print('Test blocks:',len(blocks),'files:',len(files))
print('\n'.join(x['title'] for x in blocks))
