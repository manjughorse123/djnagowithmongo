
from django.urls import path
from .views import *

urlpatterns = [

   
    path('dep/', DepastmentView.as_view(), name='dep'),#logout api
]