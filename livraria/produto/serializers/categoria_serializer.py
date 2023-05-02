from rest_framework import serializers

from produto.models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = [
            'titulo',
            'slug',
            'descricao',
            'ativo',
        ]
        extra_kwargs = {'slug': {'required': False}}