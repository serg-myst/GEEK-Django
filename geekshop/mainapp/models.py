from django.db import models

# Create your models here.
class ProductCategory(models.Model):

    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    descriptions = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активно', default=True)

    def __str__(self):
        return self.name


class Products(models.Model):

    category = models.ForeignKey(ProductCategory, on_delete = models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=64)
    image = models.ImageField(upload_to = 'products_images', blank = True)
    image_1 = models.ImageField(upload_to='products_images', blank=True)
    image_2 = models.ImageField(upload_to='products_images', blank=True)
    image_3 = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    is_active = models.BooleanField(verbose_name='активно', default=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits = 15, decimal_places = 2, default = 0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default = 0)

    def __str__(self):
        return f'{self.name} ({self.category.name} {self.image})'