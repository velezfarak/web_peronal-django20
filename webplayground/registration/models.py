from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
def custon_upload_to(instance, filename):
    old_instance = Perfil.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'perfil/'+filename

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to=custon_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

@receiver(post_save, sender=User)
def ensure_perfil_exists(sender, instance, **kwargs):
    if kwargs.get('created',False):
        Perfil.objects.get_or_create(user=instance)
        # print('se acaba de crear un usuario y su perfil')    