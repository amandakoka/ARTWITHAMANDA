from django.contrib import admin
from .models import ContactMessage

# Register your models here.


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at',)


admin.site.register(ContactMessage, ContactMessageAdmin)
