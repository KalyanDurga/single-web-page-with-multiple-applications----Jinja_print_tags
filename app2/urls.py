from app2.views import *
from django.urls import path
app_name='hiihloo'

urlpatterns=[
    path('rcb/',rcb,name='rcb'),
]