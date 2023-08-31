from django.conf.urls import url
from register import views

urlpatterns=[
    url('usereg/',views.viewreg.as_view()),
    url('imgrec/',views.express),
    url('vusr/',views.vusr.as_view()),
    url('ed/',views.ed.as_view()),
    url('tidt/',views.edit.as_view())
]
