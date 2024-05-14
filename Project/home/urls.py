
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
           path("",views.index,name='home'),
           path("a",views.a,name='a'),
            path("Services",views.Services,name='Services'),
            path("home",views.home,name='home'),
            path("contact",views.contact,name='contact'),
           
]
