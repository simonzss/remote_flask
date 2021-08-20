import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE") or "sqlite"
    driver = dbinfo.get("DRIVER") or "sqlite"
    user = dbinfo.get("USER") or ""
    password = dbinfo.get("PASSWORD") or ""
    host = dbinfo.get("HOST") or ""
    port = dbinfo.get("PORT") or ""
    dbname = dbinfo.get("DBNAME") or "sqlite.db"
    odbcname = dbinfo.get("ODBCNAME") or ""

    return "{}+{}://{}:{}@{}:{}/{}?driver={}".format(engine, driver, user, password, host, port, dbname, odbcname)
    # mssql+pyodbc://sa:zss11111111@localhost:58651/测试数据库?driver=ODBC+Driver+13+for+SQL+Server


class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "darkness"
    FLASK_ENV = "production"



class DevelopConfig(Config):
    dbinfo = {
        "ENGINE": "mssql",
        "DRIVER": "pyodbc",
        "USER": "sa",
        "PASSWORD": "zss11111111",
        "HOST": "localhost",
        "PORT": "58651",
        "DBNAME": "审批平台数据库",
        "ODBCNAME": "ODBC+Driver+13+for+SQL+Server"
    }

    bindinfo = {
        "ENGINE": "mssql",
        "DRIVER": "pyodbc",
        "USER": "sa",
        "PASSWORD": "zss11111111",
        "HOST": "localhost",
        "PORT": "58651",
        "DBNAME": "联网直报平台数据库",
        "ODBCNAME": "ODBC+Driver+13+for+SQL+Server"
    }

    bind_tk_info = {
        "ENGINE": "mssql",
        "DRIVER": "pyodbc",
        "USER": "sa",
        "PASSWORD": "zss11111111",
        "HOST": "localhost",
        "PORT": "58651",
        "DBNAME": "审批平台退出单位数据库",
        "ODBCNAME": "ODBC+Driver+13+for+SQL+Server"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)
    SQLALCHEMY_BINDS = {
        'zss': get_db_uri(bindinfo),
        'tk': get_db_uri(bind_tk_info)
    }
    # SQLALCHEMY_ECHO = True   #是否输出orm查询的sql原生语句


class TestConfig(Config):
    dbinfo = {
        "ENGINE": "",
        "DRIVER": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
        "DBNAME": "",
        "ODBCNAME": ""
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    "develop": DevelopConfig,
    "test": TestConfig,
}

# 数据库配置的格式：数据库+驱动://用户名:密码@主机:端口/具体哪一个数据库?具体驱动程序=
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db?driver=""'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
