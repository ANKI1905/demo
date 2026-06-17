import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import PyPDF2
import io

app = FastAPI(title="File Upload API", version="1.0.0")

# Configuration from environment variables
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:5000,http://localhost:3000").split(",")
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", 10_000_000))  # 10MB default
ALLOWED_EXTENSIONS = {".txt", ".pdf"}

# Enable CORS with configurable origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    """Health check endpoint for monitoring"""
    return {"status": "healthy", "service": "file-upload-api"}


@app.get("/")
def read_root():
    """Root endpoint"""
    return {
        "message": "File Upload Server is running",
        "endpoint": "/upload",
        "docs": "/docs"
    }


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)) -> dict:
    """
    Upload and process a file (.txt or .pdf)
    
    Request: multipart/form-data with file
    Response: JSON with processed output
    """
    # Check file extension
    file_extension = "." + file.filename.split(".")[-1].lower() if "." in file.filename else ""
    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"File type not supported. Allowed: {list(ALLOWED_EXTENSIONS)}"
        )
    
    try:
        file_content = await file.read()
        
        # Check file size
        if len(file_content) > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=413,
                detail=f"File too large. Max size: {MAX_FILE_SIZE} bytes"
            )
        
        # Process based on file type
        if file_extension == ".txt":
            output = file_content.decode("utf-8")
        elif file_extension == ".pdf":
            output = extract_text_from_pdf(file_content)
        
        return {
            "filename": file.filename,
            "file_type": file_extension,
            "output": output,
            "status": "success",
            "file_size": len(file_content)
        }
    
    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400,
            detail="Could not decode file. Ensure it's valid UTF-8 text."
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing file: {str(e)}"
        )


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """Extract text from PDF file"""
    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_bytes))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        raise Exception(f"Failed to extract PDF text: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    
    # Get port from environment, default to 5000
    port = int(os.getenv("PORT", 5000))
    host = os.getenv("HOST", "0.0.0.0")
    
    print(f"🚀 Starting server on {host}:{port}")
    print(f"📋 API Docs: http://localhost:{port}/docs")
    print(f"✅ Allowed origins: {ALLOWED_ORIGINS}")
    
    uvicorn.run(app, host=host, port=port)
