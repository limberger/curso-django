from django.urls import path

from pypro.videos.views import video, indice

app_name = 'videos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
    path('', indice, name='indice'),
]
