from django.urls import path

from . import views

urlpatterns = [
    path("sefirot/", views.sefirot, name="sefirot"),
    path("pathways/<int:intersection_id>/<int:meters>", views.pathways, name="pathways"),
    path("intersections/", views.intersections_index, name="intersections"),
    path("street-segments/", views.street_segments_index, name="street_segments"),
]