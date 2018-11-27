from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Feed, User
from . import forms
from first_app.forms import UserLoginForm

# Create your views here.
def loginpage(request):
    return render(request, 'login.html') 

def login(request):
    form = forms.UserLoginForm()
    if request.method == 'POST':
        form = forms.UserLoginForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else: 
            print('Error - form is invalid')

    return render(request, 'login.html',{'form': form})