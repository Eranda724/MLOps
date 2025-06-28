# Use a specific Python 3.10.7 image
FROM python:3.10.7-slim

# Set working directory inside the container
WORKDIR /app

# Optional: Install Python dependencies if you have a requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all files from your local project into the container
COPY . .

# Default command to run the training script
CMD ["python", "src/train.py"]
