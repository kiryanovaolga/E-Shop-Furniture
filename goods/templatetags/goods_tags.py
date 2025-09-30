from atexit import register
from django import template
from goods.models import Categories

# Декоратор. Эту функцию мы можем использовать как шаблонный тэг
register = template.Library()


# Создаем шаблонный тэг для возвращения категорий товаров
@register.simple_tag()
def tag_categories():
    return Categories.objects.all()
