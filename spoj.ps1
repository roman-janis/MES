# spoj.ps1 — spojí kapitolové soubory "Seminární práce <N>.md" prostě za sebe.
#
# Použití (v PowerShellu, ze složky práce):
#   .\spoj.ps1                 # spojí kapitoly 0..11 do "Seminární práce.md"
#   .\spoj.ps1 2 3 8           # spojí jen kapitoly 2 + 3 + 8 (v tomto pořadí)
#   .\spoj.ps1 2 3 8 -Out vyber.md   # spojí 2+3+8 do souboru vyber.md
#
# Pozn.: bez -Out přepíše "Seminární práce.md". Když spojuješ jen výběr,
# zadej -Out, ať si nepřepíšeš celý dokument.
# Soubory 12 a 13 jsou prázdné rezervy (NEPOUŽÍVAT) a do dokumentu nepatří.

param(
    [Parameter(Position = 0, ValueFromRemainingArguments = $true)]
    [int[]]$Chapters,

    [string]$Out = "Seminární práce.md"
)

Write-Host ""
Write-Host "spoj.ps1 — použití:"
Write-Host "  .\spoj.ps1                        # spojí kapitoly 0..11 -> 'Seminární práce.md'"
Write-Host "  .\spoj.ps1 2 3 8                  # spojí jen kapitoly 2+3+8 -> 'Seminární práce.md'"
Write-Host "  .\spoj.ps1 2 3 8 -Out vyber.md    # spojí 2+3+8 do vlastního souboru"
Write-Host ""

if (-not $Chapters) { $Chapters = 0..11 }

$dir = $PSScriptRoot
if (-not $dir) { $dir = (Get-Location).Path }

$enc = New-Object System.Text.UTF8Encoding($false)   # UTF-8 bez BOM

$blocks = foreach ($i in $Chapters) {
    $path = Join-Path $dir "Seminární práce $i.md"
    if (-not (Test-Path -LiteralPath $path)) { Write-Error "Chybí soubor: $path"; return }
    [System.IO.File]::ReadAllText($path, $enc).Trim()
}

$text = ($blocks -join "`r`n`r`n") + "`r`n"
$outPath = Join-Path $dir $Out
[System.IO.File]::WriteAllText($outPath, $text, $enc)

Write-Host ("Spojeno: {0} -> {1}  ({2} znaků)" -f ($Chapters -join '+'), $Out, $text.Length)
