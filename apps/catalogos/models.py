from django.db import models
<<<<<<< HEAD
from obras.models import Obra
from eventos.models import Evento
from galerias.models import Galeria
# Create your models here.
class Catalogo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    obras = models.ManyToManyField(Obra, related_name='catalogos', blank=True)
    eventos = models.ManyToManyField(Evento, related_name='catalogos', blank=True)
    galerias = models.ManyToManyField(Galeria, related_name='catalogos', blank=True)

    class Meta:
        verbose_name = 'Catálogo'
        verbose_name_plural = 'Catálogos'
    def __str__(self):
        return self.nome
=======

# Create your models here.

class Catalogo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Catalogo'
        verbose_name_plural = 'Catalogos'
        ordering = ['id']

    def __str__(self):
        return f"{self.nome} - {self.descricao}"
>>>>>>> origin/main
