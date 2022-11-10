# Proyecto Final

Entrega Intermedia Del Proyecto Final

## Descripción del proyecto

El proyecto consiste en la creation de un blog funcional utilization python/Django cumpliendo los requisitos planteados en los objetivos indicados

## Cómo instalar y ejecutar el proyecto
El proyecto aprovecha la posibilidad de la creation de entornos virtuales de python

```cmd
cd ProyectoFinal

virtualenv venv
```
Luego activaremos dicho entorno
```cmd
venv \Scripts\activate
```
Estando ahí procederemos a instalar los requerimientos necesarios:
asgiref==3.5.2
crispy-bootstrap5==0.7
defusedxml==0.7.1
diff-match-patch==20200713
Django==4.1.3
django-ckeditor==6.5.1
django-crispy-forms==1.14.0
django-import-export==3.0.1
django-js-asset==2.0.0
et-xmlfile==1.1.0
MarkupPy==1.14
odfpy==1.4.1
openpyxl==3.0.10
Pillow==9.3.0
PyYAML==6.0
sqlparse==0.4.3
tablib==3.2.1
tzdata==2022.6
xlrd==2.0.1
xlwt==1.3.0

## Requerimientos
Para instalar los requerimientos procederemos de la siguiente forma.
```cmd
pip install -r requirements.txt
```
Ya estamos listos para correr nuestro entorno.

## Cómo utilizar el proyecto
Para la utilización de nuestro blog deberemos iniciar nuestro proyecto.
```cmd
cd Django_Blog
python manage.py runserver
```

Si todo fue bien esto iniciara un servidor web [Blog](http://localhost:8000) en el cual ya podremos gestionar.
El proyecto cuanta con el panel [admin](http://localhost:8000/admin) habilitado: 

Las credenciales son admin admin por cuestiones prácticas.

Ahí podrás realizar los CRUD sobre los 5 modelos:
Grupos
Usuarios
Autores	
Categorías (Si bien puede realizar cambios sobre este modelo, este ya viene con 5 categoria predefinidas Tutoriales, Tecnologia, VideoJuegos, Programacion) ESTO SE DEBE A CUESTIONES DE DISEÑO- NAVBAR VIEWS TEMPLATES.
Posts

En todas las categories encontrara la barra para realizar un buscar por título y description.

El el navbar encontrara una sección CRUD permitiendo hacer crud de autores y post sin necesidad del ingresar al panel de admin.

Por cuestiones prácticas el proyecto trae un solo usuario creado como indica anteriormente el admin, si dicho usuario no se encuentra logueado todos los botones Guardar, Elimininar y Cancelar se encuentra deshabilitado dando acceso del guest únicamente por los cual solo podrá ver los posts a modo de ejemplos.

## Créditos
Mi gratitud a CoderHouse, al [Profesor] Daniel Ochoa, y a los tutores que me dieron el empujoncito que me hacía falta para empezar el lindo camino en python/django. Por ultimo y no por eso menos importante a mi FLIA que me permitió el tiempo y el espacio para estar horas tirando líneas y practicando este lenguaje tan potente.