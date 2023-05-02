from rest_framework.viewsets import ModelViewSet

from produto.serializers import CategoriaSerializer
from produto.models import Categoria

class CategoriaViewSet(ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
    
    