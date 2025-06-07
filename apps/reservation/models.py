from django.db import models
from client.models import Client

# Create your models here.
class Reservation(models.Model):
    checkin_date = models.DateField('Data de Check-in')
    checkout_date = models.DateField('Data de Check-out')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField('Status')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['id']

    def __str__(self):
        return self.name