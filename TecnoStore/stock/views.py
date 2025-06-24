from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer
from .externo import obtener_stock_externo, enviar_stock_externo



@api_view(['GET'])
def sincronizar_stock(request):
    externos = obtener_stock_externo()
    productos_guardados = []
    for item in externos:
        producto, _ = Producto.objects.update_or_create(
            sku=item['sku'],
            defaults={'nombre': item['nombre'], 'cantidad': item['cantidad']}
        )
        productos_guardados.append(producto)
    serializer = ProductoSerializer(productos_guardados, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def enviar_stock(request):
    producto_data = request.data
    result = enviar_stock_externo(producto_data)
    Producto.objects.update_or_create(
        sku=producto_data['sku'],
        defaults={
            'nombre': producto_data.get('nombre', ''),
            'cantidad': producto_data['cantidad']
        }
    )
    return Response(result)
