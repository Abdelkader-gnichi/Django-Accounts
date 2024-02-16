from bson import is_valid
from django.shortcuts import render,redirect
from .forms import SignupForm,UserForm,ProfileForm
from django.contrib.auth import authenticate,login
from .models import Profile
# Create your views here.

def signup(request):

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
             # if you want to login manually
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            return redirect("profile")
            
            

    form = SignupForm()
    
    context = {"form":form}
    return render(request,"registration/signup.html",context)

def profile(request):
    profile = Profile.objects.get(user=request.user)

    context = {'profile': profile}

    return render(request,"profile/profile.html",context)

def profile_edit(request):

    if request.method == 'POST':

        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance= request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
        
    user_form = UserForm(instance= request.user)
    profile_form = ProfileForm(instance = request.user.profile)

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request,"profile/profile_edit.html",context)