from django.urls import path, include
from rest_framework import routers

from produto import viewsets

router = routers.SimpleRouter()
router.register(r'produto', viewsets.ProdutoViewSet, basename='produto'),
router.register(r'categoria', viewsets.CategoriaViewSet, basename='categoria')

urlpatterns = [
    path('', include(router.urls))
]