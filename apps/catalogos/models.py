from django.db import models

# Create your models here.

class Catalogo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Catalogo'
        verbose_name_plural = 'Catalogos'
        ordering = ['id']

    def __str__(self):
        return f"{self.nome} - {self.descricao}"
