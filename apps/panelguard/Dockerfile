# PanelGuard - research and decision-support only, not for clinical use.
FROM python:3.15-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application (includes vendored cases/ directory); see .dockerignore for exclusions
COPY . .

# Set Python path
ENV PYTHONPATH=/app

# Run as an unprivileged user (the app only reads files under /app)
RUN useradd --uid 10001 --no-create-home --shell /usr/sbin/nologin panelguard
USER 10001

# Expose port (Cloud Run provides $PORT)
ENV PORT=8080
EXPOSE 8080

# Local/Docker health check (Cloud Run uses its own probes and ignores this)
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
  CMD python -c "import os,urllib.request;urllib.request.urlopen('http://127.0.0.1:%s/health' % os.environ.get('PORT','8080'), timeout=4)"

# Run FastAPI. 0.0.0.0 is required inside the container for Cloud Run; when run locally,
# publish only on loopback or Tailscale, e.g.  docker run -p 127.0.0.1:8080:8080 panelguard
CMD exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT}
