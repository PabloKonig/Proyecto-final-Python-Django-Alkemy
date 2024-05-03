from django.urls import path
from .views import ProveedoresListView, ProductosListView

app_name = 'compra'
# Se definen las sub-rutas de la app y su conexión con las vistas.
urlpatterns = [
    path('proveedores/listado/', ProveedoresListView.as_view(), name='proveedores_list'),
    path('productos/listado/', ProductosListView.as_view(), name='productos_list'),    
]
