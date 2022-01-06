from django import forms
from .models import Store, Category, Product


class AddStoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('name',)


class RemoveStoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('name',)


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'slug', 'image', 'description', 'price', 'category')


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'slug', 'image', 'description', 'price', 'category')

