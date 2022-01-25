from flask import Blueprint
from .controller import *

s_bp = Blueprint('students',__name__)

s_bp.route('/create_user',methods=['POST'])(create_user)
s_bp.route('/show_users')(show_users)
s_bp.route('/login_user', methods=['POST'])(login_user)