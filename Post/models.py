from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class Post(models.Model) :
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	# profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
	title = models.CharField(max_length = 50)
	content = models.TextField(default = ' ')#TODO learn about rich text fields: https://www.youtube.com/watch?v=mF5jzSXb1dc
	img = models.ImageField(upload_to = 'post_img/' , default = 'post_img/default.png')
	created = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return self.title