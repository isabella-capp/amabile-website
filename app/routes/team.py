from flask import Blueprint, render_template
import csv
import os

bp = Blueprint('team', __name__)

@bp.route('/team')
def team():
    team_members = load_team_data()
    return render_template('team.html', team_members=team_members, css_file='css/team.css')

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