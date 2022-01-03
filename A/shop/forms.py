from django import forms
from .models import Store, Category, Product


class AddStoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('name',)