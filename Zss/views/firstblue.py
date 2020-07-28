from flask import Blueprint
from flask import render_template

first_blueprint = Blueprint('zss', __name__, template_folder='../templates')


@first_blueprint.route('/')
def hello_world():
    return render_template('index.html',msg='这是坑里的消息')


@first_blueprint.route('/hello')
def hello():
    return 'Hello个鬼'
