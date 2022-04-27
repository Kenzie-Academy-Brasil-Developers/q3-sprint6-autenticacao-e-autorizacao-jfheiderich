from app.controllers import user_controller
from flask import Blueprint

bp_users = Blueprint("signup", __name__, url_prefix="/signup")

bp_users.post("")(user_controller.create_user)

bp_users.get("")(user_controller.get_user)
