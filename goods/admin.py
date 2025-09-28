from django.contrib import admin
from goods.models import Categories, Products

"""
admin.py — «как модель выглядит в админке», настраивается интерфейс админки(list_display, search_fields, list_filter, Порядок сортировки, группы полей, inline-модели)
"""


# admin.site.register(Categories)
# admin.site.register(Products)


# -----------------------------------CATEGORIES----------------------------------------------------------
@admin.register(Categories)  # мы хотим зарегистрировать модель Categories в админке.
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",)
    }  # Автоматически заполнять одно поле на основе другого


# -----------------------------------PRODUCTS----------------------------------------------------------
@admin.register(Products)  # мы хотим зарегистрировать модель Products в админке.
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
