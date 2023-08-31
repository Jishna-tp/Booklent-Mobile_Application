from rest_framework import serializers
from user_post.models import UserPost


class android_serialiser(serializers.ModelSerializer):
    gendr=serializers.CharField(source='gen.genre_name')
    class Meta:
        model=UserPost
        fields=['gendr','book_name','author_name','bio','u_id','status','book_id','image']