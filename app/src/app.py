import os
from flask import Flask, request, jsonify, render_template
from sqlalchemy import create_engine, text

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
database_username = properties.get('database.username')
database_password = properties.get('database.password')

# Construct the database URL for SQLAlchemy
if database_url and database_username and database_password:
    # Adjust the URL to fit SQLAlchemy's format
    database_url = database_url.replace("jdbc:mysql://", "mysql+pymysql://")
    # Insert username and password into the URL
    database_url = database_url.replace("mysql+pymysql://", f"mysql+pymysql://{database_username}:{database_password}@")
else:
    database_url = None

# Set up the database connection
try:
    if database_url:
        engine = create_engine(database_url)
    else:
        engine = None
except Exception as e:
    print(f"Error creating database engine: {e}")
    engine = None

@app.route('/check_db', methods=['GET'])
def check_db():
    if not engine:
        return jsonify({"error": "Database connection is not established"}), 500

    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            result.fetchone()
        return jsonify({"message": "Database connection successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/greeting', methods=['GET'])
def greeting():
    return "Hello"

@app.route('/')
def home():
    return render_template('query.html')

@app.route('/query', methods=['GET'])
def query_db():
    query = request.args.get('query')
    if not query:
        return render_template('query.html', error="No query provided")

    if not engine:
        return render_template('query.html', error="Database connection is not established")

    try:
        with engine.connect() as connection:
            result = connection.execute(text(query))
            fetched_rows = result.fetchall()
            columns = result.keys()
            rows = [dict(zip(columns, row)) for row in fetched_rows]
        return render_template('query.html', data=rows)
    except Exception as e:
        return render_template('query.html', error=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
