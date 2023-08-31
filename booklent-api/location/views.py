from django.shortcuts import render
from location.models import Location
from django.http import HttpResponse
from location.models import Loc
# Create your views here.
from location.serializers import android_serialisersssssssssss
from rest_framework.views import APIView, Response
from location.serializers import android_serialiser

class loc(APIView):
    def post(self,request):
        ab=Loc()
        ab.latitude=request.data['lat']
        ab.longitude=request.data['lon']
        ab.save()
        return HttpResponse("yess")

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