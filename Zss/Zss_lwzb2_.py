# coding: utf-8
from sqlalchemy import Column, Float, Table, Unicode
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class 201512Month(db.Model):
    __tablename__ = '201512_month'

    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    数据处理地 = db.Column(db.Unicode(255))
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



class 201602Month(db.Model):
    __tablename__ = '201602_month'

    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    数据处理地 = db.Column(db.Unicode(255))
    单位详细名称 = db.Column(db.Unicode(255))
    期别_年_ = db.Column('期别(年)', db.Unicode(255))
    期别_月_ = db.Column('期别(月)', db.Unicode(255))
    统一社会信用代码 = db.Column(db.Unicode(255))
    主要业务活动_或主要产品_1 = db.Column('主要业务活动(或主要产品)1', db.Unicode(255))
    主要业务活动_或主要产品_2 = db.Column('主要业务活动(或主要产品)2', db.Unicode(255))
    主要业务活动_或主要产品_3 = db.Column('主要业务活动(或主要产品)3', db.Unicode(255))
    行业代码_2011_ = db.Column('行业代码(2011)', db.Unicode(255))
    报表类别 = db.Column(db.Unicode(255))
    单位规模 = db.Column(db.Unicode(255))
    从业人员期末人数_人 = db.Column('从业人员期末人数;人', db.Float(53))
    女性_人 = db.Column('女性;人', db.Float(53))
    营业收入_千元 = db.Column('营业收入;千元', db.Float(53))
    主营业务收入_千元 = db.Column('主营业务收入;千元', db.Float(53))
    资产_千元 = db.Column('资产;千元', db.Float(53))
    开业_成立_时间_年_ = db.Column('开业(成立)时间(年)', db.Unicode(255))
    开业_成立_时间_月_ = db.Column('开业(成立)时间(月)', db.Unicode(255))
    行政区划代码 = db.Column(db.Unicode(255))
    单位注册地址所在行政区划代码 = db.Column(db.Unicode(255))
    登记注册类型 = db.Column(db.Unicode(255))
    是否台商投资 = db.Column(db.Unicode(255))
    企业控股情况 = db.Column(db.Unicode(255))
    隶属关系 = db.Column(db.Unicode(255))
    企业营业状态 = db.Column(db.Unicode(255))
    执行会计制度类别 = db.Column(db.Unicode(255))
    执行企业会计准则情况 = db.Column(db.Unicode(255))
    机构类型 = db.Column(db.Unicode(255))
    产业活动单位数_总计_ = db.Column('产业活动单位数(总计)', db.Unicode(255))
    企业集团情况 = db.Column(db.Unicode(255))



class 201612Month(db.Model):
    __tablename__ = '201612_month'

    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    数据处理地 = db.Column(db.Unicode(255))
    单位详细名称 = db.Column(db.Unicode(255))
    期别_年_ = db.Column('期别(年)', db.Unicode(255))
    期别_月_ = db.Column('期别(月)', db.Unicode(255))
    统一社会信用代码 = db.Column(db.Unicode(255))
    主要业务活动_或主要产品_1 = db.Column('主要业务活动(或主要产品)1', db.Unicode(255))
    主要业务活动_或主要产品_2 = db.Column('主要业务活动(或主要产品)2', db.Unicode(255))
    主要业务活动_或主要产品_3 = db.Column('主要业务活动(或主要产品)3', db.Unicode(255))
    行业代码_2011_ = db.Column('行业代码(2011)', db.Unicode(255))
    报表类别 = db.Column(db.Unicode(255))
    单位规模 = db.Column(db.Unicode(255))
    从业人员期末人数_人 = db.Column('从业人员期末人数;人', db.Float(53))
    女性_人 = db.Column('女性;人', db.Float(53))
    营业收入_千元 = db.Column('营业收入;千元', db.Float(53))
    主营业务收入_千元 = db.Column('主营业务收入;千元', db.Float(53))
    资产_千元 = db.Column('资产;千元', db.Float(53))
    开业_成立_时间_年_ = db.Column('开业(成立)时间(年)', db.Unicode(255))
    开业_成立_时间_月_ = db.Column('开业(成立)时间(月)', db.Unicode(255))
    行政区划代码 = db.Column(db.Unicode(255))
    单位注册地址所在行政区划代码 = db.Column(db.Unicode(255))
    登记注册类型 = db.Column(db.Unicode(255))
    是否台商投资 = db.Column(db.Unicode(255))
    企业控股情况 = db.Column(db.Unicode(255))
    隶属关系 = db.Column(db.Unicode(255))
    企业营业状态 = db.Column(db.Unicode(255))
    执行会计制度类别 = db.Column(db.Unicode(255))
    执行企业会计准则情况 = db.Column(db.Unicode(255))
    机构类型 = db.Column(db.Unicode(255))
    产业活动单位数_总计_ = db.Column('产业活动单位数(总计)', db.Float(53))
    企业集团情况 = db.Column(db.Unicode(255))



class 201702Month(db.Model):
    __tablename__ = '201702_month'

    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    数据处理地 = db.Column(db.Unicode(255))
    单位详细名称 = db.Column(db.Unicode(255))
    统一社会信用代码 = db.Column(db.Unicode(255))
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
    营业税金及附加_千元 = db.Column('营业税金及附加;千元', db.Unicode(255))
    主营业务税金及附加_千元 = db.Column('主营业务税金及附加;千元', db.Unicode(255))
    开业_成立_时间_年_ = db.Column('开业(成立)时间(年)', db.Unicode(255))
    开业_成立_时间_月_ = db.Column('开业(成立)时间(月)', db.Unicode(255))
    登记注册类型 = db.Column(db.Unicode(255))
    是否台商投资 = db.Column(db.Unicode(255))
    企业控股情况 = db.Column(db.Unicode(255))
    隶属关系 = db.Column(db.Unicode(255))
    企业营业状态 = db.Column(db.Unicode(255))
    执行会计制度类别 = db.Column(db.Unicode(255))
    执行企业会计准则情况 = db.Column(db.Unicode(255))
    机构类型 = db.Column(db.Unicode(255))
    产业活动单位数_总计_ = db.Column('产业活动单位数(总计)', db.Float(53))
    企业集团情况 = db.Column(db.Unicode(255))
    期别_月_ = db.Column('期别(月)', db.Unicode(255))
    期别_年_ = db.Column('期别(年)', db.Unicode(255))



