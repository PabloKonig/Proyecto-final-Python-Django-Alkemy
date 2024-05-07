from django.contrib import admin
from .models import Proveedor, Producto

# Register your models here.
admin.site.register(Proveedor)   # Se configura para que se pueda administrar el modelo Proveedor desde /admin
admin.site.register(Producto)    # Se configura para que se pueda administrar el modelo Producto desde /admin