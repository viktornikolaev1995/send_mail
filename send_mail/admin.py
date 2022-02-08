from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdminForm(admin.ModelAdmin):
    list_display = ("name", "email")

