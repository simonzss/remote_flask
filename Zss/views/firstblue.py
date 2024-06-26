import copy
import json

from flask import Blueprint, request, make_response, Response, session, jsonify
from flask import render_template
from sqlalchemy import func, or_

# from Zss.models import db, User, User1, User2, LW201912,LW201911
from Zss.models import *

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
    # user = LW201512.query.filter(LW201512.数据处理地.like('6101%')).count()
    user = TK202102.query.with_entities(TK202102.所属专业, TK202102.审核类型, func.count()).filter(
        TK202102.行业代码_17.startswith('13')).group_by('所属专业', '审核类型').all()
    # 结果为[('1', '1', 9), ('9', '7', 6)]，所属专业在前，审核类型在后
    # user = TK202102.query.with_entities(TK202102.所属专业, TK202102.审核类型,func.count()).group_by('所属专业','审核类型').all()
    print(TK202102.query, '***************************')
    print(str(user))
    return 'user的个数是{}'.format(user)


cityinfo = {
    "西安": ["6101%", "6170%"],  # 西安必须有，不可删除
    "铜川": ["6102%"],
    "宝鸡": ["6103%"],
    "咸阳": ["6104%"],
    "渭南": ["6105%"],
    "延安": ["6106%"],
    "汉中": ["6107%"],
    "榆林": ["6108%"],
    "安康": ["6109%"],
    "商洛": ["6110%"],
    "杨凌": ["6199%"],
    # "省直管": "6170%",
    "全省": ["61%"],
    "韩城市": ["610581%"],
    "神木市": ["610881%"],
    "府谷县": ["610822%"],

    # "#西安市6101_6170": ["6101", "6170%"],
    # "新城区610102": ["610102"],
    # "碑林区610103": ["610103"],
    # "莲湖区610104": ["610104"],
    # "灞桥区610111": ["610111"],
    # "未央区610112": ["610112"],
    # "雁塔区610113": ["610113"],
    # "阎良区610114": ["610114"],
    # "临潼区610115": ["610115"],
    # "长安区610116": ["610116"],
    # "高陵区610117": ["610117"],
    # "鄠邑区610118": ["610118"],
    # "蓝田县610122": ["610122"],
    # "周至县610124": ["610124"],
    # "高新技术产业开发区610161": ["610161"],
    # "经济技术开发区610162": ["610162"],
    # "曲江新区610163": ["610163"],
    # "航空产业基地610164": ["610164"],
    # "航天产业基地610165": ["610165"],
    # "西咸新区610166": ["610166"],
    # "浐灞生态区610167": ["610167"],
    # "国际港务区610168": ["610168"],
    # "西安市直管610170": ["610170"],
    # "陕西省直管617070": ["617070"],
    # "#铜川市6102": ["6102"],
    # "王益区610202": ["610202"],
    # "印台区610203": ["610203"],
    # "耀州区610204": ["610204"],
    # "宜君县610222": ["610222"],
    # "新区610260": ["610260"],
    # "#宝鸡市6103": ["6103"],
    # "市辖区610301": ["610301"],
    # "渭滨区610302": ["610302"],
    # "金台区610303": ["610303"],
    # "陈仓区610304": ["610304"],
    # "凤翔区610305": ["610305"],
    # "凤翔县610322": ["610322"],
    # "岐山县610323": ["610323"],
    # "扶风县610324": ["610324"],
    # "眉县610326": ["610326"],
    # "陇县610327": ["610327"],
    # "千阳县610328": ["610328"],
    # "麟游县610329": ["610329"],
    # "凤县610330": ["610330"],
    # "太白县610331": ["610331"],
    # "#咸阳市6104": ["6104"],
    # "秦都区610402": ["610402"],
    # "渭城区610404": ["610404"],
    # "三原县610422": ["610422"],
    # "泾阳县610423": ["610423"],
    # "乾县610424": ["610424"],
    # "礼泉县610425": ["610425"],
    # "永寿县610426": ["610426"],
    # "彬县610427": ["610427"],
    # "长武县610428": ["610428"],
    # "旬邑县610429": ["610429"],
    # "淳化县610430": ["610430"],
    # "武功县610431": ["610431"],
    # "兴平市610481": ["610481"],
    # "彬州市610482": ["610482"],
    # "#渭南市6105": ["6105"],
    # "临渭区610502": ["610502"],
    # "华州区610503": ["610503"],
    # "潼关县610522": ["610522"],
    # "大荔县610523": ["610523"],
    # "合阳县610524": ["610524"],
    # "澄城县610525": ["610525"],
    # "蒲城县610526": ["610526"],
    # "白水县610527": ["610527"],
    # "富平县610528": ["610528"],
    # "渭南市高新区610560": ["610560"],
    # "渭南市经开区610561": ["610561"],
    # "韩城市610581": ["610581"],
    # "华阴市610582": ["610582"],
    # "#延安市6106": ["6106"],
    # "宝塔区610602": ["610602"],
    # "安塞区610603": ["610603"],
    # "延长县610621": ["610621"],
    # "延川县610622": ["610622"],
    # "子长县610623": ["610623"],
    # "安塞县610624": ["610624"],
    # "志丹县610625": ["610625"],
    # "吴起县610626": ["610626"],
    # "甘泉县610627": ["610627"],
    # "富县610628": ["610628"],
    # "洛川县610629": ["610629"],
    # "宜川县610630": ["610630"],
    # "黄龙县610631": ["610631"],
    # "黄陵县610632": ["610632"],
    # "延安市统计局直管610660": ["610660"],
    # "子长市610681": ["610681"],
    # "#汉中市6107": ["6107"],
    # "汉台区610702": ["610702"],
    # "南郑区610703": ["610703"],
    # "城固县610722": ["610722"],
    # "洋县610723": ["610723"],
    # "西乡县610724": ["610724"],
    # "勉县610725": ["610725"],
    # "宁强县610726": ["610726"],
    # "略阳县610727": ["610727"],
    # "镇巴县610728": ["610728"],
    # "留坝县610729": ["610729"],
    # "佛坪县610730": ["610730"],
    # "#榆林市6108": ["6108"],
    # "榆阳区610802": ["610802"],
    # "横山区610803": ["610803"],
    # "神木县610821": ["610821"],
    # "府谷县610822": ["610822"],
    # "靖边县610824": ["610824"],
    # "定边县610825": ["610825"],
    # "绥德县610826": ["610826"],
    # "米脂县610827": ["610827"],
    # "佳县610828": ["610828"],
    # "吴堡县610829": ["610829"],
    # "清涧县610830": ["610830"],
    # "子洲县610831": ["610831"],
    # "榆林市直管610870": ["610870"],
    # "神木市610881": ["610881"],
    # "#安康市6109": ["6109"],
    # "汉滨区610902": ["610902"],
    # "恒口示范区610910": ["610910"],
    # "汉阴县610921": ["610921"],
    # "石泉县610922": ["610922"],
    # "宁陕县610923": ["610923"],
    # "紫阳县610924": ["610924"],
    # "岚皋县610925": ["610925"],
    # "平利县610926": ["610926"],
    # "镇坪县610927": ["610927"],
    # "旬阳县610928": ["610928"],
    # "白河县610929": ["610929"],
    # "高新区610960": ["610960"],
    # "旬阳市610981": ["610981"],
    # "#商洛市6110": ["6110"],
    # "商州区611002": ["611002"],
    # "洛南县611021": ["611021"],
    # "丹凤县611022": ["611022"],
    # "商南县611023": ["611023"],
    # "山阳县611024": ["611024"],
    # "镇安县611025": ["611025"],
    # "柞水县611026": ["611026"],
    # "#杨凌示范区6199": ["6199"],
    # "杨陵区619939": ["619939"],
    # ##2018年凤翔旬阳子长彬县的区划发生变动撤县设区市

}

