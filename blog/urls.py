from django.urls import path

from .views import home

app_name = 'blog' #<<this is namespace,naming url, so one app url doesn't collide with other app

urlpatterns = [
    path('home/', home)
]