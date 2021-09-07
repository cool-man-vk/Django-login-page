from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render , redirect
from django.http import HttpResponse 
from .models import Details
from .forms import DetailsForm  , CreateUserForm , LoginPageForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages 
from django.contrib.auth import authenticate , logout , login  
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request): 
    return render(request,"app/base.html",{}) 

@login_required(login_url='login')
def todo(request): 
    data = Details.objects.all()  
    context = {
        'data' : data 
    }
    return render(request,"app/todo.html",context) 

@login_required(login_url='login')
def addtasks(request):
    form = DetailsForm(request.POST or None) 
    if form.is_valid():
        form.save()
        form = DetailsForm() 
    context = {'form':form}
    return render(request,'app/addtasks.html',context)

def signup(request):  
    if request.user.is_authenticated:
        return redirect('/')
    else:
        signup_form = CreateUserForm()
        if request.method == 'POST':
            signup_form = CreateUserForm(request.POST) 
            if signup_form.is_valid():
                signup_form.save()
                messages.success(request,'Account registered successfully.You can login now.')
                return redirect('login')
        context = {'form':signup_form} 
        return render(request,"app/register.html",context) 

def loginPage(request): 
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username') 
            password = request.POST.get('password') 

            user = authenticate(request , username = username, password = password) 

            if user is not None:
                login(request,user) 
                return redirect('/') 
            else:
                messages.info(request,'Username or password is incorrect') 
        context = {} 
        return render(request,'app/login.html',context) 

def logoutPage(request):
    logout(request)
    return redirect('login')