from rest_framework import serializers
from ..models import URL
from . import VisitSerializerResponse


class URLSerializerResponse(serializers.ModelSerializer):
    visits = VisitSerializerResponse(many=True, read_only=True)

    class Meta:
        model = URL
        fields = ('id', 'long_text', 'hash', 'visits')
        depth = 1
