from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('artwork', 'text')

admin.site.register(Review, ReviewAdmin)
