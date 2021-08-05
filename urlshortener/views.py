from rest_framework import generics, status
from rest_framework.response import Response
from .models import URL
from .serializers import URLSerializerResponse, URLShortenSerializer


class URLList(generics.ListAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializerResponse


class URLDetail(generics.RetrieveAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializerResponse


class URLShortener(generics.GenericAPIView):
    serializer_class = URLShortenSerializer

    def post(self, request, format=None):
        serializer = URLShortenSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        url = URL.objects.filter(
            long_text=serializer.validated_data['long_text']).first()
        if not url:
            url = serializer.save()
        url.visit()
        return Response(URLShortenSerializer(url).data)
