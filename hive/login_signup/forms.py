from django import forms
from first_app.models import Feed, User



class UserLoginForm(forms.ModelForm):
	password = forms.CharField(widget= forms.PasswordInput())
	class Meta():
	    model = User
	    fields = ('email','password')

