from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages#for messages

# Create your views here.
def index(request):
    context={
        'var1':'Roshan is great',
        'var2':"this is sent"
    }
    messages.success(request,"WE SELL THE DELICIOUS ICE CREAM FOR OUR CUSTOMER YOU CAN't IGNORE IT !!!##### Welcome to our ice cream website, where every scoop is a celebration #####!!! ")
    return render(request,'index.html',context)
    

def a(request): 
     return render(request,'about.html')
    #return HttpResponse("this is about page") 

def home(request):
     return render(request,'home.html')
   # return HttpResponse("this is home page") 

def Services(request):
    return render(request,'Services.html')
   # return HttpResponse("this is services page page") 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()  # Save the contact object to the database
        #return render(request, 'teddy.html')  # Render a success page after saving
        messages.success(request, "your message is sent!")
    return render(request, 'contact.html')
