from django.db import models
from django.conf import settings
from django.db import models
from django.urls import reverse
from datetime import datetime

class ArticleCategory(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()

	def get_absolute_url(self):
		return reverse('wiki:category', kwargs={'pk': self.pk})


	def __str__(self):
		return self.name
		
	class Meta:
		ordering = ['-name']

class Article(models.Model):
	title = models.CharField(max_length=255)
	entry = models.TextField()
	articlecategory = models.ForeignKey('ArticleCategory', on_delete=models.CASCADE, null=True)
	created_on = models.DateTimeField(default=datetime.now, blank=True)
	updated_on = models.DateTimeField(auto_now=True)
	
	def get_absolute_url(self):
		return reverse('wiki:article', kwargs={'pk': self.pk})

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-articlecategory', '-created_on']