from django.db import models
from client.models import Client

# Create your models here.
class Reservation(models.Model):
    checkin_date = models.DateField('Data de Check-in')
    checkout_date = models.DateField('Data de Check-out')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        'Status',
        default='PENDING',
        max_length=20,
        choices=[
            ('PENDING', 'Pendente'),
            ('CONFIRMED', 'Confirmado'),
            ('CANCELED', 'Cancelado'),
        ]
    )
    payment_method = models.CharField(
        'Método de Pagamento',
        default='CREDIT_CARD',
        max_length=30,
        choices=[
            ('CREDIT_CARD', 'Cartão de Crédito'),
            ('DEBIT_CARD', 'Cartão de Débito'),
            ('PIX', 'Pix'),
            ('PAYMENT_SLIP', 'Boleto')
        ]
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['id']

    def __str__(self):
        return "%s" % (self.client)