class 201712Month(db.Model):
    __tablename__ = '201712_month'

    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    数据处理地 = db.Column(db.Unicode(255))
    单位详细名称 = db.Column(db.Unicode(255))
    统一社会信用代码 = db.Column(db.Unicode(255))
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
    营业税金及附加_千元 = db.Column('营业税金及附加;千元', db.Float(53))
    主营业务税金及附加_千元 = db.Column('主营业务税金及附加;千元', db.Float(53))
    开业_成立_时间_年_ = db.Column('开业(成立)时间(年)', db.Unicode(255))
    开业_成立_时间_月_ = db.Column('开业(成立)时间(月)', db.Unicode(255))
    登记注册类型 = db.Column(db.Unicode(255))
    是否台商投资 = db.Column(db.Unicode(255))
    企业控股情况 = db.Column(db.Unicode(255))
    隶属关系 = db.Column(db.Unicode(255))
    企业营业状态 = db.Column(db.Unicode(255))
    执行会计制度类别 = db.Column(db.Unicode(255))
    执行企业会计准则情况 = db.Column(db.Unicode(255))
    机构类型 = db.Column(db.Unicode(255))
    产业活动单位数_总计_ = db.Column('产业活动单位数(总计)', db.Float(53))
    企业集团情况 = db.Column(db.Unicode(255))
    期别_月_ = db.Column('期别(月)', db.Unicode(255))
    期别_年_ = db.Column('期别(年)', db.Unicode(255))



class 201802Month(db.Model):
    __tablename__ = '201802_month'

    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    数据处理地 = db.Column(db.Unicode(255))
    单位详细名称 = db.Column(db.Unicode(255))
    期别_年_ = db.Column('期别(年)', db.Unicode(255))
    期别_月_ = db.Column('期别(月)', db.Unicode(255))
    报表类别 = db.Column(db.Unicode(255))
    主要业务活动_或主要产品_1 = db.Column('主要业务活动(或主要产品)1', db.Unicode(255))
    单位注册地址所在行政区划代码 = db.Column(db.Unicode(255))
    营业收入_千元 = db.Column('营业收入;千元', db.Float(53))
    主营业务收入_千元 = db.Column('主营业务收入;千元', db.Float(53))
    营业税金及附加_千元 = db.Column('营业税金及附加;千元', db.Float(53))
    主营业务税金及附加_千元 = db.Column('主营业务税金及附加;千元', db.Float(53))
    开业_成立_时间_年_ = db.Column('开业(成立)时间(年)', db.Unicode(255))
    开业_成立_时间_月_ = db.Column('开业(成立)时间(月)', db.Unicode(255))
    行业代码_2011_ = db.Column('行业代码(2011)', db.Unicode(255))
    行业代码_GB_T4754_2017_ = db.Column('行业代码(GB/T4754-2017)', db.Unicode(255))
    行政区划代码 = db.Column(db.Unicode(255))
    单位规模 = db.Column(db.Unicode(255))
    资产_千元 = db.Column('资产;千元', db.Float(53))
    企业营业状态 = db.Column(db.Unicode(255))
    机构类型 = db.Column(db.Unicode(255))
    主要业务活动_或主要产品_2 = db.Column('主要业务活动(或主要产品)2', db.Unicode(255))
    主要业务活动_或主要产品_3 = db.Column('主要业务活动(或主要产品)3', db.Unicode(255))
    从业人员期末人数_人 = db.Column('从业人员期末人数;人', db.Float(53))
    女性_人 = db.Column('女性;人', db.Float(53))
    登记注册类型 = db.Column(db.Unicode(255))
    是否台商投资 = db.Column(db.Unicode(255))
    企业控股情况 = db.Column(db.Unicode(255))
    隶属关系 = db.Column(db.Unicode(255))
    执行企业会计准则情况 = db.Column(db.Unicode(255))
    产业活动单位数_总计_ = db.Column('产业活动单位数(总计)', db.Float(53))
    企业集团情况 = db.Column(db.Unicode(255))
    执行会计制度类别 = db.Column(db.Unicode(255))
    统一社会信用代码 = db.Column(db.Unicode(255))



class 201812Month(db.Model):
    __tablename__ = '201812_month'

    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    数据处理地 = db.Column(db.Unicode(255))
    单位详细名称 = db.Column(db.Unicode(255))
    期别_年_ = db.Column('期别(年)', db.Unicode(255))
    期别_月_ = db.Column('期别(月)', db.Unicode(255))
    报表类别 = db.Column(db.Unicode(255))
    主要业务活动_或主要产品_1 = db.Column('主要业务活动(或主要产品)1', db.Unicode(255))
    单位注册地址所在行政区划代码 = db.Column(db.Unicode(255))
    营业收入_千元 = db.Column('营业收入;千元', db.Float(53))
    主营业务收入_千元 = db.Column('主营业务收入;千元', db.Float(53))
    营业税金及附加_千元 = db.Column('营业税金及附加;千元', db.Float(53))
    主营业务税金及附加_千元 = db.Column('主营业务税金及附加;千元', db.Float(53))
    开业_成立_时间_年_ = db.Column('开业(成立)时间(年)', db.Unicode(255))
    开业_成立_时间_月_ = db.Column('开业(成立)时间(月)', db.Unicode(255))
    行业代码_2011_ = db.Column('行业代码(2011)', db.Unicode(255))
    行业代码_GB_T4754_2017_ = db.Column('行业代码(GB/T4754-2017)', db.Unicode(255))
    行政区划代码 = db.Column(db.Unicode(255))
    单位规模 = db.Column(db.Unicode(255))
    资产_千元 = db.Column('资产;千元', db.Float(53))
    企业营业状态 = db.Column(db.Unicode(255))
    机构类型 = db.Column(db.Unicode(255))
    主要业务活动_或主要产品_2 = db.Column('主要业务活动(或主要产品)2', db.Unicode(255))
    主要业务活动_或主要产品_3 = db.Column('主要业务活动(或主要产品)3', db.Unicode(255))
    从业人员期末人数_人 = db.Column('从业人员期末人数;人', db.Float(53))
    女性_人 = db.Column('女性;人', db.Float(53))
    登记注册类型 = db.Column(db.Unicode(255))
    是否台商投资 = db.Column(db.Unicode(255))
    企业控股情况 = db.Column(db.Unicode(255))
    隶属关系 = db.Column(db.Unicode(255))
    执行企业会计准则情况 = db.Column(db.Unicode(255))
    产业活动单位数_总计_ = db.Column('产业活动单位数(总计)', db.Float(53))
    企业集团情况 = db.Column(db.Unicode(255))
    执行会计制度类别 = db.Column(db.Unicode(255))
    统一社会信用代码 = db.Column(db.Unicode(255))



