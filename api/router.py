from .viewsets.Artist import ArtistViewSet
from .viewsets.Album import AlbumViewSet
from .viewsets.Track import TrackViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('artist', ArtistViewSet, basename='artists')
router.register('album', AlbumViewSet, basename='albums')
router.register('track', TrackViewSet, basename='tracks')

urlpatterns = router.urls
