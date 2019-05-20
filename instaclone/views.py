from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm,NewProfileForm
from .models import Image,Profile

def welcome(request):
    return render(request,'welcome.html')

@login_required(login_url='/accounts/login')
def home(request):
    all_posts=Image.objects.all()
    return render(request,'home.html',{"posts":all_posts})

@login_required(login_url='/accounts/login')
def search(request):
    if 'image' in request.GET and request.GET['image']:
        search_term=request.GET.get('image')
        searched_images=Image.objects.filter(image_name__icontains=search_term)
        message=f"{search_term}"
        return render(request,'search.html',{"message":message,"images":search_term})
    else:
        message="Please enter a valid search item"
    return render(request,'search.html',{"message":message})

@login_required(login_url='accounts/login')
def new_post(request):
    current_user=request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=current_user
            post.save()
        return redirect('home')
    else:
        form=NewImageForm()
    return render(request,'newpost.html',{'form':form})

@login_required(login_url='accounts/login')
def show_post(request,post_id):
    post=Image.objects.filter(id=post_id)
    return render(request,'post.html',{"post":post})

@login_required(login_url='accounts/login')
def update_profile(request):
    current_user=request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=current_user
            profile.save_profile()
        return redirect('home')
    else:
        form=NewProfileForm()
    return render(request,'updateprofile.html',{"form":form})

@login_required(login_url='accounts/login')
def profile(request,profile_id):
    profile=Profile.objects.filter(id=profile_id)
    return render(request,'profile.html',{"profile":profile})