t_2018_year = db.Table(
    '2018_year',
    db.Column('组织机构代码', db.Unicode(255)),
    db.Column('数据处理地', db.Unicode(255)),
    db.Column('单位详细名称', db.Unicode(255)),
    db.Column('期别(年)', db.Unicode(255)),
    db.Column('统一社会信用代码', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)1', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)2', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)3', db.Unicode(255)),
    db.Column('行业代码(GB/T4754-2017)', db.Unicode(255)),
    db.Column('经济活动名称1', db.Unicode(255)),
    db.Column('经济活动名称2', db.Unicode(255)),
    db.Column('经济活动名称3', db.Unicode(255)),
    db.Column('报表类别', db.Unicode(255)),
    db.Column('行政区划代码', db.Unicode(255)),
    db.Column('单位注册地址所在行政区划代码', db.Unicode(255)),
    db.Column('单位规模', db.Unicode(255)),
    db.Column('从业人员期末人数;人', db.Float(53)),
    db.Column('女性;人', db.Float(53)),
    db.Column('营业收入;千元', db.Float(53)),
    db.Column('主营业务收入;千元', db.Float(53)),
    db.Column('资产总计;千元', db.Float(53)),
    db.Column('税金及附加;千元', db.Float(53)),
    db.Column('开业(成立)时间(年)', db.Unicode(255)),
    db.Column('开业(成立)时间(月)', db.Unicode(255)),
    db.Column('登记注册类型', db.Unicode(255)),
    db.Column('企业控股情况', db.Unicode(255)),
    db.Column('隶属关系', db.Unicode(255)),
    db.Column('运营状态', db.Unicode(255)),
    db.Column('是否港商投资', db.Unicode(255)),
    db.Column('是否澳商投资', db.Unicode(255)),
    db.Column('是否台商投资', db.Unicode(255)),
    db.Column('执行会计标准类别', db.Unicode(255)),
    db.Column('执行企业会计准则情况', db.Unicode(255)),
    db.Column('机构类型', db.Unicode(255)),
    db.Column('企业集团情况', db.Unicode(255)),
    db.Column('上级法人统一社会信用代码', db.Unicode(255)),
    db.Column('上级法人单位组织机构代码', db.Unicode(255))
)



class 201902Month(db.Model):
    __tablename__ = '201902_month'

    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    数据处理地 = db.Column(db.Unicode(255))
    单位详细名称 = db.Column(db.Unicode(255))
    期别_年_ = db.Column('期别(年)', db.Unicode(255))
    期别_月_ = db.Column('期别(月)', db.Unicode(255))
    统一社会信用代码 = db.Column(db.Unicode(255))
    主要业务活动_或主要产品_1 = db.Column('主要业务活动(或主要产品)1', db.Unicode(255))
    主要业务活动_或主要产品_2 = db.Column('主要业务活动(或主要产品)2', db.Unicode(255))
    主要业务活动_或主要产品_3 = db.Column('主要业务活动(或主要产品)3', db.Unicode(255))
    行业代码_GB_T4754_2017_ = db.Column('行业代码(GB/T4754-2017)', db.Unicode(255))
    报表类别 = db.Column(db.Unicode(255))
    行政区划代码 = db.Column(db.Unicode(255))
    单位注册地址所在行政区划代码 = db.Column(db.Unicode(255))
    单位规模 = db.Column(db.Unicode(255))
    从业人员期末人数_人 = db.Column('从业人员期末人数;人', db.Float(53))
    女性_人 = db.Column('女性;人', db.Float(53))
    营业收入_千元 = db.Column('营业收入;千元', db.Float(53))
    营业税金及附加_千元 = db.Column('营业税金及附加;千元', db.Float(53))
    主营业务收入_千元 = db.Column('主营业务收入;千元', db.Float(53))
    资产_千元 = db.Column('资产;千元', db.Float(53))
    开业_成立_时间_年_ = db.Column('开业(成立)时间(年)', db.Unicode(255))
    开业_成立_时间_月_ = db.Column('开业(成立)时间(月)', db.Unicode(255))
    登记注册类型 = db.Column(db.Unicode(255))
    是否港商投资 = db.Column(db.Unicode(255))
    是否港商投资1 = db.Column(db.Unicode(255))
    企业控股情况 = db.Column(db.Unicode(255))
    隶属关系 = db.Column(db.Unicode(255))
    运营状态 = db.Column(db.Unicode(255))
    执行会计制度类别 = db.Column(db.Unicode(255))
    执行企业会计准则情况 = db.Column(db.Unicode(255))
    机构类型 = db.Column(db.Unicode(255))
    产业活动单位数_总计_ = db.Column('产业活动单位数(总计)', db.Unicode(255))
    企业集团情况 = db.Column(db.Unicode(255))



class 201903Month(db.Model):
    __tablename__ = '201903_month'

    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    数据处理地 = db.Column(db.Unicode(255))
    单位详细名称 = db.Column(db.Unicode(255))
    期别_年_ = db.Column('期别(年)', db.Unicode(255))
    期别_月_ = db.Column('期别(月)', db.Unicode(255))
    统一社会信用代码 = db.Column(db.Unicode(255))
    主要业务活动_或主要产品_1 = db.Column('主要业务活动(或主要产品)1', db.Unicode(255))
    主要业务活动_或主要产品_2 = db.Column('主要业务活动(或主要产品)2', db.Unicode(255))
    主要业务活动_或主要产品_3 = db.Column('主要业务活动(或主要产品)3', db.Unicode(255))
    行业代码_GB_T4754_2017_ = db.Column('行业代码(GB/T4754-2017)', db.Unicode(255))
    报表类别 = db.Column(db.Unicode(255))
    行政区划代码 = db.Column(db.Unicode(255))
    单位注册地址所在行政区划代码 = db.Column(db.Unicode(255))
    单位规模 = db.Column(db.Unicode(255))
    从业人员期末人数_人 = db.Column('从业人员期末人数;人', db.Float(53))
    女性_人 = db.Column('女性;人', db.Float(53))
    营业收入_千元 = db.Column('营业收入;千元', db.Float(53))
    营业税金及附加_千元 = db.Column('营业税金及附加;千元', db.Float(53))
    主营业务收入_千元 = db.Column('主营业务收入;千元', db.Float(53))
    资产_千元 = db.Column('资产;千元', db.Float(53))
    开业_成立_时间_年_ = db.Column('开业(成立)时间(年)', db.Unicode(255))
    开业_成立_时间_月_ = db.Column('开业(成立)时间(月)', db.Unicode(255))
    登记注册类型 = db.Column(db.Unicode(255))
    是否港商投资 = db.Column(db.Unicode(255))
    是否港商投资1 = db.Column(db.Unicode(255))
    企业控股情况 = db.Column(db.Unicode(255))
    隶属关系 = db.Column(db.Unicode(255))
    运营状态 = db.Column(db.Unicode(255))
    执行会计制度类别 = db.Column(db.Unicode(255))
    执行企业会计准则情况 = db.Column(db.Unicode(255))
    机构类型 = db.Column(db.Unicode(255))
    产业活动单位数_总计_ = db.Column('产业活动单位数(总计)', db.Unicode(255))
    企业集团情况 = db.Column(db.Unicode(255))



