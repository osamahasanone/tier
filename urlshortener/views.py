from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import URL
from .serializers import URLSerializerResponse, URLSerializerShortenResponse, URLSerializerRequest


class URLList(generics.ListAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializerResponse


class URLDetail(generics.RetrieveAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializerResponse


class URLShortener(APIView):

    def get(self, request, format=None):
        long_url = request.data.get('long_text')
        if not long_url:
            return Response('Bad Request', status=status.HTTP_400_BAD_REQUEST)
        url = URL.objects.filter(long_text=long_url).first()
        if not url:
            return Response('Not Found', status=status.HTTP_404_NOT_FOUND)
        url.visit()
        return Response(URLSerializerShortenResponse(url).data)

    def post(self, request, format=None):
        long_url = request.data.get('long_text')
        if not long_url:
            return Response('Bad Request', status=status.HTTP_400_BAD_REQUEST)
        serializer = URLSerializerRequest(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        saved_url = serializer.save()
        saved_url.visit()
        return Response(URLSerializerShortenResponse(saved_url).data)