# cityinfo = {
#     "西安": "6101%",#西安必须有，不可删除
#     "铜川": "6102%",
#     "宝鸡": "6103%",
#     "咸阳": "6104%",
#     "渭南": "6105%",
#     "延安": "6106%",
#     "汉中": "6107%",
#     "榆林": "6108%",
#     "安康": "6109%",
#     "商洛": "6110%",
#     "杨凌": "6199%",
#     "省直管": "6170%",
#     "全省": "61%",
#     "韩城市": "610581%",
# }

cityinfo_SP = {
    "西安": ["6101%"],  # 西安必须有，不可删除
    "铜川": ["6102%"],
    "宝鸡": ["6103%"],
    "咸阳": ["6104[^0]%", "61040[^3]%"],
    "渭南": ["6105%"],
    "延安": ["6106%"],
    "汉中": ["6107%"],
    "榆林": ["6108%"],
    "安康": ["6109%"],
    "商洛": ["6110%"],
    "杨凌": ["610403%"],
    "全省": ["61%"],
    "韩城市": ["610581%"],
    "神木市": ["610881%"],
    "府谷县": ["610822%"],
    # "高级咸阳": ["\b((?!610403)\w)+\b"],

    # # 西安市------------------------------
    # "新城区": ["610102%"],
    # "碑林区": ["610103%"],
    # "莲湖区": ["610104%"],
    # "灞桥区": ["610111%"],
    # "未央区": ["610112%"],
    # "雁塔区": ["610113%"],
    # "阎良区": ["610114%"],
    # "临潼区": ["610115%"],
    # "长安区": ["610116%"],
    # "高陵区": ["610117%"],
    # "鄠邑区": ["610118%"],
    # "蓝田县": ["610122%"],
    # "周至县": ["610124%"],
    # # 铜川市------------------------------
    # "王益区": ["610202%"],
    # "印台区": ["610203%"],
    # "耀州区": ["610204%"],
    # "宜君县": ["610222%"],
    # # 宝鸡市------------------------------
    # "渭滨区": ["610302%"],
    # "金台区": ["610303%"],
    # "陈仓区": ["610304%"],
    # "凤翔县": ["610322%"],
    # "岐山县": ["610323%"],
    # "扶风县": ["610324%"],
    # "眉县": ["610326%"],
    # "陇县": ["610327%"],
    # "千阳县": ["610328%"],
    # "麟游县": ["610329%"],
    # "凤县": ["610330%"],
    # "太白县": ["610331%"],
    # # 咸阳市------------------------------
    # "秦都区": ["610402%"],
    # "渭城区": ["610404%"],
    # "三原县": ["610422%"],
    # "泾阳县": ["610423%"],
    # "乾县": ["610424%"],
    # "礼泉县": ["610425%"],
    # "永寿县": ["610426%"],
    # "长武县": ["610428%"],
    # "旬邑县": ["610429%"],
    # "淳化县": ["610430%"],
    # "武功县": ["610431%"],
    # "兴平市": ["610481%"],
    # "彬州市": ["610482%"],
    # # 渭南市------------------------------
    # "临渭区": ["610502%"],
    # "华州区": ["610503%"],
    # "潼关县": ["610522%"],
    # "大荔县": ["610523%"],
    # "合阳县": ["610524%"],
    # "澄城县": ["610525%"],
    # "蒲城县": ["610526%"],
    # "白水县": ["610527%"],
    # "富平县": ["610528%"],
    # "华阴市": ["610582%"],
    # # 延安市------------------------------
    # "宝塔区": ["610602%"],
    # "安塞区": ["610603%"],
    # "延长县": ["610621%"],
    # "延川县": ["610622%"],
    # "子长县": ["610623%"],
    # "志丹县": ["610625%"],
    # "吴起县": ["610626%"],
    # "甘泉县": ["610627%"],
    # "富县": ["610628%"],
    # "洛川县": ["610629%"],
    # "宜川县": ["610630%"],
    # "黄龙县": ["610631%"],
    # "黄陵县": ["610632%"],
    # # 汉中市------------------------------
    # "汉台区": ["610702%"],
    # "南郑区": ["610703%"],
    # "城固县": ["610722%"],
    # "洋县": ["610723%"],
    # "西乡县": ["610724%"],
    # "勉县": ["610725%"],
    # "宁强县": ["610726%"],
    # "略阳县": ["610727%"],
    # "镇巴县": ["610728%"],
    # "留坝县": ["610729%"],
    # "佛坪县": ["610730%"],
    # # 榆林市------------------------------
    # "榆阳区": ["610802%"],
    # "横山区": ["610803%"],
    # "靖边县": ["610824%"],
    # "定边县": ["610825%"],
    # "绥德县": ["610826%"],
    # "米脂县": ["610827%"],
    # "佳县": ["610828%"],
    # "吴堡县": ["610829%"],
    # "清涧县": ["610830%"],
    # "子洲县": ["610831%"],
    # # 安康市------------------------------
    # "汉滨区": ["610902%"],
    # "汉阴县": ["610921%"],
    # "石泉县": ["610922%"],
    # "宁陕县": ["610923%"],
    # "紫阳县": ["610924%"],
    # "岚皋县": ["610925%"],
    # "平利县": ["610926%"],
    # "镇坪县": ["610927%"],
    # "旬阳县": ["610928%"],
    # "白河县": ["610929%"],
    # # 商洛市------------------------------
    # "商州区": ["611002%"],
    # "洛南县": ["611021%"],
    # "丹凤县": ["611022%"],
    # "商南县": ["611023%"],
    # "山阳县": ["611024%"],
    # "镇安县": ["611025%"],
    # "柞水县": ["611026%"],
    # # 杨凌区------------------------------
    # "杨陵区": ["610403%"],

}

