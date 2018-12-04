from django import forms
from first_app.models import Feed, UserProfile
from django.contrib.auth.models import User


class FeedForm(forms.Form):
  text = forms.CharField(max_length=140, widget=forms.Textarea)

class NewFeedForm(forms.ModelForm):
	
	class Meta:
		text = forms.CharField(widget=forms.Textarea)
		model = Feed
		fields = ('text',)
