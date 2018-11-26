from django.db import models

# Create your models here.


class User(models.Model):
	user_name = models.CharField(max_length=264, unique=True)
	email = models.EmailField(max_length=264)
	full_name = models.CharField(max_length=264)
	password = models.CharField(max_length=264)
	bio = models.CharField(max_length=264)
	profile_pic = models.ImageField(upload_to='profile_pics', blank=True)



	def __str__(self):
		return self.full_name



class Feed(models.Model):
	text = models.TextField(max_length=140)
	date = models.DateField(auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	like = models.CharField(max_length=26)

	def __str__(self):
		return self.text