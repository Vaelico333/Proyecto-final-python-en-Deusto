from flask import render_template
from app import app, db

@app.route('/')
@app.route('/inicio', endpoint='inicio')
def index():
    return render_template('inicio.html', title='Proyecto final - Inicio')

