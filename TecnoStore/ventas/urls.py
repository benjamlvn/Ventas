from django.urls import path
from .views import home, galeria, base
# Define the URL patterns for the ventas app    

urlpatterns = [
    path('', home, name='home'),
    path('galeria/', galeria, name='galeria'),
    path('base/', base, name='base'),
    
]
