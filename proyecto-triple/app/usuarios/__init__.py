from flask import Blueprint

usuarios_bp = Blueprint('usuarios', __name__, template_folder='templates')

from . import routes,  forms, auth
from .. import models