specinfo = {
    "工业": ["B"],
    "建筑业": ["C"],
    "贸易": ["E", "S"],
    "批发零售业": ["E"],
    "住宿餐饮业": ["S"],
    "房地产": ["X"],
    "服务业": ["F"],
    "投资": ["H"],
    "总计": ["B", "C", "E", "S", "X", "F", "H"],
    "五上": ["B", "C", "E", "S", "X", "F"],
}

specinfo_SP = {
    "工业": ["1"],
    "建筑业": ["2"],
    "贸易": ["3", "4", "5", "6"],
    "批发业": ["3"],
    "零售业": ["4"],
    "住宿业": ["5"],
    "餐饮业": ["6"],
    "房地产": ["7"],
    "服务业": ["8"],
    "投资": ["9"],
    "总计": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "五上": ["1", "2", "3", "4", "5", "6", "7", "8"],
}

highTechManu_yyzzy = ["2710", "2720", "2730", "2740", "2750", "2761", "2762", "2770", "2780"]
highTechManu_hkhtzzy = ["3741", "3742", "3743", "3744", "3749", "4343"]
highTechManu_dztxzzy = ["3562", "3563", "3569", "3832", "3833", "3841", "3921", "3922", "3940", "3931", "3932", "3933",
                        "3934", "3939", "3951", "3952", "3953", "3971", "3972", "3973", "3974", "3975", "3976", "3979",
                        "3981", "3983", "3984", "3985", "3989", "3982", "3961", "3962", "3963", "3969", "3990"]
