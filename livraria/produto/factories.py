import factory

from .models import Categoria, Produto

class CategoriaFactory(factory.django.DjangoModelFactory):
    titulo = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    descricao = factory.Faker('pystr')
    ativo = factory.Iterator([True, False])
    
    class Meta:
        model = Categoria
        
class ProdutoFactory(factory.django.DjangoModelFactory):
    preco = factory.Faker('pyint')
    categoria = factory.LazyAttribute(CategoriaFactory)
    titulo = factory.Faker('pystr')
    
    @factory.post_generation
    def categoria(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for categoria in extracted:
                self.categoria.add(categoria)
    
    class Meta:
        model = Produto