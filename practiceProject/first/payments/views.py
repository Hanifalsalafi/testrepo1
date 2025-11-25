
from django.shortcuts import render
from datetime import datetime
from payments.models import pay_method


# Create your views here.
def bk(request):
    return render(request, "payments/payments-1.html")

def rk(request):
    return render(request, "payments/payments-2.html")
# for models .pay 

def payment_method(request):
    pay_m = pay_method.objects.all()
    return render(request, "payments/pay.html", {'pay' :pay_m}) # the code represt for user view

def dt(request):
    dtime= datetime.now()
    return render(request,"payments/payments-1.html",{'dt':dtime})

# If tag for practice with fuction base view
def name(request):
    return render(request,"payments/payments-1.html", {'nm':'Hanif'})
# for loop with function base view
def name1(request):
    friends = {'fname': ['Hanif', 'Hasan', 'Rafsan','Jannat']}
    return render(request, "payments/payments-1.html",friends)
    


