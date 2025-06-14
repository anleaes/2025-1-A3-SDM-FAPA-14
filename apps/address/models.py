from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField('Rua', max_length=200)
    number = models.CharField('Número', max_length=10)
    city = models.CharField('Cidade', max_length=100)
    state = models.CharField('Estado', max_length=2)
    postal_code = models.CharField('CEP', max_length=10)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['id']

    def __str__(self):
        return f"{self.street}, {self.number} - {self.city}/{self.state}"