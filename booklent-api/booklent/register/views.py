from django.shortcuts import render
from register.models import Register
from django.http import HttpResponse
from login.models import Login
from location.models import Location
# Create your views here.

from rest_framework.views import APIView, Response
from register.serializers import android_serialiser


class viewreg(APIView):
    def get(self, request):
        ob = Register.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)

    def post(self, request):
        ob = Register()
        # ob.name = request.data['name']
        ob.username = request.data['username']
        ob.gender = request.data['gender']
        ob.age = request.data['age']
        ob.interest = request.data['interest']
        ob.phone_no = request.data['phone_no']
        ob.email = request.data['email']
        ob.password =request.data['password']
        # ob.confirm_pw =request.data['confirm_pw']
        # ob.town = request.data['town']
        # ob.city = request.data['city']
        # ob.pincode = request.data['pincode']
        # ob.genre_id = request.data['genid']
        ob.save()
        obj=Login()
        obj.username=ob.username
        obj.password=ob.password
        obj.type="user"
        obj.u_id=ob.reg_id
        obj.save()
        # obje=Location()
        # obje.town=request.data['town']
        # obje.city = request.data['city']
        # obje.pincode = request.data['pincode']
        # obje.u_id=ob.reg_id
        # obje.save()
        return HttpResponse(ob.reg_id)

