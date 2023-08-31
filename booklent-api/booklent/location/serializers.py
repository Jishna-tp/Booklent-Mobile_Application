from rest_framework import serializers
from location.models import Location


class android_serialiser(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields='__all__'