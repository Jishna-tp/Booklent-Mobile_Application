from django.conf.urls import url
from chat import views
urlpatterns=[
    url('rntcht/',views.chatrnt.as_view()),
    url('chtexch/',views.exchchat.as_view()),
    url('vw/',views.vwchat.as_view()),
    url('main/',views.mainvw.as_view()),
    url('inschat/',views.msgins.as_view())
]