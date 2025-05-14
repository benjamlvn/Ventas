from django.urls import path
from .views import home, galeria, base, listar_productos, registro, modificar_producto, eliminar_edicion, agregar_productos
# Define the URL patterns for the ventas app    

urlpatterns = [
    path('', home, name='home'),
    path('galeria/', galeria, name='galeria'),
    path('base/', base, name='base'),
    path('registro/', registro, name='registro'),
    path('agregar_productos/', agregar_productos, name='agregar_productos'),
    path('listar_productos/', listar_productos, name='listar_productos'),
    path('modificar_producto/<int:producto_id>/', modificar_producto, name='modificar_producto'),
    path('eliminar_edicion/<int:producto_id>/', eliminar_edicion, name='eliminar_edicion'),
    
]
