from django.contrib import admin
from django.urls import path , include
from intern2 import views

app_name = 'intern2'

urlpatterns =[
    path('',views.base,name='base'),
]