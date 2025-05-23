from django.contrib import admin
from .models import Jk, House, Flat, Jk_media, House_media, Flat_media, Application

class JkMediaInline(admin.TabularInline):
    model = Jk_media
    extra = 1

class HouseMediaInline(admin.TabularInline):
    model = House_media
    extra = 1

class FlatMediaInline(admin.TabularInline):
    model = Flat_media
    extra = 1

@admin.register(Jk)
class JkAdmin(admin.ModelAdmin):
    inlines = [JkMediaInline]

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    inlines = [HouseMediaInline]

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    inlines = [FlatMediaInline]

admin.site.register(Jk_media)
admin.site.register(House_media)
admin.site.register(Flat_media)
admin.site.register(Application)
