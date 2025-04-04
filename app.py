from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') # Load the secret key from .env 

# Home route
@app.route('/')
def home():
    return render_template('home.html')  # Main page where user chooses their role

# When user signs up as a helpseeker or submit
@app.route('/request-help', methods=['GET', 'POST'])
def helpseeker_sign_in():
    if request.method == 'POST':  # User submitted the form
        # Getting data from submition
        username = request.form['username']
        password = request.form['password']
        country = request.form['country']
        city = request.form['city']
        phone_number = request.form['phone_number']
        video_help = request.form['video_help']
        if video_help == 'yes':
            preferred_video = request.form['preferred_vid']
        else:
            preferred_video = None
        if request.form.get('approve_by_email') == 'yes':
            email = request.form['email'] 
        else:
            email = None
        payment = request.form['payment']

        # Save the new user to the database (helpers table)
        add_user(username, password, 'helpseeker')

        # Add the 'helpseeker' info to the 'helpseeker' table
        add_helpseeker(username, country, city, phone_number, video_help, preferred_video, email, payment)
        
        # Redirect the user to the login page after successful registration
        return redirect(url_for('login'))
    
    # If it's a GET request, show the form to the user
    return render_template('helpseeker_sign_in.html')  # The request form for tech help

#When heklper signs up
@app.route('/helper-sign-up')
def helper_sign_up():
    return render_template('helper_sign_up.html')

# Helper's homepage after login
@app.route('/browse-requests')
def browse_requests():
    return render_template('browse_requests.html')  # A page to browse help requests

# Route to handle the form submission
@app.route('/choose-role', methods=['POST'])
def choose_role():
    role = request.form['role']  # Retrieve the selected role

    # If the user selects "helpseeker"
    if role == 'helpseeker':
        return redirect(url_for('helpseeker_sign_in'))  # Redirect to request-help page for helpseekers
    
    # If the user selects "helper"
    elif role == 'helper':
        return redirect(url_for('helper_sign_up'))  # Redirect to browse-requests page for helpers
    
    # If the user selects "login"
    elif role == 'login':
        return redirect(url_for('login'))  # Redirect to the login page
    
    # In case there's any invalid selection (shouldn't occur if form is set up correctly)
    return redirect(url_for('home'))

# Route for Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Connect to the database and check user credentials
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()  # Fetch user data if found, otherwise None
        
        if user:
            session['username'] = username  # Store the username in the session
            session['role'] = user[2]  # Role is in the 3rd column (index 2)
            return redirect(url_for('home'))  # Redirect to the home page

        return "Invalid username or password!"  # If no user found or wrong password
    
    return render_template('login_page.html')  # Display the login form if it's a GET request

if __name__ == '__main__':
    app.run(debug=True)
