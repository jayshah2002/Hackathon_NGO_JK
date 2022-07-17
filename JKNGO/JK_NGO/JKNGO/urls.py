from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('feedback/',views.feedback,name='feedback'),
    path('cloth/',views.cloth,name='cloth'),
    path('rupees/',views.rupees,name='rupees'),
    path('plant/',views.plant,name='plant'),
    path('food/',views.food,name='food'),
    path('Login/',views.login,name='login'),
]