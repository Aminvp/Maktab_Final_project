from django_filters import rest_framework as filters
from .models import Product



class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='iexact')
    available = filters.BooleanFilter()
    price = filters.NumberFilter()
    price__gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    store = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ('name', 'available', 'price', 'store__name')