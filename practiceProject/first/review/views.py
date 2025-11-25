from django.shortcuts import render

# Create your views here.
def cust(request):
    return render(request,'review/review.html')   
