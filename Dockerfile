# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Python files to container
COPY app.py .
COPY test_app.py .

# Make port 80 available to the world outside this container (if needed for web app)
# EXPOSE 80

# Define environment variable
ENV PYTHONPATH=/app

# Run app.py when the container launches
CMD ["python", "app.py"]
