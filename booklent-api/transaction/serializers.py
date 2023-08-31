from rest_framework import serializers
from transaction.models import Transcation


class android_serialiser(serializers.ModelSerializer):
    # gendr=serializers.CharField(source='gen.genre_name')
    class Meta:
        model=Transcation
        fields='__all__'