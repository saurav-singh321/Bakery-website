from django.contrib import admin
from django.urls import path,include
from myapp import views #hace to import

urlpatterns = [
    path("",views.index,name='home'), #if path received blank then access index function of view file
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact')

    ]
