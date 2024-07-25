import os
from flask import Flask, request, jsonify
from sqlalchemy import create_engine

app = Flask(__name__)

# Read database configuration from application.properties
def read_properties(filepath):
    properties = {}
    with open(filepath, 'r') as file:
        for line in file:
            if "=" in line:
                name, value = line.split("=")
                properties[name.strip()] = value.strip()
    return properties

properties = read_properties('application.properties')
database_url = properties.get('DATABASE_URL')

# Set up the database connection
engine = create_engine(database_url)

@app.route('/greeting', methods=['GET'])
def greeting():
    name = request.args.get('name', os.getenv('NAME','World') )
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)