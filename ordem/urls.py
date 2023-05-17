from django.urls import path, include
from rest_framework import routers

from ordem import viewsets

router = routers.SimpleRouter()
router.register(r'ordem', viewsets.OrdemViewSet, basename='ordem')

urlpatterns = [
    path('', include(router.urls))
]
