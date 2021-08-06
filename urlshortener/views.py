from rest_framework import generics, status
from rest_framework.response import Response
from django.db import transaction
from .models import URL
from .serializers import URLSerializer, URLShortenSerializer


class URLList(generics.ListAPIView):
    '''list of urls'''
    queryset = URL.objects.all()
    serializer_class = URLSerializer


class URLDetail(generics.RetrieveAPIView):
    '''One url detail'''
    queryset = URL.objects.all()
    serializer_class = URLSerializer


class URLShortener(generics.GenericAPIView):
    '''shorten a url

    returns:
    400 (Bad Request): something wrong in request data
    201 (Created) : shorten url for the first time
    200 (OK) : shorten a url again
    '''
    serializer_class = URLShortenSerializer

    @transaction.atomic()
    def post(self, request, format=None):
        serializer = URLShortenSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        url = URL.objects.filter(
            long_text=serializer.validated_data['long_text']).first()
        if not url:
            url = serializer.save()
            url.visit()
            response = Response(URLShortenSerializer(
                url).data, status=status.HTTP_201_CREATED)
        else:
            url.visit()
            response = Response(URLShortenSerializer(url).data)
        return response
