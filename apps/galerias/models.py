from django.db import models
from museus.models import Museu
# Create your models here.

class Galeria(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=150)
    capacidade = models.IntegerField()

    museu = models.ForeignKey(Museu, on_delete=models.CASCADE, related_name='galerias')

    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galerias'
    def __str__(self):
        return self.nome
