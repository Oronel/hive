from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    follows = models.ManyToManyField('UserProfile', related_name='followed_by', symmetrical=False, blank=True)
    bio = models.CharField(max_length=264)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


    def __str__(self):
        return self.user.username


class Feed(models.Model):
	text = models.TextField(max_length=140)
	date = models.DateField(auto_now=True)
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	like = models.IntegerField(default=0)

	def __str__(self):
		return self.text