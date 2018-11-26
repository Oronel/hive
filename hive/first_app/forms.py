from django import forms
from django.contrib.auth.models import User
from first_app.models import User, Feed


class UserLoginForm(forms.ModelForm):
	class Meta():
	    model = User
	    fields = ('full_name', 'email', 'user_name','password')




class FeedForm(forms.Form):
  text = forms.CharField(max_length=140, widget=forms.Textarea)


