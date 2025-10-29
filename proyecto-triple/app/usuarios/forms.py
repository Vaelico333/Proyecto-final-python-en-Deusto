from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class UserCreationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Este campo es obligatorio'), Email(message='Introduce una dirección de email')])
    nombre = StringField('Nombre', validators=[DataRequired(message='Este campo es obligatorio'), Length(max=50, message='El nombre es demasiado largo')])
    apellidos = StringField('Apellidos', validators=[DataRequired(message='Este campo es obligatorio'), Length(max=100, message='El apellido es demasiado largo')])
    telefono = StringField('Teléfono', validators=[DataRequired(message='Este campo es obligatorio'), Length(min=9, max=9, message='El número debe tener 9 dígitos')])
    edad = StringField('Edad', validators=[DataRequired(message='Este campo es obligatorio'), Length(min=1, max=3, message='La edad debe estar entre 0 y 999')])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(message='Este campo es obligatorio'), Length(min=6, message='La contraseña debe tener más de 6 caracteres')])
    contraseña2 = PasswordField('Vuelve a introducir la contraseña', validators=[DataRequired(message='Este campo es obligatorio'), EqualTo('contraseña', message='Ambas contraseñas deben ser iguales'), Length(min=6)])
    submit = SubmitField('Crear Usuario')

class UserEditForm(FlaskForm):
    email = StringField('Email', validators=[Email(message='Introduce una dirección de email')])
    nombre = StringField('Nombre', validators=[Length(max=50, message='El nombre es demasiado largo')])
    apellidos = StringField('Apellidos', validators=[Length(max=100, message='El apellido es demasiado largo')])
    telefono = StringField('Teléfono', validators=[Length(min=9, max=9, message='El número debe tener 9 dígitos')])
    edad = StringField('Edad')
    submit = SubmitField('Actualizar Usuario')

class PasswordCheckForm(FlaskForm):
    contraseña = PasswordField('Introduce tu contraseña', validators=[DataRequired()])
    submit = SubmitField('Confirmar')

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    contraseña = PasswordField('Contraseña', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Iniciar Sesión')

class UserDeleteForm(FlaskForm):
    confirmar = SubmitField('Borrar Usuario')
    cancelar = SubmitField('Cancelar')