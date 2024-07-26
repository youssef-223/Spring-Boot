import os
from flask import Flask, request, jsonify
from sqlalchemy import create_engine

app = Flask(__name__)

# Read database configuration from application.properties
def read_properties(filepath):
    properties = {}
    try:
        with open(filepath, 'r') as file:
            for line in file:
                if "=" in line:
                    name, value = line.split("=")
                    properties[name.strip()] = value.strip()
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return properties

properties = read_properties('application.properties')
database_url = properties.get('database.url')

# Set up the database connection
try:
    engine = create_engine(database_url)
except Exception as e:
    print(f"Error creating database engine: {e}")
    engine = None

@app.route('/greeting', methods=['GET'])
def greeting():
    return "Hello"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)