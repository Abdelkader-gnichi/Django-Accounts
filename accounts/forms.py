from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = ("username","email","first_name","last_name")

class ProfileForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = ("phone_number","address")

    

