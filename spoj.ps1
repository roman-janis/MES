# spoj.ps1 — spojí kapitolové soubory "BP <N>.md" prostě za sebe.
#
# Použití (v PowerShellu, ze složky práce):
#   .\spoj.ps1                 # spojí úplnou pracovní BP 0..15 do "BP.md"
#   .\spoj.ps1 2 3 8           # spojí jen kapitoly 2 + 3 + 8 (v tomto pořadí)
#   .\spoj.ps1 2 3 8 -Out vyber.md   # spojí 2+3+8 do souboru vyber.md
#
# Pozn.: bez -Out přepíše "BP.md". Když spojuješ jen výběr,
# zadej -Out, ať si nepřepíšeš celý dokument.
# Značky BP-DOPLNIT a výrazy v závorkách ⟦...⟧ označují chybějící skutečná data.

param(
    [Parameter(Position = 0, ValueFromRemainingArguments = $true)]
    [string[]]$Chapters,

    [string]$Out = "BP.md"
)

Write-Host ""
Write-Host "spoj.ps1 — použití:"
Write-Host "  .\spoj.ps1                        # spojí kapitoly 0..15 -> 'BP.md'"
Write-Host "  .\spoj.ps1 2 3 8                  # spojí jen kapitoly 2+3+8 -> 'BP.md'"
Write-Host "  .\spoj.ps1 2 3 8 -Out výběr.md    # výběr do vlastního souboru"
Write-Host ""

if (-not $Chapters) { $Chapters = @(0..15 | ForEach-Object { "$_" }) }

$dir = $PSScriptRoot
if (-not $dir) { $dir = (Get-Location).Path }

$enc = New-Object System.Text.UTF8Encoding($false)   # UTF-8 bez BOM

$blocks = foreach ($i in $Chapters) {
    $path = Join-Path $dir "BP $i.md"
    if (-not (Test-Path -LiteralPath $path)) { Write-Error "Chybí soubor: $path"; return }
    [System.IO.File]::ReadAllText($path, $enc).Trim()
}

$text = ($blocks -join "`r`n`r`n") + "`r`n"
$outPath = Join-Path $dir $Out
[System.IO.File]::WriteAllText($outPath, $text, $enc)

Write-Host ("Spojeno: {0} -> {1}  ({2} znaků)" -f ($Chapters -join '+'), $Out, $text.Length)
$markerPattern = 'BP-(ZMĚNA|DOPLNIT|OVĚŘIT)|⟦(?:NEZAZNAMENÁNO|NEVYHODNOCENO|NEOVĚŘENO|NV|ROK ODEVZDÁNÍ|DATUM|NOT YET EVALUATED)[^⟧]*⟧'
$markerCount = [regex]::Matches($text, $markerPattern).Count
if ($markerCount -gt 0) {
    Write-Warning ("Výstup stále obsahuje {0} pracovních značek nebo zástupných údajů; nelze jej považovat za finální verzi k odevzdání." -f $markerCount)
}
