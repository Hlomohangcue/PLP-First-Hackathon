from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configure your MySQL database connection
db_config = {
    'host': 'localhost',
    'user': 'Hlomohang',
    'password': 'admin1234',
    'database': 'portfolio_db'
}

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for the About page
@app.route('/about.html')
def about():
    return render_template('about.html')

# Route for the Skills page
@app.route('/skills.html')
def skills():
    return render_template('skills.html')

# NEW: Route for the Education page
@app.route('/education.html')
def education():
    return render_template('education.html')

# Route for the Projects page
@app.route('/projects.html')
def projects():
    return render_template('projects.html')

# NEW: Route for the Interests page
@app.route('/interests.html')
def interests():
    return render_template('interests.html')

# Route for the Contact page
@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    try:
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Connect to MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # SQL query to insert data
        sql = "INSERT INTO contact_submissions (name, email, message) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, email, message))
        conn.commit()

        # Close connection
        cursor.close()
        conn.close()

        # Return a success response
        return jsonify({'message': 'Form submitted successfully!'}), 200

    except mysql.connector.Error as err:
        return jsonify({'error': f"Database error: {err}"}), 500
    except Exception as e:
        return jsonify({'error': f"An error occurred: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)