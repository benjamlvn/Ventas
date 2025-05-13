from django.urls import path
from .views import home, galeria, base
from django.contrib.auth import views as auth_views
from . import views
# Define the URL patterns for the ventas app    

urlpatterns = [
    path('', home, name='home'),
    path('galeria/', galeria, name='galeria'),
    path('base/', base, name='base'),
    path('login/', auth_views.LoginView.as_view(template_name='ventas/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
    
]
