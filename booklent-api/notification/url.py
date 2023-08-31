from django.conf.urls import url
from notification import views
urlpatterns=[
    url('notivw/',views.notivw.as_view()),
    url('pst/',views.notifi.as_view())
]