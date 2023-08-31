from django.conf.urls import url
from register import views

urlpatterns=[
    url('usereg/',views.viewreg.as_view())
]
