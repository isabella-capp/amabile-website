from flask import Blueprint, render_template

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
