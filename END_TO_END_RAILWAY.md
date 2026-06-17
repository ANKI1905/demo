# 🚀 Complete End-to-End Deployment with Railway.app

This guide walks through deploying your file upload app using Railway.app in 10 minutes.

---

## **PHASE 1: Prepare Local Code** ✅ (DONE)

Your code is already prepared:
```
✅ main.py - Backend API
✅ index.html - Frontend
✅ requirements.txt - Dependencies
✅ Dockerfile - Container config
✅ .env.example - Environment template
✅ .gitignore - Git ignore rules
✅ Git repository initialized
```

---

## **PHASE 2: Create GitHub Repository** (5 minutes)

### Step 2.1: Push to GitHub

1. **Go to [github.com](https://github.com) and log in**

2. **Create new repository:**
   - Click "+" → "New repository"
   - Name: `file-upload-app`
   - Description: "File upload and processing application with FastAPI"
   - Choose Public (for free deployment)
   - Click "Create repository"

3. **Get your repository URL** (e.g., `https://github.com/your-username/file-upload-app.git`)

4. **Push from your computer:**
   ```bash
   cd c:\Users\ankit\OneDrive\Desktop\demo
   git remote add origin https://github.com/YOUR-USERNAME/file-upload-app.git
   git branch -M main
   git push -u origin main
   ```

✅ **Your code is now on GitHub!**

---

## **PHASE 3: Deploy on Railway** (3 minutes)

### Step 3.1: Sign Up on Railway

1. Go to **[railway.app](https://railway.app)**
2. Click "Start Project"
3. Choose "GitHub" login
4. Authorize GitHub access
5. Select your `file-upload-app` repository

### Step 3.2: Configure Railway

Railway auto-detects Python! Just:

1. **Railway shows your project structure**
2. **Click "Deploy"** 
3. **Wait 2-3 minutes...**

✅ **Your backend is live!** You'll get a URL like:
```
https://file-upload-app-production.up.railway.app
```

---

## **PHASE 4: Deploy Frontend** (2 minutes)

### Option A: Deploy Frontend on Netlify (Recommended)

1. Go to **[netlify.com](https://netlify.com)**
2. Click "Add new site"
3. Choose "Deploy manually"
4. Drag & drop your `demo` folder
5. Netlify auto-detects it's a static site
6. **Wait for deployment...**

✅ **Your frontend is live!** You'll get a URL like:
```
https://file-upload-app-123456.netlify.app
```

### Option B: Host Frontend on Railway Too

1. Create `railway.json` in your demo folder:
   ```json
   {
     "build": {
       "builder": "static"
     },
     "deploy": {
       "static": "./"
     }
   }
   ```
2. Push to GitHub
3. Railway auto-deploys!

---

## **PHASE 5: Connect Frontend to Backend** (2 minutes)

### Step 5.1: Update Frontend API URL

Edit `index.html` and change:
```javascript
// OLD:
const API_URL = 'http://localhost:5000/upload';

// NEW:
const API_URL = 'https://file-upload-app-production.up.railway.app/upload';
```

### Step 5.2: Update CORS on Backend

Edit Railway project settings:

1. Go to Railway dashboard
2. Your `file-upload-app` project
3. Variables tab
4. Add:
   ```
   ALLOWED_ORIGINS=https://file-upload-app-123456.netlify.app,https://www.your-domain.com
   ```

5. Click "Deploy"

---

## **PHASE 6: Test End-to-End** (2 minutes)

### Step 6.1: Test Backend API

```bash
curl -X GET https://file-upload-app-production.up.railway.app/health
```

Response:
```json
{"status": "healthy", "service": "file-upload-api"}
```

### Step 6.2: Test Frontend

1. Go to `https://file-upload-app-123456.netlify.app`
2. Upload your test file
3. Should see output immediately!

✅ **IT WORKS!**

---

## **PHASE 7: Add Custom Domain (Optional - 5 minutes)**

### For Backend (Railway)

1. Go to Railway project
2. Settings → Domains
3. Add custom domain
4. Update DNS records

### For Frontend (Netlify)

1. Netlify dashboard
2. Domain settings
3. Connect your domain
4. Netlify handles SSL!

---

## **COMPLETE ARCHITECTURE**

```
┌─────────────────────────────────────────────┐
│         Your Computer                       │
│  (Local Development & Testing)              │
│  - main.py (backend)                        │
│  - index.html (frontend)                    │
│  - Python 3.11 + dependencies               │
└──────────────────┬──────────────────────────┘
                   │ git push
                   ▼
┌─────────────────────────────────────────────┐
│         GitHub Repository                   │
│  (Version Control & CI/CD Source)           │
│  - file-upload-app                          │
└──────────────────┬──────────────────────────┘
        │                          │
        │ auto-deploys            │ auto-deploys
        ▼                          ▼
┌──────────────────────┐  ┌────────────────────┐
│  Railway (Backend)   │  │  Netlify (Frontend)│
│  ✅ Production API   │  │  ✅ Static Site    │
│  Port: 5000          │  │  CDN: Global       │
│  URL: railway.app    │  │  URL: netlify.app  │
└──────────────────────┘  └────────────────────┘
        │                          │
        │ POST /upload             │
        │◄─────────────────────────┤
        │                          │
        └──► Processes file        │
        │                          │
        └──── Returns output ─────►│
                                   │
                          ✅ User sees result
```

---

## **ENVIRONMENT VARIABLES ON RAILWAY**

Railway sets these automatically:
- `PORT` - 5000
- `HOST` - 0.0.0.0

You can add custom variables:
```
ALLOWED_ORIGINS=https://your-frontend-url.netlify.app
MAX_FILE_SIZE=10000000
```

---

## **MONITORING & LOGS**

### View Backend Logs
```
Railway Dashboard → Your Project → Logs Tab
```

### View Frontend Logs
```
Netlify Dashboard → Your Site → Deployments → Logs
```

---

## **TROUBLESHOOTING**

### ❌ "CORS Error" 
**Solution:** Update `ALLOWED_ORIGINS` in Railway variables

### ❌ "Cannot find backend"
**Solution:** Verify URL in index.html matches Railway URL

### ❌ "File upload fails"
**Solution:** Check file size limit in `MAX_FILE_SIZE` variable

### ❌ "Deployment failed"
**Solution:** Check Railway logs for Python errors

---

## **TOTAL TIME: ~15 MINUTES**

| Phase | Time | Action |
|-------|------|--------|
| 1. Prepare code | ✅ DONE | Already done |
| 2. GitHub push | 5 min | Push repository |
| 3. Railway deploy | 3 min | Click & wait |
| 4. Netlify deploy | 2 min | Drag & drop |
| 5. Connect | 2 min | Update URLs |
| 6. Test | 2 min | Upload file |
| **TOTAL** | **15 min** | **APP LIVE!** |

---

## **COST**

- **Railway:** Free for first 5GB/month ($5/month after)
- **Netlify:** Free for static sites
- **GitHub:** Free repository
- **Total:** ~$5/month (or free if under limits)

---

## **NEXT STEPS**

1. ✅ Already done: Code prepared in Git
2. ⏭️ Push to GitHub
3. ⏭️ Deploy on Railway
4. ⏭️ Deploy on Netlify
5. ⏭️ Connect them
6. ⏭️ Test!

**Everything is ready. Just follow the steps above!** 🎉

---

## **COMMANDS CHEAT SHEET**

```bash
# Push to GitHub
cd c:\Users\ankit\OneDrive\Desktop\demo
git remote add origin https://github.com/YOUR-USERNAME/file-upload-app.git
git branch -M main
git push -u origin main

# Test locally before deploying
python main.py
# Open index.html in browser

# View what's in your repo
git log
git status
```

---

**Ready? Let's deploy! 🚀**
