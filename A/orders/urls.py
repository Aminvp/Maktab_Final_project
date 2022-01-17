from django.urls import path, include
from . import views
from . import api_views

app_name = 'orders'

api_urls = [
    path('orders/', api_views.OrderView.as_view()),
    path('orders/<int:order_id>/', api_views.OrderIdView.as_view()),
    path('orderitems/', api_views.OrderItemView.as_view()),
]

urlpatterns = [
    path('create/', views.order_create, name='create'),
    path('<int:order_id>/', views.detail, name='detail'),
    path('orders_list/<int:id>/<int:store_id>', views.orders_list, name='orders_list'),
    path('order/<int:id>/<int:store_id>/', views.order_detail, name='order_detail'),
    path('apply/<int:order_id>/', views.coupon_apply, name='coupon_apply'),
    path('order/status/', views.status, name='status'),
    path('api/', include(api_urls)),
]