highTechManu_jsjbgzzy = ["3911", "3912", "3913", "3914", "3915", "3919", "3474", "3475"]
highTechManu_ylyqybzzy = ["3581", "3582", "3583", "3584", "3585", "3586", "3589", "4011", "4012", "4013", "4014",
                          "4015", "4016",
                          "4019", "4021", "4022", "4023", "4024", "4025", "4026", "4027", "4028", "4029", "4040",
                          "4090"]
highTechManu_xxhxpzzy = ["2664", "2665"]
highTechManu = highTechManu_yyzzy + highTechManu_hkhtzzy + highTechManu_dztxzzy + highTechManu_jsjbgzzy + highTechManu_ylyqybzzy + highTechManu_xxhxpzzy

zhulaninfo_TK = {
    "工业": ["1"],  # 工业必须有，不可删除
    "建筑业": ["2"],
    "批发业": ["3"],
    "零售业": ["4"],
    "住宿业": ["5"],
    "餐饮业": ["6"],
    "房地产": ["7"],
    "服务业": ["8"],
    "投资": ["9"],
    "总计": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "五上": ["1", "2", "3", "4", "5", "6", "7", "8"],
    "农林牧渔业": ["01", "02", "03", "04", "05"],
    "采矿业": ["06", "07", "08", "09", "10", "11", "12"],
    "制造业": ["1300", "4399"],
    "高技术制造业": highTechManu,
    "高技术医药制造业": highTechManu_yyzzy,
    "高技术航空航天器及设备制造业": highTechManu_hkhtzzy,
    "高技术电子及通信设备制造业": highTechManu_dztxzzy,
    "高技术计算机及办公设备制造业": highTechManu_jsjbgzzy,
    "高技术医疗仪器设备及仪器仪表制造业": highTechManu_ylyqybzzy,
    "高技术信息化学品制造业": highTechManu_xxhxpzzy,

    # 添加新值后需要改动query_type == 'TK'下的代码，指定查询方式
}

