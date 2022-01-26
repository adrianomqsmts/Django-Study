from django.contrib import admin
from .models import *
from djrichtextfield.widgets import RichTextWidget

admin.site.register(Media)


class PlatformInstanceInline(admin.TabularInline):
    model = Platform
    raw_id_fields = ('media',)
    fields = (('name', 'year_release' ))


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['name', 'year_fundation']
    inlines = [PlatformInstanceInline]




@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ['name', 'year_release', 'memory', 'producer', 'media']
    filter_vertical = ('media',)


@admin.register(Game_Platform)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['game', 'platform', 'quantity', 'year_release', ]
