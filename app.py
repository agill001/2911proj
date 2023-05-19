import csv
from flask import Flask, request, render_template, jsonify, redirect, url_for
import random
import string


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return redirect(url_for('login'))

    @app.route('/home')
    def home():
        return render_template('index.html')

    @app.route('/staff_dashboard')
    def staff_dashboard():
        return render_template('staffdashboard.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            login_input = request.form.get('loginInput')
            password = request.form.get('password')

            login_successful = False  # flag to track if login was successful

            if login_input.isdigit() and len(login_input) == 6:  # Check if input is a 6 digit number
                with open('employees.csv', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if row['id'] == login_input and row['password'] == password:
                            login_successful = True
                            break

            elif "@" in login_input and ".com" in login_input:  # Check if it's an email address
                with open('guests.csv', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if row['email'] == login_input and row['password'] == password:
                            login_successful = True
                            break

            if login_successful:
                return redirect(url_for('staff_dashboard') if login_input.isdigit() else url_for('home'))
            else:
                return redirect(url_for('login'))

        else:
            return render_template('login.html')

    @app.route('/report', methods=['GET', 'POST'])
    def report():
        return render_template('report.html')

    @app.route('/staff_report', methods=['GET', 'POST'])
    def staff_report():
        if request.method == 'POST':
            # handle form submission here
            pass
        return render_template('staff_report.html')

    @app.route('/staffprofile')
    def staff_profile():
        return render_template('staffprofile.html')

    @app.route('/useractivereport')
    def user_active_report():
        return render_template('useractivereports.html')

    @app.route('/usercases')
    def user_cases():
        return render_template('usercases.html')

    @app.route('/userhistory')
    def user_history():
        return render_template('userhistory.html')

    @app.route('/userupdates')
    def user_updates():
        return render_template('userupdates.html')

    @app.route('/userprofile', methods=['GET', 'POST'])
    def user_profile():
        if request.method == 'POST':
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email')
            phone_number = request.form.get('phone_number')

            # Generate random password
            password = ''.join(random.choice(
                string.ascii_uppercase + string.digits) for _ in range(10))

            with open('guests.csv', mode='a', newline='') as file:
                fieldnames = ['email', 'password']
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writerow({'email': email, 'password': password})

            return redirect(url_for('login'))
        else:
            return render_template('userprofile.html')

    @app.route('/viewguests')
    def view_guests():
        return render_template('viewguests.html')

    @app.route('/viewstaff')
    def view_staff():
        return render_template('viewstaff.html')

    @app.route('/viewusercases')
    def view_user_cases():
        return render_template('viewusercases.html')

    return app


app = create_app()

if __name__ == '__main__':
    app.run(port=5009)
