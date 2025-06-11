from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField('Rua', max_length=255)
    city = models.CharField('Cidade', max_length=100)
    state = models.CharField('Estado', max_length=100)
    postal_code = models.CharField('CEP', max_length=20)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return f"{self.street}, {self.city} - {self.state} {self.postal_code}"