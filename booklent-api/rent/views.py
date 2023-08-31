from django.http import HttpResponse
from django.shortcuts import render
from rent.models import Rent
# Create your views here.
from rest_framework.views import APIView,Response
from rent.serializers import android_serialiser


class rent(APIView):
    def post(self,request):
        ab=Rent()
        ab.book_name=request.data['bookname']
        ab.date=request.data['date']
        ab.return_date=request.data['trndate']
        ab.boorower_name=request.data['borrower']
        ab.own_name=request.data['owns']
        ab.amount=request.data['amount']
        ab.status="requested"
        ab.u_id=request.data['uid']
        ab.save()
        return HttpResponse("yess")

class vwrentreq(APIView):
    def post(self, request):
        ob=Rent.objects.filter(u_id=request.data['uid'])
        ser=android_serialiser(ob,many=True)
        print(ser.data)
        return Response(ser.data)


class apprrevw(APIView):
    def post(self, request):
        ob=Rent.objects.filter(u_id=request.data['uid'],status='approved')
        ser=android_serialiser(ob,many=True)
        print(ser.data)
        return Response(ser.data)


from transaction.models import Transcation
class aprrove(APIView):
    def post(self, request):
        ob=Rent.objects.get(rnt_id=request.data['rid'])
        ob.status="approved"
        ob.save()
        bb=Transcation()
        bb.book=ob.book_name
        bb.usr_nm=ob.boorower_name
        bb.save()
        return HttpResponse("ysss")


class reject(APIView):
    def post(self, request):
        ob=Rent.objects.get(rnt_id=request.data['rid'])
        ob.status="reject"
        ob.save()
        return HttpResponse("ysss")