# Trabajo integrador - Fundamentos de Django

## Sistema de gestión de productos y proveedores.

Se creó un proyecto llamado "StockControl" y una app llamada "compra". En la app se agregaron los modelos Producto y Proveedor, donde Proveedor es una foreingkey en Producto.

Posteriormente se crearon las siguientes funcionalidades:

- Agregar un nuevo proveedor.
- Agregar un nuevo producto.
- Listar todos los proveedores.
- Listar todos los productos.
- Tener disponible los modelos de producto y proveedor en el Admin.
- Implementación de Bootstrap en los HTML.
- Generación del archivo requirements del proyecto.

También se agregaron dos funcionalidades extra como mejora:

- Agregar una página de inicio al cargar el sistema.
- Implementación de la carga y visualización de imágenes de los productos.

## Desarrollo

### Estructura general

1- Creación del repositorio remoto en GitHub. (https://github.com/PabloKonig/Proyecto-final-Python-Django-Alkemy)

2- Generar una carpeta para el proyecto y realizar el git clone del repositorio.

3- Creación del entorno virtual de Python: python -m -venv venv

4- Activar el entorno virtual con: source venv/Script/activate  (En windows).

5- Instalar el framework django: pip install django

6- Crear el proyecto StockControl: django-admin startproyect StockControl

7- Renombrar a "src" la carpeta principal del proyecto.

8- Instalar la aplicación Django Rest framework para facilitar la realización de consultas REST y otras operaciones comunes.

9- Generar el archivo .gitignore y colocarlo en la raíz del proyecto. Esto establece que archivos no se subirán al repositorio remoto. Utilicé el sitio web gitignore.io para realizarlo.

10- Crear dentro de "src" las carpetas templates, media y static.

11- Abrir settings.py y reemplazar lo siguiente:

- En TEMPLATES, reemplazar "DIRS": [], por "DIRS": [ BASE_DIR / 'templates', ], para establecer esta carpeta para las plantillas.
- Establecer LENGUAGE_CODE = "es-ar" para establecer el idioma y país.

12- Establecer en la base de datos las tablas de usuarios y sistema: python manage.py migrate

13- Crear la app "compra": python manage.py startapp compra

14- Abrir settings.py y en INSTALLED_APPS agregar 'compra', dentro del arreglo.

### Creación de modelos

15- Crear en models.py de "compra" las clases que representan a los dos modelos:

- class Proveedor con nombre y apellido con CharField() para cadena de caracteres y max_length=50 para limitar los mismo a 50. Y dni con BigIntegerField() para soportar números muy grandes a futuro sin problemas.
- class Producto con precio del tipo FloatField() para soportar decimales en el precio. Además foto con ImageField() que almacenará la ruta y nombre de una foto ("upload_to" establece una subcarpeta donde se almacenan las imagenes subidas desde el formulario y "default" la imagen por defecto si no se establece una en el formulario). Finalmente se determina "proveedor" asociado a la ForeignKey "Proveedor" y mediante on_delete=models.PROTECT establecemos que para eliminar un proveedor no debe haber ningún producto asociado a él, primero debemos eliminar o modificar los productos relacionados. Con esto queremos evitar eliminar productos por error como pasaría con CASCADE.

16- Empaquetar los cambios de los modelos en archivos de migración: python manage.py makemigrations y luego llevarlos a la base de datos con: python manage.py migrate .

### Armado de Plantillas

17- Dentro de la carpeta "templates" creamos las subcarpetas "inicio" (para la plantilla de inicio), "productos" (para las plantillas relacionadas con los productos) y "proveedores" (para plantillas relacionadas con los proveedores) para mantener un orden que simplifique la gestión a futuro.

18- Crear en la carpeta "templates" el archivo base.html que es la estructura base que tomarán las demás plantillas de modo de tener todas una misma estructura, modificable en un solo lugar. Dado que utilizaremos Bootstrap copiaremos la estructura inicial de su sitio oficial - https://getbootstrap.com/docs/5.3/getting-started/introduction/ - en su opción 2 que incluye CSS y JS de Bootstrap. Así mismo, agregamos un navbar desde el sitio de Bootstrap y luego del mismo agregamos un bloque "block" donde se insertará el contenido de las plantillas que extiendan a base.html. {% block content %} {% endblock content %} .

19- Crear las plantillas de listado de proveedores (templates/proveedores/proveedores_list.html) y lista de productos (templates/productos/productos_list.html). En ambos casos extienden de base.html, luego se establece el bloque {% block content %} y posteriormente se crea una estructura de tabla. Las columnas las completamos con los respectivos datos que queremos mostrar y luego para completar las filas utilizamos un bucle "for" leyendo la lista de objetos pasada desde la vista y generando una nueva fila con cada iteración. ({% for proveedor in lista_de_proveedores %}). Para leer un dato hacemos referencia al objeto "proveedor" y luego a la propiedad con un punto (proveedor.nombre). En el caso del listado de productos, para mostrar la foto utilizamos una etiqueta <img> donde el src lo generamos con producto.foto.url que genera la ruta absoluta a la imagen.

20- Para el caso de las plantillas para crear proveedores (templates/proveedores/proveedores_create.html) y para crear productos (templates/productos/productos_create.html), también extienden de base.html, luego se define el bloque {% block content %}, para finalmente contar con un formulario y una tabla interna. Este formulario utiliza el método post para enviar la información y en el caso de "productos" se utiliza enctype="multipart/form-data" para permitir subir las imágenes con el formulario. Utilizar {% csrf_token %} dentro del formulario para agregar un token CSRF (Cross-Site Request Forgery) al formulario HTML y proteger de ataques.

### Configuración de las vistas

21- Las vistas (compra/views.py) se realizaron todas basadas en clases. Las ListView realizan primero una consulta a la base de datos para obtener todos los registros de la tabla asociada al modelo, luego se determina la plantilla y el nombre de la lista de objetos que se envía a esta plantilla. Para las CreateView se establece el modelo, los campos que se van a recibir, la plantilla y finalmente la url a la que redirige luego de la operación.

### Configuración del enrutamiento

22- Para configurar lo referido a rutas, definir la estructura de urls del sitio y su mapeo con las vistas se utilizan los archivos urls.py, ya que es el punto de entrada de las solicitudes. El primer urls.py en consultarse es el del proyecto y luego de ahí puede derivarse a otro urls.py específico de una app. Dentro de la lista urlpatterns se coloca cada una de las rutas que se desea asociar a una vista y se le asigna un nombre que luego puede referenciarse desde las plantillas.

### Determinar información disponible en /admin

23- Para determinar que modelos serán accesibles desde /admin se debe configurar en el archivo /compra/admin.py:
- admin.site.register(Proveedor)
- admin.site.register(Producto)

De esta forma podrá administrarse ambos modelos.

### Configuraciones adicionales para referenciar a static y media

24- Para manejar las rutas de manera dinámica tanto de "static" como de "media" deben realizarse las siguientes configuraciones:

En settings.py agregar al final:

STATIC_URL = 'static/'

STATICFILES_DIRS = [ BASE_DIR / 'static' ]

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'

En urls.py del proyecto agregar al final:

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

### Generar el archivo requirements.txt

25- Para generar este archivo desde la consola de comandos y dentro de la raíz del proyecto, ejecutar el siguiente comando:

pip freeze > requirements.txt

### Para ir subiendo los cambios de nuestro proyecto al repositorio remoto.

Para hacer los commit de los cambios y subirlos a nuestro repositorio, debemos seguir estos pasos:

- git add .
- git commit -m "Descripción de los cambios que se realizaron"
- git push origin main (Sube los cambios al repositorio remoto)