from django.contrib import admin
from .models import Perfil
# Register your models here.
class AdminPerfil(admin.ModelAdmin):
    list_display = ('id','avatar','bio','link')

admin.site.register(Perfil, AdminPerfil)    