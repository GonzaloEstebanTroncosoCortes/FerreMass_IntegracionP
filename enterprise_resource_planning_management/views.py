from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer
from django.views import View

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDisponibleBodegaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Producto.objects.filter(stock__gt=0)  # Productos con stock mayor a cero
    serializer_class = ProductoSerializer

class ProductoNoDisponibleBodegaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Producto.objects.filter(stock=0)  # Productos con stock igual a cero
    serializer_class = ProductoSerializer

class ProductoDisponibleBodegaView(View):
    def get(self, request):
        productos = Producto.objects.filter(stock__gt=0)  # Productos con stock mayor a cero
        context = {
            'productos': productos
        }
        return render(request, 'enterprise_resource_planning_management/productos_disponibles_bodega.html', context)
        
class ProductoNoDisponibleBodegaView(View):
    def get(self, request):
        productos = Producto.objects.filter(stock=0)  # Productos con stock igual a cero
        context = {
            'productos': productos
        }
        return render(request, 'enterprise_resource_planning_management/productos_no_disponibles_bodega.html', context)