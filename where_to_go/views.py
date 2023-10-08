from django.shortcuts import render
from geojson import Feature, Point, FeatureCollection
from django.template.response import TemplateResponse
from places.models import Place, Image
import json



places = Place.objects.all()

for id, place in enumerate(places):
    place_details = {}
    place_details["title"] = place.title
    place_details["description_short"] = place.description_short
    place_details["description_long"] = place.description_long
    place_details["coordinates"] = {}
    place_details["coordinates"]["lng"] = place.lon
    place_details["coordinates"]["lat"] = place.lat
    place_details["imgs"] = []
    images = Image.objects.filter(title__title__contains =place.title)
    for image in images:
      place_details["imgs"].append(f"{image.img.url}") 
    place_details_json = json.dumps(place_details)

    with open(f"static/places/{id}.json", "w") as file:
        file.write(place_details_json)

place_details = []
for id, place in enumerate(places):
    place_details.append(Feature(geometry=Point((place.lat, place.lon)), properties = {"title":place.title, "placeId":id, "detailsUrl":f"static/places/{id}.json"}))

place_details = FeatureCollection(place_details)  

data = {"dict": place_details}
def index(request):
    return TemplateResponse(request,  "index.html", context=data)