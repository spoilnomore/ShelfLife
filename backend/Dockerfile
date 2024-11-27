# Use the official Python image from Docker Hub
FROM python:3.9-slim-bullseye

# Create and set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port Flask will run on
EXPOSE 8081

# Use Gunicorn to run the application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8081", "--access-logfile", "-", "--error-logfile", "-", "run:app"]

