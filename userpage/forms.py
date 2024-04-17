from django import forms
# from django.forms.widgets import ClearableFileInput
# from django.forms.widgets import ClearableMultipleFileInput
from . models import *
# from django.forms.widgets import ClearableMultipleFileInput




class Category(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['slug', 'name']

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['category','slug','name','product_image','description','price','status']

