from rest_framework import serializers
from chat.models import Chat


class android_serialiser(serializers.ModelSerializer):
    # gendr=serializers.CharField(source='gen.genre_name')
    # bokname=serializers.CharField(source='bk.book_name')
    # auther = serializers.CharField(source='bk.author_name')
    uname=serializers.CharField(source='rec.username')
    usid=serializers.IntegerField(source='rec.reg_id')
    bknm=serializers.CharField(source='book.book_name')
    bkid=serializers.IntegerField(source='book.book_id')
    class Meta:
        model=Chat
        fields=['uname','chat_id','rec_id','type','message','bknm','bkid','usid','first_msg']