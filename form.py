from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class my_form(UserCreationForm):
    First_Name=forms.CharField(max_length=15,required=None)
    Last_Name=forms.CharField(max_length=15, required=None)
    password1=forms.CharField(label='Enter password', required=None , widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', required=None,  widget=forms.PasswordInput)
    username=forms.CharField(label='username', required=None)
    
    class Meta:
        model=User
        fields=('First_Name', 'Last_Name', 'username', 'password1', 'password2')
        help_texts={ 'password1':None, 'username':None, }