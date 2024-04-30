from django.db import models

# Create your models here.
class Proveedor(models.Model):
    """Clase que representa a los proveedores de los productos """
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.BigIntegerField()        # Para no preocuparnos si se escala con los números


class Producto(models.Model):
    """ Clase que representa a los productos """
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
