from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name="inicio"),
    re_path(r'^/(?P<room_name>[^/]+)/$', views.room, name='sala'),
] 
