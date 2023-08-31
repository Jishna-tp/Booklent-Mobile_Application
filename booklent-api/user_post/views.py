from django.shortcuts import render
from user_post.models import UserPost
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from booklent import settings
from notification.models import Notification
# Create your views here.

from rest_framework.views import APIView,Response
from user_post.serializers import android_serialiser


class viewbooks(APIView):
    def get(self,request):
        ob=UserPost.objects.all()
        ser=android_serialiser(ob,many=True)
        return Response(ser.data)

    def post(self,request):
        print("helo")
        ob=UserPost()
        ob.book_name=request.data['book_name']
        print(ob.book_name)
        ob.author_name = request.data['author_name']
        print(ob.author_name)
        ob.bio = request.data['bio']
        print(ob.bio)
        ob.gen_id=request.data['genid']
        print(ob.gen_id)
        ob.u_id=request.data['uid']
        print(ob.u_id)
        ob.image=request.data['file']
        print(ob.image)
        ob.status="Available"
        ob.save()
        # kk=Notification()
        # kk.notification="New book Published"
        # kk.b_id=ob.book_id
        # kk.save()
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

class searchbooks(APIView):
    def post(self,request):
        uid = request.data['uid']
        obG = list(set(GenreSelected.objects.filter(user_id=uid).values_list('genre_id', flat=True)))
        ob=UserPost.objects.filter(gen_id__in=obG)
        ser=android_serialiser(ob,many=True)
        return Response(ser.data)

class Mybooks(APIView):
    def post(self,request):
        uid = request.data['uid']
        print(uid)
        ob=UserPost.objects.filter(u_id=35)
        ser=android_serialiser(ob,many=True)
        return Response(ser.data)

@csrf_exempt
def up(request):
    if request.method=="POST" and request.FILES['file']:
        mfile=request.FILES['file']
        fs=FileSystemStorage()
        fpath=str(settings.BASE_DIR) + (settings.STATIC_URL) + mfile.name
        fname=fs.save(fpath, mfile)
        print(fname)
        return HttpResponse("yess")


from genre_selected.models import GenreSelected
from booklent import settings
from pandas import read_excel
from sklearn.tree import DecisionTreeClassifier
from genre.models import Genre
class predict(APIView):
    def post(self,request):
        u=request.data['uid']
        bb=GenreSelected.objects.filter(user_id=u)
        t=len(bb)
        print(t)
        for i in range(t):
            print("hello")
            # c=i.genre_id
            # print(c)
        a=request.data['age']
        b=request.data['gender']
        c=request.data['author']
        d=request.data['gen']
        # dd=Genre.objects.get(genre_id=d)
        # e=dd.genre_name


        print(a)
        print(b)
        print(c)
        print(d)
        # print(e)

        imgpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + "Booknew.xlsx"
        data = read_excel(imgpath, "Sheet1")
        X = data.iloc[:, 0:4].values
        y = data.iloc[:, 4].values
        dtc = DecisionTreeClassifier()
        dtc.fit(X, y)
        # test = [int(a1),int(a2),int(a3),int(a4),int(a5),int(a6),int(a7),int(a8),int(a9),int(a10),int(a11),int(a12),
        #         int(a13),int(a14),int(a15),int(a16),int(a17),int(a18),int(a19),int(a20),int(a21),int(a22),int(a23),int(a24),
        #         int(a25),int(a26),int(a27),int(a28),int(a29),int(a30),int(a31),int(a32),int(a33),int(a34),int(a35),int(a36),
        #         int(a37),int(a38),int(a39),int(a40),int(a41)]
        test = [int(a), int(b), int(c), int(d)]
        y_pred = dtc.predict([test])
        print(y_pred)
        return HttpResponse(y_pred)


