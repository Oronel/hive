from django.urls import path
from . import views

urlpatterns = [
path('home', views.homepage, name='homepage'),
path('signup/', views.signup, name='signup'),
#path('login', views.login, name='loginpage'),

]