class 201904Month(db.Model):
    __tablename__ = '201904_month'

    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    数据处理地 = db.Column(db.Unicode(255))
    单位详细名称 = db.Column(db.Unicode(255))
    期别_年_ = db.Column('期别(年)', db.Unicode(255))
    期别_月_ = db.Column('期别(月)', db.Unicode(255))
    统一社会信用代码 = db.Column(db.Unicode(255))
    主要业务活动_或主要产品_1 = db.Column('主要业务活动(或主要产品)1', db.Unicode(255))
    主要业务活动_或主要产品_2 = db.Column('主要业务活动(或主要产品)2', db.Unicode(255))
    主要业务活动_或主要产品_3 = db.Column('主要业务活动(或主要产品)3', db.Unicode(255))
    行业代码_GB_T4754_2017_ = db.Column('行业代码(GB/T4754-2017)', db.Unicode(255))
    报表类别 = db.Column(db.Unicode(255))
    行政区划代码 = db.Column(db.Unicode(255))
    单位注册地址所在行政区划代码 = db.Column(db.Unicode(255))
    单位规模 = db.Column(db.Unicode(255))
    从业人员期末人数_人 = db.Column('从业人员期末人数;人', db.Float(53))
    女性_人 = db.Column('女性;人', db.Float(53))
    营业收入_千元 = db.Column('营业收入;千元', db.Float(53))
    营业税金及附加_千元 = db.Column('营业税金及附加;千元', db.Float(53))
    主营业务收入_千元 = db.Column('主营业务收入;千元', db.Float(53))
    资产_千元 = db.Column('资产;千元', db.Float(53))
    开业_成立_时间_年_ = db.Column('开业(成立)时间(年)', db.Unicode(255))
    开业_成立_时间_月_ = db.Column('开业(成立)时间(月)', db.Unicode(255))
    登记注册类型 = db.Column(db.Unicode(255))
    是否港商投资 = db.Column(db.Unicode(255))
    是否港商投资1 = db.Column(db.Unicode(255))
    企业控股情况 = db.Column(db.Unicode(255))
    隶属关系 = db.Column(db.Unicode(255))
    运营状态 = db.Column(db.Unicode(255))
    执行会计制度类别 = db.Column(db.Unicode(255))
    执行企业会计准则情况 = db.Column(db.Unicode(255))
    机构类型 = db.Column(db.Unicode(255))
    产业活动单位数_总计_ = db.Column('产业活动单位数(总计)', db.Unicode(255))
    企业集团情况 = db.Column(db.Unicode(255))



class 201905Month(db.Model):
    __tablename__ = '201905_month'

    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    数据处理地 = db.Column(db.Unicode(255))
    单位详细名称 = db.Column(db.Unicode(255))
    期别_年_ = db.Column('期别(年)', db.Unicode(255))
    期别_月_ = db.Column('期别(月)', db.Unicode(255))
    统一社会信用代码 = db.Column(db.Unicode(255))
    主要业务活动_或主要产品_1 = db.Column('主要业务活动(或主要产品)1', db.Unicode(255))
    主要业务活动_或主要产品_2 = db.Column('主要业务活动(或主要产品)2', db.Unicode(255))
    主要业务活动_或主要产品_3 = db.Column('主要业务活动(或主要产品)3', db.Unicode(255))
    行业代码_GB_T4754_2017_ = db.Column('行业代码(GB/T4754-2017)', db.Unicode(255))
    报表类别 = db.Column(db.Unicode(255))
    行政区划代码 = db.Column(db.Unicode(255))
    单位注册地址所在行政区划代码 = db.Column(db.Unicode(255))
    单位规模 = db.Column(db.Unicode(255))
    从业人员期末人数_人 = db.Column('从业人员期末人数;人', db.Float(53))
    女性_人 = db.Column('女性;人', db.Float(53))
    营业收入_千元 = db.Column('营业收入;千元', db.Float(53))
    营业税金及附加_千元 = db.Column('营业税金及附加;千元', db.Float(53))
    主营业务收入_千元 = db.Column('主营业务收入;千元', db.Float(53))
    资产_千元 = db.Column('资产;千元', db.Float(53))
    开业_成立_时间_年_ = db.Column('开业(成立)时间(年)', db.Unicode(255))
    开业_成立_时间_月_ = db.Column('开业(成立)时间(月)', db.Unicode(255))
    登记注册类型 = db.Column(db.Unicode(255))
    是否港商投资 = db.Column(db.Unicode(255))
    是否港商投资1 = db.Column(db.Unicode(255))
    企业控股情况 = db.Column(db.Unicode(255))
    隶属关系 = db.Column(db.Unicode(255))
    运营状态 = db.Column(db.Unicode(255))
    执行会计制度类别 = db.Column(db.Unicode(255))
    执行企业会计准则情况 = db.Column(db.Unicode(255))
    机构类型 = db.Column(db.Unicode(255))
    产业活动单位数_总计_ = db.Column('产业活动单位数(总计)', db.Unicode(255))
    企业集团情况 = db.Column(db.Unicode(255))



class 201906Month(db.Model):
    __tablename__ = '201906_month'

    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    数据处理地 = db.Column(db.Unicode(255))
    单位详细名称 = db.Column(db.Unicode(255))
    期别_年_ = db.Column('期别(年)', db.Unicode(255))
    期别_月_ = db.Column('期别(月)', db.Unicode(255))
    统一社会信用代码 = db.Column(db.Unicode(255))
    主要业务活动_或主要产品_1 = db.Column('主要业务活动(或主要产品)1', db.Unicode(255))
    主要业务活动_或主要产品_2 = db.Column('主要业务活动(或主要产品)2', db.Unicode(255))
    主要业务活动_或主要产品_3 = db.Column('主要业务活动(或主要产品)3', db.Unicode(255))
    行业代码_GB_T4754_2017_ = db.Column('行业代码(GB/T4754-2017)', db.Unicode(255))
    报表类别 = db.Column(db.Unicode(255))
    行政区划代码 = db.Column(db.Unicode(255))
    单位注册地址所在行政区划代码 = db.Column(db.Unicode(255))
    单位规模 = db.Column(db.Unicode(255))
    从业人员期末人数_人 = db.Column('从业人员期末人数;人', db.Float(53))
    女性_人 = db.Column('女性;人', db.Float(53))
    营业收入_千元 = db.Column('营业收入;千元', db.Float(53))
    营业税金及附加_千元 = db.Column('营业税金及附加;千元', db.Float(53))
    主营业务收入_千元 = db.Column('主营业务收入;千元', db.Float(53))
    资产_千元 = db.Column('资产;千元', db.Float(53))
    开业_成立_时间_年_ = db.Column('开业(成立)时间(年)', db.Unicode(255))
    开业_成立_时间_月_ = db.Column('开业(成立)时间(月)', db.Unicode(255))
    登记注册类型 = db.Column(db.Unicode(255))
    是否港商投资 = db.Column(db.Unicode(255))
    是否港商投资1 = db.Column(db.Unicode(255))
    企业控股情况 = db.Column(db.Unicode(255))
    隶属关系 = db.Column(db.Unicode(255))
    运营状态 = db.Column(db.Unicode(255))
    执行会计制度类别 = db.Column(db.Unicode(255))
    执行企业会计准则情况 = db.Column(db.Unicode(255))
    机构类型 = db.Column(db.Unicode(255))
    产业活动单位数_总计_ = db.Column('产业活动单位数(总计)', db.Unicode(255))
    企业集团情况 = db.Column(db.Unicode(255))



