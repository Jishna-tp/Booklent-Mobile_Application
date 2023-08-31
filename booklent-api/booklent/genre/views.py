from django.shortcuts import render
from genre.models import Genre
from register.models import Register
from django.http import HttpResponse
# Create your views here.

from rest_framework.views import APIView,Response
from genre.serializers import android_serialiser


class viewgenre(APIView):
    def get(self,request):
        ob=Genre.objects.all()
        ser=android_serialiser(ob,many=True)
        return Response(ser.data)

    def post(self,request):
        ob=Genre()
        ob.genre_name=request.data['genre_name']
        ob.u_id = request.data['uid']
        ob.save()
        return HttpResponse('dbhasjdi')

