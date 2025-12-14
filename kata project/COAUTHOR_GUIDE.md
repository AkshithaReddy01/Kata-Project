# How to Add Co-Author to Git Commits

## Method 1: Using the Script (Recommended)

Use the provided PowerShell script:

```powershell
.\add-coauthor.ps1 "Your commit message"
```

Or with custom co-author:

```powershell
.\add-coauthor.ps1 "feat: Add new feature" "GitHub Copilot" "copilot@users.noreply.github.com"
```

## Method 2: Manual Git Command

For new commits, use this format:

```powershell
git commit -m "Your commit message here


Co-authored-by: Cursor AI <cursor-ai@users.noreply.github.com>"
```

**Important:** Notice the two empty lines between the commit message and the co-author line!

## Method 3: Amend Existing Commit

To add co-author to the last commit:

```powershell
git commit --amend -m "Your original message


Co-authored-by: Cursor AI <cursor-ai@users.noreply.github.com>"
```

## Method 4: Using Git Template

The repository is configured with a commit template (`.gitmessage`) that includes the co-author format. When you run `git commit` without `-m`, it will open your editor with the template.

## Example Commit Messages

### Feature with AI assistance:
```
feat: Implement user registration endpoint

Used Cursor AI to generate the initial boilerplate for the
controller and service, then manually added validation logic.

Co-authored-by: Cursor AI <cursor-ai@users.noreply.github.com>
```

### Bug fix with AI help:
```
fix: Resolve authentication token expiration issue

Cursor AI suggested the token refresh pattern, which I
implemented and tested manually.

Co-authored-by: Cursor AI <cursor-ai@users.noreply.github.com>
```

### Documentation update:
```
docs: Update README with setup instructions

Co-authored-by: Cursor AI <cursor-ai@users.noreply.github.com>
```

## Multiple Co-Authors

You can add multiple co-authors:

```
feat: Add shopping cart functionality

Co-authored-by: Cursor AI <cursor-ai@users.noreply.github.com>
Co-authored-by: GitHub Copilot <copilot@users.noreply.github.com>
```

## Viewing Co-Authors

To see co-authors in commit history:

```powershell
git log --format=fuller
```

Or for a specific commit:

```powershell
git show --format=fuller <commit-hash>
```

## Notes

- The co-author email format `@users.noreply.github.com` is a GitHub convention for AI tools
- Co-authors appear in the commit history and contribute to your GitHub contribution graph
- Always use two empty lines between the commit message body and the co-author trailer
- The format follows the [Git trailer convention](https://git-scm.com/docs/git-interpret-trailers)

