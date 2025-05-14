from django.urls import path
from .views import home, galeria, base, agregar_producto, listar_productos, registro
# Define the URL patterns for the ventas app    

urlpatterns = [
    path('', home, name='home'),
    path('galeria/', galeria, name='galeria'),
    path('base/', base, name='base'),
    path('agregar_producto/', agregar_producto, name='agregar'),
    path('listar_productos/', listar_productos, name='listar_productos'),
    path('registro/', registro, name='registro'),
]
