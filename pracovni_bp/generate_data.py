"""Reprodukovatelná DEMO data; žádná měření nástrojů."""
from pathlib import Path
from decimal import Decimal, localcontext
import json, random, math

ROOT=Path(__file__).resolve().parents[1]
RI=[0,0,0,.58,.90,1.12,1.24,1.32,1.41,1.45,1.49]
def calculate(a):
    with localcontext() as ctx:
        ctx.prec=50
        d=[[Decimal(str(v)) for v in row] for row in a]; n=len(d)
        gm=[]
        for row in d:
            p=Decimal(1)
            for v in row: p*=v
            gm.append(p**(Decimal(1)/n))
        w=[x/sum(gm) for x in gm]
        aw=[sum(d[i][j]*w[j] for j in range(n)) for i in range(n)]
        lam=sum(aw[i]/w[i] for i in range(n))/n
        ci=max(Decimal(0),(lam-n)/(n-1)) if n>1 else Decimal(0)
        cr=ci/Decimal(str(RI[n])) if n>2 else Decimal(0)
        return dict(weights=list(map(float,w)),gm=list(map(float,gm)),aw=list(map(float,aw)),lambdaEstimate=float(lam),ci=float(ci),cr=float(cr))

criteria=[
 ('K1','Funkcionalita modelování','Entity, atributy, klíče, kardinality, integritní omezení; bez hodnocení DDL a importu.'),
 ('K2','Použitelnost','Srozumitelnost ovládání, počet kroků, obtíže a čas; čas není jediným měřítkem.'),
 ('K3','Kompatibilita s DBMS','Podpora návrhu a převodů pro různé DBMS; připojení samo nestačí.'),
 ('K4','Forward engineering','Spustitelnost DDL vytvořeného z modelu a zachování omezení.'),
 ('K5','Reverse engineering','Správnost načtení referenčního schématu do modelu či diagramu.'),
 ('K6','Dokumentace a komunita','Dohledatelnost návodu a relevantní podpory konkrétních modelovacích úloh.'),
 ('K7','Import a export modelu','Modelové formáty a diagramy; DDL z K4 se znovu nehodnotí.'),
 ('K8','Náklady a licence','Cena a omezení přesné edice k datu testování; nižší náklady mohou znamenat vyšší preferenci.')]
alts=[('OSDM','Oracle SQL Developer Data Modeler','https://www.oracle.com/database/sqldeveloper/technologies/sql-data-modeler/'),('DBEAVER','DBeaver Community Edition','https://dbeaver.io/'),('MYSQL','MySQL Workbench Community Edition','https://www.mysql.com/products/workbench/'),('PGMODELER','pgModeler','https://pgmodeler.io/')]
cs=[dict(id=k,name=name,description=desc,link='https://doi.org/10.1109/ACCESS.2021.3139071') for k,name,desc in criteria]
aa=[dict(id=k,name=name,description='Připravená alternativa; edici a verzi doložte při vlastním testování.',link=url) for k,name,url in alts]
rng=random.Random(20260927)
scale=sorted([1/i for i in range(2,10)]+list(range(1,10)))
attempts=[]
def random_matrix(n):
    count=0
    while True:
        count+=1
        latent=[math.exp(rng.uniform(0,math.log(5))) for _ in range(n)]
        m=[[1.0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                ratio=latent[i]/latent[j]*math.exp(rng.uniform(-.20,.20))
                val=min(scale,key=lambda s:abs(math.log(s/ratio)))
                m[i][j]=val;m[j][i]=1/val
        if calculate(m)['cr']<=.10:
            attempts.append(count);return m
def result(data):
    c=calculate(data['criteria_matrix']); ls=[calculate(m) for m in data['alternative_matrices']]
    scores=[sum(c['weights'][k]*ls[k]['weights'][i] for k in range(len(ls))) for i in range(len(data['alternatives']))]
    sensitivity=[]
    for code in ['K8','K1','K3']:
        if code not in [x['id'] for x in data['criteria']]:continue
        ix=next(i for i,x in enumerate(data['criteria']) if x['id']==code)
        ww=[v*(2 if i==ix else 1) for i,v in enumerate(c['weights'])]; ww=[v/sum(ww) for v in ww]
        pp=[sum(ww[k]*ls[k]['weights'][i] for k in range(len(ls))) for i in range(len(scores))]
        sensitivity.append(dict(criterion=code,factor=2,weights=ww,scores=pp))
    return dict(criteria=c,local=ls,scores=scores,sensitivity=sensitivity)
demo=dict(schema_version=1,title='Cykloservis – syntetická demonstrace',synthetic=True,seed=20260927,criteria=cs,alternatives=aa,criteria_matrix=random_matrix(8),alternative_matrices=[random_matrix(4) for _ in range(8)])
demo['generation']={'method':'náhodné latentní preference, zaokrouhlení na Saatyho škálu, přijetí při CR <= 0.10','attempts':attempts,'empirical_evidence':False}
control=dict(schema_version=1,title='Kontrolní příklad F/P/C',synthetic=True,criteria=[dict(id=k,name=k,description='Kontrolní kritérium',link='') for k in ['F','P','C']],alternatives=[dict(id=k,name=k,description='Abstraktní alternativa',link='') for k in ['A1','A2','A3']],criteria_matrix=[[1,3,5],[1/3,1,3],[1/5,1/3,1]],alternative_matrices=[[[1,2,4],[.5,1,2],[.25,.5,1]],[[1,.5,2],[2,1,4],[.5,.25,1]],[[1,2,1/3],[.5,1,1/6],[3,6,1]]])
blocks=json.loads((ROOT/'pracovni_bp/test_blocks.json').read_text(encoding='utf-8'))
for b in blocks:
    code=b['title'].split(' ')[0]
    b['criterion']= 'K2' if code=='1.13' else 'K1' if code.startswith('1.') else 'K4' if code.startswith('2.') or code=='4.3' else 'K5' if code.startswith('3.') else 'K7' if code.startswith('4.') else code.split('.')[0]
    b['scores']=[rng.randint(1,5) for _ in aa]
    b['status']='SYNTETICKÉ – test neproveden; bez důkazu'
for folder in ['app/data','vypocty','protokoly','outputs/bp_20260927']:(ROOT/folder).mkdir(parents=True,exist_ok=True)
for path,data in [('app/data/demo.json',demo),('app/data/control.json',control),('app/data/seed_criteria.json',cs),('app/data/seed_alternatives.json',aa),('vypocty/demo_reference.json',result(demo)),('vypocty/control_reference.json',result(control)),('vypocty/synteticke_testy.json',blocks)]:
    (ROOT/path).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'control':result(control),'demo':result(demo)},ensure_ascii=False,indent=2))
