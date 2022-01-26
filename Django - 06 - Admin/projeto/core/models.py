from re import T
from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class Producer(models.Model):
    name = models.CharField('Nome', max_length=45)
    year_fundation = models.IntegerField('Ano da Fundação', validators=[
                                         MinValueValidator(1000), MaxValueValidator(9999)])

    def __str__(self):
        return f'{self.name}'


class Media(models.Model):
    name = models.CharField('Mídia', max_length=45)
    speed = models.IntegerField(
        name="Velocidade de Leitura", validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.name}'


class Platform(models.Model):
    name = models.CharField('Plataforma', max_length=45)
    year_release = models.IntegerField('Ano de Lançamento',  validators=[
                                       MinValueValidator(1000), MaxValueValidator(9999)])
    memory = models.IntegerField("Memória", validators=[
                                 MinValueValidator(0), MaxValueValidator(9999)])
    producer = models.ForeignKey(
        Producer, verbose_name="Produtora", on_delete=models.CASCADE)

    media = models.ManyToManyField(Media, verbose_name="Mídia")

    def __str__(self):
        return f'{self.name}|{self.year_release}'


class Game(models.Model):
    name = models.CharField('Jogo', max_length=100)
    description = models.TextField("Descrição", max_length=500)
    platform = models.ManyToManyField(
        Platform, verbose_name=("Plataforma"), through='Game_Platform')

    def __str__(self):
        return f'{self.name}'


class Game_Platform(models.Model):
    game = models.ForeignKey(Game, verbose_name=(
        "Jogo"), on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, verbose_name=(
        "Plataforma"), on_delete=models.CASCADE)
    quantity = models.IntegerField('Quantidade', validators=[
                                   MinValueValidator(0), MaxValueValidator(9999)])
    year_release = models.IntegerField('Ano de Lançamento',  validators=[
                                       MinValueValidator(1000), MaxValueValidator(9999)])

    def __str__(self):
        return f'{self.game}|{self.platform}'
