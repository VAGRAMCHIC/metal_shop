from django.shortcuts import render
from .models import Product, Photo, Feedback
from .forms import *
from django.http import Http404, HttpResponseRedirect
# Create your views here.


def preview(request):
    offer_product = Product.objects.order_by('-is_offer')[0]
    photo = Photo.objects.filter(product_inst=offer_product)
    photo = photo.filter(is_preview=True)
    
    return render(request, 'preview.html', {'offer':offer_product, 'photo':photo})

def catalog(request):
    photos = Photo.objects.filter(is_preview=True)
    products = Product.objects.all()

    return render(request, 'catalog/catalog.html', {'products':products, 'photos':photos})

def show_product(request, product_id):
    try:
        photos = Photo.objects.filter(pk=product_id)
        product = Product.objects.get(pk=product_id)
        feedbacks = Feedback.objects.filter(product_inst=product)
        
        feedback_f = feedbackForm()
        if request.method == 'POST':
            feedback_f = feedbackForm(data=request.POST)
            if feedback_f.is_valid():
                new_feedback = feedback_f.save(commit=False)
                new_feedback.product_inst = product
                new_feedback.save()
            
            return HttpResponseRedirect(str(product_id))

    except Product.DoesNotExist:
        raise Http404('product dosent exist')
        
    return render(request, 'catalog/product.html',{'product':product, 'photos':photos, 'feedbacks':feedbacks, 'feedback_f':feedback_f})
