from django.urls import path
from .views import sincronizar_stock, enviar_stock

urlpatterns = [
    path('api/stock/', sincronizar_stock),
    path('api/stock/enviar/', enviar_stock),
]
