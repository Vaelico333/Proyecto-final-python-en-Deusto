from flask import render_template, request, current_app
from . import analisis_bp
from .services import _analisis_provincia, _analisis_semana_provincia
from .forms import OptionsForm


@analisis_bp.route('/analisis')
def index():
    return render_template('analisis/index.html', title='Análisis del COVID - España Mayo de 2021')


@analisis_bp.route("/pie", methods=["GET", "POST"])
def pie():
    form = OptionsForm()
    chart_data = None
    selected = None
    titles = {'num_def':'defunciones', 'new_cases':'casos nuevos', 'num_hosp':'hospitalizaciones', 'num_uci':'ingresos en UCI'}
    chart_title = None
    extremos = None

    if request.method == "POST":
        selected = form.opciones.data
        chart_data, extremos = _analisis_provincia(selected)
        chart_title = titles[selected]
    return render_template("analisis/pie.html", chart_data=chart_data, 
                           chart_title=chart_title, selected=selected,
                           title='Análisis por provincias',
                           title_result=extremos, form=form)

@analisis_bp.route("/bar", methods=["GET", "POST"])
def bar():
    form = OptionsForm()
    chart_data = None
    selected = None
    titles = {'num_def':'defunciones', 'new_cases':'casos nuevos', 'num_hosp':'hospitalizaciones', 'num_uci':'ingresos en UCI'}
    chart_title = None
    extremos = None

    if request.method == "POST":
        selected = form.opciones.data
        chart_data, extremos = _analisis_semana_provincia(selected)
        chart_title = titles[selected]
    return render_template("analisis/bar.html", chart_data=chart_data, 
                           chart_title=chart_title, selected=selected,
                           title='Análisis por días y provincias',
                           title_result=extremos, form=form)