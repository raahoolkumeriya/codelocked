from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
#from taggit.managers import TaggableManager
from django.contrib.auth.models import User

TAGS_CHOICES = (
	('PY','Python'),('SH','Shell'),('AN','ansible'),('DJ','django'),('ML','machine_learning'),
	('HT','HTML'),('CS','CSS'),
)
	
class StreamType(models.Model):
	title 		= models.CharField(max_length=200)
	summary 	= RichTextField(blank=True,null=True)
	slug		= models.SlugField(unique = True)
	category 	= models.CharField(max_length=30)
	description = RichTextUploadingField(blank=True,
									null=True, 
									config_name='special',
									external_plugin_resources=[
									('youtube','/static/youtube/','plugin.js',)
									],)
	github 		=  models.URLField(max_length=200, blank=True)
	publish		= models.BooleanField(default=True)
	created		= models.DateTimeField(auto_now_add=True)
	modified	= models.DateTimeField(auto_now=True)
	tags 		= models.CharField(default=' ', max_length=2, choices=TAGS_CHOICES)
	
	
	def __str__(self):
		return self.title
		
	class Meta:
		verbose_name = "Stream Entry"
		verbose_name_plural ="Stream Entries"
		ordering = ["-created"]	

"""
class Comment(models.Model):
	post = models.ForeignKey(StreamType,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	content = models.TextField(max_length=160)
	timestamp = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return '{}'.format(self.post.slug)
"""