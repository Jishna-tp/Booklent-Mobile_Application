from django.conf.urls import url
from genre_selected import views

urlpatterns=[
    url('selectgen/',views.selectgen.as_view())
]
