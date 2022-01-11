from rest_framework.views import APIView
from .models import Order, OrderItem
from .serializers import OrderListSerializer, OrderItemListSerializer, OrderItemCreateSerializer
from rest_framework.response import Response
from rest_framework import status


class OrderView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        srz_data = OrderListSerializer(instance=orders, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)


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

























