from django.contrib import admin

# Register your models here.
from .models import Product, Photo, Feedback

admin.site.register(Product)
admin.site.register(Photo)
admin.site.register(Feedback)