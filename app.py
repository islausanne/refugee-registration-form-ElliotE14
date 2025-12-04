
from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Registration form page
@app.route('/register')
def register():
    return render_template('register.html')

# Handle form submission (students will add JSON save code here)
@app.route('/submit', methods=['POST'])
def submit_form():
    print("TEST")
    # Get form inputs
    first_name = request.form['first_name']
    surname = request.form['surname']
    birthdate = request.form['birthdate']
    gender = request.form.get('gender')
    medical_condition = request.form['medical_condition']
    medical_condition_text = request.form.get('medical_condition_text', "")
    country = request.form['country']
    id_information1 = request.form.get('id_information1', "")
    id_information_text1 = request.form.get('id_information_text1', "")
    skills_job = request.form['skills_job']
    phone_number = request.form['phone_number']
    travelling_members = request.form['travelling_members']
    photo = request.form['photo']

    # Check if file exists
    if os.path.exists('registrations.json'):
        with open('registrations.json', 'r') as file:
            data = json.load(file)
    else:
        data = []

    # Add the new registration
    data.append({
        'first_name': first_name,
        'surname': surname,
        'birthdate': birthdate,
        'gender': gender,
        'medical_condition': medical_condition,
        'medical_condition_text': medical_condition_text,
        'country': country,
        'id_information1': id_information1,
        'id_information_text1': id_information_text1,
        'skills_job': skills_job,
        'phone_number': phone_number,
        'travelling_members': travelling_members,
        'photo': photo
    })

    # Save all registrations back to the file
    with open('registrations.json', 'w') as file:
        json.dump(data, file, indent=2)

    return redirect(url_for('index'))

    flash('Registration submitted successfully!')
    return redirect(url_for('index'))

# Display stored registrations
@app.route('/view')
def view_registrations():
    with open('registrations.json', 'r') as file:
        data = json.load(file)
    return render_template('view.html', registrations=data)

    return render_template('view.html', registrations=[])

if __name__ == '__main__':
    app.run(debug=True)
