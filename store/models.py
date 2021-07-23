from typing import Text
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(max_length=255,unique=True)


    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='product_creator')
    title = models.CharField(max_length=255)
    author=models.CharField(max_length=255,default='admin')
    description = models.TextField(blank=True)
    images = models.ImageField( upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock =  models.BooleanField(default=True)    
    is_active =  models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=False)    
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def __repr__(self):
        return Product  

