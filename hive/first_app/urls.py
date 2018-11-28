from django.urls import path
from . import views

app_name='first_app'

urlpatterns = [
path('home', views.homepage, name='homepage'),
path('signup/', views.signup, name='signup'),
path('home/<int:user_id>/', views.profile_feed, name='profile_feed'),
path('first/', views.login_and_signup, name='login_and_signup'),

#path('login', views.login, name='loginpage'),

]