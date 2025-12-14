# How to Add Screenshots to Git

## Step 1: Save Your Screenshots

Save your screenshots with these exact names in the `screenshots` folder:

1. `login.png` - Your login page screenshot
2. `dashboard.png` - Your main dashboard with sweets listing
3. `search-filter.png` - Your search and filter interface
4. `cart.png` - Your shopping cart screenshot
5. `product-cards.png` - Your product cards view (optional)

## Step 2: Add to Git

After saving the images, run these commands:

```powershell
cd "C:\Users\USER\Downloads\kata project\kata project"
git add screenshots/
git commit -m "Add application screenshots"
git push origin main
```

## Alternative: Quick Add

If you've already saved the images in the screenshots folder, just run:

```powershell
cd "C:\Users\USER\Downloads\kata project\kata project"
git add .
git commit -m "Add application screenshots"
git push origin main
```

The README.md is already configured to display these images automatically!

