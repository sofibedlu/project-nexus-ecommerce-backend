# Dockerfile (Python)
FROM python:3.8-slim

# Set environment variables for Python
ENV PYTHONUNBUFFERED=1

# Create and set work directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install system dependencies
RUN apt-get update && apt-get install -y\
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies first.
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /app

# Use gunicorn to serve the app
CMD ["gunicorn", "ecom_project_nexus.wsgi:application", "--bind", "0.0.0.0:8000"]