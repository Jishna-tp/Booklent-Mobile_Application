from django.http import HttpResponse
from django.shortcuts import render
from chat.models import Chat
from django.db.models import Q
# Create your views here.
from rest_framework.views import APIView,Response
from chat.serializers import android_serialiser


class chatrnt(APIView):
    def post(self,request):
        ab=Chat()
        ab.book_id=request.data['bid']
        ab.user_id=request.data['uid']
        ab.message="i would like to buy your book on rent"
        ab.type="rent"
        ab.rec_id=request.data['rcid']
        ab.first_msg="first"
        ab.save()
        return HttpResponse("yess")

class vwchat(APIView):
    def post(self, request):

        ob=Chat.objects.filter(Q(user_id=request.data['uid']) | Q(rec_id=request.data['uid']),book_id=request.data['bkid'])
        ser=android_serialiser(ob,many=True)
        return Response(ser.data)

from register.models import Register

class mainvw(APIView):
    def post(self, request):
        # cid=list(Chat.objects.filter(user_id=request.data['uid']).values_list('rec_id',flat=True))
        # print(cid)
        # regg=Register.objects.filter(reg_id__in=cid)
        # print(regg)
        ob=Chat.objects.filter(Q(user_id=request.data['uid']) | Q(rec_id=request.data['uid']),first_msg="first")
        ser=android_serialiser(ob,many=True)
        return Response(ser.data)


class exchchat(APIView):
    def post(self,request):
        ab=Chat()
        ab.book_id=request.data['bid']
        ab.user_id=request.data['uid']
        ab.message="i would like to exchange my book with u"
        ab.type="rent"
        ab.rec_id=request.data['rcid']
        ab.first_msg='first'
        ab.save()
        return HttpResponse("yess")


class msgins(APIView):
    def post(self,request):
        print("hellooooo")
        ab=Chat()
        chid=request.data['chid']
        obch=Chat.objects.get(chat_id=chid)
        ab.book_id=request.data['bid']
        # ab.user_id=request.data['uid']
        ab.user_id = request.data['uid']
        rcid=""
        if str(obch.user_id)==ab.user_id:
            rcid=obch.rec_id
        else:
            rcid=obch.user_id

        ab.message=request.data['msg']
        ab.type=request.data['tp']
        # ab.rec_id=request.data['rcid']
        ab.rec_id = rcid
        ab.first_msg=""
        ab.save()
        return HttpResponse("yess")