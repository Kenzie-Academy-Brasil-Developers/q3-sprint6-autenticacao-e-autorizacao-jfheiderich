from app.controllers import user_controller
from flask import Blueprint

bp_home = Blueprint('home', __name__)

bp_home.get('')(user_controller.get_home)

bp_home.put('')(user_controller.put_home)

bp_home.delete('')(user_controller.delete_user)
