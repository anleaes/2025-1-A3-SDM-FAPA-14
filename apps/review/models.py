from django.db import models
from client.models import Client
from hosting.models import Hosting

# Create your models here.
class Review(models.Model):
    rating = models.IntegerField('Avaliação', default=0)
    comment = models.TextField('Comentário', blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    hosting = models.ForeignKey(Hosting, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ['id']

    def __str__(self):
        return f"{self.client.name} - {self.rating} estrelas"