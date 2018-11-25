from django.db import models

# Create your models here.


class User(models.Model):
	first_name = models.CharField(max_length=264)
	last_name = models.CharField(max_length=264)
	bio = models.CharField(max_length=264)

	def __str__(self):
		return self.first_name


class Feed(models.Model):
	text = models.TextField(max_length=140)
	date = models.DateField(auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	like = models.CharField(max_length=26)