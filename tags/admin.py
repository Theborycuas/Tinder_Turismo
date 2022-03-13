from django.contrib import admin
from .models import Tag

class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

admin.site.register(Tag, TagAdmin)
