from django.http import HttpResponse
from django.shortcuts import render
from exchange.models import Exchange
# Create your views here.
from rest_framework.views import APIView,Response
from exchange.serializers import android_serialiser



class exch(APIView):
    def post(self,request):
        ab=Exchange()
        ab.usr_bk_nm=request.data['bookname']
        ab.book_of_exch=request.data['bkexch']
        ab.exch_date=request.data['date']
        ab.owner=request.data['owner']
        ab.usr_nm=request.data['usr']
        ab.status="requested"
        ab.save()
        return HttpResponse("yess")

from register.models import Register
class vwexch(APIView):
    def post(self, request):
        ab=Register.objects.get(reg_id=request.data['uid'])
        a=ab.username
        print(a)
        ob=Exchange.objects.filter(owner=a)
        ser=android_serialiser(ob,many=True)
        print(ser.data)
        return Response(ser.data)

class aaprvwexch(APIView):
    def post(self, request):
        ab=Register.objects.get(reg_id=request.data['uid'])
        a=ab.username
        print(a)
        ob=Exchange.objects.filter(usr_nm=a,status='approved')
        ser=android_serialiser(ob,many=True)
        print(ser.data)
        return Response(ser.data)
from transaction.models import Transcation
class aprrove(APIView):
    def post(self, request):
        ob=Exchange.objects.get(exc_id=request.data['rid'])
        ob.status="approved"
        ob.save()
        bb=Transcation()
        bb.book=ob.book_of_exch
        bb.usr_nm=ob.usr_nm
        bb.save()
        return HttpResponse("ysss")


class reject(APIView):
    def post(self, request):
        ob=Exchange.objects.get(exc_id=request.data['rid'])
        ob.status="reject"
        ob.save()
        return HttpResponse("ysss")