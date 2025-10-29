from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email, Regexp
import re

class ContactForm(FlaskForm):
    nombre = StringField('Nombre', validators=[
        DataRequired(message='Campo obligatorio'),
        Length(min=3, max=50),
        Regexp(r'^[\w\s]+$', flags=re.UNICODE, message="El nombre solo debe contener letras.")])
    telefono = StringField('Número de Teléfono', validators=[
        DataRequired(message='Campo obligatorio'),
        Length(min=9, max=9, message='El número de teléfono debe tener 9 dígitos.'),
        Regexp(r'[\d{9}]', flags=re.UNICODE, message='El número de teléfono solo debe incluir números (no poner prefijo de país)')])
    email = EmailField('Email', validators=[
        DataRequired(message='Campo obligatorio'),
        Email(message="Formato de email no válido.")
    ])
    submit = SubmitField('Enviar')

class SearchForm(FlaskForm):
    nombre = StringField('Nombre', validators=[
        DataRequired(message='Campo obligatorio'),
        Length(min=3, max=50)])
    submit = SubmitField('Buscar')
