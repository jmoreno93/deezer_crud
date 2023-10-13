from api.viewsets.Track import search_track
from django.urls import path

urlpatterns = [
    path("search/", search_track, name="search_track"),
]
