# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy the script into the container
COPY hello.py .

# Run the script when container starts
CMD ["python", "hello.py"]