from django.conf.urls import url
from user_post import views

urlpatterns=[
    url('books/',views.viewbooks.as_view()),
    url('gbks/',views.viewbooksJbase.as_view())
]
