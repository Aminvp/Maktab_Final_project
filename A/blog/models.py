from django.db import models
from accounts.models import User
from django.urls import reverse
import random
from django.utils.text import slugify
# from ckeditor_uploader.fields import RichTextUploadingField
from shop.models import Product


class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.CharField(max_length=120, unique=True)

    def get_absolute_url(self):
        return reverse('blog:category_detail', kwargs={'id': self.id})

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('publish', 'Publish')
    )
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True, null=True, blank=True, allow_unicode=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tag = models.ManyToManyField(Tag)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='posts/%Y/%m/%d/', null=True, blank=True)
    body = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS, default='draft')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='post')

    def __str__(self):
        return f'{self.user}-{self.title}'

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    def random_number_generator(self):
        return str(random.randint(1000, 9999))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        while Post.objects.filter(slug=self.slug):
            self.slug = slugify(self.title)
            self.slug += self.random_number_generator()
        return super().save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='ucomment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='pcomment')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='rcomment')
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length=400, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.body}'

    class Meta:
        ordering = ('-created', )


