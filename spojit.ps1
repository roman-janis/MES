# spojit.ps1
# Spoji casti "<nazev> <cislo>.md" do jednoho souboru "<nazev>.md".
# Poradi: ciselne 0,1,2,...,13 (ne abecedne). Spousti se ze slozky, kde lezi.
# Nazev vystupu i diakritika se berou z nazvu souboru (nic se nehardcoduje).

$ErrorActionPreference = 'Stop'

# slozka skriptu (funguje i pres pravy klik > Run with PowerShell)
$dir = $PSScriptRoot
if ([string]::IsNullOrEmpty($dir)) { $dir = (Get-Location).Path }

$numRegex = ' (\d+)\.md$'

# najdi casti = .md soubory koncici mezerou + cislo + .md (vystup ani zaloha cislo nemaji)
$parts = Get-ChildItem -LiteralPath $dir -Filter '*.md' |
    Where-Object { $_.Name -match $numRegex } |
    Sort-Object { [int]([regex]::Match($_.Name, $numRegex).Groups[1].Value) }

if ($null -eq $parts -or $parts.Count -eq 0) {
    Write-Error "Ve slozce '$dir' nebyly nalezeny zadne casti tvaru '... <cislo>.md'."
    exit 1
}

# nazev vystupu odvozeny z prvni casti: ostran ' <cislo>.md' a pridej '.md'
$base    = [regex]::Replace($parts[0].Name, $numRegex, '')
$outName = "$base.md"
$outPath = Join-Path $dir $outName

# nemic ctene casti s vystupem
$parts = $parts | Where-Object { $_.Name -ne $outName }

$sb = New-Object System.Text.StringBuilder
foreach ($p in $parts) {
    $text = [System.IO.File]::ReadAllText($p.FullName, [System.Text.Encoding]::UTF8)
    if ($sb.Length -gt 0 -and $sb[$sb.Length - 1] -ne "`n") {
        [void]$sb.Append("`n")   # zaruci oddeleni, pokud cast nekonci radkem
    }
    [void]$sb.Append($text)
    Write-Host ("  + " + $p.Name)
}

# zapis v UTF-8 bez BOM
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($outPath, $sb.ToString(), $utf8NoBom)

Write-Host ""
Write-Host ("Hotovo: " + $outName + "  (" + $parts.Count + " casti, " + $sb.Length + " znaku)")
