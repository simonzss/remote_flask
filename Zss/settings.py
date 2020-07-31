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


class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    dbinfo = {
        "ENGINE": "mssql",
        "DRIVER": "pyodbc",
        "USER": "sa",
        "PASSWORD": "zss11111111",
        "HOST": "localhost",
        "PORT": "58651",
        "DBNAME": "测试数据库",
        "ODBCNAME": "ODBC+Driver+13+for+SQL+Server"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


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
