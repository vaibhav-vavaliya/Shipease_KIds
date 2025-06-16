from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='assets')
    dis_mrp = models.CharField(max_length=50)
    og_mrp = models.CharField(max_length=50)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)