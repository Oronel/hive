from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import User,UserProfileInfo,Feed
def index(request):
	return render(request, 'home.html')

def homepage(request):
	feeds = {'feed' : Feed.objects.all().order_by('text')[:20]
	}
	return render(request, 'home.html', feeds)