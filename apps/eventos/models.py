from django.db import models
from museus.models import Museu
from obras.models import Obra
# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=150)
    dataInicio = models.DateField()
    dataFim = models.DateField()
    tema = models.CharField(max_length=100)

    museu = models.ForeignKey(Museu, on_delete=models.CASCADE, related_name='eventos')
    obras = models.ManyToManyField(Obra, related_name='eventos', blank=True)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
    def __str__(self):
        return self.titulo