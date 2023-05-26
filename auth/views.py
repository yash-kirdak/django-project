from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

#from ..adupload.models import Document
# Create your views here.
def home(request):
    return render(request, "auth/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email=request.POST['email']
        passw = request.POST['pass']
        cpass = request.POST['cpass']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username")
            return redirect('signup')
          
        if User.objects.filter(email=email):
            messages.error(request, "Email already Registered!")    
            return redirect('signup')
        
        if len (username)>10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('signup')
        if passw!=cpass :
            messages.error(request, "Passwords didn't match!")
            return redirect('signup')
        
        if not username.isalnum():
               messages.error(request, "Username must be Alpha-Numeric")
               return redirect('signup')     
        
        myuser= User.objects.create_user(username, email,passw)
        myuser.save()
        messages.success(request, "Your Account hass been successfully created.")
        return redirect('login')

    return render(request, "auth/signup.html")

def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        passw= request.POST['pass']
    
        user=authenticate(username=username, password=passw)
        if user is not None:
            login(request, user)
            return render(request,"auth/view.html")
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')    
    return render(request, "auth/login.html")

def Logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home') 

# def show(request):
#     all_data = Document.objects.all()

#     context = {
#         'data':all_data
#     }
#     return render(request,'auth/view.html')
