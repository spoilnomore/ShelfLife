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

# Set environment variables for Flask
ENV FLASK_APP=run.py
ENV FLASK_RUN_PORT=8081
ENV FLASK_RUN_HOST=0.0.0.0

# Start the Flask application using Waitress
CMD ["waitress-serve", "--port=8081", "--threads=100", "run:app"]
