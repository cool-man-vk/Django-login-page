from django.forms import widgets
from .models import Details 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date' 

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details 
        fields = "__all__" 
        widgets = {
            'start_date' : DateInput() ,
            'end_date' : DateInput() , 
        }
         
class CreateUserForm(UserCreationForm):
     username = forms.CharField(widget = forms.TextInput(attrs={
        'placeholder' : 'Your Username',
        'class' : 'usname' ,
    }))
     email = forms.EmailField(widget = forms.EmailInput(attrs = {
         'placeholder' : 'Your Email', 
         'class' : 'email' ,
     })) 
     password1  = forms.Field(widget = forms.PasswordInput(attrs = {
         'placeholder' : 'Your Password', 
         'class' : 'password'
     }))
     password2  = forms.Field(widget = forms.PasswordInput(attrs = {
         'placeholder' : 'Confirm Password',
         'class' : 'password'
     }))


class Meta:
            model = User 
            fields = ['username','email','password1','password2']  

class LoginPageForm(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={
        'placeholder' : 'Your Username',
        'class' : 'usname' ,
    }))
    password  = forms.Field(widget = forms.PasswordInput(attrs = {
         'placeholder' : 'Your Password', 
         'class' : 'password' ,
     }))
class Meta:
            model = User 
            fields = ['username','password']  