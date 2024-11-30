from flask import Blueprint, render_template
import csv
import os

bp = Blueprint('faq', __name__)

@bp.route('/faq')
def faq():
    question_information = load_question_data()
    return render_template('faq.html', question_information=question_information, css_file="css/faq.css")

def load_question_data():
    question_information = []
    csv_path = os.path.join(os.path.dirname(__file__), '../static/question.csv');

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