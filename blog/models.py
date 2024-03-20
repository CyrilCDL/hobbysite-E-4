from django.db import models

from django.urls import reverse
from datetime import datetime

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'pk':self.pk})

class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, null=True)
    entry = models.TextField()
    created_on = models.DateTimeField(default= datetime.now, blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'pk':self.pk})
