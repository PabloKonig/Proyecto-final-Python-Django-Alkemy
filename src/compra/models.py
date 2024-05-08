from django.db import models

# Create your models here.
class Proveedor(models.Model):          
    """Clase que representa a los proveedores de los productos """
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.BigIntegerField()        # Para no preocuparnos si se escala con los números

    def __str__(self):   #Método especial que devuelve una representación String de la instancia de la clase.
        return F"Nombre: {self.nombre.upper()} - Apellido: {self.apellido.upper()} - DNI: {self.dni}"

class Producto(models.Model):           
    """ Clase que representa a los productos """
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    foto = models.ImageField(upload_to='productos_img/', default='producto_default.png')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)  #No permite eliminar un proveedor si no se eliminan o modifican los productos que lo referencian.

    def __str__(self):
        return F"Nombre: {self.nombre.upper()} - Precio: {self.precio} - Stock: {self.stock_actual} - Proveedor: {self.proveedor.nombre} {self.proveedor.apellido}"
    
    