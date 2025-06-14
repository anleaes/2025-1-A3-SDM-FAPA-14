from django.db import models
from reservation.models import Reservation
from hosting.models import Hosting

# Create your models here.
class ReservationHosting(models.Model):
    quantity_days = models.IntegerField('Quantidade de dias')
    unit_price = models.DecimalField('Preço unitário', max_digits=10, decimal_places=2)
    reservation = models.ForeignKey(Reservation, verbose_name='Reserva', on_delete=models.CASCADE, null=True)
    hosting = models.ForeignKey(Hosting, verbose_name='Hospedagem', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Reserva de Hospedagem'
        verbose_name_plural = 'Reservas de Hospedagem'
        ordering = ['id']

    def __str__(self):
        return f"{self.quantity_days} dia(s) - {self.hosting.name}"