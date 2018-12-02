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

	followers = profile.follows.all()

	feed_by_user = []
	for foll in followers:

		feeds = Feed.objects.filter(user= foll)


		feed_by_user.append(feeds)


	return feed_by_user

def publish(request):
    return render(request, 'publish.html')

def profile(request):
    return render(request, 'profile.html')


def homepage(request):
	feeds = {'feeds' : Feed.objects.all().order_by('text')[:20]
	}
	return render(request, 'home.html', context=feeds)


def follow(request, user_id):
	user = get_object_or_404(User, id=user_id)
	fol = get_object_or_404(UserProfile, user=user)
	followers = fol.follows.all()
	return render(request, 'yourFollowers.html', {'user': user, 'followers': followers})


def profile_feed(request):
	user_id = request.user.id
	return render(request, 'home.html',context={
		'user': get_all_user_id(user_id),
		'feeds': get_follow_feed(user_id)
	})
