from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=70, blank=False)
    description = models.CharField(max_length=400, blank=False)
    is_offer = models.BooleanField(default=False)
    price = models.IntegerField(default=100, blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    product_inst = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Pictures/', height_field=None, width_field=None, max_length=None)
    is_preview = models.BooleanField(default=False)
    

class Comment(models.Model):
    product_inst = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=400, blank=True)

    def __str__(self):
        return product_inst+':'+self.name
