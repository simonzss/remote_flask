
from flask import Flask

from Zss.extensions import init_ext
from Zss.settings import envs
from Zss.views import first_blueprint


def create_zss_app():
    # app = Flask(__name__,static_folder="../static/")
    app = Flask(__name__,static_folder="../Zss/static/bootstrap/")
    app.register_blueprint(first_blueprint)
    app.config.from_object(envs.get("develop"))

    @app.errorhandler(404)    #用errorhandler处理404错误
    def page_not_found(error):
        return '404错误：页面不存在', 404

    init_ext(app)    # 即init_extension，涉及用插件来初始化app的都在此函数内完成
    print(app.url_map)
    return app
