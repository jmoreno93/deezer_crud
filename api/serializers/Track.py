from api.models import Track
from rest_framework import serializers

from api.serializers.Album import AlbumSerializer
from api.serializers.Artist import ArtistSerializer


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'


class TrackSerializerFull(serializers.ModelSerializer):
    album = AlbumSerializer()
    artist = ArtistSerializer()

    class Meta:
        model = Track
        fields = '__all__'
