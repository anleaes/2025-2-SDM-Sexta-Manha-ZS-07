from django.db import models

# Create your models here.
class Reserva(models.Model):
    status = models.CharField(max_length=50)
    qtd_pessoas = models.IntegerField()
    data = models.DateField()
    
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering =['id']

    def __str__(self):
        return f"{self.status} - {self.qtd_pessoas} - {self.data}"
