from django.db import models

# Create your models here.
class Museu(models.Model):
    name = models.CharField('Nome', max_length=50)
    local = models.CharField('Local', max_length=100)
    horario = models.CharField('Horário de Funcionamento', max_length=100)

    class Meta:
        verbose_name = 'Museu'
        verbose_name_plural = 'Museus'
        ordering =['id']

    def __str__(self):
        return f"{self.name} - {self.local}"