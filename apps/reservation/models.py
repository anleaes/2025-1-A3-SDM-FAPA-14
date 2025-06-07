from django.db import models

# Create your models here.
class Reservation(models.Model):
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField('Status')

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['id']

    def __str__(self):
        return self.name