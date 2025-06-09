from django.db import models

# Create your models here.
class Review(models.Model):
    rating = models.IntegerField('Avaliação', default=0)
    comment = models.TextField('Comentário', blank=True, null=True)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    def __str__(self):
        return self.name