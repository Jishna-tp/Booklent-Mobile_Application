"""booklent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    url('location/',include('location.url')),
    url('login/',include('login.url')),
    url('register/',include('register.url')),
    url('genre/',include('genre.url')),
    url('userpost/',include('user_post.url')),
    url('genreselect/',include('genre_selected.url')),
    url('notification',include('notification.url')),
    url('favoritr/',include('favorite.url')),
    url('chat/',include('chat.url')),
    url('rent/',include('rent.url')),
    url('exchange/',include('exchange.url')),
    url('trans/',include('transaction.url'))

]
