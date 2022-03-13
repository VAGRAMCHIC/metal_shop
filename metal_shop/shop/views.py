from django.shortcuts import render
from .models import Product, Photo, Comment
from django.http import Http404
# Create your views here.


def preview(request):
    offer_product = Product.objects.order_by('-is_offer')[0]
    return render(request, 'preview.html', {'offer':offer_product})

def catalog(request):
    photos = Photo.objects.filter(is_preview=True)
    products = Product.objects.all()
    content = {'products':products, 'photos':photos}
    return render(request, 'catalog/catalog.html', content)

def show_product(request, product_id):
    try:
        photos = Photo.objects.filter(pk=product_id)
        print(photos)
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404('product dosent exist')

    return render(request, 'catalog/product.html',{'product':product, 'photos':photos})
