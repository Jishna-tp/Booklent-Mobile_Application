from django.conf.urls import url
from transaction import views

urlpatterns=[
    url('vwtrans/',views.vwtrans.as_view())

]
