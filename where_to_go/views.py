from os import path
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from geojson import Feature, Point, FeatureCollection
from django.template.response import TemplateResponse
from places.models import Place, Image
import json


places_details = []
places = Place.objects.all()
for id, place in enumerate(places):
    place_details = dict()
    title_short = place.title[place.title.find("«") + 1: place.title.find("»")]
    place_details["title"] = title_short
    place_details["description_short"] = place.description_short
    place_details["description_long"] = place.description_long
    place_details["coordinates"] = {}
    place_details["coordinates"]["lng"] = place.lon
    place_details["coordinates"]["lat"] = place.lat
    place_details["imgs"] = []
    images = Image.objects.filter(title__title__contains =place.title)
    for image in images:
        place_details["imgs"].append(f"{image.img.url}") 
    place_details_json = json.dumps(places_details)
   


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


def get_GeoJSON(request):
    places = Place.objects.all()
    place_details = []
    for id, place in enumerate(places):
        title_short = place.title[place.title.find("«") + 1: place.title.find("»")]
        place_details.append(Feature(geometry=Point((place.lat, place.lon)), 
                                    properties = {"title":title_short,
                                                "placeId":id,
                                                "detailsUrl": reverse('place-archive', kwargs={'place_id':id})
                                                }
                                                ))                                       
    place_details = FeatureCollection(place_details)
    return place_details


def index(request):
    data = {"dict": get_GeoJSON}
    return TemplateResponse(request,  "index.html", context=data)
