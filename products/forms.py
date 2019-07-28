from django import forms
from .models import Products


class StoresForm(forms.Form):

    name = forms.CharField(max_length=30)
    address = forms.CharField(max_length=50)
    contact_no = forms.IntegerField()
    landmark = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=50)
    location = forms.CharField(max_length=50)


class ProductsForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = '__all__'