FROM python:3.9-slim-bullseye

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

ENV DEBIAN_FRONTEND noninteractive

RUN apt update -y && apt install -y \
    libffi-dev \
    libpq-dev \
    postgresql \
    gcc \
    g++ \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    cargo \
    pkg-config \
    curl \
    && apt clean

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt


EXPOSE 8081

# Set environment variables for Flask
ENV FLASK_APP=run.py
ENV FLASK_RUN_PORT=8081
ENV FLASK_RUN_HOST=0.0.0.0

CMD [ "waitress-serve", "--port=8081", "--threads=100", "run:app"]
