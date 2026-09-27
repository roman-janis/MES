<?php
declare(strict_types=1);
require_once __DIR__.'/../src/Evaluation.php';
$count=0;$max=0.0;
function check(bool $ok,string $label): void {global $count;if(!$ok)throw new RuntimeException($label);$count++;}
function near(float $a,float $b,string $label):void{global $max;$delta=abs($a-$b);$max=max($max,$delta);check($delta<1e-9,$label.' delta='.$delta);}
function invalid(callable $f,string $label):void{try{$f();}catch(InvalidArgumentException){check(true,$label);return;}throw new RuntimeException('Accepted invalid input: '.$label);}
foreach(['control','demo'] as $name){
 $d=json_decode(file_get_contents(__DIR__.'/../data/'.$name.'.json'),true,512,JSON_THROW_ON_ERROR);Evaluation::validate($d);
 $r=AhpCalculator::evaluate($d);$ref=json_decode(file_get_contents(__DIR__.'/../../vypocty/'.$name.'_reference.json'),true,512,JSON_THROW_ON_ERROR);
 foreach(array_merge([$r['criteria']],$r['local']) as $i=>$m){$e=array_merge([$ref['criteria']],$ref['local'])[$i];foreach($m['weights'] as $j=>$v)near($v,$e['weights'][$j],$name.' weight');foreach(['lambdaEstimate','ci','cr'] as $key)near($m[$key],$e[$key],$name.' '.$key);near(array_sum($m['weights']),1,'sum');}
 foreach($r['scores'] as $i=>$v)near($v,$ref['scores'][$i],'priority');
 foreach($r['sensitivity'] as $k=>$v){foreach($v['scores'] as $i=>$p)near($p,$ref['sensitivity'][$k]['scores'][$i],'sensitivity');near(array_sum($v['weights']),1,'sensitivity sum');}
}
near(AhpCalculator::calculate([[1]])['cr'],0,'n1');
$two=AhpCalculator::calculate([[1,3],[1/3,1]]);near($two['weights'][0],.75,'n2 weight');near($two['cr'],0,'n2 cr');
$consistent=AhpCalculator::calculate([[1,2,4],[.5,1,2],[.25,.5,1]]);near($consistent['cr'],0,'consistent');
check(AhpCalculator::calculate([[1,9,1/9],[1/9,1,9],[9,1/9,1]])['cr']>.1,'inconsistent warning');
check(AhpCalculator::ranks([.5,.5])===[1,1],'ties');
foreach([[],[[1,2]],[[1,0],[0,1]],[[1,-1],[-1,1]],[[1,10],[.1,1]],[[1,2],[2,1]],[[2,1],[1,1]],[[1,NAN],[NAN,1]],[[1,'3'],['0.3333',1]]] as $m)invalid(fn()=>AhpCalculator::calculate($m),'matrix');
invalid(fn()=>Evaluation::pairs([],3),'missing pair');
invalid(fn()=>Evaluation::pairs(['0_1'=>'2.4'],2),'off scale');
$d=json_decode(file_get_contents(__DIR__.'/../data/demo.json'),true);$d['alternatives'][0]['link']='javascript:alert(1)';invalid(fn()=>Evaluation::validate($d),'unsafe url');
$d=json_decode(file_get_contents(__DIR__.'/../data/demo.json'),true);$d['synthetic']='false';invalid(fn()=>Evaluation::validate($d),'metadata bool');
$d=json_decode(file_get_contents(__DIR__.'/../data/demo.json'),true);$d['criteria'][1]['id']=$d['criteria'][0]['id'];invalid(fn()=>Evaluation::validate($d),'duplicate id');
echo json_encode(['checks'=>$count,'max_absolute_difference'=>$max,'php'=>PHP_VERSION,'status'=>'PASS'],JSON_PRETTY_PRINT).PHP_EOL;
