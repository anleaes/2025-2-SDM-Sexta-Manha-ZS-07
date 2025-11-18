from django.db import models

# Create your models here.
class Artista(models.Model):
    name = models.CharField('Nome', max_length=50)
    nacionalidade = models.CharField('Nacionalidade', max_length=30)
    biografia = models.CharField('Biografia', max_length=500)
    
    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'
        ordering =['id']

    def __str__(self):
        return f"{self.name} - {self.nacionalidade} - {self.biografia}"
