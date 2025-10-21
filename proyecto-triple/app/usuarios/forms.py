from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class UserCreationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=50)])
    apellidos = StringField('Apellidos', validators=[DataRequired(), Length(max=100)])
    telefono = StringField('Teléfono', validators=[DataRequired(), Length(min=9, max=9)])
    edad = IntegerField('Edad', validators=[DataRequired()])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    contraseña2 = PasswordField('Vuelve a introducir la contraseña', validators=[DataRequired(), EqualTo(contraseña), Length(min=6)])
    submit = SubmitField('Crear Usuario')

class UserEditForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=50)])
    apellidos = StringField('Apellidos', validators=[DataRequired(), Length(max=100)])
    telefono = StringField('Teléfono', validators=[DataRequired(), Length(min=9, max=9)])
    edad = IntegerField('Edad', validators=[DataRequired()])
    submit = SubmitField('Actualizar Usuario')

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    contraseña = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

class UserDeleteForm(FlaskForm):
    confirm = TextAreaField('Escribe "BORRAR" para confirmar', validators=[DataRequired()])
    submit = SubmitField('Borrar Usuario')