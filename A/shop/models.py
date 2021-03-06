from django.db import models
from django.urls import reverse
from accounts.models import User
from django.utils.text import slugify


class Store(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('removed', 'Removed'),
        ('confirmed', 'Confirmed')
    )
    name = models.CharField(max_length=120)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='store')

    def __str__(self):
        return f'{self.name} - {self.user}'


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category_filter', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    description = models.TextField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_products')

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

















