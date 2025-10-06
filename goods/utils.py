from ast import keyword
from django.db.models import Q

from goods.models import Products


# Поиск на сайте по id
def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    keywords = []
    for word in query.split():  # перебираем все слова, полученные из строки query
        if len(word) > 2:  # проверяем: длина слова больше 2 символов?
            keywords.append(word)  # если да — добавляем его в список

    q_objects = Q()

    for token in keywords:
        q_objects |= Q(description__icontains=token)

    return Products.objects.filter(q_objects)
