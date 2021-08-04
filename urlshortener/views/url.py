from urlshortener.models import visit
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
import secrets
from ..models import URL, Visit
from ..serializers import URLSerializerResponse


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
            return Response('Bad', status=status.HTTP_400_BAD_REQUEST)
        
        url_db = URL.objects.filter(long_text=long_url).first()
        if url_db:
            visit = Visit(url=url_db)
            visit.save()
            return Response({'short_url': str(url_db)})
        hash = secrets.token_urlsafe(10)
        url = URL(long_text=long_url, hash=hash)
        url.save()
        visit = Visit(url=url)
        visit.save()

        return Response({'short_url': str(url)}, status=status.HTTP_201_CREATED)
