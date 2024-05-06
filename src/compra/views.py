from django.shortcuts import render
from django.views import generic
from .models import Proveedor, Producto
from django.views.generic.edit import CreateView

# Create your views here.

class ProveedoresListView(generic.ListView):            # Vista basada en clases para listar proveedores.
    queryset = Proveedor.objects.all()
    template_name = "proveedores/proveedores_list.html"
    context_object_name = 'lista_de_proveedores'

class ProveedoreCreateView(CreateView):
    model = Proveedor                                   # Vista basada en clases para crear un proveedor.
    fields = ['nombre', 'apellido', 'dni']              # Campos que se envían a la plantilla.
    template_name = "proveedores/proveedores_create.html"
    success_url = 'http://localhost:8000/compras/proveedores/crear/'

class ProductosListView(generic.ListView):              # Vista basada en clases para listar productos.
    queryset = Producto.objects.all()
    template_name = "productos/productos_list.html"
    context_object_name = 'lista_de_productos'

class ProductoCreateView(CreateView):                   # Vista basada en clases para crear un producto.
    model = Producto
    fields = ['nombre', 'precio', 'stock_actual', 'foto', 'proveedor']
    template_name = "productos/productos_create.html"
    success_url = 'http://localhost:8000/compras/productos/crear/'

def inicio(request):
    return render(request, 'inicio/inicio.html')