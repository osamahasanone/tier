from urlshortener.models import url
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import URL, Visit
from .serializers import URLSerializerResponse


class URLList(generics.ListAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializerResponse


class URLDetail(generics.RetrieveAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializerResponse


class URLShortener(APIView):
    def post(self, request, format=None):
        long_url = request.data.get('long_url')
        if not long_url:
            return Response('Bad Request', status=status.HTTP_400_BAD_REQUEST)
        url = URL.objects.shorten(long_url)
        return Response({'short_url': url.short_text})
        # return Response(URLSerializerResponse(url).data)
