from flask import Blueprint, render_template

bp = Blueprint('auth', __name__)

@bp.route('/auth')
def auth():
    return render_template('auth.html', css_file='css/auth.css')