from django.urls import path

from . import views

urlpatterns = [
    path("street-nodes/", views.street_nodes_index, name="all_nodes"),
    path("street-node/<int:id>", views.street_node, name="street_node_by_id"),
    path("crossroads/random/<int:n_nodes>/", views.random_crossroads, name="n_random_crossroads"),
    path("street-nodes/tree-of-life/", views.tree_nodes, name="default_tree_nodes"),
    path("street-nodes/tree-of-life/<int:ground_zero_coords>", views.tree_nodes, name="tree_nodes"),
    path("street-edges/", views.street_edges_index, name="all_edges"),
    path("street-edges/area/", views.area_edges, name="area_edges"),
    path("street-edges/within-radius/", views.within_radius, name="within_radius"),
]