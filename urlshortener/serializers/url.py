from rest_framework import serializers
from ..models import URL
from . import VisitSerializer


class URLSerializer(serializers.ModelSerializer):
    visits = VisitSerializer(many=True, read_only=True)

    class Meta:
        model = URL
        fields = ('id', 'long_text', 'short_text', 'visits')
        depth = 1


class URLShortenSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ('long_text', 'short_text', 'visits_count')