binlaninfo_TK = {
    "上年度营收不够": ["1"],
    "当年无经营房地产": ["2"],
    "注销吊销退出": ["3"],
    "专业变更退出": ["4"],
    "辖区跨省退出": ["5"],
    "单位界定错误": ["6"],
    "投资项目完成": ["7"],
    "停业歇业退出": ["8"],
    "其他原因退出": ["9"],
    "合计": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
}


def query_year_month(t_C, query_type, cityinfo, specinfo):
    # count_temp = t_C.query.filter(t_C.数据处理地.startswith('6101%'),t_C.报表类别=="B").count()
    # count_temp = db.session.query(func.count(t_C.组织机构代码)).filter(t_C.数据处理地.startswith('6101%'),t_C.报表类别=="B").scalar()
    s_n = {}
    s = {}
    # print(list(cityinfo.keys()))
    # print(list(specinfo.keys()))
    # print(list(cityinfo.values()))
    for i in list(cityinfo.keys()):
        if query_type == 'LW':
            count_temp_haha = t_C.query.filter(t_C.数据处理地.startswith(cityinfo[i][0]))
            if len(cityinfo[i]) > 1:
                for k in range(1, len(cityinfo[i])):
                    count_temp_haha = count_temp_haha.union_all(
                        t_C.query.filter(t_C.数据处理地.startswith(cityinfo[i][k])))
        elif query_type == 'TK':
            if i in ["工业", "建筑业", "批发业", "零售业", "住宿业", "餐饮业", "房地产", "服务业", "投资", "总计", "五上"]:
                count_temp_haha = t_C.query.filter(t_C.所属专业 == cityinfo[i][0])
                if len(cityinfo[i]) > 1:
                    for k in range(1, len(cityinfo[i])):
                        count_temp_haha = count_temp_haha.union_all(
                            t_C.query.filter(t_C.所属专业 == cityinfo[i][k]))
            elif i in ["农林牧渔业", "采矿业"]:
                count_temp_haha = t_C.query.filter(t_C.行业代码_17.startswith(cityinfo[i][0]))
                if len(cityinfo[i]) > 1:
                    for k in range(1, len(cityinfo[i])):
                        count_temp_haha = count_temp_haha.union_all(
                            t_C.query.filter(t_C.行业代码_17.startswith(cityinfo[i][k])))
            elif i in ["高技术制造业", "高技术医药制造业", "高技术航空航天器及设备制造业", "高技术电子及通信设备制造业",
                       "高技术计算机及办公设备制造业", "高技术医疗仪器设备及仪器仪表制造业", "高技术信息化学品制造业"]:
                count_temp_haha = t_C.query.filter(t_C.行业代码_17.in_(cityinfo[i]))
            elif i in ["制造业"]:
                count_temp_haha = t_C.query.filter(t_C.行业代码_17.between(cityinfo[i][0], cityinfo[i][1]))
                # print(str(count_temp_haha))

        else:  # query_type == 'SP' or 'SP_YEAR'
            count_temp_haha = t_C.query.filter(t_C.统计局代码.startswith(cityinfo[i][0]))
            if len(cityinfo[i]) > 1:
                for k in range(1, len(cityinfo[i])):
                    count_temp_haha = count_temp_haha.union_all(
                        t_C.query.filter(t_C.统计局代码.startswith(cityinfo[i][k])))

        for j in list(specinfo.keys()):  # ['工业', ... '总计']
            count_temp1 = 0
            for list_temp in specinfo[j]:  # "总计"key对应的value["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                # count_temp = t_C.query.filter(t_C.数据处理地.startswith(cityinfo[i]), t_C.报表类别 == list_temp).count()
                if query_type == 'LW':
                    count_temp = count_temp_haha.filter(t_C.报表类别 == list_temp).count()
                    # count_temp = db.session.query(func.count(t_C.组织机构代码)).filter(
                    # t_C.数据处理地.startswith(cityinfo[i]), t_C.报表类别 == list_temp).scalar()
                elif query_type == 'SP':
                    count_temp = count_temp_haha.filter(t_C.所属专业 == list_temp, t_C.单位类型 == "1",
                                                        t_C.审批类型.in_(['1', '2', '6', '9'])).count()
                elif query_type == 'SP_YEAR':
                    count_temp = count_temp_haha.filter(t_C.所属专业 == list_temp, t_C.单位类型 == "1",
                                                        t_C.审核类型.in_(['1', '2', '4'])).count()
                elif query_type == 'TK':
                    count_temp = count_temp_haha.filter(t_C.审核类型 == list_temp, t_C.单位类型 == "1",
                                                        ).count()
                count_temp1 = count_temp1 + count_temp
            s_n[j] = count_temp1
            # print(s_n, "```````````")
            s[i] = copy.deepcopy(s_n)
    # print(s)
    return s


