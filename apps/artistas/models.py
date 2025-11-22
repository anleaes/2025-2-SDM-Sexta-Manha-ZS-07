from django.db import models

# Create your models here.
class Artista(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    biografia = models.TextField()

    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'
    def __str__(self):
        return self.nome