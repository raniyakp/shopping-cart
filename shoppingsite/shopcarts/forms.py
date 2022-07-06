from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from .models import UserProfile 

class SignupForm(UserCreationForm):

    first_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter first name'}),min_length=1,max_length=20)
    last_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter last name'}),min_length=0,max_length=20)
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter username'}), min_length=4, max_length=150)
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'Enter email id'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Enter password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}))

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email id already exists")
        return email

    def save(self, commit=True):
        user = User.objects.create_user(
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
            username = self.cleaned_data['username'],
            email = self.cleaned_data['email'],
            password = self.cleaned_data['password1']
        )
        userprofile = UserProfile.objects.create(user=user)

        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']




    
        