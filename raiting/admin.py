
from django.contrib import admin
from .models import ContUs


class ContUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

admin.site.register(ContUs, ContUsAdmin)
