from here_i_am.models import StreetNode, StreetEdge
from django.contrib.gis.measure import D
from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render

def intersections_index(request):
    geojson = serialize(
        "geojson", StreetNode.objects.all(), geometry_field="geom", 
        fields=["id", "description"]
    )
    return JsonResponse(geojson, safe=False)

def sefirot(request):
    intersection_ids = [13465772, 14172266, 13463429, 13463848, 13464031, 13464314, 13464439, 13465037, 13464696, 13465233]
    default_tree_intersections = StreetNode.objects.sefirot_ordered_by_intersection_id_index(intersection_ids)
    geojson = serialize(
        "geojson", default_tree_intersections, geometry_field="geom", 
        fields=["id", "description"]
    )
    return JsonResponse(geojson, safe=False)

def street_segments_index(request):
    geojson = serialize(
        "geojson", StreetEdge.objects.all(), geometry_field="geom", 
        fields=["id", "description"]
    )
    return JsonResponse(geojson, safe=False)

def pathways(request, intersection_id, meters):
    intersection = StreetNode.objects.get(id=intersection_id)
    ss = StreetEdge.objects.filter(
        geom__distance_lte=(intersection.geom, D(m=meters))
    )
    geojson = serialize("geojson", ss, geometry_field="geom", fields=["id", "description"])
    return JsonResponse(geojson, safe=False)

