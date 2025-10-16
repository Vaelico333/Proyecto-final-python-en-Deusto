from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Acceso solicitado para el usuario {}, recuérdame={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Acceder', form=form)