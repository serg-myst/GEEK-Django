import os
import json

from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Products
from django.conf import settings


def load_from_json(file_name):
    with open(os.path.join(settings.FILE_PRODUCTS, f'{file_name}.json'), 'r', encoding='utf-8') as file:
        return json.load(file)


class Command(BaseCommand):
    help = 'Load DB new data'

    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()  # Удалим все данные из таблицы категорий

        [ProductCategory.objects.create(**category) for category in categories]  # Создаем и записываем новый элемент

        products = load_from_json('products_db')

        Products.objects.all().delete()  # Удалим все данные из таблицы продукты

        for product in products:
            category_name = product['category']

            '''
            category_db = ProductCategory.objects.filter(
                name=category_name).first()  # Ищем в таблице кактегорий по имени. Метод first() безопасен в том плане,
                                             # что вернет пустое значение, если объект не найден
            '''

            category_db = ProductCategory.objects.get(name=category_name) # Метод не безопасен. Если значения нет или
            # или несколько значений, то будет ошибка. Оборачивать в try except

            product['category'] = category_db
            new_product = Products(**product)
            new_product.save()
