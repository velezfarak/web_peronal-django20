from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    decription = models.TextField(verbose_name='Descripcion')
    image = models.ImageField(verbose_name='La Imagen', upload_to='projects')
    link = models.URLField(verbose_name='Direccion Web',blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de Creacion')
    update=models.DateTimeField(auto_now=True,verbose_name='Fecha de edicion')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Los Proyectos'
        ordering = ['-created',]

    def __str__(self):
        return self.title