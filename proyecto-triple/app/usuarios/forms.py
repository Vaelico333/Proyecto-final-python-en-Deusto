from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp
import re

class UserCreationForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(message='Este campo es obligatorio'), 
                                    Email(message='Introduce una dirección de email válida')])
    nombre = StringField('Nombre', 
                         validators=[DataRequired(message='Este campo es obligatorio'), 
                                     Length(max=50, message='El nombre es demasiado largo')])
    apellidos = StringField('Apellidos', 
                            validators=[DataRequired(message='Este campo es obligatorio'), 
                                        Length(max=100, message='El apellido es demasiado largo')])
    telefono = StringField('Teléfono', 
                           validators=[DataRequired(message='Este campo es obligatorio'), 
                                       Regexp(r'[\d{9}]', flags=re.UNICODE, message='El número de teléfono solo debe incluir números (no poner prefijo de país)'), 
                                       Length(min=9, max=9, message='El número debe tener 9 dígitos')])
    edad = StringField('Edad', 
                       validators=[DataRequired(message='Este campo es obligatorio'), 
                                   Regexp(r'[\d+]', flags=re.UNICODE, message='La edad debe ser números'), 
                                   Length(min=1, max=3, message='La edad debe estar entre 0 y 999')])
    contraseña = PasswordField('Contraseña', 
                               validators=[DataRequired(message='Este campo es obligatorio'), 
                                           Length(min=6, message='La contraseña debe tener más de 6 caracteres')])
    contraseña2 = PasswordField('Vuelve a introducir la contraseña', 
                                validators=[DataRequired(message='Este campo es obligatorio'), 
                                            EqualTo('contraseña', message='Ambas contraseñas deben ser iguales'), 
                                            Length(min=6)])
    submit = SubmitField('Crear Usuario')

class UserEditForm(FlaskForm):
    email = StringField('Email', 
                        validators=[Email(message='Introduce una dirección de email')])
    nombre = StringField('Nombre', 
                         validators=[Length(max=50, message='El nombre es demasiado largo')])
    apellidos = StringField('Apellidos', 
                            validators=[Length(max=100, message='El apellido es demasiado largo')])
    telefono = StringField('Teléfono', 
                           validators=[Length(min=9, max=9, message='El número debe tener 9 dígitos'),
                            Regexp(r'[\d{9}]', flags=re.UNICODE, message='El número de teléfono solo debe incluir números (no poner prefijo de país)')])
    edad = StringField('Edad')
    submit = SubmitField('Actualizar Usuario')

class PasswordCheckForm(FlaskForm):
    contraseña = PasswordField('Introduce tu contraseña')
    submit = SubmitField('Confirmar')
    cancel = SubmitField('Cancelar')

class UserLoginForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    contraseña = PasswordField('Contraseña', 
                               validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Iniciar Sesión')

class UserDeleteForm(FlaskForm):
    confirmar = SubmitField('Borrar Usuario')
    cancelar = SubmitField('Cancelar')