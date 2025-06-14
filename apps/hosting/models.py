from django.db import models
from category.models import Category
from address.models import Address

# Create your models here.
class Hosting(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', max_length=100)
    daily_price = models.DecimalField('Preço diário', max_digits=10, decimal_places=2)
    is_available = models.BooleanField('Disponível')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Hospedagem'
        verbose_name_plural = 'Hospedagens'
        ordering = ['id']

    def __str__(self):
        return self.name