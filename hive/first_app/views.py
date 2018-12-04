from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from first_app.models import Feed, UserProfile
from . import forms
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def index(request):
	return render(request, 'home.html')

def get_all_user_id(user_id):
	user = User.objects.filter(id = user_id)
	return user

def search_user(request):
    queryset_list = User.objects.all()
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = User.objects.all()
    query = request.GET.get("q")
    print('your sister')
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(author__icontains=query)|
            Q(user__first_name__icontains=query)|
            Q(user__username__icontains=query)
            ).distinct()
        print('ouais mongars')
    paginator = Paginator(queryset_list, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
         queryset = paginator.page(1)
    return render(request, 'search_user.html', {'queryset': queryset, 'page_request_var': page_request_var})


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

def my_profile(request):
	user_id = request.user.id
	user = get_object_or_404(User, id=user_id)
	profile = get_object_or_404(UserProfile, user=user)
	print(profile)
	print("#############")
	feeds = Feed.objects.filter(user= profile).order_by('-date')
	print(feeds)
	return render(request, 'my_profile.html',context={
		'user': user,
		'feeds': feeds
	})
	


def profile(request, username):
	user = get_object_or_404(User, username=username)
	profile = get_object_or_404(UserProfile, user=user)
	feeds = Feed.objects.filter(user= profile)
	return render(request, 'profile.html', {'feeds': feeds,'user': user, 'prof': profile })


def homepage(request):
	feeds = {'feeds' : Feed.objects.all().order_by('text')[:20]
	}
	return render(request, 'home.html', context=feeds)


def follow(request):
	user_id = request.user.id
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




def all_users(request):
	users = {'users' : UserProfile.objects.all()
	}
	return render(request, 'all_users.html', users)

def create_feed(request):
	# user = get_object_or_404(UserProfile, id=profile_id)
	user_id = request.user.id
	user = User.objects.get(id=user_id)
	profile = UserProfile.objects.get(user=user)
	form = forms.NewFeedForm()
	if request.method =='POST':
		feed_form = forms.NewFeedForm(request.POST)
		if feed_form.is_valid():
			# feed = Feed(text= text, user=user, date=datetime.datetime.now())
			feed = feed_form.save(commit=False)
			feed.user = profile
			feed.save()

			return redirect('/first_app/home/my_profile/')

	return render(request, 'publish.html', {'form': form,})



