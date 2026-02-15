# Use Python 3.9 as the base image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8000
EXPOSE 8000

# Run migrations and start the server
# FIXED: We now point to "src/manage.py" instead of just "manage.py"
CMD ["sh", "-c", "python src/manage.py makemigrations && python src/manage.py migrate && python src/manage.py runserver 0.0.0.0:8000"]