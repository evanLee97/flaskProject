from flask import Flask, url_for

from common.libs.UrlManager import UrlManager
from envirment import route_env
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(route_env, url_prefix='/bl')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456Lyf@127.0.0.1:3306/autotest'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    # put application's code here
    url = url_for('index')
    url1 = UrlManager.buildUrl('/api')

    return 'Hello World!' + url + url1


@app.route('/api')
def index():
    return 'Index page'


@app.route('/api/hello')
def hello():
    from sqlalchemy import text
    sql = text("SELECT * FROM  `user`")
    # 踩坑 最新版的flask使用了已经弃用下面的写法
    # result = db.engine.execute(sql)
    with db.engine.connect() as conn:
        result = conn.execute(sql)
    for i in result:
        app.logger.warning('查询数据库：' + str(i))

    return 'hello page'


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return 'this page not found', 404


if __name__ == '__main__':
    app.run(debug=True)
