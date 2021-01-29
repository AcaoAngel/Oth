from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from ckeditor.fields import RichTextField



class Post(models.Model) :
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length = 50)
	content = RichTextField() #TODO learn about rich text fields: https://www.youtube.com/watch?v=mF5jzSXb1dc
	img = models.ImageField(upload_to = 'post_img/', null=True, blank=True)
	created = models.DateTimeField(default=timezone.now)
	active = models.BooleanField(default=True)
	def __str__(self):
		return self.title
		


