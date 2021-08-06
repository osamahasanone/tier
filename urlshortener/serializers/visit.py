from rest_framework import serializers
from ..models import Visit


class VisitSerializer(serializers.ModelSerializer):
    '''Used for listing and retrieving'''
    class Meta:
        model = Visit
        fields = ('id', 'requested_at')
