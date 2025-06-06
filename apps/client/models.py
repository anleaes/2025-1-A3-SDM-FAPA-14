from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

    def __str__(self):
        return self.name