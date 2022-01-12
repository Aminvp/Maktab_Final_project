from .models import Order, OrderItem
from shop.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id',)


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('user', 'products',)

    def create(self, validated_data):
        # validated_data['user'] = self.context['request'].user
        # instance = Order.objects.create(**validated_data)
        # instance.save()
        print(25*'*')
        print(validated_data)
        print(25*'*')
        return 'hello'


class OrderItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

