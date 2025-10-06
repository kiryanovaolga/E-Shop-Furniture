from unicodedata import category
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from django.template import context

from goods.models import Products
from goods.utils import q_search


def catalog(request, category_slug=None):
    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None)  # запрос для поиска конкретного товара

    if category_slug == "all-categories":
        goods = Products.objects.all()

    elif query:
        goods = q_search(query)
    else:
        # найди все Products, у которых связанная category имеет поле slug, равное значению переменной category_slug» или 404
        # Пример: фильтруются товары, чья категория имеет slug == 'living-room'.
        goods = get_list_or_404(Products, category__slug=category_slug)

    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

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
