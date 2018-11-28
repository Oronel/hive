from django import forms
from first_app.models import Feed, User



class UserSignupForm(forms.ModelForm):
	password = forms.CharField(widget= forms.PasswordInput())
	class Meta():
	    model = User
	    fields = ('email','full_name','user_name','password')


class FeedForm(forms.Form):
  text = forms.CharField(max_length=140, widget=forms.Textarea)


class UserLoginForm(forms.ModelForm):
	password = forms.CharField(widget= forms.PasswordInput())
	class Meta():
	    model = User
	    fields = ('email','password')