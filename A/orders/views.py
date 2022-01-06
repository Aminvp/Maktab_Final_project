import json
import requests
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User
from shop.models import Store
from .models import Order, OrderItem, Coupon
from cart.cart import Cart
from decimal import Decimal
from django.contrib import messages
from .forms import CouponForm
from django.views.decorators.http import require_POST
from django.utils import timezone


@login_required(login_url='accounts:user_login')
def detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    form = CouponForm()
    return render(request, 'orders/order.html', {'order': order, 'form': form})


@login_required(login_url='accounts:user_login')
def order_create(request):
    cart = Cart(request)
    order = Order.objects.create(user=request.user)
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=Decimal(item['price']), quantity=item['quantity'])
    cart.clear()
    return redirect('orders:detail', order.id)


@login_required(login_url='accounts:user_login')
def orders_list(request, id, store_id):
    if request.user.id == id:
        user = User.objects.get(id=id)
        store = Store.objects.get(id=store_id)
        orders = store.store_orderitem.all()
        return render(request, 'orders/orders_list.html', {'user': user, 'store': store, 'orders': orders})
    else:
        return redirect('shop:home')


@require_POST
def coupon_apply(request, order_id):
    now = timezone.now()
    form = CouponForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code, valid_from__lte=now, valid_to__gte=now, active=True)
            order = Order.objects.get(id=order_id)
            order.discount = coupon.discount
            order.save()
            return redirect('orders:detail', order_id)
        except Coupon.DoesNotExist:
            messages.warning(request, 'This coupon does not exist', 'warning')
            return redirect('orders:detail', order_id)










