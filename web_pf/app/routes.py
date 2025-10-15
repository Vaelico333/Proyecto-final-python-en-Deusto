from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Darío'}
    posts = [
        {
            'author': {'username':'Shirly'},
            'body': 'Hace un día fantástico en Valladolid'
        },
        {
            'author': {'username':'Madre'},
            'body': '¡A ver si me llamas más!'
        },
        {
            'author': {'username':'Aleix'},
            'body':'Espero tu reporte, hermano.'
        }
    ]
    return render_template('index.html', user=user, posts=posts)