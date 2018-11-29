from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Feed, User
from . import forms



def index(request):
	return render(request, 'home.html')

def get_all_user_id(user_id):
    users = User.objects.filter(id = user_id)
    return users

def get_all_feed(user_id):
    feeds = Feed.objects.filter(user_id= user_id)
    return feeds


def homepage(request):
	feeds = {'feeds' : Feed.objects.all().order_by('text')[:20]
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



def profile_feed(request, user_id):
    return render(request, 'profile.html',context={'user': get_all_user_id(user_id), 'feeds': get_all_feed(user_id)})

def login_and_signup(request):
    signup_form = forms.UserSignupForm()
    login_form = forms.UserLoginForm()
    return render(request, 'first.html',{
        'signup_form': signup_form,
        'login_form': login_form
        })

def publish(request):
    return render(request, 'publish.html')
