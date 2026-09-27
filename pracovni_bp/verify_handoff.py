"""Read-only checks; prints JSON. No third-party Python dependencies."""
from pathlib import Path
import hashlib, json, re, zipfile, xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
ns = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
rel_ns = '{http://schemas.openxmlformats.org/package/2006/relationships}'
doc_ns = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
report = {}
old = json.loads((root/'pracovni_bp/original_hashes.json').read_text('utf-8-sig'))
report['original_files_unchanged'] = {p: hashlib.sha256((root/p).read_bytes()).hexdigest() == h for p, h in old.items()}
thesis = (root/'bakalarsa_prace.md').read_text('utf-8-sig')
report['theory_verbatim'] = {str(i): (root/f'BP {i}.md').read_text('utf-8-sig').strip() in thesis for i in (4,5,6)}
report['images_exist'] = {p: (root/p).is_file() for p in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', thesis)}
report['trailing_newline'] = thesis.endswith('\n')
report['workbooks'] = {}
for path, checks in [('vypocty/kontrolni_priklad.xlsx','kontrolni_priklad'),('outputs/bp_20260927/hodnoceni_synteticke.xlsx','hodnoceni_synteticke')]:
    with zipfile.ZipFile(root/path) as z:
        assert z.testzip() is None
        rels = {x.attrib['Id']: x.attrib['Target'] for x in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        sheets = {}
        for s in ET.fromstring(z.read('xl/workbook.xml')).find('m:sheets',ns):
            target = rels[s.attrib[doc_ns+'id']]
            target = target.lstrip('/') if target.startswith('/') else 'xl/'+target
            sheets[s.attrib['name']] = ET.fromstring(z.read(target))
        errors = []
        formulas = 0
        for name, sheet in sheets.items():
            for c in sheet.findall('.//m:c',ns):
                if c.attrib.get('t') == 'e': errors.append([name,c.attrib['r'],c.findtext('m:v',namespaces=ns)])
                formulas += c.find('m:f',ns) is not None
        expected = json.loads((root/f'outputs/bp_20260927/overeni/{checks}_verification.json').read_text('utf-8-sig'))['checks']
        diffs = []
        for check in expected:
            c = sheets[check['sheet']].find(f'.//m:c[@r="{check["addr"]}"]',ns)
            diffs.append(abs(float(c.findtext('m:v',namespaces=ns))-check['expected']))
        report['workbooks'][path] = {'sheets':len(sheets),'formulas':formulas,'errors':errors,'checked_values':len(diffs),'max_difference':max(diffs),'sha256':hashlib.sha256((root/path).read_bytes()).hexdigest()}
report['pass'] = (all(report['original_files_unchanged'].values()) and all(report['theory_verbatim'].values()) and all(report['images_exist'].values()) and report['trailing_newline'] and all(not x['errors'] and x['max_difference'] < 1e-9 for x in report['workbooks'].values()))
print(json.dumps(report, ensure_ascii=False, indent=2))
raise SystemExit(0 if report['pass'] else 1)
