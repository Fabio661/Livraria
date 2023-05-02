from rest_framework.viewsets import ModelViewSet

from produto.models import Produto
from produto.serializers.produto_serializer import ProdutoSerializer

class ProdutoViewSet(ModelViewSet):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()
    
    