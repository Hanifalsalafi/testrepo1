from django.urls import path
from . import views

urlpatterns = [
    path('', views.pdt, name='product'),
    path('form/', views.details),
    path('successfully/', views.send)
]