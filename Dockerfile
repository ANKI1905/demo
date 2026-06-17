FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY main.py .
COPY index.html .

# Expose port
EXPOSE 5000

# Run the application
CMD ["uvicorn", "main.py:app", "--host", "0.0.0.0", "--port", "5000"]
