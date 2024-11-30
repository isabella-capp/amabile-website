from flask import Blueprint, render_template, request, jsonify
import csv
import os

bp = Blueprint('main', __name__)

jewellery_data = [
    {'name': 'Lovli', 'image_path': 'media/lovli.png'},
    {'name': 'Charmi', 'image_path': 'media/charmi.png'},
    {'name': 'Orecchini', 'image_path': 'media/orecchini.png'},
    {'name': 'Anelli', 'image_path': 'media/anelli.png'},
    {'name': 'Collane', 'image_path': 'media/collane.png'},
    {'name': 'Bracciali', 'image_path': 'media/bracciale.png'}
]

@bp.route('/')
def index():
    return render_template('index.html', css_file='css/index.css', data=jewellery_data)

@bp.route('/about')
def about():
    return render_template('about.html', css_file='css/about.css')

@bp.route('/team')
def team():
    team_members = load_team_data()
    return render_template('team.html', team_members=team_members, css_file='css/team.css')

@bp.route('/api/newsletter', methods=['POST'])
def add_newsletter_information():
    try:
        new_newsletter = request.get_json()
        newsletter = load_newsletter_data()
        newsletter.append(new_newsletter)

        csv_path = os.path.join(os.path.dirname(__file__), '../static/newsletter.csv')
        with open(csv_path, mode='a', encoding='UTF-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['email'])
            writer.writerow(new_newsletter)
        return jsonify({'message': 'Contact added successfully for the newsletter', 'newsletter-email': new_newsletter}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def load_team_data():
    team_members = []
    csv_path = os.path.join(os.path.dirname(__file__), '../static/team.csv');

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

def load_newsletter_data():
    newsletter_contact = []
    csv_path = os.path.join(os.path.dirname(__file__), '../static/newsletter.csv');

    try:
        with open(csv_path, mode='r', encoding='UTF-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                newsletter_contact.append(row)
        return newsletter_contact
    except FileNotFoundError:
        print(f'Warning: File {csv_path} not found')
        return []
    except Exception as e:
        print(f'Error loading newsletter data: {e}')
        return []