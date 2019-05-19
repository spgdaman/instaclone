from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def welcome(request):
    return render(request,'welcome.html')

@login_required(login_url='/accounts/login')
def home(request):
    
    return render(request,'home.html')

@login_required(login_url='/accounts/login')
def profile(request):
    return render(request,'profile.html')

@login_required(login_url='/accounts/login')
def search(request):
    return render(request,'search.html')