@first_blueprint.route('/login2/', methods=["GET", "POST"])
def login2():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        year_select = request.form.get("year_select")
        month_start = request.form.get("month_start")
        month_select = request.form.get("month_select")
        query_type = request.form.get("query_type")
        if (month_start == 'year_report' or month_select == 'year_report') and query_type == "LW":
            return render_template('error_nonianbao.html')
        L = []
        if month_start == 'year_report':
            if month_select == 'year_report':
                L.append(month_start)
            else:
                L.append(month_start)
                for t in range(2, int(month_select) + 1, 1):
                    if t < 10:
                        L.append("0" + str(t))
                    else:
                        L.append(str(t))
        else:
            for t in range(int(month_start), int(month_select) + 1, 1):
                if t < 10:
                    L.append("0" + str(t))
                else:
                    L.append(str(t))
        print(L)

        s_all = {}
        for x in L:
            if x == "year_report":
                if query_type == "SP":
                    post_str = "SP_YEAR" + str(int(year_select) - 1)
                    t_C = globals()[post_str]
                    # print(post_str, "####")
                    # print(query_type, "####")
                    msg_temp = query_year_month(t_C, "SP_YEAR", cityinfo_SP, specinfo_SP)
                    s_all[x] = msg_temp
                elif query_type == "TK":
                    post_str = "TK_YEAR" + str(int(year_select) - 1)
                    t_C = globals()[post_str]
                    # print(post_str, "####")
                    # print(query_type, "####")
                    msg_temp = query_year_month(t_C, "TK", zhulaninfo_TK, binlaninfo_TK)
                    s_all[x] = msg_temp
            else:
                post_str = query_type + year_select + x
                print(post_str, "~~~~~")
                t_C = globals()[post_str]
                if query_type == "LW":
                    msg_temp = query_year_month(t_C, query_type, cityinfo, specinfo)
                elif query_type == "SP":
                    msg_temp = query_year_month(t_C, query_type, cityinfo_SP, specinfo_SP)
                elif query_type == "TK":
                    msg_temp = query_year_month(t_C, query_type, zhulaninfo_TK, binlaninfo_TK)
                s_all[x + "月"] = msg_temp
        msg = json.dumps(s_all, ensure_ascii=False)

        s_all_lastyear = {}
        for x in L:
            if x == "year_report":
                if query_type == "SP":
                    post_str = "SP_YEAR" + str(int(year_select) - 2)
                    t_C = globals()[post_str]
                    msg_temp = query_year_month(t_C, "SP_YEAR", cityinfo_SP, specinfo_SP)
                    s_all_lastyear[x] = msg_temp
                elif query_type == "TK":
                    post_str = "TK_YEAR" + str(int(year_select) - 2)
                    t_C = globals()[post_str]
                    msg_temp = query_year_month(t_C, "TK", zhulaninfo_TK, binlaninfo_TK)
                    s_all_lastyear[x] = msg_temp
            else:
                post_str = query_type + str(int(year_select) - 1) + x
                # print(post_str, "~~~~~")
                t_C = globals()[post_str]
                if query_type == "LW":
                    msg_temp = query_year_month(t_C, query_type, cityinfo, specinfo)
                elif query_type == "SP":
                    msg_temp = query_year_month(t_C, query_type, cityinfo_SP, specinfo_SP)
                elif query_type == "TK":
                    msg_temp = query_year_month(t_C, query_type, zhulaninfo_TK, binlaninfo_TK)
                s_all_lastyear[x + "月"] = msg_temp
        msg_lastyear = json.dumps(s_all_lastyear, ensure_ascii=False)

        s_december_lastyear = {}
        if query_type == "LW":
            post_str = query_type + str(int(year_select) - 1) + "12"
            t_C = globals()[post_str]
            msg_temp = query_year_month(t_C, "LW", cityinfo, specinfo)
            s_december_lastyear["12月"] = msg_temp
        msg_december_lastyear = json.dumps(s_december_lastyear, ensure_ascii=False)

        # print(type(msg_lastyear))
        # print(msg_lastyear)
        # print(type(msg))
        # print(msg)

        # response = 'count_temp的个数是{}'.format(count_temp)
        # response.set_cookie("cookie_username", username)     # 设置cookie
        # session["session_username"] = username  # 设置session
        return render_template('index.html', msg=msg, msg_lastyear=msg_lastyear,
                               msg_december_lastyear=msg_december_lastyear,
                               aa={"name": "Bill Gates", "age": 62, "city": "Seattle"},
                               year_select=year_select, month_start=month_start, month_select=month_select,
                               query_type=query_type)
        # 注意这里必须将response返回，否则不能set_cookie


