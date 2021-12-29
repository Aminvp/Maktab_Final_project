from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractBaseUser
from .managers import MyUserManager


class User(AbstractBaseUser):
    email = models.EmailField(max_length=120, unique=True)
    full_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin






