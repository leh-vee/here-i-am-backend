from django.urls import path

from . import views

urlpatterns = [
    path("intersections/", views.intersections_index, name="intersections"),
    path("street-segments/", views.street_segments_index, name="street_segments"),
    path("tree/intersections", views.default_tree_intersections, name="default_intersections"),
]