from django.contrib import admin
from .models import UserApp

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

admin.site.register(UserApp, UserAdmin)