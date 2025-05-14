from django.urls import path
from .views import home, galeria, base, agregar_producto, listar_productos, registro, carrito, eliminar_producto, restar_producto, limpiar_carrito, listar_productos, agregar_productos
# Define the URL patterns for the ventas app    

urlpatterns = [
    path('', home, name='home'),
    path('galeria/', galeria, name='galeria'),
    path('base/', base, name='base'),
    path('agregar_productos/', agregar_productos, name='agregar_productos'),
    path('registro/', registro, name='registro'),
    path('carrito/', carrito, name='carrito'),
    path('agregar_producto/<int:producto_id>/', agregar_producto, name='agregar_producto'),
    path('listar_productos/', listar_productos, name='listar_productos'),
    path('eliminar_producto/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
]
