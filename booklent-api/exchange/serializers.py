from rest_framework import serializers
from exchange.models import Exchange


class android_serialiser(serializers.ModelSerializer):
    # gendr=serializers.CharField(source='gen.genre_name')
    # bokname=serializers.CharField(source='bk.book_name')
    # auther = serializers.CharField(source='bk.author_name')
    # bkimg=serializers.CharField(source='bk.image')
    class Meta:
        model=Exchange
        fields='__all__'