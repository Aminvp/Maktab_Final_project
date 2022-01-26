import random
import string
import uuid
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import MyUserManager
from django.db.models.signals import post_save
from .sender import send_otp


class User(AbstractBaseUser):
    email = models.EmailField(max_length=120, unique=True)
    phone = models.CharField(max_length=14, unique=True, null=True, blank=True)
    full_name = models.CharField(max_length=120)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='profiles/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.user.email


def save_profile(sender, **kwargs):
    if kwargs['created']:
        p1 = Profile(user=kwargs['instance'])
        p1.save()


post_save.connect(save_profile, sender=User)


class OtpRequest(models.Model):
    class OtpChannel(models.TextChoices):
        ANDROID = _('Android')
        IOS = _('ios')
        WEB = _("Web")

    request_id = models.UUIDField(default=uuid.uuid4, editable=False)
    channel = models.CharField(_("channel"), max_length=12, choices=OtpChannel.choices)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=4, null=True)
    valid_from = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField(default=timezone.now() + timedelta(seconds=300))
    receipt_id = models.CharField(max_length=255, null=True)

    def generate_password(self):
        self.password = self._random_password()
        self.valid_until = timezone.now() + timedelta(seconds=300)

    def _random_password(self):
        rand = random.SystemRandom()
        digits = rand.choices(string.digits, k=4)
        return ''.join(digits)

    class Meta:
        verbose_name = _('One Time Password')
        verbose_name_plural = _('One Time Passwords')
















