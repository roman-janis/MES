<?php
declare(strict_types=1);
require_once __DIR__.'/AhpCalculator.php';
final class Evaluation
{
    public static function validate(array $d): void
    {
        if (($d['schema_version']??null)!==1 || !is_bool($d['synthetic']??null)) throw new InvalidArgumentException('Chybí verze formátu nebo příznak syntetických dat.');
        if (!is_string($d['title']??null) || trim($d['title'])==='' || strlen($d['title'])>300) throw new InvalidArgumentException('Vyplňte název hodnocení (max. 300 bajtů).');
        foreach (['criteria','alternatives'] as $group) {
            $items=$d[$group]??null;
            if (!is_array($items)||!array_is_list($items)||count($items)<2||count($items)>10) throw new InvalidArgumentException('Vyberte 2 až 10 kritérií a 2 až 10 alternativ.');
            $ids=[];
            foreach ($items as $v) {
                if (!is_array($v)) throw new InvalidArgumentException('Neplatná položka.');
                foreach (['id','name','description','link'] as $field) if (!is_string($v[$field]??null)) throw new InvalidArgumentException('Položka musí mít id, název, popis a odkaz.');
                if (!preg_match('/^[A-Za-z0-9_-]{1,40}$/D',$v['id'])||trim($v['name'])===''||strlen($v['name'])>200||strlen($v['description'])>2000||strlen($v['link'])>2000) throw new InvalidArgumentException('Neplatný identifikátor nebo příliš dlouhá položka.');
                if (in_array($v['id'],$ids,true)) throw new InvalidArgumentException('Identifikátory se nesmějí opakovat.');
                $ids[]=$v['id'];
                if ($v['link']!=='' && (!filter_var($v['link'],FILTER_VALIDATE_URL)||!in_array(strtolower((string)parse_url($v['link'],PHP_URL_SCHEME)),['http','https'],true))) throw new InvalidArgumentException('Odkaz musí být platná adresa http nebo https.');
            }
        }
        $cm=$d['criteria_matrix']??null;$lm=$d['alternative_matrices']??null;
        if (!is_array($cm)||count($cm)!==count($d['criteria'])||!is_array($lm)||!array_is_list($lm)||count($lm)!==count($d['criteria']))throw new InvalidArgumentException('Počet matic neodpovídá kritériím.');
        AhpCalculator::validate($cm);
        foreach ($lm as $m) {
            if (!is_array($m)||count($m)!==count($d['alternatives']))throw new InvalidArgumentException('Rozměr matice neodpovídá alternativám.');
            AhpCalculator::validate($m);
        }
    }
    public static function pairs(array $values,int $n): array
    {
        $m=array_fill(0,$n,array_fill(0,$n,1.0));
        for($i=0;$i<$n;$i++)for($j=$i+1;$j<$n;$j++){
            $raw=$values[$i.'_'.$j]??'';
            if(!is_string($raw)||trim($raw)==='')throw new InvalidArgumentException('Vyplňte všechna párová porovnání.');
            if(preg_match('/^1\/([2-9])$/D',$raw,$match))$v=1/(int)$match[1];
            elseif(preg_match('/^[1-9]$/D',$raw))$v=(float)$raw;
            else throw new InvalidArgumentException('Neplatná preference.');
            $m[$i][$j]=$v;$m[$j][$i]=1/$v;
        }
        return $m;
    }
}
