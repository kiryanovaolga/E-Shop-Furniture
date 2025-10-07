from ast import keyword
from django.db.models import Q
from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
    SearchHeadline,
)
from goods.models import Products


# Поиск на сайте по id
"""
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
"""


# Более гибкий поиск, принцип похожести токенов, full-text-search из джанго
def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    # SearchVector создаём поисковый вектор, который указывает, по каким полям нужно искать
    vector = SearchVector("name", "description")

    #  преобразуем строку запроса пользователя в поисковый запрос, понятный для Django.
    query = SearchQuery(query)

    #!.annotate() добавляет временные (виртуальные) поля к каждому объекту QuerySet, и эти поля можно использовать в шаблоне так же, как обычные.
    # добавляем к каждому товару поле rank(показывает, насколько хорошо товар соответствует запросу), сортируем товары по убыванию ранга
    result = (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )

    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )
    return result
