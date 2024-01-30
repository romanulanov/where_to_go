from django.contrib import admin
from .models import Place, Image
from django.utils.safestring import mark_safe

import traceback
import sys
    

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    readonly_fields = ["get_preview"]
    fields = ("title", "img", "get_preview", "num")
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


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview']
    fields = ['img', 'title','get_preview','num']
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
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    inlines = [
        ImageInline,
    ]
