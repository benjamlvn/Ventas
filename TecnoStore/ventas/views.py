# Import necessary modules
from django.shortcuts import redirect, render
from .models import Producto
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate


#funcion para mostrar vistas

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos,
    }
    return render(request, 'ventas/home.html',data)

def base(request):
    return render(request, 'ventas/base.html')

def galeria(request):
    return render(request, 'ventas/galeria.html')

def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Producto Registrado")
        else:
            data ["form"] = formulario

    return render(request, 'ventas/producto/agregar.html',data)

def listar_productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }

    return render(request, 'ventas/producto/listar.html', data)
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, "Usuario Registrado")
            return redirect(to='home')
        else:
            data["form"] = formulario

    return render(request, 'registration/registro.html', data)
