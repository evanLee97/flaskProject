from application import app
from web.controller.index import route_index

app.register_blueprint(route_index, url_prefix="/")
