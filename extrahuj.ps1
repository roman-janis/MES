# extrahuj.ps1 — z kapitol 4–7 vytvoří soubory 4x–7x bez citačních bloků (řádky začínající ">")
#
# Použití:
#   .\extrahuj.ps1           # zpracuje kapitoly 4, 5, 6, 7
#   .\extrahuj.ps1 4 6       # zpracuje jen kapitoly 4 a 6

param(
    [int[]]$Chapters = @(4, 5, 6, 7)
)

$dir = $PSScriptRoot
if (-not $dir) { $dir = (Get-Location).Path }
$enc = New-Object System.Text.UTF8Encoding($false)

foreach ($i in $Chapters) {
    $src = Join-Path $dir "Seminární práce $i.md"
    $dst = Join-Path $dir "Seminární práce ${i}x.md"

    if (-not (Test-Path -LiteralPath $src)) {
        Write-Warning "Chybí soubor: $src"
        continue
    }

    $lines     = [System.IO.File]::ReadAllLines($src, $enc)
    $output    = [System.Collections.Generic.List[string]]::new()
    $prevBlank = $false

    foreach ($line in $lines) {
        # vynech řádky s citacemi
        if ($line -match '^>') { continue }

        $isBlank = ($line.Trim() -eq '')

        # sbalit víc prázdných řádků na jeden
        if ($isBlank -and $prevBlank) { continue }

        $output.Add($line)
        $prevBlank = $isBlank
    }

    $text = ($output -join "`n").TrimEnd() + "`n"
    [System.IO.File]::WriteAllText($dst, $text, $enc)

    $contentLines = ($output | Where-Object { $_.Trim() -ne '' }).Count
    Write-Host "Vytvořen: Seminární práce ${i}x.md  (řádků s obsahem: $contentLines)"
}
