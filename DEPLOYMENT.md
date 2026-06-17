# 🚀 Deployment Guide

This guide covers multiple deployment options for your file upload application.

---

## **Option 1: Render.com (Backend) + Netlify (Frontend) ⭐ RECOMMENDED**

### Backend Deployment on Render

1. **Push code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Create account at [render.com](https://render.com)**

3. **Deploy Backend**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Set runtime: `Python 3.11`
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn main.py:app --host 0.0.0.0 --port 8000`
   - Click "Create Web Service"

4. **Get your backend URL** (e.g., `https://your-app.onrender.com`)

### Frontend Deployment on Netlify

1. **Update API URL in index.html**
   ```javascript
   const API_URL = 'https://your-app.onrender.com/upload';
   ```

2. **Create account at [netlify.com](https://netlify.com)**

3. **Deploy Frontend**
   - Drag & drop your `index.html` folder
   - Or connect GitHub repository
   - Deploy!

✅ **Cost:** Free tier available | **Uptime:** Good

---

## **Option 2: Docker Deployment (Production-Ready)**

### Prerequisites
- Install Docker from [docker.com](https://docker.com)

### Build & Run Locally
```bash
# Build Docker image
docker build -t file-upload-app .

# Run container
docker run -p 5000:5000 file-upload-app

# Or use docker-compose
docker-compose up
```

### Deploy Docker to Cloud Platforms

#### **Fly.io**
```bash
# Install Fly CLI
# curl https://fly.io/install.sh | sh

flyctl auth login
flyctl launch
flyctl deploy
```

#### **AWS (ECS/Elastic Beanstalk)**
```bash
# Push to AWS ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <your-ecr-uri>
docker tag file-upload-app:latest <your-ecr-uri>/file-upload-app:latest
docker push <your-ecr-uri>/file-upload-app:latest

# Then deploy to ECS/Elastic Beanstalk
```

---

## **Option 3: Google Cloud Run (Serverless)**

1. **Install Google Cloud CLI**
   ```bash
   # Download from cloud.google.com/sdk
   ```

2. **Build & Deploy**
   ```bash
   gcloud run deploy file-upload-app \
     --source . \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

✅ **Cost:** ~$0.40/million requests | **Uptime:** Excellent

---

## **Option 4: DigitalOcean (VPS/App Platform)**

### Using App Platform (Simple)
1. Create account at [digitalocean.com](https://digitalocean.com)
2. Connect GitHub repository
3. Set runtime to Python
4. Deploy with one click

### Using Droplet (VPS)
```bash
# SSH into your server
ssh root@your-droplet-ip

# Install Python & dependencies
apt update
apt install python3-pip

# Clone your repo & run
git clone your-repo-url
cd your-repo
pip install -r requirements.txt
uvicorn main.py:app --host 0.0.0.0 --port 80

# Or use systemd/supervisor for background service
```

---

## **Option 5: Railway.app (Simplest)**

1. Create account at [railway.app](https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub"
4. Connect repository
5. Click "Deploy"
6. Railway auto-detects Python & deploys!

✅ **Pros:** Easiest setup | **Cost:** Pay-as-you-go ($5-50/month typically)

---

## **Option 6: PythonAnywhere (Python-Specific)**

1. Create account at [pythonanywhere.com](https://pythonanywhere.com)
2. Upload files via Web UI
3. Create web app with FastAPI
4. Configure to point to `main.py`
5. Deploy!

✅ **Cost:** Free tier available

---

## **Environment Setup for Production**

### Create `.env` file
```
BACKEND_URL=https://your-app.onrender.com
FRONTEND_URL=https://your-frontend.netlify.app
```

### Update CORS settings in `main.py` for production
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-frontend.netlify.app",
        "https://www.your-domain.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## **Comparison Table**

| Platform | Backend | Frontend | Cost | Setup Time | Uptime |
|----------|---------|----------|------|------------|--------|
| **Render + Netlify** | ✅ | ✅ | Free-$7 | 10 min | 99.5% |
| **Fly.io** | ✅ | ✅ | Free-$15 | 5 min | 99.9% |
| **Google Cloud Run** | ✅ | ✅ | Free-$100 | 10 min | 99.95% |
| **Railway** | ✅ | ✅ | Free-$50 | 5 min | 99.9% |
| **DigitalOcean** | ✅ | ✅ | $5-25/mo | 20 min | 99.9% |
| **Docker Local** | ✅ | ✅ | Free | 2 min | N/A |

---

## **Quick Start Commands**

### For Render
```bash
# No special commands - connect GitHub and deploy!
```

### For Docker
```bash
docker build -t my-app .
docker run -p 5000:5000 my-app
```

### For Google Cloud Run
```bash
gcloud run deploy --source .
```

---

## **Troubleshooting**

### CORS Errors
- Make sure frontend URL is in `allow_origins` in main.py
- Check that API URL is correct in index.html

### File Upload Size Limits
- Add to `main.py`:
```python
@app.post("/upload")
async def upload_file(file: UploadFile = File(..., max_size=10_000_000)):  # 10MB
```

### Port Issues
- Render/Railway provide `PORT` environment variable
- Use: `port=int(os.getenv("PORT", 5000))`

---

## **Recommended Stack for Production**

1. **Backend:** Render.com or Railway.app (easiest)
2. **Frontend:** Netlify or Vercel (fast, CDN)
3. **Database:** (if needed) PostgreSQL on Railway or AWS RDS
4. **File Storage:** AWS S3 or similar (for production file uploads)

---

**Next Steps:**
- Choose a deployment platform
- Update CORS settings
- Deploy backend
- Update frontend API URL
- Deploy frontend
- Test end-to-end!
