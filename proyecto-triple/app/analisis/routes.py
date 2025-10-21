from flask import render_template, request, current_app
from io import BytesIO
import base64, os
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # backend sin display
import matplotlib.pyplot as plt
import seaborn as sns
from . import analisis_bp

@analisis_bp.route('/analisis')
def index():
    return render_template('analisis/index.html')

@analisis_bp.route('/analisis/bar')
def bar_chart():
    return render_template('analisis/bar.html')

@analisis_bp.route('/analisis/pie')
def pie_chart():
    return render_template('analisis/pie.html')


sns.set_theme(style="whitegrid")

def _fig_to_data_uri():
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight", dpi=144)
    buf.seek(0)
    data_uri = "data:image/png;base64," + base64.b64encode(buf.read()).decode("ascii")
    plt.close()  # evita fugas en el servidor
    return data_uri

def _load_df():
    # Usa config o un path por defecto: ../data/covid.csv
    csv_path = current_app.config.get(
        "DATA_PATH",
        os.path.join(current_app.root_path, "..", "data", "covid.csv"),
    )
    return pd.read_csv(os.path.abspath(csv_path))

@analisis_bp.route("/pie", methods=["GET", "POST"])
def pie():
    chart_data = None
    selected = None

    if request.method == "POST":
        selected = request.form.get("data_type", "casos")
        df = _load_df()

        # Columna categoría (ajústala a tu dataset, p.ej. "provincia" o "ccaa")
        categoria = current_app.config.get("ANALISIS_CATEGORIA", "provincia")

        if categoria in df.columns and selected in df.columns:
            agg = df.groupby(categoria)[selected].sum().sort_values(ascending=False).head(8)
            etiquetas = agg.index.tolist()
            valores = agg.values.tolist()
        else:
            # Fallback si las columnas no existen (demostración)
            etiquetas = ["A", "B", "C", "D"]
            valores = [25, 15, 35, 25]

        # Gráfica circular (seaborn no tiene pie; usamos matplotlib con paleta de seaborn)
        plt.figure(figsize=(6, 6))
        colores = sns.color_palette("crest", n_colors=len(valores))
        plt.pie(
            valores,
            labels=etiquetas,
            colors=colores,
            autopct="%1.1f%%",
            startangle=90,
            pctdistance=0.8,
            textprops={"color": "#0f172a", "fontsize": 10},
        )
        plt.title(f"Distribución de {selected}", fontsize=14, pad=12)
        chart_data = _fig_to_data_uri()

    return render_template("analisis/pie.html", chart_data=chart_data, selected=selected)
# ...existing code...