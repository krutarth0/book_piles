from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile 

class UserRegForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    

    class Meta: 
        model = User  #where to submit the data (basically name of the database)
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    
    class Meta: 
        model = User  
        fields = ['username','first_name', 'email']



class ProfileUpdateForm(forms.ModelForm):

	class Meta:
		model = profile
		fields =['image']


