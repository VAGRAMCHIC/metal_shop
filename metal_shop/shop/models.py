from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=20, blank=True, default="")
    def __str__(self):
        return self.name
    
class Material(models.Model):
    name = models.CharField(max_length=20, blank=True, default="")
    def __str__(self):
        return self.name
    
class Country(models.Model):
    name = models.CharField(max_length=20, blank=True, default="")
    def __str__(self):
        return self.name

class WorkPattern(models.Model):
    name = models.CharField(max_length=30, blank=True, default="")
    def __str__(self):
        return self.name
    
class DetectorType(models.Model):
    name = models.CharField(max_length=20, blank=True, default="")
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=70, blank=False)
    description = models.TextField(max_length=400, blank=False)
    d_type = models.ForeignKey(DetectorType, on_delete=models.CASCADE, null=True)
    frequency = models.IntegerField(blank=False, default="")
    discriminator = models.BooleanField(blank=False, default=False)
    ground_balance = models.BooleanField(blank=False, default=False)
    sencetivity_settings = models.BooleanField(blank=False, default=False)
    
    headphone = models.BooleanField(blank=False, default=False)
    headphone_type = models.CharField(max_length=30, blank=False, default="")

    coil_diameter = models.IntegerField(blank=True, default="")
    waterproof_coil = models.BooleanField(blank=True, default=False)

    length = models.IntegerField(blank=False, default="")
    material = models.ForeignKey(Material, on_delete=models.CASCADE, null=True)
    work_pattern = models.ForeignKey(WorkPattern, on_delete=models.CASCADE, null=True)
    producing_country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    is_offer = models.BooleanField(default="")
    price = models.IntegerField(default=100, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    product_inst = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Pictures/', height_field=None, width_field=None, max_length=None)
    is_preview = models.BooleanField(default=False)
    

class Feedback(models.Model):
    product_inst = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=25, blank=True, default=None)
    text = models.TextField(max_length=400, blank=True)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.product_inst.name+': '+self.text

class Distributor(models.Model):
    name = models.CharField(max_length=20,blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    phone = models.CharField(max_length=17, blank=False)

    def __str__(self):
        return self.name +' '+ self.last_name
    
class City(models.Model):
    name = models.CharField(max_length=20, blank=False)
    distributors = models.ManyToManyField(Distributor, blank=True)
    
    def __str__(self):
        return self.name

class Social(models.Model):
    name = models.CharField(max_length=20, blank=False)
    link = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name
    