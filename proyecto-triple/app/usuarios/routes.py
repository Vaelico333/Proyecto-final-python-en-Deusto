from flask import render_template, redirect, url_for, request, flash
from .forms import UserCreationForm, UserLoginForm, UserEditForm, UserDeleteForm, PasswordCheckForm
from ..models import User
from flask_login import login_user, logout_user, login_required, current_user
from . import usuarios_bp
from app import db
import sqlalchemy as sa
from urllib.parse import urlsplit

@usuarios_bp.route('/usuarios')
@login_required
def index():
    users = User.query.all()
    return render_template('usuarios/tabla.html', users=users, title='Vista general')

@usuarios_bp.route('/usuarios/crear', methods=['GET', 'POST'])
def create():
    form = UserCreationForm()
    if form.validate_on_submit():
        if form.contraseña.data == form.contraseña2.data:
            user = User()
            #hash_contraseña = 
            user = User(
                email=form.email.data,
                nombre=form.nombre.data.title(),
                apellidos=form.apellidos.data.title(),
                telefono=form.telefono.data,
                edad=form.edad.data,
                #hash_contraseña=hash_contraseña
            )
            user.set_password(form.contraseña.data)
            db.session.add(user)
            db.session.commit()
            flash(f'¡Bienvenido/a, {form.nombre.data}! Ya estás registrado', 'success')
        return redirect(url_for('usuarios.login'))
    return render_template('usuarios/crear.html', form=form, title='Registro')

@usuarios_bp.route('/usuarios/confirmar/<int:user_id>', methods=['GET', 'POST'])
@login_required
def confirmar(user_id):
    user = User.query.get_or_404(user_id)
    form = PasswordCheckForm()
    if form.validate_on_submit():
        if not user.check_password(form.contraseña.data):
            flash('Contraseña incorrecta')
            return redirect(url_for('usuarios.confirmar'))
        else:
            flash('Contraseña confirmada')
            return redirect(url_for('usuarios.edit',user_id=user_id))
    return render_template('usuarios/confirmar_contraseña.html', form=form, user=user, title='Confirmar contraseña')


@usuarios_bp.route('/usuarios/editar/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit(user_id):
    user = User.query.get_or_404(user_id)
    form = UserEditForm(obj=user)
    new = {}
    if form.validate_on_submit():
        for item in form:
            if item.data and item.id != 'submit' and item.id != 'csrf_token':
                new[item.id] = item.data
        update = user.update_user(user_id, new)
        if update:
            flash('Usuario actualizado con éxito', 'success')
            return redirect(url_for('usuarios.index'))
        else:
            flash('Usuario no encontrado', 'failure')
            return redirect(url_for('usuarios.index'))

    return render_template('usuarios/editar.html', form=form, user=user, title='Editar usuario')

@usuarios_bp.route('/usuarios/borrar/<int:user_id>', methods=['GET', 'POST'])
@login_required
def delete(user_id):
    form = UserDeleteForm()
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        if form.confirmar.data:
            borr = user.delete(user_id)
            flash(f'Usuario {user.email} borrado con éxito', 'success')
        elif form.cancelar.data:
            flash(f'Borrado de {user.email} abortado', 'cancel')
        return redirect(url_for('usuarios.index'))
    return render_template('usuarios/borrar.html', form=form, user=user, title='Borrar usuario')

@usuarios_bp.route('/usuarios/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('usuarios.index'))
    form = UserLoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.email == form.email.data))
        if user is None or not user.check_password(form.contraseña.data):
            flash('Nombre o contraseña incorrectos')
            return redirect(url_for('usuarios.login'))
        else:
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            if current_user.id == 1:
                next_page = url_for('usuarios.index')
            else:
                next_page = url_for('index')
        return redirect(next_page)
    return render_template('usuarios/login.html', form=form, title='Acceder')

@usuarios_bp.route('/usuarios/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('usuarios.login'))