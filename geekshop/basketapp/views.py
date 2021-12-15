from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Products

from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
def basket(request):
    title = 'корзина'
    basket_items = Basket.objects.filter(user=request.user).order_by('product')

    content = {
        'title': title,
        'basket_items': basket_items,
        'total_quantity': Basket.get_quantity(request.user)['total_quantity'],
        'total_cost': Basket.get_sum(request.user)['total_sum'],
    }

    return render(request, 'basketapp/basket.html', content)


@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))

    product = get_object_or_404(Products, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.product_quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
