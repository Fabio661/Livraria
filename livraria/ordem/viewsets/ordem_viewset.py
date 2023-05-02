from rest_framework.viewsets import ModelViewSet

from ordem.serializers import OrdemSerializer
from ordem.models import Ordem

class OrdemViewSet(ModelViewSet):
    serializer_class = OrdemSerializer
    queryset = Ordem.objects.all()