from django.views import generic
from .models import Proveedor, Producto
from django.views.generic.edit import CreateView

# Create your views here.

class ProveedoresListView(generic.ListView):            # Vista basada en clases para listar proveedores.
    queryset = Proveedor.objects.all()
    template_name = "proveedores/proveedores_list.html"
    context_object_name = 'lista_de_proveedores'

class ProductosListView(generic.ListView):              # Vista basada en clases para listar productos.
    queryset = Producto.objects.all()
    template_name = "productos/productos_list.html"
    context_object_name = 'lista_de_productos'