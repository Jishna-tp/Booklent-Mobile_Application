from django.conf.urls import url
from genre import views

urlpatterns=[
    url('genview/',views.viewgenre.as_view())
]
