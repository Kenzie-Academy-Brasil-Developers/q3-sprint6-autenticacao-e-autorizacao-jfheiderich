from app.controllers import user_controller
from flask import Blueprint

bp_signup = Blueprint('signup', __name__, url_prefix='/signup')

bp_signup.post('')(user_controller.create_user)
