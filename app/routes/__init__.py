from app.routes.home import bp_home
from app.routes.signin import bp_signin
from app.routes.signup import bp_signup
from flask import Blueprint, Flask

bp_api = Blueprint('api', __name__, url_prefix='/api')


def init_app(app: Flask):
    bp_api.register_blueprint(bp_signup)
    bp_api.register_blueprint(bp_signin)
    bp_api.register_blueprint(bp_home)

    app.register_blueprint(bp_api)
