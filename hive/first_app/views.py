from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from first_app.models import Feed, UserProfile
from . import forms
from django.shortcuts import get_object_or_404



def index(request):
	return render(request, 'home.html')

def get_all_user_id(user_id):
    user = User.objects.filter(id = user_id)
    return user

def get_follow_feed(user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(UserProfile, user=user)
    print(user)
    followers = profile.follows.all()
    print(followers)
    feed_by_user = []
    for foll in followers:
        print(foll)
        feeds = Feed.objects.filter(user= foll)
        print(feeds)
        print('#####################')
        feed_by_user.append(feeds)
    print(feed_by_user)

    return feed_by_user


def homepage(request):
	feeds = {'feeds' : Feed.objects.all().order_by('text')[:20]
	}
	return render(request, 'home.html', context=feeds)


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

def follow(request, user_id):
    user = get_object_or_404(User, id=user_id)
    fol = get_object_or_404(UserProfile, user=user)
    followers = fol.follows.all()
    return render(request, 'yourFollowers.html', {'user': user, 'followers': followers})


def profile_feed(request, user_id):
    return render(request, 'home.html',context={
        # 'user': get_all_user_id(user_id),
        'feeds': get_follow_feed(user_id)
    })

def login_and_signup(request):
    signup_form = forms.UserSignupForm()
    login_form = forms.UserLoginForm()
    return render(request, 'first.html',{
        'signup_form': signup_form,
        'login_form': login_form
        })


