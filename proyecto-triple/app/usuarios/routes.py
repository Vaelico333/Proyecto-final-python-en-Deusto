from flask import render_template, redirect, url_for, request, flash
from .forms import UserCreationForm, UserLoginForm
from ..models import User
from flask_login import login_user, logout_user, login_required, current_user
from . import usuarios_bp

@usuarios_bp.route('/usuarios')
@login_required
def index():
    users = User.query.all()
    return render_template('usuarios/tabla.html', users=users)

@usuarios_bp.route('/usuarios/crear', methods=['GET', 'POST'])
def create():
    form = UserCreationForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            name=form.name.data,
            surname=form.surname.data,
            password=form.password.data,
            phone=form.phone.data,
            age=form.age.data
        )
        user.save()
        flash('User created successfully!', 'success')
        return redirect(url_for('usuarios.index'))
    return render_template('usuarios/create.html', form=form)

@usuarios_bp.route('/usuarios/editar/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit(user_id):
    user = User.query.get_or_404(user_id)
    form = UserCreationForm(obj=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.name = form.name.data
        user.surname = form.surname.data
        user.password = form.password.data
        user.phone = form.phone.data
        user.age = form.age.data
        user.save()
        flash('User updated successfully!', 'success')
        return redirect(url_for('usuarios.index'))
    return render_template('usuarios/edit.html', form=form, user=user)

@usuarios_bp.route('/usuarios/borrar/<int:user_id>', methods=['GET', 'POST'])
@login_required
def delete(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.delete()
        flash('User deleted successfully!', 'success')
        return redirect(url_for('usuarios.index'))
    return render_template('usuarios/delete.html', user=user)

@usuarios_bp.route('/usuarios/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = (request.form.get('email') or '').strip()
        password = request.form.get('password') or ''
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Login exitoso.', 'success')
            return redirect(url_for('usuarios.index'))
        flash('Email o contraseña incorrectos.', 'danger')
    return render_template('usuarios/login.html')

@usuarios_bp.route('/usuarios/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('usuarios.login'))