from django.shortcuts import render
from django.http import HttpResponseRedirect
from product.forms import RecentProduct
from .models import laptop


# Create your views here.
def pdt(request):
    return render (request, 'product/product.html', {'nm':'Hanif'})

# httpredirect function
def send(request):
    return render(request,'product/submit.html')

# Django Form, Configure label & ID

def details(request):
    if request.method == 'POST':
        frm = RecentProduct(request.POST)
        if frm.is_valid():  
           pas = frm.cleaned_data['password']
           rpas = frm.cleaned_data['retype_password']
           lap = frm.cleaned_data['laptop']
           eml= frm.cleaned_data['email']
           abut = frm.cleaned_data['about']
           mess = frm.cleaned_data['message']
           chbox = frm.cleaned_data['Checkbox']
           rm = frm.cleaned_data['ram']
           ss = frm.cleaned_data['ssd']
           yt = frm.cleaned_data['youtube_channal']
           buy = laptop(password = pas, retype_password = rpas, laptop = lap, about = abut, email = eml, message = mess, checkbox = chbox, ram = rm, ssd = ss, youtube_channal = yt)
           buy.save()
           print('youtube_Channel :', frm.cleaned_data['youtube_channal'])
           return HttpResponseRedirect('/pdc/successfully')
             #print('Laptop :', frm.cleaned_data['laptop'])#when need specefic field data
    else:
        frm = RecentProduct(auto_id='true', label_suffix=' -') #frm like treat as object / id show as a lavel name
        print('Get Statement')
 
      #Ordering Form Field & Manually Form field
       # frm.order_fields(field_order = ['email','mobile','laptop'])

      # here dictinary 'from' is a key and 'frm' is value that work in html work as variable


    return render(request, 'product/recent.html', {'form': frm}) 