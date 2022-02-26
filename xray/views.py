from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'xray/home.html')
def about(request):
    return render(request,'xray/about.html')

@login_required(login_url='login')
def checkcovid(request):
    return render(request,'xray/checkcovid.html')
def contact(request):
    if(request.method=="POST"):
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        query=request.POST.get('query')
        contact=Contact(name=name,phone=phone,email=email,query=query)
        contact.save()
        messages.success(request,"Your Message Has Been Sended Successfully!")
        return redirect('/contact/')
    return render(request,'xray/contact.html')

def logindevta(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password is incorrect')
    context={}
    return render(request,'xray/login.html',context)

def logoutdevta(request):
    logout(request)
    return redirect("home")


def registerdevta(request):
	form=CreateUserForm()
	if(request.method=="POST"):
		form=CreateUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			username=form.cleaned_data.get('username')
			# email=form.cleaned_data.get('email')
			# Customer.objects.create(user=user,name=user.username,email=user.email)
			messages.success(request,'Account Created'+" "+username)
			return redirect('login')
	context={'form':form}
	return render(request,'xray/register.html',context)