from rest_framework import serializers
from .models import Store, Product


class StoreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class StoreConfirmedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'




















