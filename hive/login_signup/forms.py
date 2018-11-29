from django import forms
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

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput())
    class Meta():
        model = User
        fields = ('email','password')