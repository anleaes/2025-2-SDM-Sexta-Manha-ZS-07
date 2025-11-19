from django.db import models

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    tema = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering =['id']

    def __str__(self):
        return f"{self.titulo} - {self.tema} - {self.data_inicio} to {self.data_fim}"