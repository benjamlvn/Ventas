"""
URL configuration for TecnoStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ventas import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ventas.urls')),
    path('accounts/', include ('django.contrib.auth.urls')), 
     path('consumir-apis/', views.consumir_apis, name='consumir_apis'),
    path('seguridad/', views.seguridad, name='seguridad'),
    path('stock/', views.stock, name='stock'),
    path('productos/', views.productos, name='productos'),
    path('', include('ventas.urls')),
    path('', include('stock.urls')),  # ajusta si tu app se llama distinto
    path('admin/', admin.site.urls),
    path('', include('ventas.urls')),  # Aquí incluyes las urls de ventas
    

 # URL patterns for authentication

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
