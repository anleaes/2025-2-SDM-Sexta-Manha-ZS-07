from django.db import models

# Create your models here.
class Galeria(models.Model):
    name = models.CharField('Nome', max_length=50)
    endereco = models.CharField('Endereço', max_length=100)
    capacidade = models.IntegerField('Capacidade')
    
    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galerias'
        ordering =['id']

    def __str__(self):
        return f"{self.name} - {self.endereco} - {self.capacidade}"
