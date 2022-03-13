from django.contrib import admin
from .models import Province

class ProvinceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

admin.site.register(Province, ProvinceAdmin)