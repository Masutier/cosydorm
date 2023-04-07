from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'institute', 'address1', 'address2', 'city', 'zip')


admin.site.register(Profile, ProfileAdmin)
