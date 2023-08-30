from here_i_am.models import Intersection, StreetSegment
from django.contrib.gis.measure import D
from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render

def intersections_index(request):
    geojson = serialize(
        "geojson", Intersection.objects.all(), geometry_field="geom", 
        fields=["id", "description"]
    )
    return JsonResponse(geojson, safe=False)

def sefirot(request):
    intersection_ids = [13465772, 13465233, 13464696, 13465037, 13464439, 13464314, 13464031, 13463848, 13463429, 14172266]
    default_tree_intersections = Intersection.objects.filter(id__in=intersection_ids)
    geojson = serialize(
        "geojson", default_tree_intersections, geometry_field="geom", 
        fields=["id", "description"]
    )
    return JsonResponse(geojson, safe=False)

def street_segments_index(request):
    geojson = serialize(
        "geojson", StreetSegment.objects.all(), geometry_field="geom", 
        fields=["id", "description"]
    )
    return JsonResponse(geojson, safe=False)

def pathways(request, intersection_id, meters):
    intersection = Intersection.objects.get(id=intersection_id)
    ss = StreetSegment.objects.filter(
        geom__distance_lte=(intersection.geom, D(m=meters))
    )
    geojson = serialize("geojson", ss, geometry_field="geom", fields=["id", "description"])
    return JsonResponse(geojson, safe=False)

