from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField()
    city = models.CharField()
    state = models.CharField()
    postal_code = models.CharField()

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.name