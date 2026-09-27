<?php
declare(strict_types=1);

final class AhpCalculator
{
    public const RI = [0,0,0,0.58,0.90,1.12,1.24,1.32,1.41,1.45,1.49];

    public static function onScale(mixed $v): bool
    {
        if (!is_int($v) && !is_float($v)) return false;
        if (!is_finite((float)$v) || $v<=0) return false;
        for ($i=1;$i<=9;$i++) if (abs($v-$i)<1e-9 || abs($v-1/$i)<1e-9) return true;
        return false;
    }
    public static function validate(array $a): void
    {
        $n=count($a);
        if ($n<1 || $n>10 || !array_is_list($a)) throw new InvalidArgumentException('Matice musí mít rozměr 1 až 10.');
        foreach ($a as $row) if (!is_array($row) || !array_is_list($row) || count($row)!==$n) throw new InvalidArgumentException('Matice musí být čtvercová a úplná.');
        for ($i=0;$i<$n;$i++) for ($j=0;$j<$n;$j++) {
            if (!self::onScale($a[$i][$j])) throw new InvalidArgumentException('Vyberte hodnotu ze Saatyho škály 1/9 až 9.');
            if ($i===$j && abs($a[$i][$j]-1)>1e-9) throw new InvalidArgumentException('Diagonála musí být 1.');
        }
        for ($i=0;$i<$n;$i++) for ($j=0;$j<$n;$j++) if (abs($a[$i][$j]*$a[$j][$i]-1)>1e-9) throw new InvalidArgumentException('Matice není reciproční.');
    }
    public static function calculate(array $a): array
    {
        self::validate($a);$n=count($a);$gm=[];
        foreach ($a as $row) $gm[]=exp(array_sum(array_map('log',$row))/$n);
        $sum=array_sum($gm);$w=array_map(fn($x)=>$x/$sum,$gm);$aw=[];$ratios=[];
        foreach ($a as $i=>$row) {$aw[$i]=0;foreach ($row as $j=>$v) $aw[$i]+=$v*$w[$j];$ratios[]=$aw[$i]/$w[$i];}
        $lambda=array_sum($ratios)/$n;$ci=$n>1?max(0,($lambda-$n)/($n-1)):0;$cr=$n>2?$ci/self::RI[$n]:0;
        return ['weights'=>$w,'gm'=>$gm,'aw'=>$aw,'lambdaEstimate'=>$lambda,'ci'=>$ci,'cr'=>$cr];
    }
    public static function scores(array $w,array $local): array
    {
        $scores=array_fill(0,count($local[0]['weights']),0.0);
        foreach ($local as $k=>$r) foreach ($r['weights'] as $i=>$v) $scores[$i]+=$w[$k]*$v;
        return $scores;
    }
    public static function ranks(array $scores): array
    {
        return array_map(fn($v)=>1+count(array_filter($scores,fn($x)=>$x>$v+1e-12)),$scores);
    }
    public static function evaluate(array $d): array
    {
        $c=self::calculate($d['criteria_matrix']);$local=array_map([self::class,'calculate'],$d['alternative_matrices']);
        $scores=self::scores($c['weights'],$local);$sensitivity=[];
        foreach (['K8','K1','K3'] as $code) {
            $ix=array_search($code,array_column($d['criteria'],'id'),true);if ($ix===false)continue;
            $weights=$c['weights'];$weights[$ix]*=2;$total=array_sum($weights);$weights=array_map(fn($v)=>$v/$total,$weights);
            $ss=self::scores($weights,$local);$sensitivity[]=['criterion'=>$code,'factor'=>2,'weights'=>$weights,'scores'=>$ss,'ranks'=>self::ranks($ss)];
        }
        return ['criteria'=>$c,'local'=>$local,'scores'=>$scores,'ranks'=>self::ranks($scores),'sensitivity'=>$sensitivity];
    }
}
