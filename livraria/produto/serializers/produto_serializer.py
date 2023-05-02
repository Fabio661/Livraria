from rest_framework import serializers

from produto.models import Produto, Categoria
from produto.serializers.categoria_serializer import CategoriaSerializer

class ProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(required=False, many=True)
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), write_only=True, many=True)
    
    class Meta:
        model = Produto
        fields = [
            'id',
            'titulo',
            'descricao',
            'preco',
            'ativo',
            'categoria',
            'categoria_id',
        ]
        
    def create(self, validated_data):
        categoria_data = validated_data.pop('categoria_id')
        
        produto = Produto.objects.create(**validated_data)
        for categoria in categoria_data:
            produto.categoria.add(categoria)
        
        return produto