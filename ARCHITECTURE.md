# 📊 Architecture & Data Flow Diagram

## **Local Development Setup**

```
┌────────────────────────────────────────────────────────────────┐
│                    YOUR COMPUTER                               │
│                                                                │
│  ┌──────────────────┐                 ┌──────────────────┐   │
│  │   FRONTEND       │                 │   BACKEND        │   │
│  │ (index.html)     │                 │  (main.py)       │   │
│  │                  │                 │                  │   │
│  │  - Upload UI     │                 │  - FastAPI       │   │
│  │  - Drag & Drop   │                 │  - PDF parsing   │   │
│  │  - Display Res.  │                 │  - CORS enabled  │   │
│  │                  │                 │                  │   │
│  │  PORT: 5000*     │   POST Request  │  PORT: 5000      │   │
│  │ (via browser)    │────────────────→│                  │   │
│  │                  │ file + metadata │                  │   │
│  │                  │                 │  Process File    │   │
│  │                  │                 │  Extract Text    │   │
│  │                  │ JSON Response   │  Return String   │   │
│  │                  │←────────────────│                  │   │
│  │                  │ {output: "..."}│                  │   │
│  │                  │                 │                  │   │
│  │ Display Output   │                 │                  │   │
│  └──────────────────┘                 └──────────────────┘   │
└────────────────────────────────────────────────────────────────┘

        ↓ (When ready to deploy)

┌────────────────────────────────────────────────────────────────┐
│                    PRODUCTION (Cloud)                          │
│                                                                │
│  ┌──────────────────┐                 ┌──────────────────┐   │
│  │   NETLIFY        │                 │    RAILWAY       │   │
│  │  (Static Site)   │                 │  (Backend API)   │   │
│  │                  │                 │                  │   │
│  │  index.html      │   POST /upload  │  main.py         │   │
│  │  CSS + JS        │────────────────→│  uvicorn         │   │
│  │  CDN Optimized   │ file + metadata │  (Managed)       │   │
│  │                  │                 │                  │   │
│  │                  │ JSON Response   │  Env Variables   │   │
│  │                  │←────────────────│  - ALLOWED_*     │   │
│  │                  │ {output: "..."}│  - MAX_FILE_SIZE │   │
│  │                  │                 │                  │   │
│  │ Display Output   │                 │  Auto Scaling    │   │
│  └──────────────────┘                 └──────────────────┘   │
└────────────────────────────────────────────────────────────────┘
     ▲ Global CDN                            ▲ Always Available
     │                                       │
     └───────────────────┬───────────────────┘
                         │ Git Push Auto-Deploy
                         │
                    GitHub Repo
```

---

## **Request-Response Flow (Detailed)**

### **1. User Uploads File**
```
┌─────────┐
│ Browser │
└────┬────┘
     │
     │ 1. User clicks upload area
     │ 2. Selects test.txt
     │ 3. Frontend reads file
     │ 4. Creates FormData
     ▼
┌────────────────────────────────┐
│ FormData {                     │
│   file: File(test.txt)         │
│   size: 256 bytes              │
│ }                              │
└────┬───────────────────────────┘
     │
     │ POST /upload
     │ Content-Type: multipart/form-data
     │
     ▼
```

### **2. Backend Processes**
```
┌──────────────────────────────────┐
│ FastAPI /upload endpoint          │
├──────────────────────────────────┤
│ 1. Receive file                  │
│ 2. Check extension (.txt/.pdf)   │
│ 3. Check file size               │
│ 4. Decode/Extract text           │
│ 5. Return JSON response          │
└────┬─────────────────────────────┘
     │
     ▼
┌──────────────────────────────────┐
│ Response JSON {                  │
│   "filename": "test.txt",        │
│   "file_type": ".txt",           │
│   "output": "File content...",   │
│   "status": "success",           │
│   "file_size": 256               │
│ }                                │
└────┬─────────────────────────────┘
     │
     │ HTTP 200 OK
     │
     ▼
```

### **3. Frontend Displays**
```
┌──────────────────────────────────┐
│ Browser receives JSON            │
├──────────────────────────────────┤
│ 1. Parse response                │
│ 2. Extract output field          │
│ 3. Update UI                     │
│ 4. Show file name                │
│ 5. Display output text           │
│ 6. Enable download button        │
└────┬─────────────────────────────┘
     │
     ▼
┌──────────────────────────────────┐
│ ✅ User sees:                    │
│                                  │
│ 📎 test.txt                      │
│ [✓ Ready to process]             │
│                                  │
│ 📄 Output Result:                │
│ This is a test file!             │
│ You can upload this...           │
│                                  │
│ [↺ Upload Another] [⬇Download] │
└──────────────────────────────────┘
```

---

## **File Processing Logic**

```
┌─ File Upload
│
├─→ Is it .txt?
│   └─→ YES: Read as UTF-8 text
│       Return decoded string
│
├─→ Is it .pdf?
│   └─→ YES: Use PyPDF2
│       Extract text from each page
│       Combine pages
│       Return combined text
│
└─→ Something else?
    └─→ NO: Return 400 error
        "File type not supported"
```

