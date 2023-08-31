from django.conf.urls import url
from location import views

urlpatterns=[
    url('loc/',views.viewloc.as_view())
]
