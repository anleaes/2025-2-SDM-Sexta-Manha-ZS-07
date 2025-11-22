from django.db import models

# Create your models here.
class Museu(models.Model):
<<<<<<< HEAD
    nome = models.CharField(max_length=200)
    local = models.CharField(max_length=200)
    horario_funcionamento = models.CharField(max_length=100)
=======
    name = models.CharField('Nome', max_length=50)
    local = models.CharField('Local', max_length=100)
    horario = models.CharField('Horário de Funcionamento', max_length=100)
>>>>>>> origin/main

    class Meta:
        verbose_name = 'Museu'
        verbose_name_plural = 'Museus'
<<<<<<< HEAD
    def __str__(self):
        return self.nome
=======
        ordering =['id']

    def __str__(self):
        return f"{self.name} - {self.local}"
>>>>>>> origin/main
