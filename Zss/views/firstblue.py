from flask import Blueprint, request, make_response, Response
from flask import render_template

from Zss.models import db, User

first_blueprint = Blueprint('zss', __name__, template_folder='../templates')


@first_blueprint.route('/')
def hello_world():
    return render_template('index.html', msg='这是坑里的消息')


@first_blueprint.route('/hello/<my_id>/')
def hello(my_id):
    print(request.args)
    print(type(request.args))
    return 'Hello个鬼{}'.format(my_id)


# <>包裹的是被传递的参数，参数默认str类型，可以用<converter:variable_name>指定其他类型,converter类型有string,int,path等


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


@first_blueprint.route('/sendrequest/', methods=["GET", "POST"])  # 注意/sendrequest/右边的‘/’，‘/’之后的内容可以被获取为get的参数
def sendrequest():
    print(request.args)  # request.args      是接收request的地址栏参数的，GET，POST等method都可以获取到
    print(type(request.args))
    print(request.form)
    print(type(request.form))  # request.form      是接收request中form形式的请求参数的
    return 'send request success'


'''
POST http://127.0.0.1:5000/sendrequest/?name=zss HTTP/1.1
Content-Type: application/x-www-form-urlencoded

key=valueeeeeee&list=[1, 2, 3]
'''


@first_blueprint.route('/getresponse/')
def getresponse():
    # return 'get response'
    # return render_template('index.html')        #render_template将模板文件渲染为字符串返回
    # my_response=make_response('这是我自己通过flask.make_response定制的response')     # 自制response方法1
    my_response = Response('这是我自己通过flask.Response定制的response')  # 自制response方法2
    print(type(my_response))
    return my_response


@first_blueprint.errorhandler(400) # Registers an error handler that becomes active for this blueprint only.
def handler_error(error):
    print(error)
    print(type(error))
    return '页面错误已经捕获'
'''
Please be aware that routing does not happen local to a blueprint
so an error handler for 404 usually is not handled by a blueprint unless it is caused inside a view function.
请注意，路由不会在blueprint本地发生，因此404的错误处理程序通常不会由blueprint处理，除非它是在view函数内部引起的。
'''
