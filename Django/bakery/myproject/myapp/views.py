#i have created this file - Saurav
from django.http import request
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html') #index.html will open
    # return HttpResponse("this is (home) page") #http response to pass the strings

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')

    

#this whole process is called url dispatching
