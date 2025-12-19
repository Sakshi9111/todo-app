FROM python:3.12.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
# Install dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
        postgresql-client \
        libpq-dev \
        gcc \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libc6-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# ✅ install python deps as root
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser



# Copy application files
COPY . .

# Give ownership to non-root user
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

#COPY requirements.txt /app

#RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
