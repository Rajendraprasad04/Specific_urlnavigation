from django.urls import path
from app2.views import *
app_name='prasad'
urlpatterns = [
    path('loop/',loop,name='loop'),
    
]
