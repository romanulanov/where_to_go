from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from geojson import Feature, Point, FeatureCollection
from django.template.response import TemplateResponse
from places.models import Place, Image


def places(request, place_id):
    place = get_object_or_404(Place.objects.all(), pk=place_id)
    place_details = {
                    "title": place.title,
                    "short_description": place.short_description,
                    "long_description": place.long_description,
                    "coordinates": {"lng": place.lon,
                                    "lat": place.lat},
                    "imgs": []
                    }
    images = place.images.all()
    images = place.images.all()

    image_urls = [image.img.url for image in images]
    place_details["imgs"] = image_urls
    
    return JsonResponse(
        place_details,
        safe=False,
        json_dumps_params={
                           'indent': 2,
                           'ensure_ascii': False
                           }
                        )


def index(request):
    places = Place.objects.all()
    place_details = []
    for id, place in enumerate(places, start=1):
        title_short = place.title
        place_details.append(Feature
                             (geometry=Point((place.lat, place.lon)),
                                 properties={
                                    "title": title_short,
                                    "placeId": id,
                                    "detailsUrl": reverse(
                                        'place-archive',
                                        kwargs={'place_id': id}
                                                )
                                    }
                              )
                             )

    place_details = FeatureCollection(place_details)
    return TemplateResponse(request,
                            "index.html",
                            context={"dict": place_details}
                            )
