# from django.db import models
#
#
# class Cart(models.Model):
#     STATUS = (
#         ('pending', 'Pending'),
#         ('confirmed', 'Confirmed'),
#         ('canceled', 'Canceled'),
#
#     )
#     user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="cart_users")
#     product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="cart_product")
#     quantity = models.IntegerField()
#     discount_value = models.FloatField()
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=20, choices=STATUS, default='pending')


