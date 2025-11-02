from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

class OptionsForm(FlaskForm):
    opciones = SelectField('Elige una categoría', 
                           choices=[('num_def', 'Defunciones'),
                                    ('new_cases', 'Casos'),
                                    ('num_hosp', 'Hospitalizados'),
                                    ('num_uci', 'UCI')],
                                    coerce=str)
    submit_all = SubmitField('Mostrar todos')
    submit_10 = SubmitField('Mostrar top 10', name='top10')