from flask import Flask, render_template, jsonify, request
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', css_file='css/index.css')

@app.route('/about')
def about():
    return render_template('about.html', css_file='css/about.css')

@app.route('/contact')
def contact():
    return render_template('contact.html', css_file='css/contact.css')

@app.route('/api/contact', methods=['POST'])
def add_contact_information():
    try:
        new_contact = request.get_json()
        contact = load_contact_data()
        contact.append(new_contact)

        csv_path = os.path.join(os.path.dirname(__file__), 'static/contact.csv')
        with open(csv_path, mode='a', encoding='UTF-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['name', 'email', 'phone', 'description'])
            writer.writerow(new_contact)
        return jsonify({'message': 'Contact added succesfully', 'contact': new_contact}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/team')
def team():
    team_members = load_team_data()
    return render_template('team.html', team_members=team_members, css_file='css/team.css')

@app.route('/faq')
def faq():
    question_information = load_question_data()
    return render_template('faq.html', question_information=question_information, css_file="css/faq.css")


def load_team_data():
    team_members = []
    csv_path = os.path.join(os.path.dirname(__file__), 'static/team.csv');

    try:
        with open(csv_path, mode='r', encoding='UTF-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                team_members.append(row)
        return team_members
    except FileNotFoundError:
        print(f'Warning: File {csv_path} not found')
        return []
    except Exception as e:
        print(f'Error loading team data: {e}')
        return []

def load_question_data():
    question_information = []
    csv_path = os.path.join(os.path.dirname(__file__), 'static/question.csv');

    try:
        with open(csv_path, mode='r', encoding='UTF-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                question_information.append(row)
        return question_information
    except FileNotFoundError:
        print(f'Warning: File {csv_path} not found')
        return []
    except Exception as e:
        print(f'Error loading team data: {e}')
        return []

def load_contact_data():
    contact_information = []
    csv_path = os.path.join(os.path.dirname(__file__), 'static/contact.csv');

    try:
        with open(csv_path, mode='r', encoding='UTF-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                contact_information.append(row)
        return contact_information
    except FileNotFoundError:
        print(f'Warning: File {csv_path} not found')
        return []
    except Exception as e:
        print(f'Error loading team data: {e}')
        return []

if __name__ == '__main__':
    app.run(debug=True)