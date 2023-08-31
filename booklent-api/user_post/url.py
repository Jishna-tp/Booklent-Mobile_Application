from django.conf.urls import url
from user_post import views

urlpatterns=[
    url('books/',views.viewbooks.as_view()),
    url('gbks/',views.viewbooksJbase.as_view()),
    url('srch/',views.searchbooks.as_view()),
    url('my/',views.Mybooks.as_view()),
    url('up/',views.up),
    url('pre/',views.predict.as_view())
]
