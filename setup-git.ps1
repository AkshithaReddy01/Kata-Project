# Git Setup and Push Script
# Run this after Git is installed

$ErrorActionPreference = "Stop"

# Navigate to project directory
Set-Location "C:\Users\USER\Downloads\kata project\kata project"

# Refresh PATH to include Git
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Check if Git is available
try {
    $gitVersion = git --version
    Write-Host "Git found: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "Git not found. Please restart your terminal after Git installation." -ForegroundColor Red
    Write-Host "Or add Git to PATH manually: C:\Program Files\Git\bin" -ForegroundColor Yellow
    exit 1
}

# Initialize Git repository if not already initialized
if (!(Test-Path ".git")) {
    Write-Host "Initializing Git repository..." -ForegroundColor Yellow
    git init
}

# Configure Git (you'll need to provide these)
Write-Host ""
Write-Host "Please provide the following information:" -ForegroundColor Cyan
Write-Host "1. Your Git username"
Write-Host "2. Your Git email"
Write-Host "3. Your GitHub/GitLab repository URL (e.g., https://github.com/username/repo.git)"
Write-Host ""
Write-Host "After providing these, run:" -ForegroundColor Yellow
Write-Host "  git config user.name 'Your Name'"
Write-Host "  git config user.email 'your.email@example.com'"
Write-Host "  git remote add origin YOUR_REPO_URL"
Write-Host "  git add ."
Write-Host "  git commit -m 'Initial commit'"
Write-Host "  git push -u origin main"
Write-Host ""