t_201907_month = db.Table(
    '201907_month',
    db.Column('组织机构代码', db.Unicode(255)),
    db.Column('数据处理地', db.Unicode(255)),
    db.Column('单位详细名称', db.Unicode(255)),
    db.Column('期别(年)', db.Unicode(255)),
    db.Column('期别(月)', db.Unicode(255)),
    db.Column('统一社会信用代码', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)1', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)2', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)3', db.Unicode(255)),
    db.Column('行业代码(GB/T4754-2017)', db.Unicode(255)),
    db.Column('报表类别', db.Unicode(255)),
    db.Column('行政区划代码', db.Unicode(255)),
    db.Column('单位注册地址所在行政区划代码', db.Unicode(255)),
    db.Column('单位规模', db.Unicode(255)),
    db.Column('从业人员期末人数;人', db.Float(53)),
    db.Column('女性;人', db.Float(53)),
    db.Column('营业收入;千元', db.Float(53)),
    db.Column('营业税金及附加;千元', db.Float(53)),
    db.Column('主营业务收入;千元', db.Float(53)),
    db.Column('资产;千元', db.Float(53)),
    db.Column('开业(成立)时间(年)', db.Unicode(255)),
    db.Column('开业(成立)时间(月)', db.Unicode(255)),
    db.Column('登记注册类型', db.Unicode(255)),
    db.Column('是否港商投资', db.Unicode(255)),
    db.Column('是否港商投资1', db.Unicode(255)),
    db.Column('企业控股情况', db.Unicode(255)),
    db.Column('隶属关系', db.Unicode(255)),
    db.Column('运营状态', db.Unicode(255)),
    db.Column('执行会计制度类别', db.Unicode(255)),
    db.Column('执行企业会计准则情况', db.Unicode(255)),
    db.Column('机构类型', db.Unicode(255)),
    db.Column('产业活动单位数(总计)', db.Unicode(255)),
    db.Column('企业集团情况', db.Unicode(255))
)



t_201908_month = db.Table(
    '201908_month',
    db.Column('组织机构代码', db.Unicode(255)),
    db.Column('数据处理地', db.Unicode(255)),
    db.Column('单位详细名称', db.Unicode(255)),
    db.Column('期别(年)', db.Unicode(255)),
    db.Column('期别(月)', db.Unicode(255)),
    db.Column('统一社会信用代码', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)1', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)2', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)3', db.Unicode(255)),
    db.Column('行业代码(GB/T4754-2017)', db.Unicode(255)),
    db.Column('报表类别', db.Unicode(255)),
    db.Column('行政区划代码', db.Unicode(255)),
    db.Column('单位注册地址所在行政区划代码', db.Unicode(255)),
    db.Column('单位规模', db.Unicode(255)),
    db.Column('从业人员期末人数;人', db.Float(53)),
    db.Column('女性;人', db.Float(53)),
    db.Column('营业收入;千元', db.Float(53)),
    db.Column('营业税金及附加;千元', db.Float(53)),
    db.Column('主营业务收入;千元', db.Float(53)),
    db.Column('资产;千元', db.Float(53)),
    db.Column('开业(成立)时间(年)', db.Unicode(255)),
    db.Column('开业(成立)时间(月)', db.Unicode(255)),
    db.Column('登记注册类型', db.Unicode(255)),
    db.Column('是否港商投资', db.Unicode(255)),
    db.Column('是否港商投资1', db.Unicode(255)),
    db.Column('企业控股情况', db.Unicode(255)),
    db.Column('隶属关系', db.Unicode(255)),
    db.Column('运营状态', db.Unicode(255)),
    db.Column('执行会计制度类别', db.Unicode(255)),
    db.Column('执行企业会计准则情况', db.Unicode(255)),
    db.Column('机构类型', db.Unicode(255)),
    db.Column('产业活动单位数(总计)', db.Float(53)),
    db.Column('企业集团情况', db.Unicode(255))
)



t_201909_month = db.Table(
    '201909_month',
    db.Column('组织机构代码', db.Unicode(255)),
    db.Column('数据处理地', db.Unicode(255)),
    db.Column('单位详细名称', db.Unicode(255)),
    db.Column('期别(年)', db.Unicode(255)),
    db.Column('期别(月)', db.Unicode(255)),
    db.Column('统一社会信用代码', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)1', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)2', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)3', db.Unicode(255)),
    db.Column('行业代码(GB/T4754-2017)', db.Unicode(255)),
    db.Column('报表类别', db.Unicode(255)),
    db.Column('行政区划代码', db.Unicode(255)),
    db.Column('单位注册地址所在行政区划代码', db.Unicode(255)),
    db.Column('单位规模', db.Unicode(255)),
    db.Column('从业人员期末人数;人', db.Float(53)),
    db.Column('女性;人', db.Float(53)),
    db.Column('营业收入;千元', db.Float(53)),
    db.Column('营业税金及附加;千元', db.Float(53)),
    db.Column('主营业务收入;千元', db.Float(53)),
    db.Column('资产;千元', db.Float(53)),
    db.Column('开业(成立)时间(年)', db.Unicode(255)),
    db.Column('开业(成立)时间(月)', db.Unicode(255)),
    db.Column('登记注册类型', db.Unicode(255)),
    db.Column('是否港商投资', db.Unicode(255)),
    db.Column('是否港商投资1', db.Unicode(255)),
    db.Column('企业控股情况', db.Unicode(255)),
    db.Column('隶属关系', db.Unicode(255)),
    db.Column('运营状态', db.Unicode(255)),
    db.Column('执行会计制度类别', db.Unicode(255)),
    db.Column('执行企业会计准则情况', db.Unicode(255)),
    db.Column('机构类型', db.Unicode(255)),
    db.Column('产业活动单位数(总计)', db.Float(53)),
    db.Column('企业集团情况', db.Unicode(255))
)



