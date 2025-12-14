# 🚀 Quick Push to GitHub - 2 Minutes!

## Option 1: Create Repo on GitHub (Fastest - 1 minute)

1. **Go to**: https://github.com/new
2. **Repository name**: `sweet-shop-management`
3. **Description**: Sweet Shop Management System
4. **Visibility**: ✅ **Public**
5. **DO NOT** check any initialization boxes
6. Click **"Create repository"**

## Option 2: Use Personal Access Token

If you have a GitHub Personal Access Token:

```powershell
cd "C:\Users\USER\Downloads\kata project\kata project"
git remote set-url origin https://YOUR_TOKEN@github.com/akshithareddy01/sweet-shop-management.git
git push -u origin main
```

## After Repository is Created

Once the repository exists on GitHub, run:

```powershell
cd "C:\Users\USER\Downloads\kata project\kata project"
git push -u origin main
```

You'll be prompted for credentials - use your GitHub username and a Personal Access Token (not password).

## Create Personal Access Token

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Name: "Sweet Shop Project"
4. Select scopes: ✅ `repo` (full control)
5. Click "Generate token"
6. Copy the token and use it as password when pushing

---

**Your Repository URL will be:**
**https://github.com/akshithareddy01/sweet-shop-management**

