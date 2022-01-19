from django.contrib import admin

from .models import sites, score, persons


@admin.register(persons)
class personsAdmin(admin.ModelAdmin):
    list_display = ('id', "recorder", 'email', 'telefono',)
    list_display_links = ('recorder', 'email', 'telefono',)
    search_fields = ('recorder',)


@admin.register(sites)
class sitesAdmin(admin.ModelAdmin):
    list_display = ('daterecord', 'schedule', 'ubicacion', 'descripcion',)
    list_display_links = ('daterecord', 'schedule', 'ubicacion', 'descripcion')
    search_fields = ('daterecord', 'schedule', 'ubicacion', 'descripcion')


@admin.register(score)
class scoreAdmin(admin.ModelAdmin):
    list_display = ("recorder", 'site',)
    list_display_links = ("recorder",)
    raw_id_fields = ('recorder', 'site',)
    search_fields = ("recorder",)

# Register your models here.
