from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import pre_save
from . utils import unique_slug_generator
from django.urls import reverse
# Create your models here.

class Post(models.Model):
	
	title=models.CharField(max_length=1000)
	content=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	slug =models.SlugField(default='post-slug',blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse ('post-detail' ,kwargs={'slug':self.slug})



def pre_save_reciever_post(sender ,instance ,*args,**kwargs):

	instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_reciever_post , sender=Post)