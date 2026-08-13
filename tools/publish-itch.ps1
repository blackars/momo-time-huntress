param(
    [string]$ProjectPath = (Get-Location).Path,
    [string]$ButlerPath = "$env:USERPROFILE\butler\butler.exe",
    [string]$Version = "",
    [switch]$SkipBuild,
    [string]$ButlerApiKey = ""
)

$ErrorActionPreference = "Stop"

Write-Host "== Momo Time Huntress - publicly in itch.io =="

if (-not $SkipBuild) {
    $sdk = Get-ChildItem -Path "$env:USERPROFILE", "C:\", "D:\" -Directory -Filter "renpy-*-sdk" -ErrorAction SilentlyContinue |
        Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName "*") } | Select-Object -First 1
    if (-not $sdk) {
        throw "Ren'Py SDK not found. Pass -SkipBuild rebuild or install the SDK."
    }
    $sdkRoot = Get-ChildItem -LiteralPath $sdk.FullName -Directory -Filter "renpy-*-sdk" | Select-Object -First 1
    if (-not $sdkRoot) { $sdkRoot = $sdk }
    $renpy = Join-Path $sdkRoot.FullName "renpy.exe"
    Write-Host "Building web distribution with $renpy ..."
    & $renpy (Join-Path $sdkRoot.FullName "launcher") web_build $ProjectPath
    if ($LASTEXITCODE -ne 0) { throw "Web build failed with exit code $LASTEXITCODE." }
} else {
    Write-Host "Skipping build (-SkipBuild)."
}

$dist = Get-ChildItem -LiteralPath (Join-Path $ProjectPath "MomoTimeHuntress-1.0-dists") -Directory -Filter "*-web" | Select-Object -First 1
if (-not $dist) {
    throw "Web distribution not found under MomoTimeHuntress-1.0-dists."
}
Write-Host "Distribution: $($dist.FullName)"

if (-not (Test-Path -LiteralPath $ButlerPath)) {
    Write-Host "butler not found, downloading..."
    New-Item -ItemType Directory -Force -Path (Split-Path $ButlerPath) | Out-Null
    $zip = "$env:TEMP\butler.zip"
    Invoke-WebRequest -Uri "https://github.com/itchio/butler/releases/download/v15.30.0/butler-windows-amd64.zip" -OutFile $zip
    Expand-Archive -Path $zip -DestinationPath (Split-Path $ButlerPath) -Force
    $found = Get-ChildItem -LiteralPath (Split-Path $ButlerPath) -Recurse -Filter "butler.exe" | Select-Object -First 1
    if ($found) { $ButlerPath = $found.FullName } else { throw "butler.exe not found after extraction." }
}

if ($ButlerApiKey) {
    $env:BUTLER_API_KEY = $ButlerApiKey
}

if (-not $env:BUTLER_API_KEY) {
    Write-Warning "BUTLER_API_KEY not set; butler will require a previous 'butler login'."
}

if (-not $Version) {
    $Version = "1.0.$((git -C $ProjectPath rev-list --count HEAD 2>$null) ?? '1')"
}

Write-Host "Publishing to blackars/momo-time-huntress:web as version $Version ..."
& $ButlerPath push $dist.FullName "blackars/momo-time-huntress:web" --userversion $Version
if ($LASTEXITCODE -ne 0) { throw "butler push failed with exit code $LASTEXITCODE." }
Write-Host "Done."