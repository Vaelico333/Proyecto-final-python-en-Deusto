# Proyecto final del curso de python con Deusto

Se me propusieron 3 opciones sencillas, pero he decidido hacer una mezcla de las 3, ya que será más interesante. Sobre todo, teniendo en cuenta que yo apenas he trabajado con Flask, y aquí se me pide.

## :building_construction: Estructura del proyecto

- App en Flask para contener y mostrar el proyecto
  - [Página de bienvenida](#wave-página-de-bienvenida): Mensaje de bienvenida y acceso a los 3 proyectos.
  - [Proyecto agenda](#card_index-proyecto-agenda)
  - [Proyecto usuarios](#person_bald-proyecto-usuarios)
  - [Proyecto análisis](#bar_chart-proyecto-análisis)

## :card_file_box: Desglose

Veamos en qué consiste cada parte.

### :wave: Página de bienvenida

Será una página en Flask con los siguientes atributos:

- Mensaje de bienvenida al proyecto
- Fondo de la página: un paisaje natural o un amanecer
- Explicación de mi decisión
- Enlaces a los 3 proyectos  

[:arrow_up:](#proyecto-final-del-curso-de-python-con-deusto)

### :card_index: Proyecto agenda

Se trata de un gestor de contactos con la capacidad de realizar las operaciones CRUD sobre al menos 3 atributos: nombre, Nº de teléfono y email.  
**Restricciones y contenido**:  

- Funciones:
  - Agregar contacto
  - Buscar un contacto
  - Editar contacto
  - Eliminar contacto
  - Mostrar todos
- Almacenamiento: usaré SQLAlchemy, la extensión de Flask para bases de datos. Tendrá su propia tabla.
- Control de inputs mediante RegEx (nombre: letras, tlf: 9 dígitos, email: `x@x.x`) o herramientas integradas de Flask.  

**Observaciones**:

- Crear un formulario o menú de botones con un cuadro debajo que muestre los resultados.
- Almacenamiento: sqlite3
- Incluir botón de vuelta a la página de bienvenida del proyecto.

[:arrow_up:](#proyecto-final-del-curso-de-python-con-deusto)

### :person_bald: Proyecto usuarios

Se trata de un panel de administración de usuarios.  
**Contenido**:

- Página de gestión de los usuarios:
  - Menú principal:
    - Ver todas: link a la tabla
    - Ver entrada: link a mostrar una
    - Editar entrada: link a página de edición
    - Borrar entrada: link a página de borrado
    - Crear entrada: link a página de creación
  - Página de tabla: mostrar todas las entradas en una tabla.
  - Página de mostrar 1 contacto: pedir email.
  - Página con formulario de edición: pedir email y contraseña; permitir reescribir todos los campos. Si no se porporciona, no editar el campo.
  - Página con formulario de creación: email, nombre, apellidos, contraseña, teléfono y edad.
  - Página con formulario de borrado: pedir email y contraseña y pedir confirmación de borrado.

**Observaciones**:

- Árbol de páginas web interconectadas
- Almacenamiento: tabla en SQLite con SQLAlchemy.
- Incluir botón de vuelta a la página de bienvenida del proyecto.  
- Incluir botón de vuelta a la página de menú principal.

[:arrow_up:](#proyecto-final-del-curso-de-python-con-deusto)

### :bar_chart: Proyecto análisis

Se trata de un dashboard de análisis de datos procedentes de un archivo csv proporcionado por la escuela.  
**Contenido**:

- Página de bienvenida  
  - Enlaces de acceso a las otras dos páginas
- Página 1 con un menú que permita elegir defunciones, casos, hospitalizados o UCI y mostrarlo como una gráfica de barras en la página.
- Página 2 con un menú que permita elegir defunciones, casos, hospitalizados o UCI y mostrarlo como una gráfica circular en la página.

**Observaciones**:

- Almacenamiento: fichero .txt con formato interno JSON.
- Agrupar datos por día de la semana y provincias.
- Página 1: menú de botones con un cuadro debajo que muestre la gráfica correspondiente. Mostrar ocurrencias por día de la semana.
- Página 2: menú de botones con un cuadro debajo que muestre la gráfica correspondiente. Mostrar gráfica circular con desglose por provincias.
- Incluir botón de vuelta a la página de bienvenida del proyecto.  
- Incluir botón de vuelta a la página de bienvenida del subproyecto.  

[:arrow_up:](#proyecto-final-del-curso-de-python-con-deusto)
