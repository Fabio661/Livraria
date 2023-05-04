from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from produto.models import Produto
from produto.serializers.produto_serializer import ProdutoSerializer

class ProdutoViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()
    
    