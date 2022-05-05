from app.controllers import user_controller
from flask import Blueprint

bp_signin = Blueprint('signin', __name__, url_prefix='/signin')

bp_signin.post('')(user_controller.signin)
