$ErrorActionPreference = "Stop"
$ProjectDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ProjectDir

if (-not (Test-Path ".venv\Scripts\python.exe")) {
    py -m venv .venv
}

& ".venv\Scripts\python.exe" -m pip install --upgrade pip
& ".venv\Scripts\python.exe" -m pip install -r requirements.txt

& ".venv\Scripts\pyinstaller.exe" `
    --noconfirm `
    --clean `
    --onefile `
    --windowed `
    --name merge_pdf `
    merge_pdf.py

$SplitArgs = @(
    "--noconfirm",
    "--clean",
    "--onefile",
    "--windowed",
    "--name", "split_pdf"
)

$SplitArgs += "split_pdf.py"
& ".venv\Scripts\pyinstaller.exe" @SplitArgs

Write-Host "Done. Programs are in the dist folder."
