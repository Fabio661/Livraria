import json

from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from rest_framework.authtoken.models import Token

from django.urls import reverse

from produto.factories import CategoriaFactory, ProdutoFactory
from ordem.factories import UsuarioFactory
from produto.models import Produto

class TesteProdutoViewSet(APITestCase):
    client = APIClient()
    
    def setUp(self):
        
        self.user = UsuarioFactory()
    
        self.client.force_authenticate(user=self.user)
        token = Token.objects.create(user=self.user)
        token.save()
           
        self.produto = ProdutoFactory(
            titulo='controle',
            preco=200,
        )
        
    def teste_get_all_produto(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token' + token.key)
        response = self.client.get(
            reverse('produto-list', kwargs={'version': 'v1'})
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        produto_data = json.loads(response.content)
        
        self.assertEqual(produto_data['results'][0]['titulo'], self.produto.titulo)
        self.assertEqual(produto_data['results'][0]['preco'], self.produto.preco)
        self.assertEqual(produto_data['results'][0]['ativo'], self.produto.ativo)
        
    def test_create_produto(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token' + token.key)
        
        categoria = CategoriaFactory()
        data = json.dumps({
            'titulo': 'pc',
            'preco': 200,
            'categoria_id': [ categoria.id ]
        })    
        
        response = self.client.post(
            reverse('produto-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )
                
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        produto_criado = Produto.objects.get(titulo='pc')
        
        self.assertEquals(produto_criado.titulo, 'pc')
        self.assertEquals(produto_criado.preco, 200 )

