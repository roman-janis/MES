from pathlib import Path
import urllib.request,urllib.parse,urllib.error,http.cookiejar,json,re,sys,time,subprocess,tempfile
ROOT=Path(__file__).resolve().parents[2]
TMP=Path(tempfile.gettempdir())/'mes-bp-20260927'
TMP.mkdir(exist_ok=True);(TMP/'sessions').mkdir(exist_ok=True)
php=sys.argv[1];port=18763
log=open(TMP/'php-server.log','w')
proc=subprocess.Popen([php,'-d','session.save_path='+str(TMP/'sessions'),'-S',f'127.0.0.1:{port}','-t',str(ROOT/'app/public')],stdout=log,stderr=log)
(TMP/'server_pid.txt').write_text(str(proc.pid))
base=f'http://127.0.0.1:{port}/'
jar=http.cookiejar.CookieJar();op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar));checks=[]
def req(data=None,path=''):
    try:
        r=op.open(base+path,None if data is None else urllib.parse.urlencode(data,doseq=True).encode());return r.status,r.read().decode('utf-8')
    except urllib.error.HTTPError as e:return e.code,e.read().decode('utf-8')
def post(action,**kw):
    code,html=req();token=re.search(r'name="csrf" value="([a-f0-9]+)"',html)[1]
    return req(dict(csrf=token,action=action,**kw))
def assert_ok(condition,label):
    if not condition:raise AssertionError(label)
    checks.append(label)
for _ in range(50):
    try:req();break
    except OSError:time.sleep(.1)
for name in ['demo','control']:
    code,html=post(name);assert_ok(code==200 and 'SYNTETICKÁ DATA' in html,name+' page')
    code,raw=post('export');d=json.loads(raw);ref=json.loads((ROOT/f'vypocty/{name}_reference.json').read_text(encoding='utf-8'))
    assert_ok(max(abs(x-y) for x,y in zip(d['result']['scores'],ref['scores']))<1e-9,name+' HTTP results')
    code,html=post('import',json=raw);assert_ok(code==200,name+' import roundtrip')
code,html=post('calculate',criteria_pairs='');assert_ok(code==422 and 'Vyplňte' in html,'empty pairs rejected')
code,html=req(dict(action='demo',csrf='wrong'));assert_ok(code==422,'CSRF rejected')
code,html=post('import',json='{broken');assert_ok(code==422,'bad JSON rejected')
code,html=post('select',title='Test',**{'criteria[]':['K1'],'alternatives[]':['OSDM','MYSQL']});assert_ok(code==422,'one criterion rejected')
code,html=post('select',title='Vlastní <script>alert(1)</script>',custom_criteria='Vlastní kritérium | Popis | https://example.org',custom_alternatives='Vlastní nástroj | Popis | https://example.org',synthetic='on',**{'criteria[]':['K1'],'alternatives[]':['OSDM']})
assert_ok(code==200 and 'Vyberte preferenci' in html and '<script>alert' not in html,'custom items and escaping')
pairs={'criteria_pairs[0_1]':'3','alternative_pairs[0][0_1]':'2','alternative_pairs[1][0_1]':'1/2'}
code,html=post('calculate',**pairs);assert_ok(code==200 and 'Pořadí podle' in html,'custom evaluation form')
_,raw=post('export');d=json.loads(raw);assert_ok(abs(d['result']['scores'][0]-7/12)<1e-9,'custom exact result')
# Záměrně nekonzistentní matice musí projít výpočtem a vyvolat varování.
d=json.loads((ROOT/'app/data/control.json').read_text(encoding='utf-8'));d['criteria_matrix']=[[1,9,1/9],[1/9,1,9],[9,1/9,1]]
code,html=post('import',json=json.dumps(d));assert_ok(code==200 and 'vyšší než 0,10' in html,'high CR warning through UI')
# Ponechat lokální server pro vizuální kontrolu; žádná veřejná síť.
(TMP/'http_tests.json').write_text(json.dumps({'status':'PASS','checks':checks,'base_url':base,'server_pid':proc.pid},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'status':'PASS','checks':len(checks),'url':base,'pid':proc.pid}))
