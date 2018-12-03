from django.urls import path
from . import views

app_name='first_app'

urlpatterns = [
path('home/', views.profile_feed, name='home'),
path('home/yourFollowers/', views.follow, name='followers'),
path('home/publish/', views.publish, name='publish'),
path('home/profile/<username>', views.profile, name='profile'),
path('home/my_profile/', views.my_profile, name='my_profile'),
]