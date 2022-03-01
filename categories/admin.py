from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ('category_name', 'order')

admin.site.register(Category, CategoryAdmin)