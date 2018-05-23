from django.contrib import admin

# Register your models here.
from .models import Project

class AdminProject(admin.ModelAdmin):

    readonly_fields=('created','update')

    list_display = ('id','title','decription','image','created','update')

admin.site.register(Project, AdminProject)