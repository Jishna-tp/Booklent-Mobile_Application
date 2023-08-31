from rest_framework import serializers
from genre_selected.models import GenreSelected


class android_serialiser(serializers.ModelSerializer):
    class Meta:
        model=GenreSelected
        fields='__all__'