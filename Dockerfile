# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY app/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app /app

# Expose the FastAPI default port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
