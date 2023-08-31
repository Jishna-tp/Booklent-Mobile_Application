from django.conf.urls import url
from exchange import views
urlpatterns=[
    url('exch/',views.exch.as_view()),
    url('vwc/',views.vwexch.as_view()),
    url('appr/',views.aprrove.as_view()),
    url('rej/',views.reject.as_view()),
    url('appvwc/',views.aaprvwexch.as_view())
]