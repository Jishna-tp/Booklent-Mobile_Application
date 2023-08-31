from django.shortcuts import render
from location.models import Location
from django.http import HttpResponse
# Create your views here.

from rest_framework.views import APIView, Response
from location.serializers import android_serialiser


class viewloc(APIView):
    def get(self, request):
        ob = Location.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)

    def post(self, request):
        ob = Location()
        ob.town = request.data['town']
        ob.city = request.data['city']
        ob.pincode = request.data['pincode']
        # ob.u_id=request.data['uid']
        ob.save()
        return HttpResponse('dbhasjdi')