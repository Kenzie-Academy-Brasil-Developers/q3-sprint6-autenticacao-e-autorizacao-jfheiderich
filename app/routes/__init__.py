from app.routes.user_route import bp_users
from flask import Blueprint, Flask

bp_api = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    bp_api.register_blueprint(bp_users)

    app.register_blueprint(bp_api)
