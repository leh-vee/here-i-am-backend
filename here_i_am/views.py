from here_i_am.models import StreetNode, StreetEdge
from django.contrib.gis.measure import D
from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render

def street_nodes_index(request):
    geojson = serialize(
        "geojson", StreetNode.objects.all(), geometry_field="geom", fields=["n_street_edges"]
    )
    return JsonResponse(geojson, safe=False)

def tree_nodes(request):
    node_ids = [13465772, 14172266, 13463429, 13463848, 13464031, 13464314, 13464439, 13465037, 13464696, 13465233]
    nodes = StreetNode.objects.ordered_by_ids(node_ids)
    geojson = serialize(
        "geojson", nodes, geometry_field="geom", fields=["n_street_edges"]
    )
    return JsonResponse(geojson, safe=False)

def street_edges_index(request):
    geojson = serialize(
        "geojson", StreetEdge.objects.all(), geometry_field="geom", fields=["description"]
    )
    return JsonResponse(geojson, safe=False)

def local_edges(request, node_id, meters):
    node = StreetNode.objects.get(id=node_id)
    edges = StreetEdge.objects.filter(geom__distance_lte=(node.geom, D(m=meters)))
    geojson = serialize("geojson", edges, geometry_field="geom", fields=["description"])
    return JsonResponse(geojson, safe=False)

