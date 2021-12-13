from django.shortcuts import render, get_object_or_404
from django.conf import settings  # В настройках пропишем путь до файла products.json
import json  # модуль для преобразования текста в json и затем в словарь
import \
    os  # надо определить абсолютный путь к файлу products.json (через относительный не понимает. Говорит нет такого файла.).
# Для этого в settings.py добавил путь FILE_PRODUCTS

from basketapp.views import Basket

from mainapp.models import ProductCategory, Products
import random

# Create your views here.
main_menu = [
    {'href': 'index', 'name': 'домой'},
    {'href': 'products', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]

'''
links_menu = [
    {'href': 'products_all', 'name': 'все'},
    {'href': 'product_home', 'name': 'дом'},
    {'href': 'product_office', 'name': 'офис'},
    {'href': 'product_modern', 'name': 'модерн'},
    {'href': 'product_classic', 'name': 'классика'},
]
'''


def index(request):
    context = {
        'title': 'Магазин',
        'main_menu': main_menu,
    }

    return render(request, 'mainapp/index.html', context)


def products(request):
    links_menu = ProductCategory.objects.all().order_by('name')
    all_products = Products.objects.all()
    hot_product = get_hot_product()

    basket = []

    total_quantity = 0
    total_sum = 0

    if request.user.is_authenticated:
        # basket = Basket.objects.filter(user=request.user)
        total_quantity = Basket.get_quantity(request.user)['total_quantity']
        total_sum = Basket.get_sum(request.user)['total_sum']

    context = {
        'main_menu': main_menu,
        'links_menu': links_menu,
        'products': all_products,
        'hot_product': hot_product,
        'total_quantity': total_quantity,
        'total_sum': total_sum,
    }

    return render(request, 'mainapp/products.html', context=context)


def get_hot_product():
    products = Products.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    return Products.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]


def contact(request):
    context = {
        'main_menu': main_menu,
    }

    return render(request, 'mainapp/contact.html', context)


def show_category_products(request, category_id=None):
    links_menu = ProductCategory.objects.all().order_by('name')

    if category_id in (3, None):  # пока привяжимся к id категории "ВСЕ"
        all_products = Products.objects.all()
    else:
        all_products = Products.objects.filter(category=category_id)

    hot_product = get_hot_product()

    context = {
        'main_menu': main_menu,
        'links_menu': links_menu,
        'products': all_products,
        'active_category_id': category_id,  # передаем для установки активного класса - active
        'hot_product': hot_product,
    }

    return render(request, 'mainapp/products.html', context=context)


def get_products():
    filename = os.path.join(settings.FILE_PRODUCTS, 'products.json')

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.loads(f.read().replace("'", '"'))
    return data


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def product(request, pk):
    title = 'продукты'
    links_menu = ProductCategory.objects.all().order_by('name')

    content = {
        'title': title,
        'links_menu': links_menu,
        'product': get_object_or_404(Products, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)