from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'go_rhaibh_math_agat'
app.config.from_object(Config)
db.init_app(app)
acceso = LoginManager(app)
acceso.login_view = 'usuarios.login'

# Importar y registrar blueprints
from .agenda import agenda_bp as agenda_blueprint
from .usuarios import usuarios_bp as usuarios_blueprint
from .analisis import analisis_bp as analisis_blueprint

app.register_blueprint(agenda_blueprint)
app.register_blueprint(usuarios_blueprint)
app.register_blueprint(analisis_blueprint)

from app import routes, models