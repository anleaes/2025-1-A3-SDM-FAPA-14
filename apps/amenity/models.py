from django.db import models

# Create your models here.
class Amenity(models.Model):
    name = models.CharField('Nome', max_length=100, unique=True)
    description = models.TextField('Descrição', max_length=100)
    is_available = models.BooleanField('Disponível', default=True)
    extra_cost = models.DecimalField('Custo Extra', max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Comodidade'
        verbose_name_plural = 'Comodidades'
        ordering = ['id']

    def __str__(self):
        return self.name