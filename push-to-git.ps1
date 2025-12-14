# Complete Git Setup and Push Script
# Run this script to push your code to Git

param(
    [string]$GitUsername = "",
    [string]$GitEmail = "",
    [string]$RepoUrl = ""
)

$ErrorActionPreference = "Stop"

# Navigate to project directory
$projectPath = "C:\Users\USER\Downloads\kata project\kata project"
Set-Location $projectPath

# Refresh PATH
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Try to find Git
$gitPath = $null
$possiblePaths = @(
    "C:\Program Files\Git\bin\git.exe",
    "C:\Program Files (x86)\Git\bin\git.exe",
    "git"
)

foreach ($path in $possiblePaths) {
    if ($path -eq "git") {
        try {
            $null = & git --version 2>&1
            $gitPath = "git"
            break
        } catch {
            continue
        }
    } else {
        if (Test-Path $path) {
            $gitPath = $path
            break
        }
    }
}

if (!$gitPath) {
    Write-Host "ERROR: Git not found!" -ForegroundColor Red
    Write-Host "Please install Git from: https://git-scm.com/download/win" -ForegroundColor Yellow
    Write-Host "Or restart your terminal after installation." -ForegroundColor Yellow
    exit 1
}

Write-Host "Git found! Proceeding with setup..." -ForegroundColor Green

# Get Git credentials if not provided
if (!$GitUsername) {
    $GitUsername = Read-Host "Enter your Git username"
}
if (!$GitEmail) {
    $GitEmail = Read-Host "Enter your Git email"
}
if (!$RepoUrl) {
    $RepoUrl = Read-Host "Enter your repository URL (e.g., https://github.com/username/repo.git)"
}

# Configure Git
Write-Host "Configuring Git..." -ForegroundColor Yellow
& $gitPath config user.name $GitUsername
& $gitPath config user.email $GitEmail

# Initialize repository if needed
if (!(Test-Path ".git")) {
    Write-Host "Initializing Git repository..." -ForegroundColor Yellow
    & $gitPath init
}

# Check if remote exists
$remoteExists = & $gitPath remote get-url origin 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "Adding remote repository..." -ForegroundColor Yellow
    & $gitPath remote add origin $RepoUrl
} else {
    Write-Host "Remote already exists. Updating..." -ForegroundColor Yellow
    & $gitPath remote set-url origin $RepoUrl
}

# Add all files
Write-Host "Adding files to Git..." -ForegroundColor Yellow
& $gitPath add .

# Commit
Write-Host "Creating commit..." -ForegroundColor Yellow
$commitMessage = "Initial commit: Sweet Shop Management System"
& $gitPath commit -m $commitMessage

# Check current branch
$currentBranch = & $gitPath branch --show-current 2>&1
if (!$currentBranch -or $currentBranch -eq "") {
    & $gitPath branch -M main
    $currentBranch = "main"
}

# Push to repository
Write-Host "Pushing to repository..." -ForegroundColor Yellow
& $gitPath push -u origin $currentBranch

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "SUCCESS! Code pushed to Git repository!" -ForegroundColor Green
    Write-Host "Repository URL: $RepoUrl" -ForegroundColor Cyan
} else {
    Write-Host ""
    Write-Host "Push failed. You may need to:" -ForegroundColor Red
    Write-Host "1. Set up authentication (SSH key or Personal Access Token)" -ForegroundColor Yellow
    Write-Host "2. Check your repository URL" -ForegroundColor Yellow
    Write-Host "3. Make sure the repository exists and you have access" -ForegroundColor Yellow
}

