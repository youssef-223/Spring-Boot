#!/bin/bash

# Define database connection details
DB_HOST="jdbc:mysql://192.168.124.128:3306/"
DB_NAME="giza_db"

SUDO_PASSWORD=1234
run_sudo() {
  echo $SUDO_PASSWORD | sudo -S $@
}

# Create the database
echo "Creating database ${DB_NAME}..."
run_sudo mysql -u root -e "CREATE DATABASE IF NOT EXISTS ${DB_NAME};"

if [ $? -eq 0 ]; then
    echo ">> Database setup complete."
  else
    echo ">> Failed to create DB"
    exit 1
  fi

# echo "Database setup complete."