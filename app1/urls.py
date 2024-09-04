from django.urls import path
from app1.views import *
app_name='raj'
urlpatterns = [
    path('cond/',cond,name='cond'),
    
]
