from django.shortcuts import render,render_to_response
from django.shortcuts import render,redirect
from .models import Reg
from .forms import Sigupform,Signinform
from django.http import HttpResponse
from random import randint
from django.core.mail import send_mail

    
def adminhome(request):
    return render(request,'adminhome.html')
    
def signup(request):
    Rform = Sigupform()
    if request.method=="POST":
        Rform = Sigupform(request.POST)
        if Rform.is_valid():            
            Rform.save()
        return redirect(signin)
    return render(request,'signup.html',{'Rform':Rform})

def signin(request):
    rform = Signinform()
    if request.method == 'POST':
        form= Signinform(request.POST)
        if form.is_valid():
            Email = request.POST.get('Email')
            password = request.POST.get('password')

            m = Reg.objects.filter(Email=Email,password=password)
            if not m:
                return render(request,'signin.html')
            else:
                return redirect(signout)
        else:
            return render(request,'signin.html',{'form':form})
    return render(request,'signin.html',{'form':rform})

def signout(request):
    return render(request,"signout.html")

def dashboard(request):
    return render(request,"index.html")








