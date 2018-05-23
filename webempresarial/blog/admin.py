from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','update')

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','update')
    list_display = ('title','autor','published','post_categories')
    ordering = ('autor','published')
    search_fields = ('title','content','autor__username','categories__name')
    date_hierarchy = 'published'
    list_filter = ('autor__username','categories__name')

    def post_categories(self, obj):

        return ", ".join(c.name for c in obj.categories.all().order_by('name'))
    post_categories.short_description = 'Categorias'

admin.site.register(Post, PostAdmin)
