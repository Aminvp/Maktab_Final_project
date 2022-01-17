from .models import Order, OrderItem
from accounts.models import User
from shop.models import Product
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id',)


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('user', 'products', )

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        return order


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validate_data):
        order = Order.objects.create(**validate_data)
        return order


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

