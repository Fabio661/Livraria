from rest_framework import serializers

from ordem.models import Ordem
from produto.models import Produto
from produto.serializers.produto_serializer import ProdutoSerializer

class OrdemSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(required=False, many=True)
    produto_id = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all(), write_only=True, many=True)
    total = serializers.SerializerMethodField()
    
    def get_total(self, instance):
        total = sum([produto.preco for produto in instance.produto.all()])
        return total
    
    class Meta:
        model = Ordem
        fields = ['produto', 'total', 'usuario', 'produto_id']
        extra_kwargs = {'produto': {'required': False}}
        
    def create(self, validated_data):
        produto_data = validated_data.pop('produto_id')
        usuario_data = validated_data.pop('usuario')
        
        ordem = Ordem.objects.create(usuario=usuario_data)
        for produto in produto_data:
            ordem.produto.add(produto)
        
        return ordem