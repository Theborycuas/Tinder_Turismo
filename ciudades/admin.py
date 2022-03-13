from django.contrib import admin
from .models import City

class CityAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

admin.site.register(City, CityAdmin)