---

## **CORS & Security Flow**

```
Browser Request
      ↓
From: https://frontend-site.netlify.app
To: https://backend-api.railway.app
      ↓
Backend checks: Is origin allowed?
      ├─ YES: In ALLOWED_ORIGINS env var
      │       ↓ Add CORS headers
      │       ↓ Allow request
      │       ✅ Response sent
      │
      └─ NO: Not in allowed origins
              ↓ Reject request
              ❌ CORS Error in console
```

---

## **Data Flow: From Upload to Download**

```
Step 1: User Action
┌─────────────────────┐
│ Drag file to upload │
└─────┬───────────────┘
      │
      ▼
Step 2: Frontend
┌────────────────────────┐
│ Read file with FileAPI │
└─────┬──────────────────┘
      │
      ▼
Step 3: HTTP POST
┌──────────────────────────┐
│ Send multipart/form-data │
└─────┬────────────────────┘
      │
      ▼
Step 4: Backend Receives
┌──────────────────────┐
│ UploadFile object    │
│ Validate extension   │
│ Check file size      │
└─────┬────────────────┘
      │
      ▼
Step 5: Processing
┌───────────────────────┐
│ .txt → Read UTF-8     │
│ .pdf → Extract text   │
└─────┬─────────────────┘
      │
      ▼
Step 6: Return Response
┌──────────────────────────┐
│ JSON with:               │
│ - filename               │
│ - file_type              │
│ - output (processed)     │
│ - status                 │
└─────┬────────────────────┘
      │
      ▼
Step 7: Frontend Display
┌───────────────────────────┐
│ Show output in text box   │
│ Enable download button    │
└─────┬─────────────────────┘
      │
      ▼
Step 8: Download (Optional)
┌──────────────────────────────┐
│ Create blob from output text │
│ Generate download URL        │
│ User clicks download         │
│ Saves as output_*.txt        │
└──────────────────────────────┘
```

---

## **Error Handling Flow**

```
Upload triggers

     ↓
┌────────────────────────────────────┐
│ Try block: Process file            │
└────┬─────────────────────────────┬─┘
     │                             │
     ▼ Success                     ▼ Error
   JSON Response          ┌──────────────────────┐
   200 OK                 │ Exception caught     │
   {output: "..."}        │                      │
                          │ Type?                │
                          ├─ FileNotAllowed     │
                          │  └→ 400 error       │
                          ├─ FileTooLarge       │
                          │  └→ 413 error       │
                          ├─ DecodeError        │
                          │  └→ 400 error       │
                          ├─ PDFError           │
                          │  └→ 500 error       │
                          └─ Other              │
                             └→ 500 error       │
     
        ▼                           ▼
     Frontend            Error message shown
     shows output        User can retry
```

---

## **Production Deployment Architecture**

```
          ┌─────────────────────────────────────┐
          │         Your GitHub Repo            │
          │      file-upload-app                │
          └────┬─────────────────────────────┬──┘
               │ On push                     │ On push
               │ to main                     │ to main
               ▼                            ▼
        ┌──────────────┐          ┌────────────────┐
        │   Railway    │          │    Netlify     │
        │   CI/CD      │          │    CI/CD        │
        └──────┬───────┘          └────┬───────────┘
               │                       │
               │ Auto-builds &         │ Auto-builds &
               │ deploys               │ deploys
               │                       │
               ▼                       ▼
        ┌──────────────────┐  ┌──────────────────┐
        │    Backend       │  │    Frontend      │
        │  API Running     │  │  Static Files    │
        │  Uvicorn:5000    │  │  CDN Cached      │
        │                  │  │                  │
        │ https://api...   │  │ https://app...   │
        └──────┬───────────┘  └────┬─────────────┘
               │                   │
               └───────┬───────────┘
                       │
                       ▼
                   Users Access
                   Full Application
```

---

## **Key Endpoints**

```
GET http://localhost:5000/
├─ Returns: Server status message
├─ Used for: Health check
└─ No auth needed

GET http://localhost:5000/health
├─ Returns: {"status": "healthy", ...}
├─ Used for: Monitoring
└─ No auth needed

POST http://localhost:5000/upload
├─ Accepts: multipart/form-data with file
├─ Returns: {"filename": "...", "output": "..."}
├─ Used for: File processing
├─ Validation:
│  ├─ File extension must be .txt or .pdf
│  ├─ File size < MAX_FILE_SIZE
│  └─ File must be readable
└─ Error codes:
   ├─ 200: Success
   ├─ 400: Bad request (invalid file type, decode error)
   ├─ 413: Payload too large
   └─ 500: Server error

GET /docs
├─ Returns: Interactive API documentation
├─ Powered by: Swagger UI
└─ Useful for: API testing
```

---

**This architecture supports:**
- ✅ Multiple concurrent uploads
- ✅ Cross-platform (Windows, Mac, Linux)
- ✅ Mobile-responsive UI
- ✅ Fast CDN delivery (frontend)
- ✅ Scalable backend (Railway auto-scales)
- ✅ Automatic HTTPS
- ✅ Zero-downtime deployments
