from django.db import models
<<<<<<< HEAD
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
=======

# Create your models here.
class Galeria(models.Model):
    name = models.CharField('Nome', max_length=50)
    endereco = models.CharField('Endereço', max_length=100)
    capacidade = models.IntegerField('Capacidade')
    
    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galerias'
        ordering =['id']

    def __str__(self):
        return f"{self.name} - {self.endereco} - {self.capacidade}"
>>>>>>> origin/main
