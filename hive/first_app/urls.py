from django.urls import path
from . import views

app_name='first_app'

urlpatterns = [
path('home/', views.profile_feed, name='home'),
path('home/your_followers/', views.follow, name='followers'),
path('home/publish/', views.create_feed, name='publish'),
path('home/profile/<username>', views.profile, name='profile'),
path('home/my_profile/', views.my_profile, name='my_profile'),
path('home/all_users', views.all_users, name='all_users'),
path('home/search_user/', views.search_user, name='search_user'),
path('home/edit_profile', views.edit_page, name='edit_page'),
path('home/search_user/', views.search_user, name='search_user'), 
]