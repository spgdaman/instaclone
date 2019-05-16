from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    return render(request,'welcome.html')

def home(request):
    return render(request,'home.html')

def profile(request):
    return render(request,'profile.html')