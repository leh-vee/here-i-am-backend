from here_i_am.models import Intersection
from django.http import JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render

def intersections_index(request):
    geojson = serialize("geojson", Intersection.objects.all(), 
        geometry_field="geom", fields=["id", "description"])
    return JsonResponse(geojson, safe=False)
