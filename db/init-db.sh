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

EOSQL
