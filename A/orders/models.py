from django.db import models
from django.conf import settings
from shop.models import Product, Store
from django.core.validators import MinValueValidator, MaxValueValidator


class Order(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('canceled', 'Canceled'),
        ('confirmed', 'Confirmed'),
        ('paid', 'Paid')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product, through='OrderItem', related_name='orders')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    discount = models.IntegerField(blank=True, null=True, default=None)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user} - {str(self.id)}'

    @property
    def get_total_cost(self):
        total = sum(item.get_cost() for item in self.items.all())
        if self.discount:
            discount_price = (self.discount / 100) * total
            return int( total - discount_price )
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.IntegerField()
    quantity = models.PositiveSmallIntegerField(default=1)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_orderitem')

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity


class Coupon(models.Model):
    code = models.CharField(max_length=30, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.code





















