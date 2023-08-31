from django.conf.urls import url
from genre import views

urlpatterns=[
    url('genview/',views.viewgenre.as_view()),
    url('vg/',views.vgen.as_view())
]
