from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
def login(request):
     return render(request, 'login.html')
def register (request):
    return render(request,'register.html')
def feedback(request):
    return render(request,'feedback.html')
def cloth(request):
    return render(request,'cloth.html')
def rupees(request):
    return render(request,'rupees.html')