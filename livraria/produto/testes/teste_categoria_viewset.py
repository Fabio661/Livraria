import json

from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from django.urls import reverse

from produto.factories import CategoriaFactory
from produto.models import Categoria

class TesteCategoriaViewSet(APITestCase):
    
    def setUp(self):
        
        self.client = APIClient()     
        self.categoria = CategoriaFactory(titulo='livros')   
             
    def teste_get_all_categoria(self):
        response = self.client.get(
            reverse('categoria-list', kwargs={'version': 'v1'})
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        categoria_data = json.loads(response.content)
        
        self.assertEqual(categoria_data[0]['titulo'], self.categoria.titulo)
        
    def test_create_categoria(self):
        data = json.dumps({
            'titulo': 'tecnologia',
        })    
        
        response = self.client.post(
            reverse('categoria-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )
                
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        categoria_criada = Categoria.objects.get(titulo='tecnologia')
        
        self.assertEquals(categoria_criada.titulo, 'tecnologia')

