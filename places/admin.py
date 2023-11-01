from django.contrib import admin
from .models import Place, Image
from django.utils.safestring import mark_safe


    

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    readonly_fields = ["headshot_image"]
    
    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.headshot.url,
            width=obj.headshot.width,
            height=obj.headshot.height,
            )
    )


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    inlines = [
        ImageInline,
    ]
