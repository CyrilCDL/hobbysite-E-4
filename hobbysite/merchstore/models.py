from django.db import models
from django.urls import reverse
# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('merchstore:product_type', args=[self.pk])
    
    class Meta:
        ordering=['name']

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        related_name="products",
        null=True,
    )
    price = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('merchstore:product', args=[self.pk])
        
    class Meta:
        ordering=['name']