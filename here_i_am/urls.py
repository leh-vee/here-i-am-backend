from django.urls import path

from . import views

urlpatterns = [
    path("street-nodes/", views.street_nodes_index, name="nodes"),
    path("street-nodes/tree-of-life/", views.tree_nodes, name="default_tree_nodes"),
    path("street-nodes/tree-of-life/<int:ground_zero_coords>", views.tree_nodes, name="tree_nodes"),
    path("street-edges/", views.street_edges_index, name="edges"),
    path("street-edges/area/", views.area_edges, name="area_edges"),
    path("street-edges/local/<int:node_id>/<int:meters>", views.local_edges, name="local_edges"),
]