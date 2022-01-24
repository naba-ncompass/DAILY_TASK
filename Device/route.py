from flask import Blueprint
from Device.controller import *

device_bp = Blueprint('device_bp',__name__)

device_bp.route("/getPeakConsumption",methods=['GET']) (get_peak_consumption_between_times)
device_bp.route("/getSumConsumption",methods=['GET']) (get_sum_consumption_between_times)
device_bp.route("/getDuplicateTime",methods=['GET']) (get_duplicate_time_between_times)