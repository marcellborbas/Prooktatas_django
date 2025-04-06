from django import forms
from .models import Product


class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=10, required=True)
    last_name = forms.CharField(max_length=20, required=False)
    email = forms.EmailField(max_length=200, required=False)
    phone_number = forms.CharField(max_length=15, required=False)
    email = forms.CharField(max_length=200, required=False)

class ProductForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    price_limit_lower = forms.IntegerField()
    price_limit_higher = forms.IntegerField()

class ProductForm2(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ['name', 'price']
        fields = '__all__'
        # exclude = ['expiry_date']