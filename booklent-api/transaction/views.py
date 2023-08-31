from django.shortcuts import render
from transaction.models import Transcation
# Create your views here.
from rest_framework.views import APIView,Response
from transaction.serializers import android_serialiser


class vwtrans(APIView):
    def get(self, request):
        ob=Transcation.objects.all()
        ser=android_serialiser(ob,many=True)
        # print(ser.data)
        return Response(ser.data)

