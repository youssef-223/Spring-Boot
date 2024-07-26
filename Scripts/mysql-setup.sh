#!/bin/bash

# Define database connection details
DB_HOST="localhost:3306"
DB_USER="root"
DB_PASS="password"
DB_NAME="Giza-db"

# Create the database
echo "Creating database ${DB_NAME}..."
mysql -h $DB_HOST -u $DB_USER -p$DB_PASS -e "CREATE DATABASE IF NOT EXISTS ${DB_NAME};"


echo "Database setup complete."