t_201910_month = db.Table(
    '201910_month',
    db.Column('组织机构代码', db.Unicode(255)),
    db.Column('数据处理地', db.Unicode(255)),
    db.Column('单位详细名称', db.Unicode(255)),
    db.Column('期别(年)', db.Unicode(255)),
    db.Column('期别(月)', db.Unicode(255)),
    db.Column('统一社会信用代码', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)1', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)2', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)3', db.Unicode(255)),
    db.Column('行业代码(GB/T4754-2017)', db.Unicode(255)),
    db.Column('报表类别', db.Unicode(255)),
    db.Column('行政区划代码', db.Unicode(255)),
    db.Column('单位注册地址所在行政区划代码', db.Unicode(255)),
    db.Column('单位规模', db.Unicode(255)),
    db.Column('从业人员期末人数;人', db.Float(53)),
    db.Column('女性;人', db.Float(53)),
    db.Column('营业收入;千元', db.Float(53)),
    db.Column('营业税金及附加;千元', db.Float(53)),
    db.Column('主营业务收入;千元', db.Float(53)),
    db.Column('资产;千元', db.Float(53)),
    db.Column('开业(成立)时间(年)', db.Unicode(255)),
    db.Column('开业(成立)时间(月)', db.Unicode(255)),
    db.Column('登记注册类型', db.Unicode(255)),
    db.Column('是否港商投资', db.Unicode(255)),
    db.Column('是否港商投资1', db.Unicode(255)),
    db.Column('企业控股情况', db.Unicode(255)),
    db.Column('隶属关系', db.Unicode(255)),
    db.Column('运营状态', db.Unicode(255)),
    db.Column('执行会计制度类别', db.Unicode(255)),
    db.Column('执行企业会计准则情况', db.Unicode(255)),
    db.Column('机构类型', db.Unicode(255)),
    db.Column('产业活动单位数(总计)', db.Float(53)),
    db.Column('企业集团情况', db.Unicode(255))
)



t_201911_month = db.Table(
    '201911_month',
    db.Column('组织机构代码', db.Unicode(255)),
    db.Column('数据处理地', db.Unicode(255)),
    db.Column('单位详细名称', db.Unicode(255)),
    db.Column('期别(年)', db.Unicode(255)),
    db.Column('期别(月)', db.Unicode(255)),
    db.Column('统一社会信用代码', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)1', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)2', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)3', db.Unicode(255)),
    db.Column('行业代码(GB/T4754-2017)', db.Unicode(255)),
    db.Column('报表类别', db.Unicode(255)),
    db.Column('行政区划代码', db.Unicode(255)),
    db.Column('单位注册地址所在行政区划代码', db.Unicode(255)),
    db.Column('单位规模', db.Unicode(255)),
    db.Column('从业人员期末人数;人', db.Float(53)),
    db.Column('女性;人', db.Float(53)),
    db.Column('营业收入;千元', db.Float(53)),
    db.Column('营业税金及附加;千元', db.Float(53)),
    db.Column('主营业务收入;千元', db.Float(53)),
    db.Column('资产;千元', db.Float(53)),
    db.Column('开业(成立)时间(年)', db.Unicode(255)),
    db.Column('开业(成立)时间(月)', db.Unicode(255)),
    db.Column('登记注册类型', db.Unicode(255)),
    db.Column('是否港商投资', db.Unicode(255)),
    db.Column('是否港商投资1', db.Unicode(255)),
    db.Column('企业控股情况', db.Unicode(255)),
    db.Column('隶属关系', db.Unicode(255)),
    db.Column('运营状态', db.Unicode(255)),
    db.Column('执行会计制度类别', db.Unicode(255)),
    db.Column('执行企业会计准则情况', db.Unicode(255)),
    db.Column('机构类型', db.Unicode(255)),
    db.Column('产业活动单位数(总计)', db.Float(53)),
    db.Column('企业集团情况', db.Unicode(255))
)



t_201912_month = db.Table(
    '201912_month',
    db.Column('组织机构代码', db.Unicode(255)),
    db.Column('数据处理地', db.Unicode(255)),
    db.Column('单位详细名称', db.Unicode(255)),
    db.Column('期别(年)', db.Unicode(255)),
    db.Column('期别(月)', db.Unicode(255)),
    db.Column('统一社会信用代码', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)1', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)2', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)3', db.Unicode(255)),
    db.Column('行业代码(GB/T4754-2017)', db.Unicode(255)),
    db.Column('报表类别', db.Unicode(255)),
    db.Column('行政区划代码', db.Unicode(255)),
    db.Column('单位注册地址所在行政区划代码', db.Unicode(255)),
    db.Column('单位规模', db.Unicode(255)),
    db.Column('从业人员期末人数;人', db.Float(53)),
    db.Column('女性;人', db.Float(53)),
    db.Column('营业收入;千元', db.Float(53)),
    db.Column('营业税金及附加;千元', db.Float(53)),
    db.Column('主营业务收入;千元', db.Float(53)),
    db.Column('资产;千元', db.Float(53)),
    db.Column('开业(成立)时间(年)', db.Unicode(255)),
    db.Column('开业(成立)时间(月)', db.Unicode(255)),
    db.Column('登记注册类型', db.Unicode(255)),
    db.Column('是否港商投资', db.Unicode(255)),
    db.Column('是否港商投资1', db.Unicode(255)),
    db.Column('企业控股情况', db.Unicode(255)),
    db.Column('隶属关系', db.Unicode(255)),
    db.Column('运营状态', db.Unicode(255)),
    db.Column('执行会计制度类别', db.Unicode(255)),
    db.Column('执行企业会计准则情况', db.Unicode(255)),
    db.Column('机构类型', db.Unicode(255)),
    db.Column('产业活动单位数(总计)', db.Float(53)),
    db.Column('企业集团情况', db.Unicode(255))
)



t_202002_month = db.Table(
    '202002_month',
    db.Column('组织机构代码', db.Unicode(255)),
    db.Column('数据处理地', db.Unicode(255)),
    db.Column('单位详细名称', db.Unicode(255)),
    db.Column('期别(年)', db.Unicode(255)),
    db.Column('期别(月)', db.Unicode(255)),
    db.Column('统一社会信用代码', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)1', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)2', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)3', db.Unicode(255)),
    db.Column('行业代码(GB/T4754-2017)', db.Unicode(255)),
    db.Column('报表类别', db.Unicode(255)),
    db.Column('行政区划代码', db.Unicode(255)),
    db.Column('单位注册地址所在行政区划代码', db.Unicode(255)),
    db.Column('单位规模', db.Unicode(255)),
    db.Column('从业人员期末人数;人', db.Float(53)),
    db.Column('女性;人', db.Float(53)),
    db.Column('营业收入;千元', db.Float(53)),
    db.Column('税金及附加;千元', db.Float(53)),
    db.Column('主营业务收入;千元', db.Float(53)),
    db.Column('资产;千元', db.Float(53)),
    db.Column('开业时间(年)', db.Unicode(255)),
    db.Column('开业时间(月)', db.Unicode(255)),
    db.Column('成立时间(年)', db.Unicode(255)),
    db.Column('成立时间(月)', db.Unicode(255)),
    db.Column('登记注册类型', db.Unicode(255)),
    db.Column('是否港商投资', db.Unicode(255)),
    db.Column('是否澳商投资', db.Unicode(255)),
    db.Column('是否台商投资', db.Unicode(255)),
    db.Column('企业控股情况', db.Unicode(255)),
    db.Column('隶属关系', db.Unicode(255)),
    db.Column('运营状态', db.Unicode(255)),
    db.Column('执行会计制度类别', db.Unicode(255)),
    db.Column('执行企业会计准则情况', db.Unicode(255)),
    db.Column('机构类型', db.Unicode(255)),
    db.Column('产业活动单位数(总计)', db.Float(53)),
    db.Column('企业集团情况', db.Unicode(255)),
    db.Column('是否为“视同法人单位”？如是，请勾选', db.Unicode(255))
)



