from django.urls import path
from . import views


app_name = 'live'

urlpatterns = [

	path('video', views.video, name='video'),
	path('', views.live, name='index'),
]