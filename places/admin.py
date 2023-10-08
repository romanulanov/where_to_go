from django.contrib import admin
from .models import Place, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    search_fields = ("title",)


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    inlines = [
        ImageInline,
    ]
