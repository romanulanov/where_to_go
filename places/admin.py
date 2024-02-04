from django.contrib import admin
from .models import Place, Image
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminBase, SortableAdminMixin, SortableInlineAdminMixin


import traceback
import sys
    

@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ("title",)
    readonly_fields = ["get_preview"]
    fields = ("title", "img", "get_preview", "num")
    ordering = ['num']
    def get_preview(self, obj):
        try:
            return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url = obj.img.url,
                width=200,
                height=200,
                )
            )
        except Exception:
            print(traceback.format_exc())


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview']
    fields = ['img', 'title','get_preview','num']
    ordering = ['num']
    sortable_field_name = 'num'

    def get_preview(self, obj):
        try:
            return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
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
    
  
        
