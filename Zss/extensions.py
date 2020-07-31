"""
除了路由之外的扩展都在本文件内设置，因为路由一般是最后一步，并且路由是对外暴露的，如果路由放在这里可能出现问题
"""

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate=Migrate()


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app,db)