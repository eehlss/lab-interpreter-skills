FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Set Python path
ENV PYTHONPATH=/app

# Expose port (Cloud Run provides $PORT)
ENV PORT=8080
EXPOSE 8080

# Run FastAPI
CMD exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT}
