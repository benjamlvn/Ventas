from django.db import models
from collections import UserList
from django.contrib.auth.models import User
# Create your models here.c
class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

##modelo del carrito
class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    elementos = models.ManyToManyField(Producto, through='ElementoCarrito')

    def __str__(self):
        return f"Carrito de {self.usuario.username}"    
    



class ElementoCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Elemento del carrito {self.carrito} - Producto: {self.producto} - Cantidad: {self.cantidad}"
    
    
    def subtotal(self):
        return self.producto.precio * self.cantidad
    

