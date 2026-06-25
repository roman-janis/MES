# extrahuj.ps1 — z kapitol 4–7 vytvoří soubory 4x–7x s nadpisy a pracovním textem
# (text mezi **** a ****). Bloky bez obsahu jsou přeskočeny, nadpis zůstane.
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

    $lines  = [System.IO.File]::ReadAllLines($src, $enc)
    $output = [System.Collections.Generic.List[string]]::new()
    $inBlock      = $false
    $blockContent = [System.Collections.Generic.List[string]]::new()

    foreach ($line in $lines) {
        if ($line -match '^\*{3,4}$') {
            if (-not $inBlock) {
                # vstup do bloku
                $inBlock = $true
                $blockContent.Clear()
            } else {
                # výstup z bloku — přidej obsah jen pokud není prázdný
                $inBlock = $false
                $hasContent = $blockContent | Where-Object { $_.Trim() -ne '' }
                if ($hasContent) {
                    $output.Add('')
                    foreach ($bl in $blockContent) { $output.Add($bl) }
                }
                $blockContent.Clear()
            }
        } elseif ($inBlock) {
            $blockContent.Add($line)
        } elseif ($line -match '^#{1,6}\s') {
            # nadpis — vždy zachovat
            $output.Add('')
            $output.Add($line)
        }
        # vše ostatní (vzor, blockquoty, ---, prázdné řádky mimo blok) se ignoruje
    }

    # Sestav výstupní text — odstraň úvodní prázdný řádek
    $text = (($output | Select-Object -Skip 1) -join "`n").TrimEnd() + "`n"
    [System.IO.File]::WriteAllText($dst, $text, $enc)

    $contentBlocks = ($output | Where-Object { $_ -ne '' -and $_ -notmatch '^#{1,6}\s' }).Count
    Write-Host "Vytvořen: Seminární práce ${i}x.md  (bloků s obsahem: $contentBlocks)"
}
