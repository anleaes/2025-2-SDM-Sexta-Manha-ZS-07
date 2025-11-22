from django.db import models

# Create your models here.
class Museu(models.Model):

    nome = models.CharField(max_length=200)
    local = models.CharField(max_length=200)
    horario_funcionamento = models.CharField(max_length=100)


    class Meta:
        verbose_name = 'Museu'
        verbose_name_plural = 'Museus'

    def __str__(self):
        return self.nome

