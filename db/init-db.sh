#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    ALTER USER pantryowner WITH PASSWORD 'spoilnomore';

    -- Create households table
    CREATE TABLE IF NOT EXISTS households (
        id SERIAL PRIMARY KEY,
        household_name VARCHAR(255) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- Update users table with foreign key to households
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        google_id VARCHAR(4000) UNIQUE NOT NULL,
        household_id INTEGER REFERENCES households(id) ON DELETE SET NULL
    );


     -- Create Food Table
    CREATE TABLE IF NOT EXISTS food (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        location VARCHAR(255) NOT NULL,
        owner VARCHAR(255) NOT NULL,
        expiration_date DATE NOT NULL,
        sharing VARCHAR(50) NOT NULL,
        image_path VARCHAR(255),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        household_id INTEGER,
        FOREIGN KEY (household_id) REFERENCES households(id)
    );

EOSQL


