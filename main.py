from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import PyPDF2
import io

app = FastAPI()

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)) -> dict:
    """
    Upload and process a file (.txt or .pdf)
    Returns the processed content as a string
    """
    allowed_extensions = {".txt", ".pdf"}
    
    # Check file extension
    file_extension = "." + file.filename.split(".")[-1].lower() if "." in file.filename else ""
    if file_extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"File type not supported. Allowed: {allowed_extensions}"
        )
    
    try:
        file_content = await file.read()
        
        # Process based on file type
        if file_extension == ".txt":
            output = file_content.decode("utf-8")
        elif file_extension == ".pdf":
            output = extract_text_from_pdf(file_content)
        
        return {
            "filename": file.filename,
            "file_type": file_extension,
            "output": output,
            "status": "success"
        }
    
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
        return text
    except Exception as e:
        raise Exception(f"Failed to extract PDF text: {str(e)}")


@app.get("/")
def read_root():
    """Health check endpoint"""
    return {"message": "File Upload Server is running", "endpoint": "/upload"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
