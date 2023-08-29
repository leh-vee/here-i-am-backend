from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("hia-data/", include("here_i_am.urls")),
    path('admin/', admin.site.urls),
]
