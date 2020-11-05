# coding: utf-8
from sqlalchemy import Column, Integer, String, Table, Unicode
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class 2017Year1(db.Model):
    __tablename__ = '2017_year_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    审核类型 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    年主营业务收入 = db.Column(db.Unicode(255))
    次年定报调查单位 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    填表处理地代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))



class 2017Year2(db.Model):
    __tablename__ = '2017_year_2'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    填表处理地代码 = db.Column(db.Unicode(255))
    审核类型 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    实际单位类型 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))
    备注 = db.Column(db.Unicode(255))



class 201803Month1(db.Model):
    __tablename__ = '201803_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 201804Month1(db.Model):
    __tablename__ = '201804_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 201805Month1(db.Model):
    __tablename__ = '201805_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 201806Month1(db.Model):
    __tablename__ = '201806_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 201807Month1(db.Model):
    __tablename__ = '201807_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 201808Month1(db.Model):
    __tablename__ = '201808_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 201809Month1(db.Model):
    __tablename__ = '201809_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 201810Month1(db.Model):
    __tablename__ = '201810_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 201811Month1(db.Model):
    __tablename__ = '201811_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 2018Year1(db.Model):
    __tablename__ = '2018_year_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    审核类型 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    年主营业务收入 = db.Column(db.Unicode(255))
    次年定报调查单位 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    填表处理地代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    id = db.Column(db.Integer, nullable=False)



class 2018Year2(db.Model):
    __tablename__ = '2018_year_2'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    填表处理地代码 = db.Column(db.Unicode(255))
    审核类型 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    实际单位类型 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))
    备注 = db.Column(db.Unicode(255))



t_2018年新增单位集合 = db.Table(
    '2018年新增单位集合',
    db.Column('期别', db.Unicode(255)),
    db.Column('单位类型', db.Unicode(255)),
    db.Column('所属专业', db.Unicode(255)),
    db.Column('审批类型', db.Unicode(255)),
    db.Column('组织机构代码', db.Unicode(255)),
    db.Column('详细名称', db.Unicode(255)),
    db.Column('所在地区划代码', db.Unicode(255)),
    db.Column('注册地区划代码', db.Unicode(255)),
    db.Column('行业代码_17', db.Unicode(255)),
    db.Column('主要业务活动', db.Unicode(255)),
    db.Column('填表信息', db.Unicode(255)),
    db.Column('统计局代码', db.Unicode(255))
)



class 201902Month1(db.Model):
    __tablename__ = '201902_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 201903Month1(db.Model):
    __tablename__ = '201903_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 201904Month1(db.Model):
    __tablename__ = '201904_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 201905Month1(db.Model):
    __tablename__ = '201905_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 201906Month1(db.Model):
    __tablename__ = '201906_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 201907Month1(db.Model):
    __tablename__ = '201907_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 201908Month1(db.Model):
    __tablename__ = '201908_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 201909Month1(db.Model):
    __tablename__ = '201909_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 201910Month1(db.Model):
    __tablename__ = '201910_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 201911Month1(db.Model):
    __tablename__ = '201911_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 201912Month1(db.Model):
    __tablename__ = '201912_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 2019Year1(db.Model):
    __tablename__ = '2019_year_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    审核类型 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    年主营业务收入 = db.Column(db.Unicode(255))
    次年定报调查单位 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    填表处理地代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    id = db.Column(db.Integer, nullable=False)



class 2019Year2(db.Model):
    __tablename__ = '2019_year_2'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    填表处理地代码 = db.Column(db.Unicode(255))
    审核类型 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    实际单位类型 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))
    备注 = db.Column(db.Unicode(255))



t_2019年新增单位集合 = db.Table(
    '2019年新增单位集合',
    db.Column('期别', db.Unicode(255)),
    db.Column('单位类型', db.Unicode(255)),
    db.Column('所属专业', db.Unicode(255)),
    db.Column('审批类型', db.Unicode(255)),
    db.Column('组织机构代码', db.Unicode(255)),
    db.Column('详细名称', db.Unicode(255)),
    db.Column('所在地区划代码', db.Unicode(255)),
    db.Column('注册地区划代码', db.Unicode(255)),
    db.Column('行业代码_17', db.Unicode(255)),
    db.Column('主要业务活动', db.Unicode(255)),
    db.Column('填表信息', db.Unicode(255)),
    db.Column('统计局代码', db.Unicode(255))
)



class 202002Month1(db.Model):
    __tablename__ = '202002_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 202003Month1(db.Model):
    __tablename__ = '202003_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 202004Month1(db.Model):
    __tablename__ = '202004_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.String(10, 'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True, nullable=False)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 202005Month1(db.Model):
    __tablename__ = '202005_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.String(10, 'Chinese_PRC_CI_AS'), primary_key=True, nullable=False)
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True, nullable=False)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 202006Month1(db.Model):
    __tablename__ = '202006_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 202007Month1(db.Model):
    __tablename__ = '202007_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))



class 202008Month1(db.Model):
    __tablename__ = '202008_month_1'

    期别 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    详细名称_变更前 = db.Column(db.Unicode(255))
    详细名称_变更后 = db.Column(db.Unicode(255))
    所在地区划代码 = db.Column(db.Unicode(255))
    注册地区划代码 = db.Column(db.Unicode(255))
    行业代码_17 = db.Column(db.Unicode(255))
    主要业务活动 = db.Column(db.Unicode(255))
    填表信息 = db.Column(db.Unicode(255))
    统计局代码 = db.Column(db.Unicode(255))
    专业审批_县_状态 = db.Column(db.Unicode(255))
    名录审批_县_状态 = db.Column(db.Unicode(255))
    领导审批_县_状态 = db.Column(db.Unicode(255))
    名录初审_市_状态 = db.Column(db.Unicode(255))
    专业审批_市_状态 = db.Column(db.Unicode(255))
    名录终审_市_状态 = db.Column(db.Unicode(255))
    名录初审_省_状态 = db.Column(db.Unicode(255))
    专业审批_省_状态 = db.Column(db.Unicode(255))
    名录终审_省_状态 = db.Column(db.Unicode(255))
    专业审批_国家_状态 = db.Column(db.Unicode(255))
    名录终审_国家_状态 = db.Column(db.Unicode(255))