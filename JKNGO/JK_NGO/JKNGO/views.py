from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def login(request):
     return render(request, 'login.html')
def register (request):
    if request.method == "GET":
        return render(request,"register.html")
    if request.method == "POST":
        username = request.POST['userame']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password2']
        city=request.POST['city']
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('Login')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('Login')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('Login')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('Login')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('Login')
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        return redirect('Login')
    return render(request,'register.html')
def feedback(request):
    return render(request,'feedback.html')
def cloth(request):
    return render(request,'cloth.html')
def rupees(request):
    return render(request,'rupees.html')
def plant(request):
    return render(request,'plant.html')
def food(request):
    return render(request,'food.html')
def Login(request):
     if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
           
              login(request,user)
              fname = user.username
              superuser = user.is_superuser
              firstname= user.first_name
              context= {'fname' :fname,'superuser' :superuser,'firstname' : firstname}
         
            # messages.success(request, "Logged In Sucessfully!!")
              return redirect('index')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('Login')
    
     return render(request, "login.html")   
     
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('Login')