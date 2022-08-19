"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

#adding manually to change the text of django administration in database
admin.site.site_header = "Bakery Admin"
admin.site.site_title = "Bakery Admin Portal"
admin.site.index_title = "Welcome to Saurav's Bskery Portal"

urlpatterns = [
    path('admin/', admin.site.urls), #if enter admin then take to admin page
    path("",include('myapp.url')) #IF Blank then take to url file of myapp
]
