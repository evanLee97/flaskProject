from flask import Blueprint

route_env = Blueprint("env_page", __name__)


@route_env.route('/')
def index():
    return 'env index'


@route_env.route('/hello')
def hello():
    return 'env hello'
