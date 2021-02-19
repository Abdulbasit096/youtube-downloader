from django.urls import path
from . import views


urlpatterns = [
    path('' , views.home,name='home'),
    path('download/' , views.download , name = 'download'),
    path('video/<res>' , views.complete, name='video'),
    path('audio/<format>', views.audio , name = 'audio')
    
]
