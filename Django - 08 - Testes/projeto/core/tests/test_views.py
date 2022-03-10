from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):
    
    def setUp(self):
        self.nome = 'Nome'
        self.email = 'email@email.com'
        self.assunto = 'Assunto'
        self.mensagem = 'Mensagem'
        
        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem,
        }
        
        self.dados2 = {
            'nome': self.nome,
            'assunto': self.assunto,
        }

        self.cliente = Client()
        
    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302) # redirect
        
        
    def test_form_invalid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados2)
        self.assertEquals(request.status_code, 200) # invalido