from django.conf.urls import url
from favorite import views
urlpatterns=[
    url('fav/',views.favorite.as_view()),
    url('vw/',views.vw.as_view())
]