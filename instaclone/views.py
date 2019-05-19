from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm
from .models import Image,Profile

def welcome(request):
    return render(request,'welcome.html')

@login_required(login_url='/accounts/login')
def home(request):
    all_posts=Image.objects.all()
    return render(request,'home.html',{"posts":all_posts})

@login_required(login_url='/accounts/login')
def profile(request,profile_id):
    my_profile=Profile.objects.filter(id=profile_id)
    return render(request,'profile.html',{"profiles":my_profile})

@login_required(login_url='/accounts/login')
def search(request):
    return render(request,'search.html')

@login_required(login_url='accounts/login')
def new_post(request):
    current_user=request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            article=form.save(commit=False)
            article.editor=current_user
            article.save()
        return redirect('home.html')
    else:
        form=NewImageForm()
    return render(request,'newpost.html',{'form':form})