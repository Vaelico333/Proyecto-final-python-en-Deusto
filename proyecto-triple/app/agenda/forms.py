from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email, Regexp

class ContactForm(FlaskForm):
    name = StringField('Nombre', validators=[
        DataRequired(),
        Length(min=3, max=50),
        Regexp(r'^[A-Za-z\s]+$', message="El nombre solo debe contener letras.")
    ])
    phone = StringField('Número de Teléfono', validators=[
        DataRequired(),
        Regexp(r'^\d{9}$', message="El número de teléfono debe tener 9 dígitos.")
    ])
    email = EmailField('Email', validators=[
        DataRequired(),
        Email(message="Formato de email no válido.")
    ])
    submit = SubmitField('Enviar')