from django import forms
from first_app.models import Feed, UserProfile
from django.contrib.auth.models import User



class UserSignupForm(forms.ModelForm):
	password = forms.CharField(widget= forms.PasswordInput())
	class Meta():
		model = User
		fields = ('email','first_name','username','password')


class FeedForm(forms.Form):
  text = forms.CharField(max_length=140, widget=forms.Textarea)


class UserLoginForm(forms.ModelForm):
	password = forms.CharField(widget= forms.PasswordInput())
	class Meta():
		model = User
		fields = ('email','password')