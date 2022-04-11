from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Social)
admin.site.register(City)
admin.site.register(Distributor)
admin.site.register(Product)
admin.site.register(Photo)
admin.site.register(Feedback)