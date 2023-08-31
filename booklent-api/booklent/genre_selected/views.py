from django.shortcuts import render
from genre_selected.models import GenreSelected
from django.http import HttpResponse
# Create your views here.

from rest_framework.views import APIView, Response
from genre_selected.serializers import android_serialiser


class selectgen(APIView):
    def get(self, request):
        ob = GenreSelected.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)

    def post(self, request):
        ob = GenreSelected()
        ob.user_id = request.data['uid']
        ob.genre_id = request.data['genid']
        ob.save()
        return HttpResponse('dbhasjdi')