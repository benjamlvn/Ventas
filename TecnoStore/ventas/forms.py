from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'
    
class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario", max_length=100)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

class RegistroForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    familyName = forms.CharField(max_length=100)
class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario", max_length=100)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)