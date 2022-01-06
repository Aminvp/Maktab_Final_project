from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('create/', views.order_create, name='create'),
    path('<int:order_id>/', views.detail, name='detail'),
    path('orders_list/<int:id>/<int:store_id>', views.orders_list, name='orders_list'),
    path('apply/<int:order_id>/', views.coupon_apply, name='coupon_apply'),
]