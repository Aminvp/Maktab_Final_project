from rest_framework.views import APIView
from .models import Store, Product
from .serializers import StoreListSerializer, ProductListSerializer, ProductStoreSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django_filters import rest_framework as filters
from .filters import ProductFilter


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


class ProductListView(generics.ListAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductListSerializer
        filter_backends = (filters.DjangoFilterBackend,)
        filterset_class = ProductFilter



class ProductStoreView(APIView):
    def get(self, request, pk):
        store = Store.objects.get(pk=pk)
        products = Product.objects.filter(store=store)
        srz_data = ProductStoreSerializer(instance=products, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)




















