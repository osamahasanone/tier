from rest_framework import generics, status
from rest_framework.response import Response
from .models import URL
from .serializers import URLSerializerResponse, URLSerializerShortenResponse, URLSerializerRequest


class URLList(generics.ListAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializerResponse


class URLDetail(generics.RetrieveAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializerResponse


class URLShortener(generics.CreateAPIView):
    serializer_class = URLSerializerRequest

    def post(self, request, format=None):
        long_url = request.data.get('long_text')
        if not long_url:
            return Response('Bad Request', status=status.HTTP_400_BAD_REQUEST)
        url = URL.objects.shorten(long_url)
        return Response(URLSerializerShortenResponse(url).data)
