from rest_framework import serializers
from location.models import Location
from location.models import Loc


class android_serialiser(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields='__all__'


class android_serialisersssssssssss(serializers.ModelSerializer):
    class Meta:
        model=Loc
        fields='__all__'