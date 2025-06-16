from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', null=False, blank=False)
    cell_phone = models.CharField('Telefone celular', max_length=20)
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    gender = models.CharField('Gênero', max_length=1, choices=GENDER_CHOICES)
    photo = models.ImageField('Foto', upload_to='clients/photos', null=True)
    doc = models.FileField('Documentos', upload_to='clients/docs', null=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

    def __str__(self):
        return self.name