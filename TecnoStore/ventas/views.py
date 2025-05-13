from django.urls import path
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#funcion para mostrar vistas
def home(request):
    return render(request, 'ventas/home.html')

def base(request):
    return render(request, 'ventas/base.html')

def galeria(request):
    return render(request, 'ventas/galeria.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'ventas/register.html', {'form': form})