@first_blueprint.errorhandler(500)
def internal_error(error):
    return render_template('error_500.html'), 500

    # def query_year_month(t_C, query_type, cityinfo, specinfo):
    #     # count_temp = t_C.query.filter(t_C.数据处理地.startswith('6101%'),t_C.报表类别=="B").count()
    #     # count_temp = db.session.query(func.count(t_C.组织机构代码)).filter(t_C.数据处理地.startswith('6101%'),t_C.报表类别=="B").scalar()
    #     s_n = {}
    #     s = {}
    #     print(list(cityinfo.keys()))
    #     print(list(specinfo.keys()))
    #     for i in list(cityinfo.keys()):
    #         for j in list(specinfo.keys()):  # ['工业', ... '总计', '同比']
    #             count_temp1 = 0
    #             for list_temp in specinfo[j]:  # "总计"key对应的value["1", "2", "3", "4", "5", "6", "7", "8", "9"],
    #                 # count_temp = t_C.query.filter(t_C.数据处理地.startswith(cityinfo[i]), t_C.报表类别 == list_temp).count()
    #                 if query_type == 'LW':
    #                     count_temp = db.session.query(func.count(t_C.组织机构代码)).filter(
    #                         t_C.数据处理地.startswith(cityinfo[i]), t_C.报表类别 == list_temp).scalar()
    #                 elif query_type == 'SP':
    #                     if cityinfo[i] == "6104%":
    #                         count_temp = db.session.query(func.count(t_C.组织机构代码)).filter(
    #                             or_(t_C.统计局代码.like('6104[^0]%'), t_C.统计局代码.like('61040[^3]%'))).filter(
    #                             t_C.所属专业 == list_temp, t_C.单位类型 == "1").filter(
    #                             t_C.审批类型.in_(['1', '2', '6', '9'])).scalar()
    #                     else:
    #                         count_temp = db.session.query(func.count(t_C.组织机构代码)).filter(
    #                             t_C.统计局代码.startswith(cityinfo[i]), t_C.所属专业 == list_temp,
    #                                                                t_C.单位类型 == "1").filter(
    #                             t_C.审批类型.in_(['1', '2', '6', '9'])).scalar()
    #                 elif query_type == 'SP_YEAR':
    #                     if cityinfo[i] == "6104%":
    #                         count_temp = db.session.query(func.count(t_C.组织机构代码)).filter(
    #                             or_(t_C.统计局代码.like('6104[^0]%'), t_C.统计局代码.like('61040[^3]%'))).filter(
    #                             t_C.所属专业 == list_temp, t_C.单位类型 == "1").filter(
    #                             t_C.审核类型.in_(['1', '2', '4'])).scalar()
    #                     else:
    #                         count_temp = db.session.query(func.count(t_C.组织机构代码)).filter(
    #                             t_C.统计局代码.startswith(cityinfo[i]), t_C.所属专业 == list_temp,
    #                                                                t_C.单位类型 == "1").filter(
    #                             t_C.审核类型.in_(['1', '2', '4'])).scalar()
    #
    #                 count_temp1 = count_temp1 + count_temp
    #             s_n[j] = count_temp1
    #         # print(s_n, "```````````")
    #         s[i] = copy.deepcopy(s_n)
    #     print(s)
    #     return s


