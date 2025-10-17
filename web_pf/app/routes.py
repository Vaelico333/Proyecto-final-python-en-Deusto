from flask import render_template, flash, redirect, url_for, request
from urllib.parse import urlsplit
from app import app, db
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Nombre o contraseña incorrectos')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Acceder', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))