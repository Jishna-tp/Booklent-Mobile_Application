from django.shortcuts import render
from register.models import Register
from django.http import HttpResponse
from login.models import Login
from location.models import Location
# Create your views here.

from rest_framework.views import APIView, Response
from register.serializers import android_serialiser

class vusr(APIView):
    def get(self, request):
        ob = Register.objects.all()
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)


class ed(APIView):
    def post(self, request):
        print(request.data['drid'])
        ob = Register.objects.filter(reg_id=request.data['drid'])
        ser = android_serialiser(ob, many=True)
        return Response(ser.data)

class edit(APIView):
    def post(self, request):
        ob = Register.objects.get(reg_id=request.data['drid'])
        # ob.name = request.data['name']
        ob.username = request.data['username']
        ob.gender = request.data['gender']
        ob.age = request.data['age']
        ob.interest = request.data['interest']
        ob.phone_no = request.data['phone_no']
        ob.email = request.data['email']
        # ob.password =request.data['password']
        # ob.confirm_pw =request.data['confirm_pw']
        # ob.town = request.data['town']
        # ob.city = request.data['city']
        # ob.pincode = request.data['pincode']
        # ob.genre_id = request.data['genid']
        ob.save()
        return HttpResponse(ob.reg_id)

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


from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
import cv2
classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
from booklent import settings

@csrf_exempt
def express(request):
    if request.method=="POST":
        print("hello")
        # a=request.POST.get('file')
        myfiles=request.FILES['file']
        fs=FileSystemStorage()
        filename=fs.save(myfiles.name,myfiles)

        hfile = "haarcascade_frontalface_default.xml"
        haar = str(settings.BASE_DIR) + str(settings.STATIC_URL) + hfile
        classifier = cv2.CascadeClassifier(haar)

        filename = filename
        fname = str(settings.BASE_DIR) + str(settings.STATIC_URL) + filename
        image = cv2.imread(fname)
        faces = classifier.detectMultiScale(image)

        if len(faces) > 0:  # 5
            #         print('face detected')
            # engine = pyttsx3.init()
            # engine.say("Face Detected and captured")
            # engine.runAndWait()
            # cv2.imwrite('newface.jpg', im)
            return HttpResponse("yess")
        else:
            return HttpResponse("No face")



