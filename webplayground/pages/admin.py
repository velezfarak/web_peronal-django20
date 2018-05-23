from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

    class Meta:
        css = {
            'all':('pages/css/custom_ckeditor',)
        }

admin.site.register(Page, PageAdmin)
