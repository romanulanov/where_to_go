from django.contrib import admin
from .models import Place, Coordinate




@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ("title",)
 
@admin.register(Coordinate)
class CoordinateAdmin(admin.ModelAdmin):
    pass