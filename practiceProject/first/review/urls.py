from django.urls import path
from . import views

urlpatterns =[
    path('custv', views.cust, name='review'),
]