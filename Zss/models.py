from Zss.extensions import db
#  db的来源是from flask_sqlalchemy import SQLAlchemy  #db = SQLAlchemy()

year = ["2013", "2014", "2015", "2016","2017", "2018", "2019", "2020","2021"]
month = ["02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
query_type = ["LW", "SP","TK"]
query_type1 = ["SP_YEAR","TK_YEAR"]


def create_class(query_type, year, month=[""]):
    for x in query_type:
        for y in year:
            for z in month:
                if x == "LW":
                    # if z in ("2", "3", "4", "5", "6", "7", "8", "9"):
                    #     globals()[str(x + y + z)] = type(x + y + z, (db.Model, Month),
                    #                                      {'__tablename__': y + "0" + z + "_month",
                    #                                       '__bind_key__': 'zss'})
                    # else:
                    globals()[str(x + y + z)] = type(x + y + z, (db.Model, MonthLW),
                                                     {'__tablename__': y + z + "_month", '__bind_key__': 'zss'})
                elif x == "SP":
                    # if z in ("2", "3", "4", "5", "6", "7", "8", "9"):
                    #     globals()[str(x + y + z)] = type(x + y + z, (db.Model, Month),
                    #                                      {'__tablename__': y + "0" + z + "_month_1"})
                    # else:
                    globals()[str(x + y + z)] = type(x + y + z, (db.Model, MonthSP),
                                                     {'__tablename__': y + z + "_month_1"})
                elif x == "SP_YEAR":
                    globals()[str(x + y + z)] = type(x + y + z, (db.Model, MonthSPYEAR),
                                                     {'__tablename__': y + z + "_year_1"})
                elif x == "TK":
                    globals()[str(x + y + z)] = type(x + y + z, (db.Model, Month_TK),
                                                     {'__tablename__': y + z + "_month_2",'__bind_key__': 'tk'})
                elif x == "TK_YEAR":
                    globals()[str(x + y + z)] = type(x + y + z, (db.Model, Month_TKYEAR),
                                                     {'__tablename__': y + z + "_year_2",'__bind_key__': 'tk'})

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16))
    password = db.Column(db.String(16))


class User1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16))
    password = db.Column(db.String(16))


class User2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16))
    password = db.Column(db.String(16))


class MonthLW():
    数据处理地 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    单位详细名称 = db.Column(db.Unicode(255))
    期别_年_ = db.Column('期别(年)', db.Unicode(255))
    期别_月_ = db.Column('期别(月)', db.Unicode(255))
    主要业务活动_或主要产品_1 = db.Column('主要业务活动(或主要产品)1', db.Unicode(255))
    主要业务活动_或主要产品_2 = db.Column('主要业务活动(或主要产品)2', db.Unicode(255))
    主要业务活动_或主要产品_3 = db.Column('主要业务活动(或主要产品)3', db.Unicode(255))
    # 行业代码_2011_ = db.Column('行业代码(2011)', db.Unicode(255))
    报表类别 = db.Column(db.Unicode(255))
    行政区划代码 = db.Column(db.Unicode(255))
    单位注册地址所在行政区划代码 = db.Column(db.Unicode(255))
    单位规模 = db.Column(db.Unicode(255))
    从业人员期末人数_人 = db.Column('从业人员期末人数;人', db.Float(53))
    女性_人 = db.Column('女性;人', db.Float(53))
    营业收入_千元 = db.Column('营业收入;千元', db.Float(53))
    主营业务收入_千元 = db.Column('主营业务收入;千元', db.Float(53))
    资产_千元 = db.Column('资产;千元', db.Float(53))
    # 开业_成立_时间_年_ = db.Column('开业(成立)时间(年)', db.Unicode(255))
    # 开业_成立_时间_月_ = db.Column('开业(成立)时间(月)', db.Unicode(255))
    登记注册类型 = db.Column(db.Unicode(255))
    企业控股情况 = db.Column(db.Unicode(255))
    隶属关系 = db.Column(db.Unicode(255))
    # 企业营业状态 = db.Column(db.Unicode(255))
    执行会计制度类别 = db.Column(db.Unicode(255))
    执行企业会计准则情况 = db.Column(db.Unicode(255))
    机构类型 = db.Column(db.Unicode(255))
    产业活动单位数_总计_ = db.Column('产业活动单位数(总计)', db.Float(53))
    企业集团情况 = db.Column(db.Unicode(255))


class MonthSP():
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    统计局代码 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))


class MonthSPYEAR():
    审核类型 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    统计局代码 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))

