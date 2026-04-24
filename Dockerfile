# Use lightweight official Python 3.11 image (smaller size for faster builds)
FROM python:3.11-slim

# Prevent Python from creating .pyc files (reduces unnecessary files in container)
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure Python output is sent directly to terminal (useful for logging/debugging)
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container to /app
# All subsequent commands will run from this directory
WORKDIR /app

# Install system-level dependencies required for some Python packages
# build-essential includes tools like gcc, make (needed for compiling dependencies)
RUN apt-get update && apt-get install -y \
    build-essential \
    # Clean up apt cache to reduce image size
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements.txt first
# This helps Docker cache dependencies and avoid reinstalling them on every code change
COPY requirements.txt .

# Upgrade pip and install Python dependencies from requirements.txt
# --no-cache-dir reduces image size by not storing pip cache
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy all project files from local machine to container (/app directory)
COPY . .

# Create a directory named "data" if it doesn't exist
# Useful if your app stores files (like CSVs, uploads, etc.)
RUN mkdir -p data

# Expose port 8000 so it can be accessed from outside the container
# FastAPI (uvicorn) will run on this port
EXPOSE 8000

# Command to start the FastAPI application using Uvicorn server
# app.main:app → means "app" object inside main.py inside app folder
# --host 0.0.0.0 → makes the app accessible from outside the container
# --port 8000 → runs the app on port 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]