# Use a slim Python 3.8 image as the base
FROM python:3.8-slim

# Set working directory within the container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies using pip
RUN pip install -r requirements.txt

# Copy the entire project directory
COPY . .

# Expose port 8000 (default for FastAPI development server)
EXPOSE 8000

# Set the command to run the application 
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
