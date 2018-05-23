from django.db import models

# Create your models here.

class Service(models.Model):

    title = models.CharField(max_length=200,verbose_name='Titulo')
    subtitle = models.CharField(max_length=200,verbose_name='Subtitulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='La Imagen', upload_to='services')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Los Servicios'
        ordering = ['-created', ]

    def __str__(self):
        return self.title
