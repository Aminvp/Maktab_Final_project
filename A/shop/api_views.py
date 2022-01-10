from rest_framework.views import APIView
from .models import Store, Product
from .serializers import StoreListSerializer, ProductListSerializer, ProductStoreSerializer
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters


class StoreListView(APIView):
    def get(self, request):
        stores = Store.objects.all()
        srz_data = StoreListSerializer(instance=stores, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)


class StoreConfirmedView(APIView):
    def get(self, request):
        stores = Store.objects.filter(status='confirmed')
        srz_data = StoreListSerializer(instance=stores, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        srz_data = ProductListSerializer(instance=products, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='iexact')
    available = filters.BooleanFilter()
    price = filters.NumberFilter()
    price__gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    store = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ('name', 'available', 'price', 'store')


class ProductStoreView(APIView):
    def get(self, request, pk):
        store = Store.objects.get(pk=pk)
        products = Product.objects.filter(store=store)
        srz_data = ProductStoreSerializer(instance=products, many=True).data
        filter_backends = (filters.DjangoFilterBackend,)
        filterset_class = ProductFilter
        return Response(srz_data, status=status.HTTP_200_OK)


















