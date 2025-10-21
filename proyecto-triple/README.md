# Proyecto Flask Multiproject

Este proyecto es una aplicación web desarrollada con Flask que incluye una página de bienvenida y tres proyectos separados: Agenda, Usuarios y Análisis. A cada uno de estos proyectos se puede acceder desde la página de inicio.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```
flask-multiproject-app
├── app
│   ├── __init__.py
│   ├── extensions.py
│   ├── static
│   │   └── css
│   │       └── styles.css
│   ├── templates
│   │   ├── base.html
│   │   └── index.html
│   ├── agenda
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── models.py
│   │   ├── forms.py
│   │   └── templates
│   │       └── agenda
│   │           ├── index.html
│   │           ├── list.html
│   │           ├── create.html
│   │           ├── edit.html
│   │           └── detail.html
│   ├── usuarios
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── models.py
│   │   ├── forms.py
│   │   ├── auth.py
│   │   └── templates
│   │       └── usuarios
│   │           ├── index.html
│   │           ├── table.html
│   │           ├── create.html
│   │           ├── edit.html
│   │           ├── delete.html
│   │           ├── detail.html
│   │           └── login.html
│   └── analisis
│       ├── __init__.py
│       ├── routes.py
│       ├── services.py
│       └── templates
│           └── analisis
│               ├── index.html
│               ├── bar.html
│               └── pie.html
├── data
│   ├── covid.csv
│   └── analysis_store.txt
├── instance
│   └── .gitkeep
├── tests
│   ├── test_agenda.py
│   ├── test_usuarios.py
│   └── test_analisis.py
├── wsgi.py
├── config.py
├── requirements.txt
└── README.md
```

## Instalación

1. Clona el repositorio en tu máquina local.
2. Navega al directorio del proyecto.
3. Crea un entorno virtual y actívalo.
4. Instala las dependencias usando `pip install -r requirements.txt`.
5. Configura la base de datos y otros parámetros en `config.py`.
6. Ejecuta la aplicación usando `python wsgi.py`.

## Uso

- Accede a la página de bienvenida en `http://localhost:5000` para navegar a los proyectos de Agenda, Usuarios y Análisis.
- Cada proyecto tiene su propia funcionalidad y se puede acceder a través de enlaces en la página de inicio.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.