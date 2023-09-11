# Generated by Django 4.2.4 on 2023-09-11 19:53

from django.db import migrations
from django.contrib.gis.geos import GEOSGeometry
import json

def insert_street_data(apps, schema_editor):
    StreetEdge = apps.get_model('here_i_am', 'StreetEdge')
    StreetNode = apps.get_model('here_i_am', 'StreetNode')

    with open('here_i_am/data/toronto-centreline.geojson') as data_file:
        edges_json = json.load(data_file)
        features = edges_json['features']
        for feature in features:
            f_props = feature['properties']
            f_geom = feature['geometry']
            edge_properties = { 
                "id": f_props["id"], 
                "description": f_props["description"],
                "from_street_node_id": f_props["from_intersection_id"],
                "to_street_node_id": f_props["to_intersection_id"]
            }
            edge_properties['geom'] = GEOSGeometry(json.dumps(f_geom))
            edge = StreetEdge(**edge_properties)
            edge.save()
            edge_coordinates = f_geom['coordinates']
            create_or_increment_node(edge.from_street_node_id, edge_coordinates[0], StreetNode)
            create_or_increment_node(edge.to_street_node_id, edge_coordinates[-1], StreetNode)

def create_or_increment_node(id, node_coordinates, model_klass):
    try:
        node = model_klass.objects.get(id=id)
        node.n_street_edges += 1
        node.save()
    except model_klass.DoesNotExist:
        point_geometry_dict = { "type": "Point", "coordinates": node_coordinates }
        new_node_fields = { "id": id, "geom": GEOSGeometry(json.dumps(point_geometry_dict)), "n_street_edges": 1 }
        new_node = model_klass(**new_node_fields)
        new_node.save()

def delete_all_street_data(apps, schema_editor):
    StreetNode = apps.get_model('here_i_am', 'StreetNode')
    StreetNode.objects.all().delete()
    StreetEdge = apps.get_model('here_i_am', 'StreetEdge')
    StreetEdge.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('here_i_am', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_street_data, delete_all_street_data),
    ]