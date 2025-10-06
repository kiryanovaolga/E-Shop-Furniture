from atexit import register
from django.utils.http import urlencode
from django import template
from goods.models import Categories

# Декоратор. Эту функцию мы можем использовать как шаблонный тэг
register = template.Library()


# Создаем шаблонный тэг для возвращения категорий товаров
@register.simple_tag()
def tag_categories():
    return Categories.objects.all()


# Этот тег берёт текущие GET-параметры, обновляет их новыми значениями и возвращает строку для URL,
# чтобы при пагинации сохранялись фильтры и сортировка.
@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context["request"].GET.dict()
    query.update(kwargs)
    return urlencode(query)


"""
urlencode
превращает словарь параметров в строку GET-параметров, пригодную для URL()
params = {"on_sale": "on", "page": 2, "order_by": "price"}
urlencode(params) = 'on_sale=on&page=2&order_by=price'

"""
