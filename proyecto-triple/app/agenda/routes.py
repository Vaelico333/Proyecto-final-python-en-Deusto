from flask import render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from ..models import User
from .models import Contact
from .forms import ContactForm, SearchForm
from app import db
from . import agenda_bp
import sqlalchemy as sa

@login_required
@agenda_bp.route('/agenda')
def index():
    if not current_user.is_authenticated:
        return current_app.login_manager.unauthorized()
    contactos = Contact.query.all()
    return render_template('agenda/agenda.html', contacts=contactos)

@login_required
@agenda_bp.route('/agenda/lista', methods=['GET', 'POST'])
def lista_contactos():
    if not current_user.is_authenticated:
        return current_app.login_manager.unauthorized()
    user_id = current_user.id
    if user_id == 1:
        contactos = Contact.query.all()
    else:
        contactos = Contact.query.filter(Contact.user_id == user_id).all()
    return render_template('agenda/lista.html', contactos=contactos, user_id=user_id)

@login_required
@agenda_bp.route('/agenda/crear', methods=['GET', 'POST'])
def crear():
    form = ContactForm()
    if form.validate_on_submit():
        new_contact = Contact(nombre=form.nombre.data.title(), telefono=form.telefono.data, email=form.email.data, user_id=current_user.id)
        db.session.add(new_contact)
        db.session.commit()
        flash('Contacto añadido a la agenda', 'success')
        return redirect(url_for('agenda.lista_contactos'))
    return render_template('agenda/crear.html', form=form)

@login_required
@agenda_bp.route('/agenda/editar/<int:contact_id>', methods=['GET', 'POST'])
def editar(contact_id):
    contacto = Contact.query.get_or_404(contact_id)
    form = ContactForm(obj=contacto)
    if form.validate_on_submit():
        contacto.nombre = form.nombre.data.title()
        contacto.telefono = form.telefono.data
        contacto.email = form.email.data
        db.session.commit()
        flash('Contacto actualizado con éxito', 'success')
        return redirect(url_for('agenda.index'))
    return render_template('agenda/editar.html', form=form, contact=contacto)

@login_required
@agenda_bp.route('/agenda/borrar/<int:contact_id>', methods=['GET','POST'])
def borrar(contact_id):
    contacto = Contact.query.get_or_404(contact_id)
    db.session.delete(contacto)
    db.session.commit()
    flash('Contacto borrado de la agenda', 'success')
    return redirect(url_for('agenda.lista_contactos'))

@login_required
@agenda_bp.route('/agenda/buscar', methods=['GET','POST'])
def buscar():
    form = SearchForm()
    if request.method == 'POST':
        if form.validate_on_submit:
            contact = db.session.scalar(
                sa.select(Contact).where(Contact.nombre == form.nombre.data.title()))
            if contact:
                return redirect(url_for('agenda.detalle', contact_id=contact.id))
            else:
                flash(f'{form.nombre.data} no encontrado')
    return render_template('agenda/buscar.html', form=form)

@login_required
@agenda_bp.route('/agenda/ver_contacto/<int:contact_id>')
def detalle(contact_id):
    contacto = Contact.query.get_or_404(contact_id)
    user = User.query.get_or_404(contacto.user_id)
    return render_template('agenda/ver_contacto.html', contact=contacto, user=user)