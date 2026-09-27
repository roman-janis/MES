param([int]$Port = 8080)
$ErrorActionPreference = 'Stop'
$candidates = @((Join-Path $env:TEMP 'mes-bp-20260927\php\php.exe'))
$found = Get-Command php -ErrorAction SilentlyContinue
if ($found) { $candidates += $found.Source }
$phpBinary = $null
foreach ($candidate in $candidates) {
    if (Test-Path -LiteralPath $candidate) {
        $version = & $candidate -r 'echo PHP_VERSION_ID;'
        if ($LASTEXITCODE -eq 0 -and [int]$version -ge 80200) { $phpBinary = $candidate; break }
    }
}
if (-not $phpBinary) { throw 'Je potřeba PHP 8.2 nebo novější. Současné PHP 7.0 nestačí.' }
$sessionDir = Join-Path $env:TEMP 'mes-bp-ahp-sessions'
New-Item -ItemType Directory -Path $sessionDir -Force | Out-Null
Write-Host "AHP: http://127.0.0.1:$Port | ukončení Ctrl+C"
& $phpBinary -d "session.save_path=$sessionDir" -S "127.0.0.1:$Port" -t (Join-Path $PSScriptRoot 'public')
exit $LASTEXITCODE
