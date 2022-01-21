from flask import Blueprint 
from .controller import *

bp = Blueprint('crud',__name__)

bp.route("/")(home)
bp.route("/read_shows", methods=['GET'])(read_from_db)
bp.route("/create_show",methods=['POST'])(insert_to_db)   
bp.route("/update_show",methods=['PUT'])(update_to_db)
bp.route("/delete_show", methods=['DELETE'])(delete_from_db)
