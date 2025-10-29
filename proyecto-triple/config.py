import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-secretísima'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data', 'app.db')
    DATA_PATH = os.path.join(basedir, 'data', 'covid.csv')
    ANALYSIS_STORE = os.path.join(basedir, 'data', 'analysis_store.txt')
    LOGIN_MESSAGE = "Por favor, identifícate para continuar."
