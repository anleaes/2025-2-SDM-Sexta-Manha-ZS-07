from django.db import models
<<<<<<< HEAD
from artistas.models import Artista
from galerias.models import Galeria
# Create your models here.

class Obra(models.Model):
    titulo = models.CharField(max_length=150)
    localizacao = models.CharField(max_length=150)
    status = models.CharField(max_length=50)

    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='obras')
    galeria = models.ForeignKey(Galeria, on_delete=models.CASCADE, related_name='obras')

    class Meta:
        verbose_name = 'Obra'
        verbose_name_plural = 'Obras'
    def __str__(self):
        return self.titulo
=======

# Create your models here.
class Obra(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    localizacao = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Obra'
        verbose_name_plural = 'Obras'
        ordering =['id']
    def __str__(self):
        return f"{self.titulo} - {self.artista} - {self.status} - {self.localizacao}"

>>>>>>> origin/main
