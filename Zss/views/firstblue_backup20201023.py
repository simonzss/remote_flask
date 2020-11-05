import copy
import json

from flask import Blueprint, request, make_response, Response, session, jsonify
from flask import render_template
from sqlalchemy import func

from Zss.models import db, User, User1, User2, LW201512

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


@first_blueprint.errorhandler(400)  # Registers an error handler that becomes active for this blueprint only.
def handler_error(error):
    print(error)
    print(type(error))
    return '页面错误已经捕获'


'''
Please be aware that routing does not happen local to a blueprint
so an error handler for 404 usually is not handled by a blueprint unless it is caused inside a view function.
请注意，路由不会在blueprint本地发生，因此404的错误处理程序通常不会由blueprint处理，除非它是在view函数内部引起的。
'''


@first_blueprint.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        username = request.form.get("username")
        response = Response("登陆成功%s" % username)
        # response.set_cookie("cookie_username", username)     # 设置cookie
        session["session_username"] = username  # 设置session
        return response  # 注意这里必须将response返回，否则不能set_cookie


@first_blueprint.route('/mine/')
def mine():
    # username = request.cookies.get('cookie_username')       # 使用cookie
    session_username = session.get("session_username")  # 使用session
    return '欢迎回来{}'.format(session_username)


# 通过flask-session扩展可以将session储存在服务器端的redis中，redis是一个高效的可基于内存亦可持久化的数据库
# 具体见千锋教程P376

@first_blueprint.route('/getuser/')
def getuser():
    user = LW201512.query.filter(LW201512.数据处理地.like('6101%')).count()
    print(LW201512.query)
    return 'user的个数是{}'.format(user)


cityinfo = {
    "西安": "6101%",
    "铜川": "6102%",
    "宝鸡": "6103%",
}

specinfo = {
    "工业": "B",
    "建筑业": "C",
    "批发零售业": "E",
}


@first_blueprint.route('/login2/', methods=["GET", "POST"])
def login2():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        year_select = request.form.get("year_select")
        month_select = request.form.get("month_select")
        query_type = request.form.get("query_type")
        post_str = query_type + year_select + month_select
        t_C = globals()[post_str]
        # count_temp = t_C.query.filter(t_C.数据处理地.startswith('6101%'),t_C.报表类别=="B").count()
        # count_temp = db.session.query(func.count(t_C.组织机构代码)).filter(t_C.数据处理地.startswith('6101%'),t_C.报表类别=="B").scalar()
        s_n = {}
        s = {}
        print(list(cityinfo.keys()))
        print(list(specinfo.keys()))
        for i in list(cityinfo.keys()):
            for j in list(specinfo.keys()):
                count_temp = t_C.query.filter(t_C.数据处理地.startswith(cityinfo[i]), t_C.报表类别 == specinfo[j]).count()
                s_n[j] = count_temp
                print(s_n, "```````````")
            s[i] = copy.deepcopy(s_n)
        print(s)
        msg = json.dumps(s,ensure_ascii=False)
        print(type(msg))
        print(msg)
        #response = 'count_temp的个数是{}'.format(count_temp)
        # response.set_cookie("cookie_username", username)     # 设置cookie
        # session["session_username"] = username  # 设置session
        return render_template('index.html',msg=msg,aa={ "name":"Bill Gates",  "age":62, "city":"Seattle" },
                               year_select=year_select,month_select=month_select,query_type=query_type)  # 注意这里必须将response返回，否则不能set_cookie
        #return msg # 注意这里必须将response返回，否则不能set_cookie