import django.forms
from django.forms import ModelForm ,Textarea, TextInput, HiddenInput

from .models import *


class feedbackForm(ModelForm):
    
    class Meta:
        model = Feedback
        fields = ("text", "author")

        widgets ={
            'author': TextInput(attrs={'class':'form-control', 'placeholder':'Как вас зовут?'}),
            'text': Textarea(attrs={'class':'d-block form-control', 'rows':'6', 'placeholder':'Ваш отзыв'}),
        }