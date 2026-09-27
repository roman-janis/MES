<?php
declare(strict_types=1);
require_once __DIR__.'/../src/Evaluation.php';
session_start(['cookie_httponly'=>true,'cookie_samesite'=>'Lax','use_strict_mode'=>true]);
header('X-Content-Type-Options: nosniff');header('Content-Security-Policy: default-src \'self\'; style-src \'self\'; base-uri \'none\'; frame-ancestors \'none\'; form-action \'self\'');
$_SESSION['csrf']??=bin2hex(random_bytes(24));
function h(mixed $s): string{return htmlspecialchars((string)$s,ENT_QUOTES|ENT_SUBSTITUTE,'UTF-8');}
function num(float $v): string{return number_format($v,4,',',' ');}
function readData(string $name): array{return json_decode(file_get_contents(__DIR__.'/../data/'.$name.'.json'),true,512,JSON_THROW_ON_ERROR);}
function csrf(): void{echo '<input type="hidden" name="csrf" value="'.h($_SESSION['csrf']).'">';}
function button(string $action,string $label,string $class=''): void {echo '<form method="post" class="inline">';csrf();echo '<button class="'.h($class).'" name="action" value="'.h($action).'">'.h($label).'</button></form>';}
function itemInfo(array $item): void {echo '<strong>'.h($item['name']).'</strong><p>'.h($item['description']).'</p>';if($item['link'])echo '<a href="'.h($item['link']).'" target="_blank" rel="noopener noreferrer">Podrobnosti ↗</a>';}
$error='';$view=$_GET['view']??'home';$seedC=readData('seed_criteria');$seedA=readData('seed_alternatives');
if($_SERVER['REQUEST_METHOD']==='POST'){
 try{
  if(!is_string($_POST['csrf']??null)||!hash_equals($_SESSION['csrf'],$_POST['csrf']))throw new InvalidArgumentException('Platnost formuláře vypršela. Obnovte stránku.');
  $action=$_POST['action']??'';
  if(in_array($action,['demo','control'],true)){
   $d=readData($action);Evaluation::validate($d);$_SESSION['evaluation']=$d;$_SESSION['complete']=true;$view='results';
  }elseif($action==='select'){
   $d=['schema_version'=>1,'synthetic'=>isset($_POST['synthetic']),'title'=>trim((string)($_POST['title']??''))];
   foreach(['criteria'=>$seedC,'alternatives'=>$seedA] as $group=>$seed){
    $ids=$_POST[$group]??[];if(!is_array($ids))throw new InvalidArgumentException('Neplatný výběr.');
    $items=array_values(array_filter($seed,fn($x)=>in_array($x['id'],$ids,true)));
    $custom=$_POST['custom_'.$group]??'';if(!is_string($custom)||strlen($custom)>20000)throw new InvalidArgumentException('Příliš dlouhý vstup.');
    foreach(preg_split('/\R/',$custom) as $k=>$line){if(trim($line)==='')continue;$parts=array_pad(explode('|',$line,3),3,'');$items[]=['id'=>'U_'.$group.'_'.$k,'name'=>trim($parts[0]),'description'=>trim($parts[1]),'link'=>trim($parts[2])];}
    $d[$group]=$items;
   }
   $nc=count($d['criteria']);$na=count($d['alternatives']);
   if($nc<2||$nc>10||$na<2||$na>10)throw new InvalidArgumentException('Vyberte 2 až 10 kritérií a 2 až 10 alternativ.');
   $d['criteria_matrix']=array_fill(0,$nc,array_fill(0,$nc,1));$d['alternative_matrices']=array_fill(0,$nc,array_fill(0,$na,array_fill(0,$na,1)));
   Evaluation::validate($d);$_SESSION['evaluation']=$d;$_SESSION['complete']=false;$view='pairs';
  }elseif($action==='calculate'){
   $d=$_SESSION['evaluation']??throw new InvalidArgumentException('Nejprve založte hodnocení.');
   if(!is_array($_POST['criteria_pairs']??null)||!is_array($_POST['alternative_pairs']??null))throw new InvalidArgumentException('Vyplňte všechna párová porovnání.');
   $d['criteria_matrix']=Evaluation::pairs($_POST['criteria_pairs'],count($d['criteria']));
   foreach($d['criteria'] as $k=>$c){$pairs=$_POST['alternative_pairs'][$k]??[];if(!is_array($pairs))throw new InvalidArgumentException('Neplatné páry.');$d['alternative_matrices'][$k]=Evaluation::pairs($pairs,count($d['alternatives']));}
   Evaluation::validate($d);$_SESSION['evaluation']=$d;$_SESSION['complete']=true;$view='results';
  }elseif($action==='import'){
   $raw=$_POST['json']??'';if(!is_string($raw)||strlen($raw)>1000000)throw new InvalidArgumentException('Import může mít nejvýše 1 MB.');
   $d=json_decode($raw,true,32,JSON_THROW_ON_ERROR);if(!is_array($d))throw new InvalidArgumentException('Import musí být JSON dokument.');Evaluation::validate($d);
   unset($d['result']);$_SESSION['evaluation']=$d;$_SESSION['complete']=true;$view='results';
  }elseif($action==='export'){
   $d=$_SESSION['evaluation']??throw new InvalidArgumentException('Není co exportovat.');
   if(!($_SESSION['complete']??false))throw new InvalidArgumentException('Nejdříve vyplňte matice.');
   Evaluation::validate($d);$d['result']=AhpCalculator::evaluate($d);
   header('Content-Type: application/json; charset=utf-8');header('Content-Disposition: attachment; filename="ahp-hodnoceni.json"');echo json_encode($d,JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT|JSON_THROW_ON_ERROR);exit;
  }else throw new InvalidArgumentException('Neznámá akce.');
 }catch(Throwable $e){$error=$e instanceof JsonException?'Neplatný JSON.':$e->getMessage();http_response_code(422);$view=($action??'')==='calculate'?'pairs':(($action??'')==='select'?'new':'home');}
}
$d=$_SESSION['evaluation']??null;
if(in_array($view,['pairs','results'],true)&&!$d)$view='home';
if($view==='results'&&!($_SESSION['complete']??false))$view='pairs';
function renderPairs(string $name,array $items,array $m,bool $complete): void {
 echo '<div class="pairs">';
 for($i=0;$i<count($items);$i++)for($j=$i+1;$j<count($items);$j++){
  $key=$name.'['.$i.'_'.$j.']';$id=preg_replace('/[^a-zA-Z0-9]/','_',$key);
  echo '<label class="pair" for="'.$id.'"><span>'.h($items[$i]['name']).' <small>vůči</small> '.h($items[$j]['name']).'</span><select id="'.$id.'" name="'.h($key).'" required><option value="">Vyberte preferenci</option>';
  $options=[];for($q=9;$q>=2;$q--)$options['1/'.$q]=1/$q;for($q=1;$q<=9;$q++)$options[(string)$q]=$q;
  foreach($options as $label=>$value){$selected=$complete&&abs($m[$i][$j]-$value)<1e-9?' selected':'';$text=$value===1?'1 – stejně':($value>1?$label.' – převaha prvního':$label.' – převaha druhého');echo '<option value="'.h($label).'"'.$selected.'>'.h($text).'</option>';}
  echo '</select></label>';
 }echo '</div>';
}
?><!doctype html><html lang="cs"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AHP | Výběr databázového nástroje</title><link rel="stylesheet" href="assets/style.css"></head><body>
<header><a class="brand" href="?">AHP<span> / databázové nástroje</span></a><nav><a href="?view=new">Nové hodnocení</a><?php if($d):?><a href="?view=pairs">Porovnání</a><a href="?view=results">Výsledky</a><?php endif;?></nav></header><main>
<?php if($error):?><div role="alert" class="warning"><?=h($error)?></div><?php endif;?>
<?php if($d&&in_array($view,['pairs','results'],true)):?><p class="badge"><?=$d['synthetic']?'SYNTETICKÁ DATA · testy nástrojů nebyly provedeny':'VLASTNÍ VSTUPY · za jejich podklady odpovídá hodnotitel'?></p><p><?=h($d['title'])?></p><?php endif;?>
<?php if($view==='home'):?>
<section class="hero"><p class="eyebrow">ROZHODOVÁNÍ KROK ZA KROKEM</p><h1>Vyberte nástroj.<br>Podle svých priorit.</h1><p>Porovnejte databázové nástroje po dvojicích. AHP propojí vaše preference, ověří jejich konzistenci a vypočítá pořadí.</p><a class="button" href="?view=new">Začít vlastní hodnocení →</a></section>
<div class="cards"><section><h2>Vyzkoušet ukázku</h2><p>Čtyři nástroje a osm kritérií na syntetických datech. Ukázka není doporučením konkrétního produktu.</p><?php button('demo','Načíst demo','secondary');?></section><section><h2>Zkontrolovat výpočet</h2><p>Malý příklad se třemi kritérii a alternativami A, B, C pro porovnání s kontrolním Excelem.</p><?php button('control','Kontrolní příklad','secondary');?></section></div>
<details><summary>Obnovit hodnocení z JSON</summary><form method="post"><?php csrf();?><label>Vložte obsah exportovaného souboru<textarea name="json" rows="8" required></textarea></label><button name="action" value="import">Importovat a přepočítat</button></form></details>
<?php elseif($view==='new'):?><h1>Co budete porovnávat?</h1><p>Vyberte 2–10 alternativ a 2–10 kritérií. V dalším kroku zadáte jednotlivé preference.</p><form method="post"><?php csrf();?><label>Název hodnocení<input name="title" value="Výběr nástroje pro Cykloservis" maxlength="150" required></label><label class="check"><input type="checkbox" name="synthetic" checked> Používám zkušební / syntetická data</label>
<?php foreach(['alternatives'=>['Nástroje',$seedA],'criteria'=>['Kritéria',$seedC]] as $g=>[$title,$items]):?><h2><?=h($title)?></h2><div class="choices"><?php foreach($items as $item):?><div class="choice"><label class="check"><input type="checkbox" name="<?=h($g)?>[]" value="<?=h($item['id'])?>" checked><?=h($item['name'])?></label><p><?=h($item['description'])?></p><a href="<?=h($item['link'])?>" target="_blank" rel="noopener noreferrer">Podrobnosti ↗</a></div><?php endforeach;?></div><label>Vlastní položky: jeden řádek = název | popis | odkaz<textarea name="custom_<?=h($g)?>" rows="3" placeholder="Vlastní položka | Co hodnotí | https://..."></textarea></label><?php endforeach;?><button name="action" value="select">Pokračovat k porovnání →</button></form>
<?php elseif($view==='pairs'):?><h1>Párová porovnání</h1><p>Hodnota 1 znamená rovnocennost. Hodnoty 2–9 upřednostňují první položku, 1/2–1/9 druhou. Obrácené porovnání se doplní automaticky.</p><p>U ceny porovnávejte výhodnost nabídky. Nižší cena nemusí převážit omezení licence.</p><form method="post"><?php csrf();?><section><h2>1. Důležitost kritérií</h2><?php renderPairs('criteria_pairs',$d['criteria'],$d['criteria_matrix'],$_SESSION['complete']??false);?></section>
<?php foreach($d['criteria'] as $k=>$c):?><section><h2><?=($k+2).'. '.h($c['name'])?></h2><p><?=h($c['description'])?></p><?php renderPairs('alternative_pairs['.$k.']',$d['alternatives'],$d['alternative_matrices'][$k],$_SESSION['complete']??false);?></section><?php endforeach;?><button name="action" value="calculate">Vypočítat pořadí →</button></form>
<?php elseif($view==='results'):$r=AhpCalculator::evaluate($d);$order=array_keys($r['scores']);usort($order,fn($a,$b)=>$r['scores'][$b]<=>$r['scores'][$a]);$bad=$r['criteria']['cr']>.10||count(array_filter($r['local'],fn($x)=>$x['cr']>.10))>0;?>
<div class="result-heading"><div><p class="eyebrow">VÝSLEDEK AHP</p><h1>Pořadí podle vašich vstupů</h1></div><a class="button secondary" href="?view=pairs">Upravit preference</a></div>
<?php if($bad):?><div class="warning" role="alert">Některá matice má CR vyšší než 0,10. Výpočet je zobrazen, ale párová porovnání je potřeba přehodnotit.</div><?php endif;?><section><table><thead><tr><th>Pořadí</th><th>Nástroj</th><th>Priorita</th><th>Podíl</th></tr></thead><tbody><?php foreach($order as $i):?><tr><td><?=$r['ranks'][$i]?></td><td><?=h($d['alternatives'][$i]['name'])?></td><td><?=num($r['scores'][$i])?></td><td><meter min="0" max="1" value="<?=$r['scores'][$i]?>"><?=num($r['scores'][$i])?></meter></td></tr><?php endforeach;?></tbody></table><p>Součet priorit: <?=num(array_sum($r['scores']))?>. Jde o relativní preference v této sestavě alternativ, nikoli o procento kvality nástroje.</p></section>
<section><h2>Váhy kritérií a konzistence</h2><p>CR kritérií: <strong><?=num($r['criteria']['cr'])?></strong> · hranice 0,1000. Odhad λ: <?=num($r['criteria']['lambdaEstimate'])?>.</p><table><thead><tr><th>Kritérium</th><th>Váha</th><th>CR alternativ</th></tr></thead><tbody><?php foreach($d['criteria'] as $k=>$c):?><tr><td><?=h($c['name'])?></td><td><?=num($r['criteria']['weights'][$k])?></td><td><?=num($r['local'][$k]['cr'])?></td></tr><?php endforeach;?></tbody></table><p>Pro dvě položky je CR z definice zde 0; nevypovídá o správnosti preference. Pro vyšší rozměry jde o kontrolu vnitřní soudržnosti úsudků.</p></section>
<section><h2>Lokální preference</h2><div class="scroll"><table><thead><tr><th>Nástroj</th><?php foreach($d['criteria'] as $c):?><th title="<?=h($c['name'])?>"><?=h($c['id'])?></th><?php endforeach;?></tr></thead><tbody><?php foreach($d['alternatives'] as $i=>$a):?><tr><td><?=h($a['name'])?></td><?php foreach($r['local'] as $l):?><td><?=num($l['weights'][$i])?></td><?php endforeach;?></tr><?php endforeach;?></tbody></table></div></section>
<?php if($r['sensitivity']):?><section><h2>Co se změní při jiných prioritách?</h2><p>Každá změna zdvojnásobí jednu váhu a všechny váhy znovu normalizuje. Ostatní vstupy zůstávají stejné. Změny se nekombinují.</p><table><thead><tr><th>Nástroj</th><th>Základ</th><?php foreach($r['sensitivity'] as $v):?><th><?=h($v['criterion'])?> ×2</th><?php endforeach;?></tr></thead><tbody><?php foreach($d['alternatives'] as $i=>$a):?><tr><td><?=h($a['name'])?></td><td><?=num($r['scores'][$i])?></td><?php foreach($r['sensitivity'] as $v):?><td><?=num($v['scores'][$i])?> (<?=$v['ranks'][$i]?>.)</td><?php endforeach;?></tr><?php endforeach;?></tbody></table><p>Jde o přímou citlivost vah. Nevznikají nové párové matice, proto se pro změněné váhy neuvádí nové CR.</p></section><?php endif;?>
<details><summary>Popisy hodnocených položek</summary><?php foreach(array_merge($d['criteria'],$d['alternatives']) as $item):?><article><?php itemInfo($item);?></article><?php endforeach;?></details><?php button('export','Stáhnout vstupy a výsledky JSON','secondary');?>
<?php endif;?></main><footer>AHP · pracovní aplikace k bakalářské práci · geometrické průměry · <?=date('Y')?> </footer></body></html>
