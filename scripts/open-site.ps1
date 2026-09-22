$ErrorActionPreference = 'Stop'
$siteRoot = Split-Path -Parent $PSScriptRoot
$siteUrl = 'http://localhost:4322/'
$logRoot = Join-Path $siteRoot '.review'

function Test-SiteReady {
    try {
        $response = Invoke-WebRequest -Uri $siteUrl -UseBasicParsing -TimeoutSec 2
        return ($response.StatusCode -eq 200 -and $response.Content -match 'Kiden Scruton')
    } catch { return $false }
}

try {
    if (-not (Test-SiteReady)) {
        $node = (Get-Command node.exe -ErrorAction Stop).Source
        $astro = Join-Path $siteRoot 'node_modules\astro\astro.js'
        if (-not (Test-Path -LiteralPath $astro)) {
            throw "Site dependencies are missing from $siteRoot. Run npm install in that folder first."
        }
        New-Item -ItemType Directory -Path $logRoot -Force | Out-Null
        $server = Start-Process -FilePath $node -ArgumentList @(('"{0}"' -f $astro), 'dev', '--port', '4322') -WorkingDirectory $siteRoot -WindowStyle Hidden -RedirectStandardOutput (Join-Path $logRoot 'desktop-server.log') -RedirectStandardError (Join-Path $logRoot 'desktop-server-error.log') -PassThru
        $deadline = (Get-Date).AddSeconds(90)
        while (-not (Test-SiteReady)) {
            if ($server.HasExited) { throw 'The site server stopped. Check .review\desktop-server-error.log in the site folder.' }
            if ((Get-Date) -gt $deadline) { throw 'The site did not start within 90 seconds. Check .review\desktop-server.log in the site folder.' }
            Start-Sleep -Milliseconds 500
        }
    }
    Start-Process $siteUrl
} catch {
    Add-Type -AssemblyName System.Windows.Forms
    [System.Windows.Forms.MessageBox]::Show($_.Exception.Message, 'Portfolio launcher') | Out-Null
    exit 1
}
