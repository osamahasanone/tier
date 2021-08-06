from rest_framework import serializers
from ..models import URL
from . import VisitSerializer


class URLSerializer(serializers.ModelSerializer):
    '''Used in listing urls and retrieving one url'''
    visits = VisitSerializer(many=True, read_only=True)

    class Meta:
        model = URL
        fields = ('id', 'long_text', 'short_text', 'visits')
        depth = 1


class URLShortenSerializer(serializers.ModelSerializer):
    '''Used for shorten url endpoint'''
    class Meta:
        model = URL
        fields = ('id', 'long_text', 'short_text', 'visits_count')
