from django.contrib import admin


# Register your models here.
from .models import *

admin.site.register(DetectorType)
admin.site.register(WorkPattern)
admin.site.register(Country)
admin.site.register(Material)
admin.site.register(Brand)
admin.site.register(Social)
admin.site.register(City)
admin.site.register(Distributor)
admin.site.register(Product)
admin.site.register(Photo)
admin.site.register(Feedback)

