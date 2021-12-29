from django.db import models
from accounts.models import User
from orders.models import Order


class Cart(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('removed', 'Removed'),
        ('confirmed', 'Confirmed'),
        ('paid', 'Paid')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='order_cart')
    status = models.CharField(max_length=20, choices=STATUS, default='pending')

