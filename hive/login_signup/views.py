from django.shortcuts import render,redirect
from django.http import HttpResponse
from first_app.models import Feed, UserProfile
from django.contrib.auth import authenticate, login, logout
from . import forms
from django.contrib.auth.models import User

# Create your views here.

def log_in(request):
    errors = False
    if request.method == 'POST':
        login_form = forms.UserLoginForm(request.POST)
        if login_form.is_valid():
            clean_data = login_form.clean_email()
            user = authenticate(username=clean_data['username'], password=clean_data['password'])
            print(user)

            if user is not None:
                login(request, user)
                print('Logged In: {}'.format(user))
                return redirect('/first_app/home/', permanent=True)
            else:
                errors = True
    else:
        login_form = forms.UserLoginForm()
        logout(request)

    return render(request, 'login.html', {
            'login_form': login_form,
            'errors': errors,})



def signup(request):
    registered = False
    if request.method =='POST':
        user_form = forms.UserSignupForm(data= request.POST) 
        profile_form = forms.UserProfileForm(data= request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit= False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
            return redirect('/login_signup/login/')



        else :
            print(user_form.errors, profile_form.errors)

    else:  
        user_form = forms.UserSignupForm()
        profile_form = forms.UserProfileForm()

    return render(request, 'signup.html', context = {
        'user_form' : user_form,
        'profile_form' : profile_form, 
        'registered': registered
        })