from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from .views import ProductoDisponibleBodegaView, CategoriaViewSet, ProductoViewSet, ProductoNoDisponibleBodegaViewSet

router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'productos_disponibles_bodega', views.ProductoDisponibleBodegaViewSet)
router.register(r'productos_no_disponibles_bodega', views.ProductoNoDisponibleBodegaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('productos_disponibles_bodega/', ProductoDisponibleBodegaView.as_view(), name='productos_disponibles_bodega')
]
