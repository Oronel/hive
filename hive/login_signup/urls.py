from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'login_signup'


urlpatterns = [
	path('login/', views.log_in, name='login'),
	path('signup/', views.signup, name='signup'),
]