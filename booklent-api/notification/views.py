from django.http import HttpResponse
from django.shortcuts import render
from notification.models import Notification
# Create your views here.

from rest_framework.views import APIView,Response
from notification.serializers import android_serialiser

class notivw(APIView):
    def get(self,request):
        ob=Notification.objects.all()
        ser=android_serialiser(ob,many=True)
        return Response(ser.data)

class notifi(APIView):
    def post(self,request):
        ob=Notification()
        ob.book=request.data['bkname']
        ob.notification="new book published"
        ob.save()
        return HttpResponse("yess")