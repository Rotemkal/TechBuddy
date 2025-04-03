from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('home.html')  # Main page where user chooses their role

# When user chooses "Technophobe" (needs help)
@app.route('/request-help')
def request_help():
    return render_template('request_help.html')  # The request form for tech help

# When user chooses "Tech-Savvy" (wants to help)
@app.route('/browse-requests')
def browse_requests():
    return render_template('browse_requests.html')  # A page to browse help requests

# Route to handle the form submission
@app.route('/choose-role', methods=['POST'])
def choose_role():
    role = request.form['role']
    if role == 'technophobe':
        return redirect(url_for('request_help'))  # Redirect to request-help page for Technophobes
    else:
        return redirect(url_for('browse_requests'))  # Redirect to browse-requests page for Tech-Savvy users

if __name__ == '__main__':
    app.run(debug=True)
