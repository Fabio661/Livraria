import json

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from django.urls import reverse

from produto.factories import CategoriaFactory, ProdutoFactory
from ordem.factories import UsuarioFactory, OrdemFactory
from produto.models import Produto
from ordem.models import Ordem

class TesteOrdemViewSet(APITestCase):
    
    client = APIClient()
    
    def setUp(self):
        self.user = UsuarioFactory()
        self.client.force_authenticate(user=self.user)
        
        self.categoria = CategoriaFactory(titulo='tecnologia')
        self.produto = ProdutoFactory(titulo='mouse', preco=100, categoria=[self.categoria])
        self.ordem = OrdemFactory(produto=[self.produto])
        
    def teste_ordem(self):
        response = self.client.get(
            reverse('ordem-list', kwargs={'version': 'v1'})
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        ordem_data = json.loads(response.content)
        self.assertEqual(ordem_data['results'][0]['produto'][0]['titulo'], self.produto.titulo)
        self.assertEqual(ordem_data['results'][0]['produto'][0]['preco'], self.produto.preco)
        self.assertEqual(ordem_data['results'][0]['produto'][0]['ativo'], self.produto.ativo)
        self.assertEqual(ordem_data['results'][0]['produto'][0]['categoria'][0]['titulo'], self.categoria.titulo)
        
    def teste_create_ordem(self):
        usuario = UsuarioFactory()
        produto = ProdutoFactory()
        data = json.dumps({
            'produto_id': [produto.id],
            'usuario': usuario.id
        })
        
        response = self.client.post(
            reverse('ordem-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )           
        
   
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        created_ordem = Ordem.objects.get(usuario=usuario)