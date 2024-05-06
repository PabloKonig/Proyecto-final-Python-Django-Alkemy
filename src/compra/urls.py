from django.urls import path
from .views import ProveedoresListView, ProductosListView, ProductoCreateView, ProveedoreCreateView, inicio

app_name = 'compra'
# Se definen las sub-rutas de la app y su conexión con las vistas.
urlpatterns = [
    path('proveedores/listado/', ProveedoresListView.as_view(), name='proveedores_list'),
    path('productos/listado/', ProductosListView.as_view(), name='productos_list'),
    path('productos/crear/', ProductoCreateView.as_view(), name='productos_create'),
    path('proveedores/crear/', ProveedoreCreateView.as_view(), name='proveedores_create'),
    path('', inicio, name='inicio')    
]
