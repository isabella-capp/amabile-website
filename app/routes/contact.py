from flask import Blueprint, render_template, jsonify, request
import os
import csv

bp = Blueprint('contact', __name__)

@bp.route('/contact')
def contact():
    return render_template('contact.html', css_file='css/contact.css')

@bp.route('/api/contact', methods=['POST'])
def add_contact_information():
    try:
        new_contact = request.get_json()
        contact = load_contact_data()
        contact.append(new_contact)

        csv_path = os.path.join(os.path.dirname(__file__), '../static/contact.csv')
        with open(csv_path, mode='a', encoding='UTF-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['name', 'email', 'phone', 'description'])
            writer.writerow(new_contact)
        return jsonify({'message': 'Contact added successfully', 'contact': new_contact}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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