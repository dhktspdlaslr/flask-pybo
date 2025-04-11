from flask import Blueprint, url_for, main_views.py
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))
    current_app.logger.info("INFO 레벨로 출력")