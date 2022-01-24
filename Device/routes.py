from flask import Blueprint
from .controller import *

d_bp = Blueprint('device', __name__)

d_bp.route("/sum", methods=['GET'])(get_sum_consumption)
d_bp.route("/peak", methods=['GET'])(get_peak_consumption)
d_bp.route("/duplicate", methods=['GET'])(get_duplicate_time)
