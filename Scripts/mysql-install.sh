#!/bin/bash

sudo apt-get update
sudo apt-get install mysql-server

# Function to start MySQL service
start_mysql() {
  echo "Starting MySQL service..."
  sudo systemctl start mysql
  if [ $? -eq 0 ]; then
    echo "MySQL service started successfully."
  else
    echo "Failed to start MySQL service."
    exit 1
  fi
}

# Function to enable MySQL to start on boot
enable_mysql_service() {
  echo "Enabling MySQL service to start on boot..."
  sudo systemctl enable mysql
  if [ $? -eq 0 ]; then
    echo "MySQL service enabled to start on boot successfully."
  else
    echo "Failed to enable MySQL service to start on boot."
    exit 1
  fi
}

# Main script execution
echo "Starting MySQL setup script..."

# Start MySQL
start_mysql

# Enable MySQL service to start on boot
enable_mysql_service

echo "MySQL setup completed successfully."
