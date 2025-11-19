from django.db import models

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    tema = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()