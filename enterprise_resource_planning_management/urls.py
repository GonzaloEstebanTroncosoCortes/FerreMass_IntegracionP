from django.urls import path
from .views import ProductoDisponibleBodegaView, ProductoNoDisponibleBodegaView

urlpatterns = [
    path('productos_disponibles_bodega/', ProductoDisponibleBodegaView.as_view(), name='productos_disponibles_bodega'),
    path('productos_no_disponibles_bodega/', ProductoNoDisponibleBodegaView.as_view(), name='productos_no_disponibles_bodega'),
]
