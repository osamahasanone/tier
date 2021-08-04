from rest_framework import serializers
from ..models import URL
from . import VisitSerializerResponse


class URLSerializerResponse(serializers.ModelSerializer):
    visits = VisitSerializerResponse(many=True, read_only=True)

    class Meta:
        model = URL
        fields = ('id', 'long_text', 'short_text', 'visits')
        depth = 1


class URLSerializerShortenResponse(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ('short_text',)


class URLSerializerRequest(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ('long_text',)
