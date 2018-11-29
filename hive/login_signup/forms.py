from django import forms
from django.core import validators
from first_app.models import Feed, UserProfile
from django.contrib.auth.models import User



class UserSignupForm(forms.ModelForm):
	password = forms.CharField(widget= forms.PasswordInput())
	class Meta():
		model = User
		fields = ('email','first_name','username','password')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('bio',)

    def clean_email(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username'] 

class UserLoginForm(forms.Form): 
    username = forms.CharField(max_length= 150)
    password = forms.CharField(widget= forms.PasswordInput())

    def clean_email(self):
        all_clean_data = super().clean()
        return all_clean_data

