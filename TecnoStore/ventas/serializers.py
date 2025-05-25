from rest_framework import serializers
from .models import Producto, Carrito, Boleta, OrdenDespacho

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = '__all__'

class OrdenDespachoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenDespacho
        fields = '__all__'
