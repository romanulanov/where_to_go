import traceback

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE

from .models import Place, Image


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ('title__title',)
    readonly_fields = ['get_preview']
    fields = ('place', 'img', 'get_preview')
    ordering = ['order']
    raw_id_fields = ('place',)

    def get_preview(self, obj):
        try:
            return format_html(
                '<img src="{}" style="max-width:200px; max-height:200px;" />',
                obj.img.url)
        except Exception:
            print(traceback.format_exc())


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview']
    fields = ['img', 'place', 'get_preview', 'order']
    ordering = ['order']
    sortable_field_name = 'order'

    def get_preview(self, obj):
        try:
            return format_html(
                '<img src="{}" style="max-width:200px; max-height:200px;" />',
                obj.img.url)
        except Exception as e:
            print(e)


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin,  admin.ModelAdmin):
    search_fields = ("title",)
    inlines = [ImageInline]
    ordering = ['id']
    content = HTMLField()
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
