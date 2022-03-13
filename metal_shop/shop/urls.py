from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.preview, name='prewiew'), 
    path('catalog', views.catalog, name='catalog'),
    path('catalog/<int:product_id>', views.show_product, name='show_product'),

]
