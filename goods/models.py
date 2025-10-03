from os import name
from tabnanny import verbose
from django.db import models

"""
models.py — «структура данных, описывается сама модель»(какие поля, типы данных, ограничения, class Meta, Методы модели)
"""


# --------------------------------------------CATEGORIES------------------------------------------------------------
class Categories(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,  # unique=True-значения в этом поле не могут повторяться
        verbose_name="Category Title",  # имя поля, которое показывается в админке
    )

    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="Category URL"
    )  # Поле необязательное и в базе, и в формах

    class Meta:
        db_table = "category"  # название нашей таблицы БД
        verbose_name = "Category"  # название нашей таблицы в админ панеле в ед. ч.(Select Category to change...)
        verbose_name_plural = (
            "Categories"  # название нашей таблицы в админ панеле во мн. ч.
        )

    def __str__(self):
        return self.name


# --------------------------------------------PRODUCTS-------------------------------------------------------------------
class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Product Title")

    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="Product URL"
    )

    description = models.TextField(
        blank=True, null=True, verbose_name="Product Description"
    )

    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True
    )  # models.ImageField-Храним ПУТЬ изображени....upload_to='goods_images'—указывает папку, куда Django будет сохранять загруженные картинки.

    price = models.DecimalField(
        default=0.00,
        max_digits=7,  # Сколько чисел до запятой
        decimal_places=2,  # Сколько чисел после запятой
        verbose_name="Product Price",
    )  # поле для чисел с точкой

    discount = models.DecimalField(
        default=0.00,
        max_digits=4,  # Сколько чисел до запятой
        decimal_places=2,  # Сколько чисел после запятой
        verbose_name="Product Discount in %",
    )  # поле для чисел с точкой

    quantity = models.PositiveIntegerField(
        default=0, verbose_name="Product Quantity"
    )  # поле для целых положительных чисел (0 и выше).

    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Product Category"
    )

    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("id",)  # Сортируем продукты по id

    def __str__(self):
        return f"{self.name} | Quantity - {self.quantity}"

    # Работа с id. Выводит нули через f-строку, чтобы в id было 5 знаков
    def display_id(self):
        return f"{self.id:05}"  # 00007

    # Расчет окончательной цены товара со скидкой
    @property
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
