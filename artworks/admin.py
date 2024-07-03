from django.contrib import admin
from .models import Category, Artwork


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)


class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'image')
    ordering = ('name',)
    search_fields = ('name', 'description')
    list_filter = ('category', 'price')

admin.site.register(Artwork, ArtworkAdmin)