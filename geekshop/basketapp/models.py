from django.db import models
from django.db.models import Sum
from mainapp.models import Products
from django.conf import settings


# Create your models here.
class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    created = models.DateTimeField(verbose_name='время', auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.product}'

    @staticmethod
    def get_quantity(user=None):
        if user is None:
            return {'total_quantity': 0}
        return Basket.objects.filter(user=user).aggregate(total_quantity=Sum('product_quantity'))

    @staticmethod
    def get_sum(user=None):
        if user is None:
            return {'total_sum': 0}

        products = Basket.objects.filter(user=user)
        total_sum = 0
        for product in products:
            total_sum += product.product_quantity * product.product.price
        return {'total_sum': total_sum}
