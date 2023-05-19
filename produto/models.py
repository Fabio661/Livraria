from django.db import models

# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    descricao = models.CharField(max_length=200, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo
    
class Produto(models.Model):
    titulo = models.CharField(max_length=120)
    descricao = models.TextField(max_length=500, blank=True, null=True)
    preco = models.PositiveIntegerField(null=True)
    ativo = models.BooleanField(default=True)
    categoria = models.ManyToManyField(Categoria, blank=True)

    def __str__(self):
        return self.titulo