import fs from 'node:fs/promises';
import path from 'node:path';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const root=process.argv[2], out=process.argv[3];
await fs.mkdir(out,{recursive:true});
const read=async p=>JSON.parse(await fs.readFile(path.join(root,p),'utf8'));
const demo=await read('app/data/demo.json'), control=await read('app/data/control.json');
const blocks=await read('vypocty/synteticke_testy.json');
const col=n=>String.fromCharCode(65+n);
function base(w,name,title){
 const s=w.worksheets.add(name);s.showGridLines=false;
 s.getRange('A1:O35').format.font={name:'Arial',size:10,color:'#233047'};
 s.getRange('A1:A35').format.columnWidth=33;
 s.getRange('B1:O35').format.columnWidth=12;
 s.getRange('A1:O35').format.rowHeight=23;
 s.getRange('A2').values=[[title]];s.getRange('A2').format.font={bold:true,size:14};
 s.getRange('A3').values=[['SYNTETICKÁ / KONTROLNÍ DATA – nejde o provedené testy nástrojů']];
 s.getRange('A3').format.font={color:'#9A4F00'};
 return s;
}
const set=(s,a,v)=>s.getRange(a).values=[[v]];
const formula=(s,a,v)=>s.getRange(a).formulas=[[v]];
function header(s,r){s.getRange(r).format={fill:'#27384C',font:{bold:true,color:'#FFFFFF'},rowHeight:30,wrapText:true};}
function matrix(s,m,labels){
 const n=m.length;
 s.getRange(`A5:${col(n)}5`).values=[['Prvek',...labels]];header(s,`A5:${col(n)}5`);
 s.getRange('L5:O5').values=[['GM','Váha','Aw','Aw / w']];header(s,'L5:O5');
 for(let i=0;i<n;i++){
  const r=6+i;set(s,`A${r}`,labels[i]);
  for(let j=0;j<n;j++){
   const cell=`${col(j+1)}${r}`;
   if(i>j)formula(s,cell,`=1/${col(i+1)}${6+j}`);else set(s,cell,m[i][j]);
   if(i<j)s.getRange(cell).format.fill='#FFF1CC';
  }
  formula(s,`L${r}`,`=GEOMEAN(B${r}:${col(n)}${r})`);
  formula(s,`M${r}`,`=L${r}/SUM($L$6:$L$${5+n})`);
  formula(s,`N${r}`,'='+Array.from({length:n},(_,j)=>`${col(j+1)}${r}*$M$${6+j}`).join('+'));
  formula(s,`O${r}`,`=N${r}/M${r}`);
 }
 s.getRange(`B6:O${5+n}`).setNumberFormat('0.0000');
 const metric=[['Součet vah',`=SUM(M6:M${5+n})`],['Odhad lambda',`=AVERAGE(O6:O${5+n})`],['CI',`=MAX(0,(M18-${n})/(${n}-1))`],['RI',[0,0,0,.58,.9,1.12,1.24,1.32,1.41,1.45,1.49][n]],['CR','=M19/M20'],['Konzistence','=IF(M21<=0.1,"Přijatelná","Přehodnotit páry")']];
 metric.forEach(([label,v],i)=>{set(s,`L${17+i}`,label);typeof v==='string'&&v[0]==='='?formula(s,`M${17+i}`,v):set(s,`M${17+i}`,v)});
 s.getRange('M17:M21').setNumberFormat('0.000000');
 s.getRange('M21').conditionalFormats.addCustom('M21>0.1',{fill:'#FEE2E2',font:{color:'#991B1B',bold:true}});
 set(s,'A17','Žluté buňky: upravujte pouze horní trojúhelník (1/9 … 9).');
 set(s,'A19','Spodní trojúhelník a výsledky obsahují vzorce.');
 set(s,'A21','Zdroj: AHP_SPECIFIKACE.md; RI dle Saaty (1990).');
 set(s,'A23','CR je kontrola soudržnosti, nikoli pravdivosti dat.');
}
async function exportBook(w,name,checks){
 w.recalculate();
 const checkResults=[];
 for(const [sheet,addr,expected] of checks){
  const v=w.worksheets.getItem(sheet).getRange(addr).values[0][0];
  if(typeof v!=='number'||Math.abs(v-expected)>1e-9)throw Error(`${sheet}!${addr}: ${v} != ${expected}`);
  checkResults.push({sheet,addr,value:v,expected});
 }
 // Ověření živé závislosti: změna horního páru musí změnit váhu.
 const ms=w.worksheets.getItem(name==='kontrolni_priklad'?'1_matice_kriterii':'Kriteria');
 const before=ms.getRange('M6').values[0][0],original=ms.getRange('C6').values[0][0];
 set(ms,'C6',original===9?8:9);w.recalculate();
 const after=ms.getRange('M6').values[0][0];if(Math.abs(after-before)<1e-8)throw Error('No reactive change');
 set(ms,'C6',original);w.recalculate();
 await fs.writeFile(path.join(out,`${name}_verification.json`),JSON.stringify({checks:checkResults,mutation:{before,after,restored:ms.getRange('M6').values[0][0]}},null,2));
 for(let i=0;i<w.worksheets.items.length;i++){
  const s=w.worksheets.items[i];
  const preview=await w.render({sheetName:s.name,range:s.name==='Testy'?'A1:H12':s.name==='Souhrn'?'A1:J26':s.name==='Citlivost'?'A1:G25':'A1:O24',scale:1,format:'png'});
  await fs.writeFile(path.join(out,`${name}_${i}.png`),new Uint8Array(await preview.arrayBuffer()));
 }
 await (await SpreadsheetFile.exportXlsx(w)).save(path.join(out,name+'.xlsx'));
 console.log(name+': checks and export OK');
}
const w=Workbook.create();
const controlNames=['0_zadani','1_matice_kriterii','2_vahy_kriterii','3_konzistence_krit','4_matice_alt_K1','5_matice_alt_K2','6_matice_alt_K3','7_lokalni_vahy','8_globalni','9_souhrn'];
controlNames.forEach(n=>base(w,n,n.replaceAll('_',' ')));
let s=w.worksheets.getItem('0_zadani');
['Kontrolní příklad F/P/C a A1/A2/A3 z AHP_NAVOD_SAATY.md, oddíl 5.','Metoda: geometrické průměry; výpočty se nezaokrouhlují.','Žluté vstupy lze měnit; ostatní buňky obsahují vzorce.','9_souhrn: vypočtené hodnoty vedle neměnného etalonu Decimal.','Tolerance kontrolního srovnání 1e-9; osobní kontrola autora teprve následuje.'].forEach((x,i)=>set(s,`A${6+i*2}`,x));
matrix(w.worksheets.getItem('1_matice_kriterii'),control.criteria_matrix,['F','P','C']);
control.alternative_matrices.forEach((m,i)=>matrix(w.worksheets.getItem(controlNames[4+i]),m,['A1','A2','A3']));
s=w.worksheets.getItem('2_vahy_kriterii');s.getRange('A5:C5').values=[['Kritérium','GM','Váha']];header(s,'A5:C5');
for(let i=0;i<3;i++){set(s,`A${6+i}`,['F','P','C'][i]);formula(s,`B${6+i}`,`='1_matice_kriterii'!L${6+i}`);formula(s,`C${6+i}`,`='1_matice_kriterii'!M${6+i}`)}
s.getRange('B6:C8').setNumberFormat('0.000000000');
s=w.worksheets.getItem('3_konzistence_krit');
['Součet vah','Odhad lambda','CI','RI','CR'].forEach((x,i)=>{set(s,`A${6+i}`,x);formula(s,`B${6+i}`,`='1_matice_kriterii'!M${17+i}`)});s.getRange('B6:B10').setNumberFormat('0.000000000');
s=w.worksheets.getItem('7_lokalni_vahy');s.getRange('A5:D5').values=[['Alternativa','F','P','C']];header(s,'A5:D5');
for(let i=0;i<3;i++){set(s,`A${6+i}`,['A1','A2','A3'][i]);for(let k=0;k<3;k++)formula(s,`${col(k+1)}${6+i}`,`='${controlNames[4+k]}'!M${6+i}`)}
s.getRange('B6:D8').setNumberFormat('0.000000000');
s=w.worksheets.getItem('8_globalni');s.getRange('A5:C5').values=[['Alternativa','Priorita','Pořadí']];header(s,'A5:C5');
for(let i=0;i<3;i++){set(s,`A${6+i}`,['A1','A2','A3'][i]);formula(s,`B${6+i}`,'='+[0,1,2].map(k=>`'2_vahy_kriterii'!C${6+k}*'7_lokalni_vahy'!${col(k+1)}${6+i}`).join('+'));formula(s,`C${6+i}`,`=RANK(B${6+i},$B$6:$B$8,0)`)}s.getRange('B6:B8').setNumberFormat('0.000000000');
const ref=await read('vypocty/control_reference.json');
s=w.worksheets.getItem('9_souhrn');s.getRange('A5:D5').values=[['Výsledek','Vzorec','Etalon Decimal','Absolutní rozdíl']];header(s,'A5:D5');s.getRange('C5:D5').format.columnWidth=21;
const metrics=[...ref.criteria.weights.map((v,i)=>[`Váha ${['F','P','C'][i]}`,`='2_vahy_kriterii'!C${6+i}`,v]),['CR kritérií',"='3_konzistence_krit'!B10",ref.criteria.cr],...ref.scores.map((v,i)=>[`Priorita ${['A1','A2','A3'][i]}`,`='8_globalni'!B${6+i}`,v])];
metrics.forEach(([label,f,v],i)=>{let r=6+i;set(s,`A${r}`,label);formula(s,`B${r}`,f);set(s,`C${r}`,v);formula(s,`D${r}`,`=ABS(B${r}-C${r})`)});s.getRange('B6:D12').setNumberFormat('0.000000000');
await exportBook(w,'kontrolni_priklad',metrics.map((x,i)=>['9_souhrn',`B${6+i}`,x[2]]));

