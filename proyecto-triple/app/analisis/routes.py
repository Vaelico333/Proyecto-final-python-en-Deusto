from flask import render_template, request, current_app
from . import analisis_bp
from .services import _analisis_provincia, _analisis_semana_provincia


@analisis_bp.route('/analisis')
def index():
    return render_template('analisis/index.html')


@analisis_bp.route("/pie", methods=["GET", "POST"])
def pie():
    chart_data = None
    selected = None
    titles = {'num_def':'Defunciones', 'new_cases':'Casos nuevos', 'num_hosp':'Hospitalizaciones', 'num_uci':'Ingresos en UCI'}
    chart_title = None

    if request.method == "POST":
        selected = request.form.get("data_type")
        chart_data = _analisis_provincia(selected)
        chart_title = titles[selected]
    return render_template("analisis/pie.html", chart_data=chart_data, chart_title=chart_title, selected=selected)

@analisis_bp.route("/bar", methods=["GET", "POST"])
def bar():
    chart_data = None
    selected = None
    titles = {'num_def':'Defunciones', 'new_cases':'Casos nuevos', 'num_hosp':'Hospitalizaciones', 'num_uci':'Ingresos en UCI'}
    chart_title = None

    if request.method == "POST":
        selected = request.form.get("data_type")
        chart_data = _analisis_semana_provincia(selected)
        chart_title = titles[selected]
    return render_template("analisis/bar.html", chart_data=chart_data, chart_title=chart_title, selected=selected)