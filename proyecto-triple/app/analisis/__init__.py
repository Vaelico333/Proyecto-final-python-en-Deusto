from flask import Blueprint

analisis_bp = Blueprint('analisis', __name__, template_folder='templates')

from . import routes, services