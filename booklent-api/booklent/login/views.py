from django.shortcuts import render
from login.models import Login
# Create your views here.
from rest_framework.views import APIView,Response
from login.serializers import android_serialiser

class log(APIView):
    def get(self,reguest):
        ob = Login.objects.all()
        ser = android_serialiser(ob,many=True)
        return  Response(ser.data)

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        ob = Login.objects.filter(username=username, password=password)
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)