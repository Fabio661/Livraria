from django.db import models
from django.contrib.auth.models import User
from produto.models import Produto

# Create your models here.

class Ordem(models.Model):
    produto = models.ManyToManyField(Produto, blank=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)