class Month():
    数据处理地 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    单位详细名称 = db.Column(db.Unicode(255))
    期别_年_ = db.Column('期别(年)', db.Unicode(255))
    期别_月_ = db.Column('期别(月)', db.Unicode(255))
    主要业务活动_或主要产品_1 = db.Column('主要业务活动(或主要产品)1', db.Unicode(255))
    主要业务活动_或主要产品_2 = db.Column('主要业务活动(或主要产品)2', db.Unicode(255))
    主要业务活动_或主要产品_3 = db.Column('主要业务活动(或主要产品)3', db.Unicode(255))
    行业代码_2011_ = db.Column('行业代码(2011)', db.Unicode(255))
    报表类别 = db.Column(db.Unicode(255))
    行政区划代码 = db.Column(db.Unicode(255))
    单位注册地址所在行政区划代码 = db.Column(db.Unicode(255))
    单位规模 = db.Column(db.Unicode(255))
    从业人员期末人数_人 = db.Column('从业人员期末人数;人', db.Float(53))
    女性_人 = db.Column('女性;人', db.Float(53))
    营业收入_千元 = db.Column('营业收入;千元', db.Float(53))
    主营业务收入_千元 = db.Column('主营业务收入;千元', db.Float(53))
    资产_千元 = db.Column('资产;千元', db.Float(53))
    开业_成立_时间_年_ = db.Column('开业(成立)时间(年)', db.Unicode(255))
    开业_成立_时间_月_ = db.Column('开业(成立)时间(月)', db.Unicode(255))
    登记注册类型 = db.Column(db.Unicode(255))
    企业控股情况 = db.Column(db.Unicode(255))
    隶属关系 = db.Column(db.Unicode(255))
    企业营业状态 = db.Column(db.Unicode(255))
    执行会计制度类别 = db.Column(db.Unicode(255))
    执行企业会计准则情况 = db.Column(db.Unicode(255))
    机构类型 = db.Column(db.Unicode(255))
    产业活动单位数_总计_ = db.Column('产业活动单位数(总计)', db.Float(53))
    企业集团情况 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审核类型 = db.Column(db.Unicode(255))

class Month_TK():
    单位类型 = db.Column(db.Unicode(255))
    审核类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255),primary_key=True)
    单位详细名称 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    实际单位类型 = db.Column(db.Unicode(255))
    备注 = db.Column(db.Unicode(255))
    #填表处理地代码 = db.Column(db.Unicode(255))

class Month_TKYEAR():
    单位类型 = db.Column(db.Unicode(255))
    审核类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255),primary_key=True)
    详细名称 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    实际单位类型 = db.Column(db.Unicode(255))
    备注 = db.Column(db.Unicode(255))
    填表处理地代码 = db.Column(db.Unicode(255))



create_class(query_type, year, month=month)
create_class(query_type1, year)

# class TK202102(db.Model, Month_TK):
#     __tablename__ = '202102_month_2'
#     __bind_key__ = 'tk'

# class LW201912(db.Model, Month):
#     __tablename__ = '201912_month'
#     __bind_key__ = 'zss'
#
#
# class LW201911(db.Model, Month):
#     __tablename__ = '201911_month'
#     __bind_key__ = 'zss'
#
#
# class LW201910(db.Model, Month):
#     __tablename__ = '201910_month'
#     __bind_key__ = 'zss'
#
#
# class LW20199(db.Model, Month):
#     __tablename__ = '201909_month'
#     __bind_key__ = 'zss'
#
#
# class LW20198(db.Model, Month):
#     __tablename__ = '201908_month'
#     __bind_key__ = 'zss'
#
#
# class LW20197(db.Model, Month):
#     __tablename__ = '201907_month'
#     __bind_key__ = 'zss'
#
#
# class LW20196(db.Model, Month):
#     __tablename__ = '201906_month'
#     __bind_key__ = 'zss'
#
#
# class LW20195(db.Model, Month):
#     __tablename__ = '201905_month'
#     __bind_key__ = 'zss'
#
#
# class LW20194(db.Model, Month):
#     __tablename__ = '201904_month'
#     __bind_key__ = 'zss'
#
#
# class LW20193(db.Model, Month):
#     __tablename__ = '201903_month'
#     __bind_key__ = 'zss'
#
#
# class LW20192(db.Model, Month):
#     __tablename__ = '201902_month'
#     __bind_key__ = 'zss'
#
#
# class SP20192(db.Model, Month):
#     __tablename__ = '201902_month_1'
#
#
# class SP20193(db.Model, Month):
#     __tablename__ = '201903_month_1'
#
#
# class SP20194(db.Model, Month):
#     __tablename__ = '201904_month_1'
#
#
# class SP20195(db.Model, Month):
#     __tablename__ = '201905_month_1'
#
#
# class SP20196(db.Model, Month):
#     __tablename__ = '201906_month_1'
#
#
# class SP20197(db.Model, Month):
#     __tablename__ = '201907_month_1'
#
#
# class SP20198(db.Model, Month):
#     __tablename__ = '201908_month_1'
#
#
# class SP20199(db.Model, Month):
#     __tablename__ = '201909_month_1'
#
#
# class SP201910(db.Model, Month):
#     __tablename__ = '201910_month_1'
#
#
# class SP201911(db.Model, Month):
#     __tablename__ = '201911_month_1'
#
#
# class SP201912(db.Model, Month):
#     __tablename__ = '201912_month_1'
