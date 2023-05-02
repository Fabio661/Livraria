import factory

from django.contrib.auth.models import User
from produto.factories import ProdutoFactory

from .models import Ordem

class UsuarioFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('pystr')
    username = factory.Faker('pystr')
    
    class Meta:
        model = User

class OrdemFactory(factory.django.DjangoModelFactory):
    usuario = factory.SubFactory(UsuarioFactory)
    
    @factory.post_generation
    def produto(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for produto in extracted:
                self.produto.add(produto)
    
    class Meta:
        model = Ordem