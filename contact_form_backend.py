import os
from flask import Flask, request, jsonify
import mysql.connector
from dotenv import load_dotenv
from flask_cors import CORS

# --- Load environment variables from .env file ---
load_dotenv()

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# --- Database Connection Configuration ---
# Get credentials from environment variables for security
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

# Function to establish a new database connection
def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

# --- API Routes ---

@app.route('/api/health', methods=['GET'])
def health_check():
    """A simple endpoint to check if the server is running."""
    return jsonify({"status": "ok", "message": "Python backend is up and running."}), 200

@app.route('/api/submit-form', methods=['POST'])
def submit_form():
    """Receives form data and inserts it into the MySQL database."""
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        # Basic server-side validation
        if not name or not email or not message:
            return jsonify({"message": "All fields are required."}), 400

        # Create a database connection
        conn = get_db_connection()
        if conn is None:
            return jsonify({"message": "Failed to connect to the database."}), 500

        cursor = conn.cursor()

        # SQL to insert data into the contact_submissions table
        sql = "INSERT INTO contact_submissions (name, email, message) VALUES (%s, %s, %s)"
        values = (name, email, message)

        cursor.execute(sql, values)
        conn.commit()

        submission_id = cursor.lastrowid
        
        cursor.close()
        conn.close()

        print(f"Form submission successful. ID: {submission_id}")
        return jsonify({"message": "Form submitted successfully!", "submissionId": submission_id}), 200

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"message": "An internal server error occurred."}), 500

if __name__ == '__main__':
    # Running the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)