from django.shortcuts import render
from user_post.models import UserPost
from django.http import HttpResponse
# Create your views here.

from rest_framework.views import APIView,Response
from user_post.serializers import android_serialiser


class viewbooks(APIView):
    def get(self,request):
        ob=UserPost.objects.all()
        ser=android_serialiser(ob,many=True)
        return Response(ser.data)

    def post(self,request):
        ob=UserPost()
        ob.book_name=request.data['book_name']
        ob.author_name = request.data['author_name']
        ob.bio = request.data['bio']
        ob.gen_id=request.data['genid']
        ob.u_id=request.data['uid']
        ob.save()
        return HttpResponse('dbhasjdi')

from genre_selected.models import GenreSelected
class viewbooksJbase(APIView):
    def get(self,request):
        ob=UserPost.objects.all()
        ser=android_serialiser(ob,many=True)
        return Response(ser.data)

    def post(self,request):
        uid=request.data['uid']
        print(uid)
        obG = list(set(GenreSelected.objects.filter(user_id=uid).values_list('genre_id',flat=True)))
        print(obG)
        ob = UserPost.objects.filter(gen_id__in=obG)
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)
        # return HttpResponse('dbhasjdi')