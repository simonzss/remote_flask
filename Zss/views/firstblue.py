from flask import Blueprint
from flask import render_template

from Zss.models import db, User

first_blueprint = Blueprint('zss', __name__, template_folder='../templates')


@first_blueprint.route('/')
def hello_world():
    return render_template('index.html', msg='这是坑里的消息')


@first_blueprint.route('/hello/<my_id>')
def hello(my_id):
    return 'Hello个鬼{}'.format(my_id)
# <>包裹的是被传递的参数，参数默认str类型，可以用<converter:variable_name>指定其他类型


@first_blueprint.route('/createdb')
def createdb():
    db.create_all()
    return '创建成功！！！'


@first_blueprint.route('/adduser')
def adduser():
    user = User()
    user.username = "Tom"
    db.session.add(user)
    db.session.commit()
    return 'User表内添加数据成功！！！'
