from django.db import models

from django.contrib.auth.models import User, AbstractUser


# Create your models here.

class ShopUser(AbstractUser):
    age = models.PositiveSmallIntegerField(verbose_name='возраст', null=True)
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
