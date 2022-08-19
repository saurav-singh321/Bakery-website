# I have created this file
from django import http
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    #getting the text of textarea 
    djtext = request.GET.get("text","default")

    # getting the checkbox
    RemovePunctions = request.GET.get("RemovePunctions","off")

    print(djtext)
    print(about)

    a = {'djtext':djtext} #we have to pass dict only

    #checking which chekbox is on
    if RemovePunctions=='on':
        return render(request,'about.html',a)
    else:
        return HttpResponse("""<a href = "\ "> << BACK</a> <br> Please Select any option""")