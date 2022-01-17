from rest_framework.views import APIView
from .models import Order, OrderItem, Product
from accounts.models import User
from .serializers import OrderListSerializer, OrderItemListSerializer, OrderItemCreateSerializer, OrderCreateSerializer, OrderDetailSerializer, OrderUpdateSerializer
from rest_framework.response import Response
from rest_framework import status


class OrderView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        srz_data = OrderListSerializer(instance=orders, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)

    def post(self, request):
        srz_order = OrderCreateSerializer(data=request.data)
        if srz_order.is_valid():
            srz_order.save()
            return Response(srz_order.data, status=status.HTTP_201_CREATED)
        return Response(srz_order.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, user_id):
    #     order = Order.objects.get(pk=user_id)
    #     orderitem = OrderItem.objects.create(order=order)
    #     srz_order = OrderItemCreateSerializer(instance=orderitem, data=request.data)
    #     if srz_order.is_valid():
    #         srz_order.save()
    #         return Response(srz_order.data, status=status.HTTP_201_CREATED)
    #     return Response(srz_order.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderIdView(APIView):
    def get(self, request, order_id):
        order = Order.objects.get(pk=order_id)
        srz_data = OrderDetailSerializer(instance=order).data
        return Response(srz_data, status=status.HTTP_201_CREATED)

    def put(self, request, order_id):
        order = Order.objects.get(pk=order_id)
        srz_data = OrderUpdateSerializer(instance=order, data=request.data)
        if srz_data.is_valid():
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderItemView(APIView):
    def get(self, request):
        orderitems = OrderItem.objects.all()
        srz_data = OrderItemListSerializer(instance=orderitems, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)

    def post(self, request):
        srz_data = OrderItemCreateSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

























