from django.test import TestCase
import uuid
from model_mommy import mommy
from ..models import *

class GetFilePathTestCase(TestCase):

    def setUp(self) -> None:
        self.filename = f'{uuid.uuid4()}.png'
        
    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))
        
class ServicoTestCase(TestCase):
    
    def setUp(self) -> None:
        self.servico = mommy.make('Servico')
        
    def test_str(self) :
        self.assertEquals(str(self.servico), self.servico.servico)
        
class CargoTestCase(TestCase):
    
    def setUp(self) -> None:
        self.cargo = mommy.make('Cargo')
        
    def test_str(self) :
        self.assertEquals(str(self.cargo), self.cargo.cargo)
        
class FuncionarioTestCase(TestCase):
    
    def setUp(self) -> None:
        self.funcionario = mommy.make('Funcionario')
        
    def test_str(self) :
        self.assertEquals(str(self.funcionario), self.funcionario.nome)