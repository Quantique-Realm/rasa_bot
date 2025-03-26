# Use an ARM64-compatible Python base image
FROM python:3.10-slim

# Set environment variables
ENV PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:$PATH"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Rasa and additional dependencies
RUN pip install rasa rasa-sdk \
    && pip install --no-cache-dir sentence-transformers

# Set work directory
WORKDIR /app

# Copy project files
COPY . /app

# Ensure a model exists (if not, create a dummy model)
RUN mkdir -p /app/models && rasa train --fixed-model-name model

# Expose Rasa and Action Server ports
EXPOSE 5005 5055

# Default command to start Rasa server
CMD ["rasa", "run", "--enable-api", "--cors", "*"]
