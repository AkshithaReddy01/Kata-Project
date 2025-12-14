# Script to add co-author to Git commits
# Usage: .\add-coauthor.ps1 "Your commit message" "Cursor AI" "cursor-ai@users.noreply.github.com"

param(
    [string]$Message = "",
    [string]$CoAuthorName = "Cursor AI",
    [string]$CoAuthorEmail = "cursor-ai@users.noreply.github.com"
)

if ($Message -eq "") {
    Write-Host "Usage: .\add-coauthor.ps1 'Your commit message' [CoAuthorName] [CoAuthorEmail]" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Example:" -ForegroundColor Cyan
    Write-Host "  .\add-coauthor.ps1 'feat: Add user authentication'"
    Write-Host "  .\add-coauthor.ps1 'fix: Resolve login bug' 'GitHub Copilot' 'copilot@users.noreply.github.com'"
    exit 1
}

$fullMessage = "$Message`n`nCo-authored-by: $CoAuthorName <$CoAuthorEmail>"

Write-Host "Commit message with co-author:" -ForegroundColor Green
Write-Host $fullMessage -ForegroundColor Cyan
Write-Host ""

$confirm = Read-Host "Proceed with commit? (y/n)"
if ($confirm -eq "y" -or $confirm -eq "Y") {
    git commit -m $fullMessage
    Write-Host "Commit created with co-author!" -ForegroundColor Green
} else {
    Write-Host "Commit cancelled." -ForegroundColor Yellow
}

