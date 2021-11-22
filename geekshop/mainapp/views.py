from django.shortcuts import render
from django.conf import settings # В настройках пропишем путь до файла products.json
import json # модуль для преобразования текста в json и затем в словарь
import os # надо определить абсолютный путь к файлу products.json (через относительный не понимает. Говорит нет такого файла.).
# Для этого в settings.py добавил путь FILE_PRODUCTS

from datetime import datetime

# Create your views here.


def index(request):

    context = {
        'title': 'Магазин',
    }

    return render(request, 'mainapp/index.html', context)


def products(request):
    return render(request, 'mainapp/products.html', get_products())


def contact(request):
    return render(request, 'mainapp/contact.html')


def get_products():

    filename = os.path.join(settings.FILE_PRODUCTS, 'products.json')

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.loads(f.read().replace("'", '"'))
    return data