const b=Workbook.create();['Souhrn','Citlivost','Kriteria',...demo.criteria.map(x=>x.id),'Testy','Pokyny'].forEach(n=>base(b,n,n==='Souhrn'?'Cykloservis | výsledky DEMO':n));
matrix(b.worksheets.getItem('Kriteria'),demo.criteria_matrix,demo.criteria.map(x=>x.id));
demo.alternative_matrices.forEach((m,i)=>matrix(b.worksheets.getItem('K'+(i+1)),m,demo.alternatives.map(x=>x.id)));
s=b.worksheets.getItem('Souhrn');s.tabColor='#27384C';s.getRange('A5:C5').values=[['Nástroj','Priorita','Pořadí']];header(s,'A5:C5');s.getRange('A1:A26').format.columnWidth=40;
for(let i=0;i<4;i++){
 set(s,`A${6+i}`,demo.alternatives[i].name);
 formula(s,`B${6+i}`,'='+demo.criteria.map((x,k)=>`'Kriteria'!M${6+k}*'${x.id}'!M${6+i}`).join('+'));
 formula(s,`C${6+i}`,`=RANK(B${6+i},$B$6:$B$9,0)`);
}
s.getRange('B6:B9').setNumberFormat('0.0000');
s.getRange('A12:C12').values=[['Kritérium','Váha','CR alternativ']];header(s,'A12:C12');
demo.criteria.forEach((x,k)=>{set(s,`A${13+k}`,x.id+' '+x.name);formula(s,`B${13+k}`,`='Kriteria'!M${6+k}`);formula(s,`C${13+k}`,`='${x.id}'!M21`)});
s.getRange('B13:C20').setNumberFormat('0.0000');set(s,'A23','CR matice kritérií');formula(s,'B23',"='Kriteria'!M21");s.getRange('B23').setNumberFormat('0.0000');
set(s,'A25','Pořadí platí výhradně pro náhodné demo vstupy.');
s=b.worksheets.getItem('Citlivost');s.getRange('A5:E5').values=[['Kritérium','Základ','K8 ×2','K1 ×2','K3 ×2']];header(s,'A5:E5');
const targets=[7,0,2];
for(let k=0;k<8;k++){
 set(s,`A${6+k}`,demo.criteria[k].id);formula(s,`B${6+k}`,`='Kriteria'!M${6+k}`);
 for(let v=0;v<3;v++)formula(s,`${col(v+2)}${6+k}`,`=$B${6+k}*${targets[v]===k?2:1}/(1+$B$${6+targets[v]})`);
}
s.getRange('B6:E13').setNumberFormat('0.0000');
s.getRange('A16:E16').values=[['Alternativa','Základ','K8 ×2','K1 ×2','K3 ×2']];header(s,'A16:E16');
for(let i=0;i<4;i++){
 set(s,`A${17+i}`,demo.alternatives[i].id);formula(s,`B${17+i}`,`='Souhrn'!B${6+i}`);
 for(let v=0;v<3;v++)formula(s,`${col(v+2)}${17+i}`,'='+demo.criteria.map((x,k)=>`${col(v+2)}${6+k}*'${x.id}'!M${6+i}`).join('+'));
}
s.getRange('B17:E20').setNumberFormat('0.0000');set(s,'A23','Tři oddělené změny vah; matice alternativ se nemění.');set(s,'A25','Přímá změna vah nevytváří nové Saatyho matice ani nové CR.');
s=b.worksheets.getItem('Testy');s.getRange('A5:H5').values=[['Test','Kritérium','OSDM','DBEAVER','MYSQL','PGMODELER','Stav','Postup / očekávání']];header(s,'A5:H5');
s.getRange('A6:H'+(5+blocks.length)).values=blocks.map(x=>[x.title,x.criterion,...x.scores,x.status,x.task+' | '+x.expected]);
s.getRange('A6:A56').format.wrapText=true;s.getRange('A6:H56').format.rowHeight=64;
s.getRange('B6:B56').format.columnWidth=10;s.getRange('C6:F56').format.columnWidth=13;s.getRange('C6:F56').format.fill='#FFF1CC';s.getRange('G5:G56').format.columnWidth=32;s.getRange('H5:H56').format.columnWidth=90;s.getRange('G6:H56').format.wrapText=true;
s.freezePanes.freezeRows(5);
s=b.worksheets.getItem('Pokyny');
const notes=['Seed 20260927; všechny známky a matice jsou syntetické.','Známky 1–5: 1 nejlepší, 5 nejhorší. Nejsou vstupem AHP.','Matice AHP byly generovány nezávisle; nepředstavují úsudek autora.','Po reálných testech nahraďte známky i všechny párové matice.','Zdroj úloh: hodnoceni_4_nastroju.xlsx, 51 bloků, 11 tabulek.','Přesné verze, data testů, licence, ceny a důkazy zde nejsou vymyšleny.','V aplikaci lze importovat JSON; Excel upravujte ve žlutých buňkách.','Pro shodu Excel/PHP musí být v obou stejné vstupní matice.','Zdroj metody: Saaty (1990); Ishizaka a Labib (2011); AHP_SPECIFIKACE.md.','Nízké CR znamená soudržnost, nikoli věrohodnost syntetických dat.'];
notes.forEach((x,i)=>set(s,`A${6+i*2}`,x));
const dr=await read('vypocty/demo_reference.json');
const checks=dr.scores.map((v,i)=>['Souhrn',`B${6+i}`,v]);
checks.push(['Souhrn','B23',dr.criteria.cr]);
dr.sensitivity.forEach((v,k)=>v.scores.forEach((p,i)=>checks.push(['Citlivost',`${col(k+2)}${17+i}`,p])));
await exportBook(b,'hodnoceni_synteticke',checks);
