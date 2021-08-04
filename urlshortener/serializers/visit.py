from rest_framework import serializers
from ..models import Visit


class VisitSerializerResponse(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = ('id', 'requested_at')
