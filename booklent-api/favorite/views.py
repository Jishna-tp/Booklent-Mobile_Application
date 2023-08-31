from django.http import HttpResponse
from django.shortcuts import render
from favorite.models import Favorite
# Create your views here.
from rest_framework.views import APIView,Response
from favorite.serializers import android_serialiser

class favorite(APIView):
    def post(self,request):
        ff=Favorite()
        print("hello")
        print(request.data['uid'])
        ff.u_id=request.data['uid']
        print(request.data['bid'])
        ff.bk_id=request.data['bid']
        ff.save()
        return HttpResponse("yess")

    # def get(self,request):
    #     ob=Favorite.objects.all()
    #     ser=android_serialiser(ob,many=True)
    #     return Response(ser.data)


class vw(APIView):
    def post(self, request):
        ob=Favorite.objects.filter(u_id=request.data['uid'])
        ser=android_serialiser(ob,many=True)
        return Response(ser.data)