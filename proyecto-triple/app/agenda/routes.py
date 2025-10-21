from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from .models import Contact
from .forms import ContactForm
from ..extensions import db
from . import agenda_bp

@agenda_bp.route('/agenda')
def index():
    contacts = Contact.query.all()
    return render_template('agenda/index.html', contacts=contacts)

@login_required
@agenda_bp.route('/agenda/list', endpoint='list')
def contact_list():
    contacts = Contact.query.all()
    return render_template('agenda/list.html', contactos=contacts)

@login_required
@agenda_bp.route('/agenda/create', methods=['GET', 'POST'])
def create():
    form = ContactForm()
    if form.validate_on_submit():
        new_contact = Contact(name=form.name.data, phone=form.phone.data, email=form.email.data)
        db.session.add(new_contact)
        db.session.commit()
        flash('Contact created successfully!', 'success')
        return redirect(url_for('agenda.index'))
    return render_template('agenda/create.html', form=form)

@login_required
@agenda_bp.route('/agenda/edit/<int:contact_id>', methods=['GET', 'POST'])
def edit(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    form = ContactForm(obj=contact)
    if form.validate_on_submit():
        contact.name = form.name.data
        contact.phone = form.phone.data
        contact.email = form.email.data
        db.session.commit()
        flash('Contact updated successfully!', 'success')
        return redirect(url_for('agenda.index'))
    return render_template('agenda/edit.html', form=form, contact=contact)

@login_required
@agenda_bp.route('/agenda/delete/<int:contact_id>', methods=['POST'])
def delete(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact deleted successfully!', 'success')
    return redirect(url_for('agenda.index'))

@login_required
@agenda_bp.route('/agenda/detail/<int:contact_id>')
def detail(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    return render_template('agenda/detail.html', contact=contact)