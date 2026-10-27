FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Copy synthetic cases from repo root into image
# Build context is apps/panelguard, so cases are at ../../cases
COPY ../../cases/transfusion-medicine-interpreter /app/cases/transfusion-medicine-interpreter

# Set Python path
ENV PYTHONPATH=/app

# Expose port (Cloud Run provides $PORT)
ENV PORT=8080
EXPOSE 8080

# Run FastAPI
CMD exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT}
