from django.db import models
from category.models import Category
from address.models import Address

# Create your models here.
class Hosting(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', max_length=100)
    daily_price = models.DecimalField('Preço diário', max_digits=10, decimal_places=2)
    is_available = models.BooleanField('Disponível')
    photo = models.ImageField('Foto', upload_to='hosting/photos', null=True)
    doc = models.FileField('Documentos', upload_to='hosting/docs', null=True)
    category = models.ForeignKey(Category, verbose_name='Categoria', on_delete=models.CASCADE, null=True)
    address = models.OneToOneField(Address, verbose_name='Endereço', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Hospedagem'
        verbose_name_plural = 'Hospedagens'
        ordering = ['id']

    def __str__(self):
        return self.name