'''原版正确运行的s_all
        s_all = {}
        for x in L:
            if x == "year_report":
                post_str = "SP_YEAR" + str(int(year_select) - 1)
                t_C = globals()[post_str]
                # print(post_str, "####")
                # print(query_type, "####")
                msg_temp = query_year_month(t_C, "SP_YEAR", cityinfo_SP, specinfo_SP)
                s_all[x] = msg_temp
            else:
                post_str = query_type + year_select + x
                # print(post_str, "~~~~~")
                t_C = globals()[post_str]
                if query_type == "LW":
                    msg_temp = query_year_month(t_C, query_type, cityinfo, specinfo)
                elif query_type == "SP":
                    msg_temp = query_year_month(t_C, query_type, cityinfo_SP, specinfo_SP)
                s_all[x + "月"] = msg_temp
        msg = json.dumps(s_all, ensure_ascii=False)
        # print(type(msg))
        # print(msg)
'''

# 原版正确的s_all_lastyear
# s_all_lastyear = {}
# for x in L:
#     if x == "year_report":
#         post_str = "SP_YEAR" + str(int(year_select) - 2)
#         t_C = globals()[post_str]
#         # print(post_str, "####")
#         # print(query_type, "####")
#         msg_temp = query_year_month(t_C, "SP_YEAR", cityinfo_SP, specinfo_SP)
#         s_all_lastyear[x] = msg_temp
#     else:
#         post_str = query_type + str(int(year_select) - 1) + x
#         # print(post_str, "~~~~~")
#         t_C = globals()[post_str]
#         if query_type == "LW":
#             msg_temp = query_year_month(t_C, query_type, cityinfo, specinfo)
#         elif query_type == "SP":
#             msg_temp = query_year_month(t_C, query_type, cityinfo_SP, specinfo_SP)
#         s_all_lastyear[x + "月"] = msg_temp
# msg_lastyear = json.dumps(s_all_lastyear, ensure_ascii=False)


'''原版正确运行的query_year_month函数
def query_year_month(t_C, query_type, cityinfo, specinfo):
    # count_temp = t_C.query.filter(t_C.数据处理地.startswith('6101%'),t_C.报表类别=="B").count()
    # count_temp = db.session.query(func.count(t_C.组织机构代码)).filter(t_C.数据处理地.startswith('6101%'),t_C.报表类别=="B").scalar()
    s_n = {}
    s = {}
    # print(list(cityinfo.keys()))
    # print(list(specinfo.keys()))
    # print(list(cityinfo.values()))
    for i in list(cityinfo.keys()):
        if query_type == 'LW':
            count_temp_haha = t_C.query.filter(t_C.数据处理地.startswith(cityinfo[i][0]))
            if len(cityinfo[i]) > 1:
                for k in range(1, len(cityinfo[i])):
                    count_temp_haha = count_temp_haha.union_all(
                        t_C.query.filter(t_C.数据处理地.startswith(cityinfo[i][k])))
        else:
            count_temp_haha = t_C.query.filter(t_C.统计局代码.startswith(cityinfo[i][0]))
            if len(cityinfo[i]) > 1:
                for k in range(1, len(cityinfo[i])):
                    count_temp_haha = count_temp_haha.union_all(
                        t_C.query.filter(t_C.统计局代码.startswith(cityinfo[i][k])))
        for j in list(specinfo.keys()):  # ['工业', ... '总计']
            count_temp1 = 0
            for list_temp in specinfo[j]:  # "总计"key对应的value["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                # count_temp = t_C.query.filter(t_C.数据处理地.startswith(cityinfo[i]), t_C.报表类别 == list_temp).count()
                if query_type == 'LW':
                    count_temp = count_temp_haha.filter(t_C.报表类别 == list_temp).count()
                    # count_temp = db.session.query(func.count(t_C.组织机构代码)).filter(
                    # t_C.数据处理地.startswith(cityinfo[i]), t_C.报表类别 == list_temp).scalar()
                elif query_type == 'SP':
                    count_temp = count_temp_haha.filter(t_C.所属专业 == list_temp, t_C.单位类型 == "1",
                                                        t_C.审批类型.in_(['1', '2', '6', '9'])).count()
                elif query_type == 'SP_YEAR':
                    count_temp = count_temp_haha.filter(t_C.所属专业 == list_temp, t_C.单位类型 == "1",
                                                        t_C.审核类型.in_(['1', '2', '4'])).count()

                count_temp1 = count_temp1 + count_temp
            s_n[j] = count_temp1
            # print(s_n, "```````````")
            s[i] = copy.deepcopy(s_n)
    # print(s)
    return s
'''
