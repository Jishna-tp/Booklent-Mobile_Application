from django.conf.urls import url
from rent import views
urlpatterns=[
    url('rent/',views.rent.as_view()),
    url('vwrt/',views.vwrentreq.as_view()),
    url('aprv/',views.aprrove.as_view()),
    url('rej/',views.reject.as_view()),
    url('reqvwapp/',views.apprrevw.as_view())

]