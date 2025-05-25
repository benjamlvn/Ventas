# Import necessary modules
from django.shortcuts import redirect, render, get_object_or_404
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

#Producotps 
def agregar_productos(request):
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

# listar
def listar_productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }

    return render(request, 'ventas/producto/listar.html', data)

def modificar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        else:
            data["form"] = formulario
    
    return render(request, 'ventas/producto/modificar.html', data)

def eliminar_edicion(request, producto_id):   
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect(to="listar_productos")
from django.shortcuts import render
import requests

def consumir_apis(request):
    # Ejemplo simple de consumo de API externa
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = response.json() if response.status_code == 200 else []
    return render(request, 'api_result.html', {'data': data})

def seguridad(request):
    return render(request, 'seguridad.html')

def stock(request):
    return render(request, 'stock.html')

def productos(request):
    return render(request, 'productos.html')

    
