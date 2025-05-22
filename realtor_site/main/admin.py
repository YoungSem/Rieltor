from django.contrib import admin

from .models import Jk

@admin.register(Jk)
class JkAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'description')
    search_fields = ('name', 'area')
    list_filter = ('area',)
