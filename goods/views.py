from unicodedata import category
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from django.template import context

from goods.models import Products


def catalog(request, category_slug):
    page = request.GET.get("page", 1)

    if category_slug == "all-categories":
        goods = Products.objects.all()
    else:
        # найди все Products, у которых связанная category имеет поле slug, равное значению переменной category_slug» или 404
        # Пример: фильтруются товары, чья категория имеет slug == 'living-room'.
        goods = get_list_or_404(Products, category__slug=category_slug)

    paginator = Paginator(goods, 3)  # Разбить goods на страницы по 3 товара
    current_page = paginator.page(int(page))  # Получаем текущую страницу

    context = {
        "title": "Home Catalog",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        "product": product,
    }
    return render(request, "goods/products.html", context)
