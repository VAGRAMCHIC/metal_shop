from django import forms
from django.forms import ModelForm,CheckboxInput, Textarea, TextInput, Select, CheckboxSelectMultiple
from django.db.models import Min, Max
from .models import *


class feedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ("text", "author")

        widgets ={
            'author': TextInput(attrs={'class':'form-control', 'placeholder':'Как вас зовут?'}),
            'text': Textarea(attrs={'class':'d-block form-control', 'rows':'6', 'placeholder':'Ваш отзыв'}),
        }

class FilterProdForm(ModelForm):
    class Meta:
        
        model = Product
        exclude = ['description']
        
        min_price=model.objects.all().aggregate(Min('price'))
        max_price=model.objects.all().aggregate(Max('price'))
        
        widgets= {
            'name': TextInput(attrs={'type':'text', 'class':'form-control','placeholder':'Название'}),
            'd_type': CheckboxSelectMultiple(attrs={'class':'form-check-input d-type','type':'checkbox', 'value':''}),
            'frequency': TextInput(attrs={'placeholder':'Название'}),
            'discriminator': CheckboxInput(attrs={}),
            'ground_balance': TextInput(attrs={}),
            'sencetivity_settings': CheckboxInput(attrs={}),
            'headphone': CheckboxInput(attrs={}),
            'headphone_type': TextInput(attrs={}),
            'coil_diameter': TextInput(attrs={}),
            'waterproof_coil': CheckboxInput(attrs={}),
            'length': TextInput(attrs={}),
            'material': Select(attrs={'class':'form-select'}),
            'work_pattern': CheckboxSelectMultiple(attrs={'class':'form-check-input','type':'checkbox', 'value':''}),
            'producing_country': CheckboxSelectMultiple(attrs={'class':'form-check-input','type':'checkbox', 'value':''}),
            'brand': CheckboxSelectMultiple(attrs={'class':'form-check-input','type':'checkbox', 'value':''}),
            'is_offer': CheckboxInput(attrs={}),
            'price': TextInput(attrs={'type':'range', 'class':'form-range', 'id':'customRange1', 'min':min_price, 'max':max_price, 'step':'1'}),
        }


            