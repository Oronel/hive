from django.urls import path
from . import views

app_name='first_app'

urlpatterns = [
# path('home/', views.homepage, name='homepage'),
path('home/', views.profile_feed, name='home'),
path('home/yourFollowers/<int:user_id>', views.follow, name='followers'),
]