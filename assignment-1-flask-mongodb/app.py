"""
Flask Application - TuteDude DevOps Assignment 1
=================================================
Task 1: /api route - Returns JSON data read from a backend file (data.json)
Task 2: /form route - HTML form that submits data to MongoDB Atlas
"""

import json
import os
from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# ============================================================
# TASK 1: Flask API Route - Read JSON from backend file
# ============================================================

@app.route('/api', methods=['GET'])
def get_api_data():
    """
    Reads data from the backend file 'data.json' and returns it
    as a JSON response to the client.
    """
    try:
        # Get the path to data.json (same directory as app.py)
        data_file = os.path.join(os.path.dirname(__file__), 'data.json')

        # Open and read the JSON file
        with open(data_file, 'r') as f:
            data = json.load(f)

        # Return the data as a JSON response
        return jsonify(data), 200

    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON in data file"}), 500


# ============================================================
# TASK 2: MongoDB Form Submission
# ============================================================

def get_mongo_client():
    """
    Creates and returns a MongoDB client using the connection
    string built from separate environment variables.
    This ensures special characters in password are properly handled.
    """
    import urllib.parse

    username = os.getenv('MONGO_USERNAME')
    password = os.getenv('MONGO_PASSWORD')
    host = os.getenv('MONGO_HOST')
    db_name = os.getenv('MONGO_DB', 'tutedude')

    if not username or not password or not host:
        raise Exception("MongoDB credentials not found. Check MONGO_USERNAME, MONGO_PASSWORD, MONGO_HOST in .env file.")

    # URL-encode username and password to handle special characters (@, #, etc.)
    encoded_username = urllib.parse.quote_plus(username)
    encoded_password = urllib.parse.quote_plus(password)

    # Build the connection string
    mongo_uri = f"mongodb+srv://{encoded_username}:{encoded_password}@{host}/{db_name}?retryWrites=true&w=majority&appName=Cluster0"

    print(f"[INFO] Connecting to MongoDB Atlas at {host}...")
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    return client


@app.route('/')
def home():
    """Home page - redirects to the form."""
    return redirect(url_for('show_form'))


@app.route('/form', methods=['GET'])
def show_form():
    """Renders the HTML form for data submission."""
    return render_template('form.html', error=None)


@app.route('/submit', methods=['POST'])
def submit_form():
    """
    Handles form submission:
    - Receives form data (name, email, message)
    - Inserts it into MongoDB Atlas
    - On success: redirects to /success page
    - On error: re-renders the form with error message
    """
    try:
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        # Basic validation
        if not name or not email or not message:
            return render_template('form.html', error="All fields are required. Please fill in all fields.")

        # Connect to MongoDB Atlas
        client = get_mongo_client()
        db = client['tutedude']              # Database name
        collection = db['submissions']        # Collection name

        # Create the document to insert
        document = {
            "name": name,
            "email": email,
            "message": message
        }

        # Insert into MongoDB
        result = collection.insert_one(document)
        print(f"[SUCCESS] Data inserted with ID: {result.inserted_id}")

        # Close connection
        client.close()

        # Redirect to success page
        return redirect(url_for('success'))

    except Exception as e:
        # On error: stay on the same page and display the error
        print(f"[ERROR] {str(e)}")
        return render_template('form.html', error=f"Error: {str(e)}")


@app.route('/success')
def success():
    """Displays the success message after data submission."""
    return render_template('success.html')


# ============================================================
# Run the Flask application
# ============================================================

if __name__ == '__main__':
    print("=" * 50)
    print("  Flask App - TuteDude DevOps Assignment")
    print("=" * 50)
    print("  Routes:")
    print("    GET  /api     → Returns JSON data from file")
    print("    GET  /form    → Shows the submission form")
    print("    POST /submit  → Submits data to MongoDB Atlas")
    print("    GET  /success → Success confirmation page")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
