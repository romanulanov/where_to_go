from django.contrib import admin
from .models import Place, Image
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE
from django.db import models
import traceback


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ('title__title',)
    readonly_fields = ['get_preview']
    fields = ('place', 'img', 'get_preview')
    ordering = ['order']
    raw_id_fields = ('place',)

    def get_preview(self, obj):
        try:
            return mark_safe('<img src="{url}" width="{width}" height={height}\
                             />'.format(
                url=obj.img.url,
                width=200,
                height=200,
                )
            )
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
            return mark_safe('<img src="{url}" width="{width}" height={height}\
                             />'.format(
                url=obj.img.url,
                width=200,
                height=200,
            ))
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
