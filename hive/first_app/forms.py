from django import forms
from django.contrib.auth.models import User
from first_app.models import User, UserProfileInfo, Feed


class UserLoginForm(forms.ModelForm):

  class Meta():
    model = User
    fields = ('user_name', 'password')

class UserProfileForm(forms.ModelForm):

  class Meta():
    model = UserProfileInfo
    fields = ('user', 'profile_pic', 'bio' )



class FeedForm(forms.Form):
  text = forms.CharField(max_length=140, widget=forms.Textarea)


