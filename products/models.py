from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    dis_mrp = models.CharField(max_length=50)
    og_mrp = models.CharField(max_length=50)
    img = models.ImageField(upload_to='assets')

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    fullname = models.CharField(max_length=100)

# class checkout(models.Model):
    