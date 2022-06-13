from django.shortcuts import render


# Create your views here.

def home(requist):

    return render(requist,'home/index.html',{'x':0})