t_202003_month = db.Table(
    '202003_month',
    db.Column('组织机构代码', db.Unicode(255)),
    db.Column('数据处理地', db.Unicode(255)),
    db.Column('单位详细名称', db.Unicode(255)),
    db.Column('期别(年)', db.Unicode(255)),
    db.Column('期别(月)', db.Unicode(255)),
    db.Column('统一社会信用代码', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)1', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)2', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)3', db.Unicode(255)),
    db.Column('行业代码(GB/T4754-2017)', db.Unicode(255)),
    db.Column('报表类别', db.Unicode(255)),
    db.Column('行政区划代码', db.Unicode(255)),
    db.Column('单位注册地址所在行政区划代码', db.Unicode(255)),
    db.Column('单位规模', db.Unicode(255)),
    db.Column('从业人员期末人数;人', db.Float(53)),
    db.Column('女性;人', db.Float(53)),
    db.Column('营业收入;千元', db.Float(53)),
    db.Column('税金及附加;千元', db.Float(53)),
    db.Column('主营业务收入;千元', db.Float(53)),
    db.Column('资产;千元', db.Float(53)),
    db.Column('开业时间(年)', db.Unicode(255)),
    db.Column('开业时间(月)', db.Unicode(255)),
    db.Column('成立时间(年)', db.Unicode(255)),
    db.Column('成立时间(月)', db.Unicode(255)),
    db.Column('登记注册类型', db.Unicode(255)),
    db.Column('是否港商投资', db.Unicode(255)),
    db.Column('是否澳商投资', db.Unicode(255)),
    db.Column('是否台商投资', db.Unicode(255)),
    db.Column('企业控股情况', db.Unicode(255)),
    db.Column('隶属关系', db.Unicode(255)),
    db.Column('运营状态', db.Unicode(255)),
    db.Column('执行会计制度类别', db.Unicode(255)),
    db.Column('执行企业会计准则情况', db.Unicode(255)),
    db.Column('机构类型', db.Unicode(255)),
    db.Column('产业活动单位数(总计)', db.Float(53)),
    db.Column('企业集团情况', db.Unicode(255)),
    db.Column('是否为“视同法人单位”？如是，请勾选', db.Unicode(255))
)



t_202004_month = db.Table(
    '202004_month',
    db.Column('组织机构代码', db.Unicode(255)),
    db.Column('数据处理地', db.Unicode(255)),
    db.Column('单位详细名称', db.Unicode(255)),
    db.Column('期别(年)', db.Unicode(255)),
    db.Column('期别(月)', db.Unicode(255)),
    db.Column('统一社会信用代码', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)1', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)2', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)3', db.Unicode(255)),
    db.Column('行业代码(GB/T4754-2017)', db.Unicode(255)),
    db.Column('报表类别', db.Unicode(255)),
    db.Column('行政区划代码', db.Unicode(255)),
    db.Column('单位注册地址所在行政区划代码', db.Unicode(255)),
    db.Column('单位规模', db.Unicode(255)),
    db.Column('从业人员期末人数;人', db.Float(53)),
    db.Column('女性;人', db.Float(53)),
    db.Column('营业收入;千元', db.Float(53)),
    db.Column('税金及附加;千元', db.Float(53)),
    db.Column('主营业务收入;千元', db.Float(53)),
    db.Column('资产;千元', db.Float(53)),
    db.Column('开业时间(年)', db.Unicode(255)),
    db.Column('开业时间(月)', db.Unicode(255)),
    db.Column('成立时间(年)', db.Unicode(255)),
    db.Column('成立时间(月)', db.Unicode(255)),
    db.Column('登记注册类型', db.Unicode(255)),
    db.Column('是否港商投资', db.Unicode(255)),
    db.Column('是否澳商投资', db.Unicode(255)),
    db.Column('是否台商投资', db.Unicode(255)),
    db.Column('企业控股情况', db.Unicode(255)),
    db.Column('隶属关系', db.Unicode(255)),
    db.Column('运营状态', db.Unicode(255)),
    db.Column('执行会计制度类别', db.Unicode(255)),
    db.Column('执行企业会计准则情况', db.Unicode(255)),
    db.Column('机构类型', db.Unicode(255)),
    db.Column('产业活动单位数(总计)', db.Float(53)),
    db.Column('企业集团情况', db.Unicode(255)),
    db.Column('是否为“视同法人单位”？如是，请勾选', db.Unicode(255))
)



t_202005_month = db.Table(
    '202005_month',
    db.Column('组织机构代码', db.Unicode(255)),
    db.Column('数据处理地', db.Unicode(255)),
    db.Column('单位详细名称', db.Unicode(255)),
    db.Column('期别(年)', db.Unicode(255)),
    db.Column('期别(月)', db.Unicode(255)),
    db.Column('统一社会信用代码', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)1', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)2', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)3', db.Unicode(255)),
    db.Column('行业代码(GB/T4754-2017)', db.Unicode(255)),
    db.Column('报表类别', db.Unicode(255)),
    db.Column('行政区划代码', db.Unicode(255)),
    db.Column('单位注册地址所在行政区划代码', db.Unicode(255)),
    db.Column('单位规模', db.Unicode(255)),
    db.Column('从业人员期末人数;人', db.Float(53)),
    db.Column('女性;人', db.Float(53)),
    db.Column('营业收入;千元', db.Float(53)),
    db.Column('税金及附加;千元', db.Float(53)),
    db.Column('主营业务收入;千元', db.Float(53)),
    db.Column('资产;千元', db.Float(53)),
    db.Column('开业时间(年)', db.Unicode(255)),
    db.Column('开业时间(月)', db.Unicode(255)),
    db.Column('成立时间(年)', db.Unicode(255)),
    db.Column('成立时间(月)', db.Unicode(255)),
    db.Column('登记注册类型', db.Unicode(255)),
    db.Column('是否港商投资', db.Unicode(255)),
    db.Column('是否澳商投资', db.Unicode(255)),
    db.Column('是否台商投资', db.Unicode(255)),
    db.Column('企业控股情况', db.Unicode(255)),
    db.Column('隶属关系', db.Unicode(255)),
    db.Column('运营状态', db.Unicode(255)),
    db.Column('执行会计制度类别', db.Unicode(255)),
    db.Column('执行企业会计准则情况', db.Unicode(255)),
    db.Column('机构类型', db.Unicode(255)),
    db.Column('产业活动单位数(总计)', db.Float(53)),
    db.Column('企业集团情况', db.Unicode(255)),
    db.Column('是否为“视同法人单位”？如是，请勾选', db.Unicode(255))
)



