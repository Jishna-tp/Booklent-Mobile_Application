from rest_framework import serializers
from favorite.models import Favorite


class android_serialiser(serializers.ModelSerializer):
    # gendr=serializers.CharField(source='gen.genre_name')
    bokname=serializers.CharField(source='bk.book_name')
    auther = serializers.CharField(source='bk.author_name')
    bkimg=serializers.CharField(source='bk.image')
    class Meta:
        model=Favorite
        fields=['bokname','fav_id','u_id','auther','bkimg']