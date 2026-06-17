# 🚀 Quick Deployment Reference

## **⭐ BEST OPTIONS (Pick One)**

### 1. **Render + Netlify** (Easiest for beginners)
- **Backend:** render.com
- **Frontend:** netlify.com
- **Time:** 15 minutes
- **Cost:** Free-$7/month
- **Steps:** Connect GitHub → Deploy → Done

### 2. **Railway** (All-in-one simplest)
- **Time:** 5 minutes
- **Cost:** Free-$50/month
- **Steps:** Connect GitHub → Deploy → Done
- **Website:** railway.app

### 3. **Docker + Fly.io** (Production-ready)
- **Time:** 10 minutes
- **Cost:** Free-$15/month
- **Steps:**
  ```bash
  flyctl launch
  flyctl deploy
  ```

---

## **STEP-BY-STEP: Render + Netlify (Recommended)**

### Backend on Render
```
1. Go to render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repo
4. Runtime: Python 3.11
5. Build: pip install -r requirements.txt
6. Start: uvicorn main.py:app --host 0.0.0.0 --port 8000
7. Deploy!
```

### Frontend on Netlify
```
1. Go to netlify.com
2. Drag & drop your demo folder (or GitHub)
3. Update API_URL in index.html to Render URL
4. Deploy!
```

---

## **DOCKER QUICK START**

```bash
# Build
docker build -t file-upload-app .

# Run locally
docker run -p 5000:5000 file-upload-app

# Deploy to Fly.io
flyctl launch
flyctl deploy
```

---

## **ENVIRONMENT VARIABLES**

Create `.env` file:
```
PORT=5000
ALLOWED_ORIGINS=https://your-frontend.netlify.app
MAX_FILE_SIZE=10000000
```

---

## **FILES TO REMEMBER**

✅ **For all deployments:**
- `main.py` - Backend
- `index.html` - Frontend
- `requirements.txt` - Dependencies
- `.env` - Configuration

✅ **For Docker:**
- `Dockerfile` - Docker config
- `docker-compose.yml` - Docker Compose

✅ **For Git/GitHub:**
- `.gitignore` - Hide sensitive files

---

## **DEPLOYMENT CHECKLIST**

- [ ] Update CORS origins in main.py
- [ ] Update API_URL in index.html
- [ ] Create .env with environment variables
- [ ] Push to GitHub
- [ ] Choose platform (Render/Railway/Fly.io)
- [ ] Connect GitHub repo
- [ ] Set environment variables on platform
- [ ] Deploy
- [ ] Test upload functionality
- [ ] Set custom domain (optional)

---

## **COST COMPARISON**

| Platform | Frontend | Backend | Monthly Cost |
|----------|----------|---------|--------------|
| **Render** | Free | $7 | $7 |
| **Netlify** | Free | - | $0-19 |
| **Railway** | Included | Included | Free-$50 |
| **Fly.io** | Included | Included | Free-$15 |
| **Google Cloud** | Free | Usage-based | $0-100 |

---

## **NEED HELP?**

1. **Local Testing:** `python main.py` then open `index.html`
2. **Docker Testing:** `docker-compose up`
3. **See DEPLOYMENT.md** for detailed guides
4. **Check CORS errors** - Update allowed origins
5. **Check API URL** - Make sure frontend points to right backend

---

**Ready to deploy? Pick Railway or Render and you'll be live in 10 minutes!** 🚀
