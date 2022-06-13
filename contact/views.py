from django.shortcuts import render
from .models import Send_Message
# Create your views here.
def contact1(request):
   
    
    return render(request,"contact/contact.html",{"x":0})