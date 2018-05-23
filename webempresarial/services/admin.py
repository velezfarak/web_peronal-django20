from django.contrib import admin
from .models import Service
from django.utils.safestring import mark_safe
# Register your models here.

class AdminService(admin.ModelAdmin):

    readonly_fields=('created','update')

    list_display = ('id','title','subtitle','get_image_tag','created','update')
    ordering = ('id','title','subtitle')
    def get_image_tag(self, obj):
            if obj.image:
                return mark_safe('<img src="%s" width="40" height="40" />' % obj.image.url)
            else:
                return ' '
    get_image_tag.short_description = 'Photo'
    #get_image_tag.allow_tags = True #redundant
    get_image_tag.admin_order_field = 'name'

admin.site.register(Service, AdminService)
