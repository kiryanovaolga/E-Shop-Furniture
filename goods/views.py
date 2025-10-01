from unicodedata import category
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template import context

from goods.models import Products


def catalog(request, category_slug):
    if category_slug == "all-categories":
        goods = Products.objects.all()
    else:
        # найди все Products, у которых связанная category имеет поле slug, равное значению переменной category_slug» или 404
        # Пример: фильтруются товары, чья категория имеет slug == 'living-room'.
        goods = get_list_or_404(Products, category__slug=category_slug)

    context = {"title": "Home Catalog", "goods": goods}
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        "product": product,
    }
    return render(request, "goods/products.html", context)
