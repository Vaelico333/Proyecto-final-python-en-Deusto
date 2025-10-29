from flask import request, current_app
import pandas as pd
import os
import matplotlib
matplotlib.use("Agg")  # backend sin display
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64, os

def _fig_to_data_uri():
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight", dpi=144)
    buf.seek(0)
    data_uri = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode("ascii")
    plt.close()  
    return data_uri

def _volcar_datos() -> None:
    """Extrae los datos del CSV proporcionado y vuélcalos en un .txt con formato JSON."""

    import csv
    import json
    results = []
    with open(current_app.config['DATA_PATH'], encoding='UTF-8') as origen:
        reader = csv.DictReader(origen)
        for row in reader:
            results.append(row)
    with open(current_app.config['ANALYSIS_STORE'], mode='w+', encoding='UTF-8') as almacen:
        json.dump(results,fp=almacen,ensure_ascii=False, indent=0)

def _cargar_datos():
    """Carga los datos del almacén .txt en formato JSON y devuelve un Data Frame de Pandas"""
    with open(current_app.config['ANALYSIS_STORE'], encoding='UTF-8') as almacen:
            df = pd.read_json(almacen)
    return df

def _analisis_provincia(selected):
    """Agrupa los datos y crea una gráfica circular con un formato específico"""

    # Comprueba que el txt con los datos existe, y si no, lo creo:
    if not os.path.exists(current_app.config.get('ANALYSIS_STORE')):
        from .services import _volcar_datos
        _volcar_datos()
    
    topN = [10 if "top10" in request.form else 52]
    df =_cargar_datos()
    df = df.groupby('province', as_index=False)[selected].sum()

    # Las provincias con 0 ocurrencias se apilan, quedando los nombres sobrepuestos. Por tanto, las elimino de la gráfica:
    df = df[df[selected] != 0]

    top_prov = (df.groupby('province')[selected]
                .sum().sort_values(ascending=False).head(*topN).index)
    df_plot = df[df['province'].isin(top_prov)]

    primera_ultima = [top_prov[0], top_prov[-1]]
    fig, ax = plt.subplots(figsize=(16,8), facecolor='teal')
    n = len(df[selected])
    xp = len(df_plot[selected])
    exp = [0.15]*xp

    with sns.axes_style( rc={'axes.facecolor':'darkgrey', 'figure.facecolor':'teal'}):
        colors = sns.color_palette('Paired', n_colors=n)
        sns.set_theme(context='paper')
        ax.pie(df_plot[selected],startangle=290, shadow=True, explode=exp, colors=colors, counterclock=False, labels=df_plot['province'], rotatelabels=True, labeldistance=1.05)
        ax.legend(labels=df_plot['province'] ,title='Provincias', ncol=2, bbox_to_anchor=(-0.1,1), loc='upper right')
    
    chart_data = _fig_to_data_uri()
    return chart_data, primera_ultima

def _analisis_semana_provincia(selected):
    """Agrupa los datos y crea una gráfica de barras con un formato específico"""

    # Comprueba que el txt con los datos existe, y si no, lo creo:
    if not os.path.exists(current_app.config.get('ANALYSIS_STORE')):
        from .services import _volcar_datos
        _volcar_datos()
    
    # Variables importantes:
    topN = [10 if "top10" in request.form else 52]
    cols = {'num_def':'Defunciones', 'new_cases':'Casos nuevos', 'num_hosp':'Hospitalizaciones', 'num_uci':'Ingresos en UCI'}
    dias = {0:'Lunes', 1:'Martes', 2:'Miércoles', 3:'Jueves', 4:'Viernes', 5:'Sábado', 6:'Domingo'}
    dias_ord = list(dias.values())   

    # Creación del DF
    df = _cargar_datos()
    df['date'] = pd.to_datetime(df['date'], yearfirst=True)
    df = df.assign(dia_semana=df['date'].dt.day_of_week.map(dias))
    df = df.groupby(['province', 'dia_semana'], as_index=False)[selected].sum()

    # Asegura orden categórico en el eje hue, para una representación ordenada de los días de la semana
    df['dia_semana'] = pd.Categorical(df['dia_semana'],
                                        categories=dias_ord, ordered=True)

    # Muestra sólo las provincias con más casos (por defecto, muestra todas)
    top_prov = (df.groupby('province')[selected]
                .sum().sort_values(ascending=False).head(*topN).index)
    df_plot = df[df['province'].isin(top_prov)]
    primera_ultima = [top_prov[0], top_prov[-1]]

    # Colores, formas y leyenda:
    paleta = sns.color_palette('Paired', n_colors=len(dias_ord))
    plt.figure(figsize=(11,5), facecolor='teal')

    # Modifica los parámetros de los ejes de manera temporal mientras creamos la gráfica:
    with sns.axes_style( rc={ 'axes.facecolor':'black'}):
        ax = sns.barplot(data=df_plot, x='province', y=selected,
                    hue='dia_semana', palette=paleta, dodge=True, linewidth=0)
        ax.legend(title='Día de la semana', bbox_to_anchor=(1,0.75), loc='upper left', facecolor='silver')
        ax.set_xticks(range(len(df_plot['province'].unique())))
        ax.set_xticklabels(df_plot['province'].unique(), rotation=90, ha='center')
        ax.set_ylabel('Provincia')
        ax.set_xlabel(cols[selected])

    plt.tight_layout()
    chart_data = _fig_to_data_uri()
    return chart_data, primera_ultima