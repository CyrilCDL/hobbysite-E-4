from django.db import models
from django.urls import reverse
# Create your models here.

class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    peopleRequired = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Commission: '{self.title}' - People Required: {self.peopleRequired}"
    
    def get_absolute_url(self):
        return reverse('commissions:commission',args=[self.pk])
    
    class Meta:
        ordering = ['created']
    
class Comments(models.Model):
    commission = models.ForeignKey(Commission, 
                on_delete=models.CASCADE)
    
    entry = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment on'{self.commission.title}':{self.entry[:20]}"
    
    def get_absolute_url(self):
        return reverse('commissions:comment',args=[self.pk])
    
    class Meta:
        ordering = ['-created']
        

