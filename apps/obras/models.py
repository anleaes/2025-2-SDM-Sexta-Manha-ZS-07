from django.db import models

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

