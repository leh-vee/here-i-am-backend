from here_i_am.models import StreetNode, StreetEdge 
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Polygon
from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

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

@csrf_exempt
def area_edges(request):
    # bbox_coords = (-79.4709882303466, 43.66370616979132, -79.46271217330582, 43.65074842368979)
    bbox_coords = json.loads(request.body.decode('utf-8'))
    bbox_geometry = Polygon.from_bbox(bbox_coords)
    edges = StreetEdge.objects.filter(geom__intersects=bbox_geometry)
    geojson = serialize(
        "geojson", edges, geometry_field="geom", fields=[
            "description", "from_street_node_id", "to_street_node_id"
        ]
    )
    return JsonResponse(geojson, safe=False)

