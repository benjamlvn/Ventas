from django.urls import path
from django.shortcuts import render

#funcion para mostrar vistas
def home(request):
    return render(request, 'ventas/home.html')