from rest_framework import serializers
from notification.models import Notification


class android_serialiser(serializers.ModelSerializer):
    # gendr=serializers.CharField(source='gen.genre_name')
    # bkname=serializers.CharField(source='b.book_name')
    class Meta:
        model=Notification
        fields=['book','notification','noti_id']