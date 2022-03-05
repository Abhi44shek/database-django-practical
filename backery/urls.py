from django.urls import path
from .views import *

urlpatterns = [
    path('',backery_menu,name ='backery_menu'),
]