from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from api.serializers.Track import TrackSerializer, Track, TrackSerializerFull
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_track(request):
    if request.method == 'GET':
        keyword = request.GET.get('q', None)

        if keyword is None:
            return Response({'error': 'Please provide a keyword (q)'}, status=status.HTTP_400_BAD_REQUEST)

        tracks = Track.objects.filter(artist__name__icontains=keyword) | Track.objects.filter(
            album__title__icontains=keyword) | Track.objects.filter(title__icontains=keyword)

        serializer = TrackSerializerFull(tracks, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
