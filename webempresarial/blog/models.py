from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Las Categorias'
        ordering = ['-created', ]

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha Publicacion', default=now)
    image = models.ImageField(verbose_name='La Imagen', upload_to='blogs', null=True, blank=True)
    autor = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category,verbose_name='Categorias', related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Las Entradas'
        ordering = ['-created', ]

    def __str__(self):
        return self.title