t_202006_month = db.Table(
    '202006_month',
    db.Column('组织机构代码', db.Unicode(255)),
    db.Column('数据处理地', db.Unicode(255)),
    db.Column('单位详细名称', db.Unicode(255)),
    db.Column('期别(年)', db.Unicode(255)),
    db.Column('期别(月)', db.Unicode(255)),
    db.Column('统一社会信用代码', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)1', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)2', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)3', db.Unicode(255)),
    db.Column('行业代码(GB/T4754-2017)', db.Unicode(255)),
    db.Column('报表类别', db.Unicode(255)),
    db.Column('行政区划代码', db.Unicode(255)),
    db.Column('单位注册地址所在行政区划代码', db.Unicode(255)),
    db.Column('单位规模', db.Unicode(255)),
    db.Column('从业人员期末人数;人', db.Float(53)),
    db.Column('女性;人', db.Float(53)),
    db.Column('营业收入;千元', db.Float(53)),
    db.Column('税金及附加;千元', db.Float(53)),
    db.Column('主营业务收入;千元', db.Float(53)),
    db.Column('资产;千元', db.Float(53)),
    db.Column('开业时间(年)', db.Unicode(255)),
    db.Column('开业时间(月)', db.Unicode(255)),
    db.Column('成立时间(年)', db.Unicode(255)),
    db.Column('成立时间(月)', db.Unicode(255)),
    db.Column('登记注册类型', db.Unicode(255)),
    db.Column('是否港商投资', db.Unicode(255)),
    db.Column('是否澳商投资', db.Unicode(255)),
    db.Column('是否台商投资', db.Unicode(255)),
    db.Column('企业控股情况', db.Unicode(255)),
    db.Column('隶属关系', db.Unicode(255)),
    db.Column('运营状态', db.Unicode(255)),
    db.Column('执行会计制度类别', db.Unicode(255)),
    db.Column('执行企业会计准则情况', db.Unicode(255)),
    db.Column('机构类型', db.Unicode(255)),
    db.Column('产业活动单位数(总计)', db.Float(53)),
    db.Column('企业集团情况', db.Unicode(255)),
    db.Column('是否为“视同法人单位”？如是，请勾选', db.Unicode(255))
)



t_202007_month = db.Table(
    '202007_month',
    db.Column('组织机构代码', db.Unicode(255)),
    db.Column('数据处理地', db.Unicode(255)),
    db.Column('单位详细名称', db.Unicode(255)),
    db.Column('期别(年)', db.Unicode(255)),
    db.Column('期别(月)', db.Unicode(255)),
    db.Column('统一社会信用代码', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)1', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)2', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)3', db.Unicode(255)),
    db.Column('行业代码(GB/T4754-2017)', db.Unicode(255)),
    db.Column('报表类别', db.Unicode(255)),
    db.Column('行政区划代码', db.Unicode(255)),
    db.Column('单位注册地址所在行政区划代码', db.Unicode(255)),
    db.Column('单位规模', db.Unicode(255)),
    db.Column('从业人员期末人数;人', db.Float(53)),
    db.Column('女性;人', db.Float(53)),
    db.Column('营业收入;千元', db.Float(53)),
    db.Column('税金及附加;千元', db.Float(53)),
    db.Column('主营业务收入;千元', db.Float(53)),
    db.Column('资产;千元', db.Float(53)),
    db.Column('开业时间(年)', db.Unicode(255)),
    db.Column('开业时间(月)', db.Unicode(255)),
    db.Column('成立时间(年)', db.Unicode(255)),
    db.Column('成立时间(月)', db.Unicode(255)),
    db.Column('登记注册类型', db.Unicode(255)),
    db.Column('是否港商投资', db.Unicode(255)),
    db.Column('是否澳商投资', db.Unicode(255)),
    db.Column('是否台商投资', db.Unicode(255)),
    db.Column('企业控股情况', db.Unicode(255)),
    db.Column('隶属关系', db.Unicode(255)),
    db.Column('运营状态', db.Unicode(255)),
    db.Column('执行会计制度类别', db.Unicode(255)),
    db.Column('执行企业会计准则情况', db.Unicode(255)),
    db.Column('机构类型', db.Unicode(255)),
    db.Column('产业活动单位数(总计)', db.Float(53)),
    db.Column('企业集团情况', db.Unicode(255)),
    db.Column('是否为“视同法人单位”？如是，请勾选', db.Unicode(255))
)



t_202008_month = db.Table(
    '202008_month',
    db.Column('组织机构代码', db.Unicode(255)),
    db.Column('数据处理地', db.Unicode(255)),
    db.Column('单位详细名称', db.Unicode(255)),
    db.Column('期别(年)', db.Unicode(255)),
    db.Column('期别(月)', db.Unicode(255)),
    db.Column('统一社会信用代码', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)1', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)2', db.Unicode(255)),
    db.Column('主要业务活动(或主要产品)3', db.Unicode(255)),
    db.Column('行业代码(GB/T4754-2017)', db.Unicode(255)),
    db.Column('报表类别', db.Unicode(255)),
    db.Column('行政区划代码', db.Unicode(255)),
    db.Column('单位注册地址所在行政区划代码', db.Unicode(255)),
    db.Column('单位规模', db.Unicode(255)),
    db.Column('从业人员期末人数;人', db.Float(53)),
    db.Column('女性;人', db.Float(53)),
    db.Column('营业收入;千元', db.Float(53)),
    db.Column('税金及附加;千元', db.Float(53)),
    db.Column('主营业务收入;千元', db.Float(53)),
    db.Column('资产;千元', db.Float(53)),
    db.Column('开业时间(年)', db.Unicode(255)),
    db.Column('开业时间(月)', db.Unicode(255)),
    db.Column('成立时间(年)', db.Unicode(255)),
    db.Column('成立时间(月)', db.Unicode(255)),
    db.Column('登记注册类型', db.Unicode(255)),
    db.Column('是否港商投资', db.Unicode(255)),
    db.Column('是否澳商投资', db.Unicode(255)),
    db.Column('是否台商投资', db.Unicode(255)),
    db.Column('企业控股情况', db.Unicode(255)),
    db.Column('隶属关系', db.Unicode(255)),
    db.Column('运营状态', db.Unicode(255)),
    db.Column('执行会计制度类别', db.Unicode(255)),
    db.Column('执行企业会计准则情况', db.Unicode(255)),
    db.Column('机构类型', db.Unicode(255)),
    db.Column('产业活动单位数(总计)', db.Float(53)),
    db.Column('企业集团情况', db.Unicode(255)),
    db.Column('是否为“视同法人单位”？如是，请勾选', db.Unicode(255))
)
