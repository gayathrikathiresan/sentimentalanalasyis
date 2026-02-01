# How to Deploy on Vercel - Simple Steps

## Step 1: Connect GitHub to Vercel
1. Go to https://vercel.com
2. Click **"Sign Up"** (or login if you have account)
3. Select **"Continue with GitHub"**
4. Authorize Vercel to access your GitHub

## Step 2: Import Your Project
1. Click **"New Project"**
2. Click **"Import Git Repository"**
3. Find and select your repo: **sentimentalanalasyis**
4. Click **"Import"**

## Step 3: Configure Project (Just Click Next)
1. Leave all settings as default
2. Click **"Deploy"**
3. Wait 2-3 minutes for deployment

## Step 4: Your App is Live!
- Vercel will give you a URL like: `https://your-app.vercel.app`
- Your API will be at: `https://your-app.vercel.app/api/predict`
- Frontend will be at: `https://your-app.vercel.app`

## What I Already Set Up For You:
✅ `vercel.json` - tells Vercel how to run your app
✅ `api/predict.py` - serverless API function
✅ `requirements.txt` - all dependencies

## IMPORTANT: Upload Model File to GitHub
Your `best_fer_model.h5` file is NOT in GitHub (too large).

**Option 1: Remove from .gitignore and try (might fail if >100MB)**
```
Edit .gitignore and remove: *.h5
Then: git add best_fer_model.h5
      git commit -m "Add model file"
      git push
```

**Option 2: Use Vercel Environment (Better)**
- Upload model to free cloud storage (Google Drive, Dropbox)
- Download it during deployment using API

That's it! Your app will work on Vercel automatically.
