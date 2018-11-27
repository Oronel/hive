from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import User,Feed
from . import forms
from first_app.forms import UserLoginForm


def index(request):
	return render(request, 'home.html')

def loginpage(request):
    return render(request, 'login.html') 

def homepage(request):
	feeds = {'feed' : Feed.objects.all().order_by('text')[:20]
	}
	return render(request, 'home.html', feeds)


def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserLoginForm(data=request.POST)
       

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()


            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_form.errors)
    else:
        user_form = UserLoginForm()
     

    return render(request, 'signup.html', {
        'user_form': user_form,
        'registered': registered
        })
