from os import path
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from geojson import Feature, Point, FeatureCollection
from django.template.response import TemplateResponse
from places.models import Place, Image


def places(request, place_id):
    place = get_object_or_404(Place.objects.all(), pk=place_id)
    place_details = dict()
    title_short = place.title[place.title.find("«") + 1: place.title.find("»")]
    place_details = {
                    "title" : title_short,
                    "description_short" : place.description_short,
                    "description_long" : place.description_long,
                    "coordinates": {"lng" : place.lon,
                                    "lat" : place.lat},
                    "imgs" : []
                    }
    images = Image.objects.filter(title__title__contains =place.title)
    for image in images:
      place_details["imgs"].append(f"{image.img.url}") 
    return JsonResponse(place_details, safe=False, json_dumps_params={'indent': 2, 'ensure_ascii': False})


def index(request):
    places = Place.objects.all()
    place_details = []
    for id, place in enumerate(places):
        title_short = place.title[place.title.find("«") + 1: place.title.find("»")]
        place_details.append(Feature
                                (
                                geometry=Point((place.lat, place.lon)), 
                                properties = {
                                    "title":title_short,
                                    "placeId": int(id+1),
                                    "detailsUrl": reverse('place-archive', kwargs={'place_id': int(id+1)})
                                }
                                )
                            )                                       
    
    place_details = FeatureCollection(place_details)
    return TemplateResponse(request, "index.html", context={"dict": place_details})
