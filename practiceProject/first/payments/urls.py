from django.urls import path
from . import views

urlpatterns =[
    path('bkash/', views.bk,name='paymentone'),
     # This from href of html
    path('rocket/', views.rk , name='paymenttwo'),
    path('pays/', views.payment_method),
    path('time/', views.dt),
    path('tag/', views.name),
    path('friend/', views.name1)
    
]