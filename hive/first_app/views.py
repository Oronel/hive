from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Feed, User
from . import forms
from first_app.forms import UserSignupForm


def index(request):
	return render(request, 'home.html')

def loginpage(request):
    return render(request, 'login.html') 

def homepage(request):
	feeds = {'feed' : Feed.objects.all().order_by('text')[:20]
	}
	return render(request, 'home.html', feeds)


def signup(request):
    form = forms.UserSignupForm()
    if request.method == 'POST':
        form = forms.UserSignupForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else: 
            print('Error - form is invalid')

    return render(request, 'signUp.html',{'form': form})