from django.db import models

# Create your models here.

class Produto(models.Model):
  #models.tipoDeDados CharField("label", tamanho máximo)
  nome = models.CharField('Nome', max_length=100)
  #decimal_places = quantidade de casas decimais e max_digits é a quantidade de dígitos máximo
  preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
  estoque = models.IntegerField('Quantidade em estoque')
  #Apresenta o objeto instanciado pelo nome dele no admin
  def __str__(self):
    return self.nome