# File Upload & Processing Application

A Python FastAPI backend with a modern frontend for uploading and processing files (.txt and .pdf).

## Features

- ✅ Upload .txt and .pdf files
- ✅ Extract and process file content
- ✅ Returns output as a string
- ✅ Beautiful, responsive UI
- ✅ Drag-and-drop support
- ✅ Download processed output

## Setup & Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Backend Server

```bash
python main.py
```

The server will start at `http://localhost:8000`

You can check if it's running by visiting: `http://localhost:8000/`

### 3. Open Frontend

Open `index.html` in your web browser (or use Live Server extension in VS Code)

Simply double-click the file or right-click → "Open with Live Server"

## API Endpoint

### POST `/upload`

Upload and process a file.

**Request:**
- Method: `POST`
- Content-Type: `multipart/form-data`
- Body: File (txt or pdf)

**Response:**
```json
{
  "filename": "example.txt",
  "file_type": ".txt",
  "output": "File content here...",
  "status": "success"
}
```

**Example cURL:**
```bash
curl -X POST \
  -F "file=@path/to/file.txt" \
  http://localhost:8000/upload
```

## File Structure

```
demo/
├── main.py           # FastAPI backend server
├── index.html        # Frontend UI
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Supported File Types

- `.txt` - Text files (plain text)
- `.pdf` - PDF documents (text extraction)

## Troubleshooting

### Error: "Backend server is not running"
Make sure you've started the backend:
```bash
python main.py
```

### PDF extraction not working
Ensure PyPDF2 is installed:
```bash
pip install PyPDF2 --upgrade
```

### CORS errors
The backend has CORS enabled for all origins during development. For production, modify the `CORSMiddleware` configuration in `main.py`.

## Customization

To modify file processing logic, edit the functions in `main.py`:
- `extract_text_from_pdf()` - Change PDF processing
- `upload_file()` - Add custom logic for different file types

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- PyPDF2
- Modern web browser

---

**Author:** Created with FastAPI and modern web technologies
