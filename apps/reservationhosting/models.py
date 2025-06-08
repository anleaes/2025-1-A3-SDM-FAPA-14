from django.db import models

# Create your models here.
class ReservationHosting(models.Model):
    quantity_days = models.IntegerField('Quantidade de dias')
    unit_price = models.DecimalField('Preço unitário', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Reserva de Hospedagem'
        verbose_name_plural = 'Reservas de Hospedagem'
        ordering = ['id']

    def __str__(self):
        return self.name