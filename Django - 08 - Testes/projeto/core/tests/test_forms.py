from django.test import TestCase
from model_mommy import mommy
from ..forms import *

class ContatoFormTestCase(TestCase):

    def setUp(self) -> None:
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
        
        self.form = ContatoForm(data=self.dados)
        
    def test_send_mail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_email()
        
        form2 = self.form
        form2.is_valid()
        res2 = form2.send_email()
        
        self.assertEquals(res1, res2)