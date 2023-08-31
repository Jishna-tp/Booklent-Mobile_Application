from rest_framework import serializers
from user_post.models import UserPost


class android_serialiser(serializers.ModelSerializer):
    class Meta:
        model=UserPost
        fields='__all__'